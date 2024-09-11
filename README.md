# Screen Scrape GUI

## The basics

This code uses Python to extract battery and/or screen use information from screenshots taken from Apple iPhones. A simple GUI is provided to enable manual entry of grid information in the event that automatic grid capture fails. 


### How it works
- Ensure all requirements (including `pytesseract` for OCR) are installed
- Launch the GUI by running `screenshot_app.py`
- Select either a folder of Screen Time screenshots or a folder of Battery images. The code will recursively search over all subdirectories to find images in the folder hierarchy.
- The program will attempt to identify a grid showing 24 hours of use. It will display two images in the middle column of the GUI if successful: The extracted grid and a graph of the extracted data.
- If either the grid or the extracted data looks incorrect, the user can reselect the grid by clicking the upper left and lower right corners of the leftmost image. 
- Relevant metadata extracted from the image is displayed in the rightmost column, with the specific information extracted depending on the screenshot type
- When the user proceeds to the next image, the information extracted is saved as a new row in a .csv file with the name of the outermost folder. 


## Screen Time notes

- The Screen Time scraping capability is more likely to succeed at the automatic grid extraction than the Battery capability. 
- Any screen use (color of bar) counts towards the totals
- OCR is used to attempt to extract the title at the top of the screenshot (e.g. "Daily Total" or "YouTube")
- To prevent any numbers in the top part of the screenshot from interfering with grid detection, a percentage of the top of the image is cropped during the extraction phase
- Errors in grid extraction can be corrected manually by clicking the leftmost image.


## Battery extraction notes

- Automatic detection is more likely to fail for Battery screenshot grid extraction, though this may be related to the image quality in our test datasets.
- Only phone use (currently dark blue as of 6/5/24) counts towards the detected totals
- OCR is used to identify the start date in the screenshot. This can be manually changed in the metadata field.
- The start time is assumed to be midnight unless the slider, visible only for Battery folders, is updated to reflect a different start for the 24-hour period.
