
Authentification API
============

The GetToken API is provided by Focalx and is called by the client's backend system to obtain a Focalx token. This token must be passed back to the Focalx plugin to access the service. The token is valid for 2 hours.

.. contents::
   :local:
   :depth: 2

Prerequisites
-------------

- IP whitelisting is required.

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
            "client_key": "dfdfdfduyy383dsfd",
            "client_secret": "6c6b9652-b696-45e4-b3d7-fd1b222521bc",
            "user_hash": "3f009d72559f51e7e454b16e5d0687a1"
        }

    AES-256 encrypted JSON containing a client key (string), client secret (string), and user email hash (MD5 hash). The client key, client secret, and encryption private key for encryption will be shared by Focalx.

- **pubKey**:
  - *Value*: String
  - *Description*: Provided by Focalx.

Response
--------

**Response Parameters**:

- **token**:
  - *Value*: User token
  - *Description*: The token provided to the user.
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
