React Native  library Integration
==================================

This guide outlines the steps for integrating the Focalx React native into your applications.


Prerequisites
-------------

- **Focalx library**:
    -  It will be provided by Focalx.


Downloading and Adding the SDK
------------------------------

We are at the moment supporting integration via local file path

Go to devDependancies in your package.json and all our library path like following

    "react-native-focalx-inspect": "link:../"



Usage in the project 
------------------------------

.. code-block:: javascript

    import FocalxInspect from 'react-native-focalx-inspect';

    const custom_images = {
            "front":true,
            "front-right":true,
            "right-front":true,
            "right-rear":true,
            "rear-right":true,
            "rear":true,   
            "rear-left":true,
            "left-rear":true,
            "left-front":true,
            "front-left":true,
            "dashboard":false,
            "driver-seat":true,
            "front-passenger":true,
            "right-rear-passenger":true,
            "left-rear-passenger":true,
            "trunck":true,
            "top":true
        }

        const jsonObject = {
            registration_num: 'BB20972',
            vin_number: 'BVSFF132438430843',
            model_name: 'Skoda',
            make: 'Fabia',
            mileage: '113000',
            year: '2010',
            auth_token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MzcyMzI4LCJqdGkiOiJjNzY2ZjYzNWUxMzE0MTkxYjlhZWE3ODBiZGQwYjAyZSIsInVzZXJfaWQiOjg0fQ.Ojd4tVmxuR592RYUDBs04WuMBXiQxt-KBnsMYYQMeKc',
            take_custom_images: false, //Keep it false unless you want controll what images to take
            custom_image_set: custom_images,
        };
        
        FocalxInspect.showFocalx(jsonObject, (err, r) => {
            console.log(r);
            //the result will contain inspection_id, registration_number and error
        });

