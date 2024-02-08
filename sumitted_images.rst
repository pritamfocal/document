Final Inspection Submision API
================

This API allows clients to inform focalx that they have uploaded all the images.

.. contents::
   :local:
   :depth: 2

Prerequisites
-------------

- A valide URL and Token
- The Token to send in the header that you have received in Authention API

Request
-------

**Content Type**: ``application/json``.

- **Method**: ``POST``
- **URL**: {URL}/api/v2/service/inspections/{{inspection_id}}/submitImages/

**Header Parameters**:

- **Authorization**: 
    - *Type*: Bearer Token
    - *Description*: Client must send the token received from the previous API.

- **Content-Type**: 
    - *Type*: application/json
    - *Description*: The request should be of JSON data type.

- **Content-Type**: 

    - Empty

    Example :

       .. code-block:: form-data

        curl --location --request POST {URL} \
        --header 'Authorization: Bearer Token' \
        --data ''

Response
--------

The response will on successful upload will not return any content, but HTTP status code will indicate success.

Status Codes
------------

- **200**: Success 
- **4xx/5xx**: Client/Server Errors.
