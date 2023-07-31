# Google Docs
  
Module to control Google Docs  

*Read this in other languages: [English](Manual_GoogleDocs.md), [Português](Manual_GoogleDocs.pr.md), [Español](Manual_GoogleDocs.es.md)*
  
![banner](imgs/Banner_GoogleDocs.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## How to use this module

Before using this module, you must register your app into the Google Cloud Portal.

1. Sign in with a google account to the following link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete the form and then press Create
3. Within the Navigation Menu (Left), enter API and Services
4. In the upper section, enter "+ ENABLE API AND SERVICES"
5. Search for "Google Docs API", select and finally enable
6. Again go to Navigation Menu (Left) > API and Services > Credentials
7. Press the "Configure Consent Screen" button. In User type choose if possible "Internal". If it is not available, you must select "External" and complete the mandatory fields.
8. Complete the required fields with the information of your application and press Save and continue.
9. In step 2, click on "Add or remove permissions", filter "Google Docs API", mark all permissions and press Update. Then press Save and continue.
10. Go back to "Credentials"
11. Press Create Credentials > OAuth Client ID, select as Application Type: Desktop App, put a name and create.
12. Download the JSON credentials file.
13. If the application was created as "External", you must go to Navigation Menu (Left) > Consent Screen and add user within the "Test Users" section

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
