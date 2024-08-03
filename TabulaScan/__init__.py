import numpy as np
import pandas as pd
import cv2
import csv
from ultralyticsplus import YOLO
from paddleocr import PaddleOCR
import tensorflow as tf
from PIL import Image #pillow

def ImgTable2ExcelTable(anaylise):
  # Input image
  # anaylise = cv2.imread(img_path)
  anaylise1 = Image.fromarray(anaylise)

  # load model yolov8m
  model = YOLO('keremberke/yolov8m-table-extraction')

  # set model parameters
  model.overrides['conf'] = 0.25  # NMS confidence threshold
  model.overrides['iou'] = 0.45  # NMS IoU threshold
  model.overrides['agnostic_nms'] = False  # NMS class-agnostic
  model.overrides['max_det'] = 1000  # maximum number of detections per image

  # perform inference
  results = model.predict(anaylise1)

  # Cropped The RIO
  def RIO_select(img):
      x1, y1, x2, y2, _, _ = tuple(int(item) for item in results[0].boxes.data.numpy()[0]) # (96, 586, 947, 1286)
      cropped_image = img[y1:y2, x1:x2]
      print(cropped_image.shape)
      return cropped_image

  rio = RIO_select(anaylise)
  Image.fromarray(rio)

  # Preprpcessed Image Functions
  def add_10_percent_padding(img):
      image_height = img.shape[0]
      padding = int(image_height * 0.1)
      padded_img = cv2.copyMakeBorder(img, padding, padding, padding, padding, cv2.BORDER_CONSTANT, value=[255, 255, 255])
      return padded_img

  def RIO_Preprpcessing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    # simple_kernel = np.ones((5,5), np.uint8)
    erode_img = cv2.erode(img,kernel)
    processed_img = cv2.cvtColor(erode_img, cv2.COLOR_BGR2RGB)
    return processed_img

  def generate_excel_file(input_table,excel_file_path):
      df = pd.DataFrame(input_table)
      df.to_excel(excel_file_path, index=False, header=False)

  # Extact Text from detected table (RIO)
  ocr = PaddleOCR(lang='en')  # the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`

  image_with_padding = add_10_percent_padding(rio)
  processed_img = RIO_Preprpcessing(image_with_padding)
  image_height = processed_img.shape[0]
  image_width = processed_img.shape[1]

  result_ = ocr.ocr(processed_img)
  result_extracted = result_[0]
  bounding_boxes = [line[0] for line in result_extracted]
  text_extracted = [line[1][0] for line in result_extracted]
  probabilities =[line[1][1] for line in result_extracted]

  # Text reconstraction

  # Get Horizontal and Vertical Lines
  horiz_boxes = []
  vert_boxes = []

  for box in bounding_boxes:
    x_h, x_v = 0,int(box[0][0])
    y_h, y_v = int(box[0][1]),0
    width_h,width_v = image_width, int(box[2][0]-box[0][0])
    height_h,height_v = int(box[2][1]-box[0][1]),image_height
    horiz_boxes.append([x_h,y_h,x_h+width_h,y_h+height_h])
    vert_boxes.append([x_v,y_v,x_v+width_v,y_v+height_v])

  # Non-Max Suppression
  horiz_out = tf.image.non_max_suppression(
      horiz_boxes,
      probabilities,
      max_output_size = 1000,
      iou_threshold=0.1,
      score_threshold=float('-inf'),
      name=None
  )

  vert_out = tf.image.non_max_suppression(
      vert_boxes,
      probabilities,
      max_output_size = 1000,
      iou_threshold=0.1,
      score_threshold=float('-inf'),
      name=None
  )

  horiz_lines = np.sort(np.array(horiz_out))
  vert_lines = np.sort(np.array(vert_out))

  # Convert the table to CSV
  table = [['' for i in range(len(vert_lines))] for j in range(len(horiz_lines))]

  unordered_boxes = []
  for i in vert_lines:
    unordered_boxes.append(vert_boxes[i][0])

  ordered_boxes = np.argsort(unordered_boxes)

  # Intersection Over Union (IOU) = intersection / union
  def intersection(box_1, box_2):
    return [box_2[0], box_1[1],box_2[2], box_1[3]]

  def iou(box_1, box_2):

    x_1 = max(box_1[0], box_2[0])
    y_1 = max(box_1[1], box_2[1])
    x_2 = min(box_1[2], box_2[2])
    y_2 = min(box_1[3], box_2[3])

    inter = abs(max((x_2 - x_1, 0)) * max((y_2 - y_1), 0))
    if inter == 0:
        return 0

    box_1_area = abs((box_1[2] - box_1[0]) * (box_1[3] - box_1[1]))
    box_2_area = abs((box_2[2] - box_2[0]) * (box_2[3] - box_2[1]))

    return inter / float(box_1_area + box_2_area - inter)


  for i in range(len(horiz_lines)):
    for j in range(len(vert_lines)):
      resultant = intersection(horiz_boxes[horiz_lines[i]], vert_boxes[vert_lines[ordered_boxes[j]]] )

      for b in range(len(bounding_boxes)):
        the_box = [bounding_boxes[b][0][0],bounding_boxes[b][0][1],bounding_boxes[b][2][0],bounding_boxes[b][2][1]]
        if(iou(resultant,the_box)>0.1):
          table[i][j] = text_extracted[b]

  # Save Data in CSV file & Convert it to Excel

  # save data in cvs
  excel_file_path = "Excel_Table.xlsx"
  generate_excel_file(table,excel_file_path)
  return  excel_file_path