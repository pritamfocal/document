Authentication API
==================

The GetToken API is provided by Focalx and is called by the client's backend system to obtain a Focalx token. This token must be passed back to the Focalx plugin to access the service. The token is valid for 2 hours.

.. contents::
   :local:
   :depth: 2

Prerequisites
-------------

- **Secrete keys**:
    - *Type*: String
    - *Description*: It will be provided by Focalx.

Request
-------

**Content Type**: ``application/json``

- **Method**: ``GET``
- **URL**: ``/GetToken``

**Header Parameters**:

- **auth**: 
    - *Type*: AES-256 Encrypted JSON
    - *Requirement*: Mandatory
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
    - *Requirement*: Mandatory
    - *Description*: Provided by Focalx


    example (request): 

        .. code-block:: json

            curl --location 'https://{url}/?clientKey={provided by focalx}' \
            --header 'auth: 7zqTet0zah83+ZH' \
            --header 'pubKey: ssss==' \
            --data ''

Response
--------

**Response Parameters**:

- **token**:
    - *Type*: Access Token
    - *Description*: The token provided to the client for accessing other APIs.

- **expiry_time**:
    - *Type*: Date Time
    - *Description*: The expiry time of the token.

    example (responce):
    
        .. code-block:: json

            {
                "token": "eyJ0eXAiOiJKV1",
                "expiry_time": "5 days, 0:00:00"
            }

Status Codes
------------

- **200**: Success
- **401**: Application Error with client key issue
- **402**: Application Error with client secret issue
- **403**: Application Error with public key issue
- **500**: Server Error
