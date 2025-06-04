Generate Link API
=================

The Generate Link API allows users to generate a unique application link for provided emails, including optional metadata and site information.

.. contents::
   :local:
   :depth: 2

Request
-------

**Content Type**: ``application/json``

- **Method**: ``POST``
- **URL**: ``/generate-link-api/``
- **Headers**:
    - ``Authorization``: ``Bearer <access_token>``
    - ``Content-Type``: ``application/json``
    - ``Cookie``: ``sessionid=<session_id>`` (optional)

**Input Parameters**:

- **metadata**: 
    - *Type*: String
    - *Description*: Any metadata associated with the request.

- **workflows_list**: 
    - *Type*: String
    - *Description*: Workflows to be triggered (leave empty for none).

- **site**: 
    - *Type*: String
    - *Description*: Site identifier or description.

- **emails**: 
    - *Type*: List of Strings
    - *Description*: List of email addresses to generate the application link for.

Example (request):

.. code-block:: shell

    curl --location 'http://localhost:8000/generate-link-api/' \
      --header 'Authorization: Bearer <your-access-token>' \
      --header 'Content-Type: application/json' \
      --header 'Cookie: sessionid=<your-session-id>' \
      --data-raw '{
        "metadata":"testing",
        "workflows_list":"",
        "site":"testing",
        "emails":["pritam@focalx.ai"]
      }'

Example (request payload):

.. code-block:: json

    {
        "metadata": "testing",
        "workflows_list": "",
        "site": "testing",
        "emails": ["pritam@focalx.ai"]
    }

Response
--------

**Response Parameters**:

- **user**: 
    - *Type*: String
    - *Description*: The email address for which the link was generated.

- **GeneratedMessage**: 
    - *Type*: String (URL)
    - *Description*: The generated application link.

Example (response):

.. code-block:: json

    [
        {
            "user": "pritam@focalx.ai",
            "GeneratedMessage": "https://store.app.develops.focalx.ai/app.html?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5NDc4Mjc0LCJqdGkiOiI0ZDJjNTIyMzEwY2I0ZDg3OTVmOWUyOTlhMTZkMGVmNSIsInVzZXJfaWQiOjI5MX0.vWm1GF7fhZvebwYp9vYUbZDuo3zroRDRu5BatEaRYxg&licencePlate=&vin=&username=pritam@focalx.ai@chamcha&metadata=testing"
        }
    ]

Status Codes
------------

- **2xx**: Success
- **400**: Bad Request (invalid/missing parameters)
- **401**: Unauthorized (invalid or expired access token)
- **5xx**: Server Error

Response Error (when status code is 400)
----------------------------------------

- **error**: 
    - *Type*: String
    - *Description*: Details about the error (e.g., missing required parameters).

Example:

.. code-block:: json

    {
        "error": "Missing required parameter: emails"
    }

