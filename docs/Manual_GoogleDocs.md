# Google Docs
  
Module to control Google Docs  

*Read this in other languages: [English](Manual_GoogleDocs.md), [Português](Manual_GoogleDocs.pr.md), [Español](Manual_GoogleDocs.es.md)*
  
![banner](imgs/Banner_GoogleDocs.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Setup G-Suite credentials
  
Get permissions to handle Google Docs with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path|Select the G-Suite credentials file|Path|
|Assign result to variable|Assign the connection result to a variable|result|

### New Document
  
Create new  Google Docs document.
|Parameters|Description|example|
| --- | --- | --- |
|Document name|Name of the document to create|Name: |
|Variable where the ID will be saved|Variable where the ID of the created document will be saved|result|

### Write in document
  
Write in Google Docs document
|Parameters|Description|example|
| --- | --- | --- |
|Document ID|Enter the ID of the Google Docs document|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Write text|Text to write in the Google Docs document|Lorem ipsum dolor sit amet, consectetur adipiscing elit.|

### Read document
  
Read a Google Docs document
|Parameters|Description|example|
| --- | --- | --- |
|Document ID|Google Docs document ID|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Variable where the result will be saved|Variable where the result of reading the document will be saved|result|

### Add Picture
  
Add an image to the document.
|Parameters|Description|example|
| --- | --- | --- |
|Document ID|Document ID to which the image will be added. The document ID is in the document URL|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Image Url|Url of the image that will be added to the document|https://example.com/image.jpg|
