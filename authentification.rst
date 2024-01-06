
Authentification API
============

The GetToken API is provided by Focalx and is called by the client's backend system to obtain a Focalx token. This token must be passed back to the Focalx plugin to access the service. The token is valid for 2 hours.

.. contents::
   :local:
   :depth: 2

Prerequisites
-------------

- secrete keys: it will be provided by focalx

Request
-------

**Content Type**: ``application/json``

- **Method**: ``GET``
- **URL**: ``/GetToken``

**Header Parameters**:

- **auth**: 
  - *Value*: AES-256 encrypted JSON value.
  - *Description*: Contains client key, client secret, and user email hash in the following format:

    .. code-block:: json

        {
            "client_key": "adbsk-sfghid77-fdfd",
            "client_secret": "sdsdsds-b696-dssd-b3sdsd7-fd1bdsds222521bc",
            "user_hash": "3f009d725ss9f51e7ess454b16e5d0sds687a1"
        }

    AES-256 encrypted JSON containing a client key (string), client secret (string), and user email hash (MD5 hash). The client key, client secret, and encryption private key for encryption will be shared by Focalx.

- **pubKey**:
  - *Type*: String
  - *Description*: Provided by Focalx.

Response
--------

**Response Parameters**:

- **token**:
  - *Type*: Access Token
  - *Description*: The token provided to the client for accessing other APIs.
- **expiry_time**:
  - *Value*: Date Time
  - *Description*: The expiry time of the token.

Status Codes
------------

- **200**: Success
- **401**: Application Error with client key issue
- **402**: Application Error with client secret issue
- **403**: Application Error with public key issue
- **500**: Server Error
