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

    Example :

       .. code-block:: form-data

            curl --location --globoff --request PUT '{{genarated_url}}' \
            --header 'Content-Type: image/jpeg' \
            --data '@/Users/test/Downloads/1bcd3bb2-d712-4e11-b3a9-5eedc3e28955_09e800a6-ffd0-4282-9c71-034f68e0b164.jpg'


Response
--------

The response will on successful upload will not return any content, but HTTP status code will indicate success.

Status Codes
------------

- **200**: Success - File uploaded successfully.
- **4xx/5xx**: Client/Server Errors.


.. raw:: html

    <iframe src="https://www.loom.com/embed/8f1a21ce57f3487bb3d9e49f26c205aa?sid=5ddd4245-14bc-4995-af44-65fa8bc25340"
            style="margin-top: 40px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>