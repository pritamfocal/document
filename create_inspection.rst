CreateInspection API
====================

The CreateInspection API is provided by Focalx and can be called by the client's backend system or frontend to create an inspection.

.. contents::
   :local:
   :depth: 2

Prerequisites
-------------

- A valid token is required to call this API.

Request
-------

**Content Type**: ``multipart/form-data``

- **Method**: ``POST``
- **URL**: ``/Create-Inspection``

**Header Parameters**:

- **Authorization**: 
    - *Type*: Bearer Token
    - *Description*: Client must send the token received from the previous API.

- **Content-Type**: 
    - *Type*: multipart/form-data
    - *Description*: The request should be of form data type.

**Input Parameters**:

- **provider**: 
    - *Type*: String
    - *Description*: Customer ID (provided by Client).

- **frame_number**: 
    - *Type*: String
    - *Description*: Customer Frame number (provided by Client).

- **userid**: 
    - *Type*: String
    - *Description*: ID of user in Focalx backend.

- **registration number**: 
    - *Type*: String
    - *Description*: Vehicle plate number.

- **name**: 
    - *Type*: String
    - *Description*: User name.

- **email**: 
    - *Type*: String
    - *Description*: User email.

- **phone**: 
    - *Type*: String
    - *Description*: User phone number.

- **mileage**: 
    - *Type*: String
    - *Description*: Vehicle mileage.

- **meta_data**: 
    - *Type*: String
    - *Description*: JSON data in string format received from client.

- **make**: 
    - *Type*: String
    - *Description*: Car manufacturer.

- **model**: 
    - *Type*: String
    - *Description*: Car model.

- **color**: 
    - *Type*: String
    - *Description*: Color of the car.

- **body_type**: 
    - *Type*: String
    - *Description*: Car body type.

Response
--------

**Response Parameters**:

- **inspection**: 
    - *Type*: Inspection Object
    - *Description*: Contains the inspection results with inspection ID.

- **car**: 
    - *Type*: Car Object
    - *Description*: Car information.

- **car_master**: 
    - *Type*: Car Master Object
    - *Description*: Car properties.

**Inspection Object Details**:

- **id**: 
    - *Type*: String
    - *Description*: Inspection id.

- **latitude**: 
    - *Type*: String
    - *Description*: Latitude for inspection.

[...Repeat for each inspection parameter...]

**Car Object Details**:

- **vin**: 
    - *Type*: String
    - *Description*: Car VIN.

[...Repeat for each car parameter...]

**Car Master Object Details**:

- **year**: 
    - *Type*: String
    - *Description*: Year of the car.

[...Repeat for each car_master parameter...]

Status Codes
------------

- **2xx**: Success
- **400**: Application Error with parameter issue
- **401**: Unauthorized error
- **500**: Server Error

Response Error (when status code is 400)
----------------------------------------

- **error**: 
    - *Type*: String
    - *Description*: This will provide a JSON error indicating that parameters are missing or incorrect.
