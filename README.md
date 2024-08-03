# **TabulaScan**

TabulaScan: Streamlined Scanned Image Table Extraction and Excel Conversion

# Project Overview :

TabulaScan is a cutting-edge solution designed to automate the process of table detection, 
recognition, and extraction from scanned images, transforming them into Excel files with remarkable accuracy and efficiency. 
With TabulaScan, you can swiftly transform paper-based tables into structured, editable Excel files, 
enabling seamless integration into your data management processes.

# Key Features :

**Precise Table Identification** : Our algorithm can precisely locate tables within scanned images, even in cases with complex layouts and diverse fonts.

**Robust Image Quality Handling** : It's capable of handling varying image quality levels, ensuring reliable performance across different scanned documents.

**Data Extraction** : Beyond table detection, this algorithm excels at extracting data from these tables, making it a comprehensive tool for data analysis

**Output to Excel** : Convert recognized tables into Excel files, preserving data structure and format.


## Installation

To install TabulaScan, you can use pip:

```bash
pip install TabulaScan
```

## Usage
**Example: Converting an Image to an Excel Table**
Here’s a simple example demonstrating how to use TabulaScan to convert an image of a table into an Excel file and then read it using Pandas:

```bash
import TabulaScan as ts
import cv2
import pandas as pd

# Load your image
img_path = 'path_to_your_image.jpg'
anaylise = cv2.imread(img_path)

# Convert the image table to an Excel table
result = ts.ImgTable2ExcelTable(anaylise)

# Load the resulting Excel file into a Pandas DataFrame
excel_table = pd.read_excel(result)

# Display the extracted table (the table is auto downloaded)
excel_table
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request on GitHub.

## Support
If you encounter any issues or have any questions, please feel free to open an issue on the GitHub repository.
