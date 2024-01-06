Upload Image API
================

This API allows clients to upload an image to a pre-signed Amazon Web Services (AWS) S3 URL.

.. contents::
   :local:
   :depth: 2

Prerequisites
-------------

- A valid signed URL generated from GenerateUrl API.
- The image file ready for upload.

Request
-------

**Content Type**: ``multipart/form-data`` or appropriate content type based on the file.

- **Method**: ``PUT``
- **URL**: [Your pre-signed URL]

**Header Parameters**:

- **Content-Type**: 
    - *Type*: String
    - *Description*: The content type of the file being uploaded (e.g., `image/jpeg`, `image/png`).

**Input Parameters**:

- **file**: 
    - *Type*: File
    - *Description*: The image file to be uploaded.

Response
--------

The response will on successful upload will not return any content, but HTTP status code will indicate success.

Status Codes
------------

- **200**: Success - File uploaded successfully.
- **4xx/5xx**: Client/Server Errors.
