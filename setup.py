from setuptools import setup, find_packages

setup(
    name="TabulaScan",
    version="0.1.0",  
    author="Oussama Boussaid",
    author_email="oussama.bouss3id95@gmail.com",
    description="Streamlined Scanned Image Table Extraction and Excel Conversion",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/oussama95boussaid/TabulaScan",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "opencv-python",  
        "ultralyticsplus==0.0.23",  
        "ultralytics==8.0.21",  
        "paddlepaddle",  
        "paddleocr",  
        "tensorflow",
        "Pillow"
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
