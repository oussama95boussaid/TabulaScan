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


# Getting Started :
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

# Prerequisites :

To run this project, you'll need:

    - paddleocr
    - ultralyticsplus (version 0.0.23)
    - ultralytics (version 8.0.21)
    - opencv2
    - pandas
    - csv
    - tensorflow
    - PIL

# Install the required libraries :

    !pip install paddlepaddle
    !pip install paddleocr
    !pip install pytesseract transformers ultralyticsplus==0.0.23 ultralytics==8.0.21

**If you are using Google Colab Add (Optional)**

    !wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.19_amd64.deb
    !sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.19_amd64.deb


# Run the algorithm:

    python TabulaScan.py
