Damage Report API
=================

The Damage Report API is provided by Tenant and will be called by Focalx backend system to push damage reports to Tenant System asynchronously.

.. contents::
   :local:
   :depth: 2

Request
-------

**Content Type**: ``application/json``

- **Method**: ``POST``
- **URL**: ``/DamageReport``
- **Query Parameter**: ``?x-api-key={{api-key}}``

**Input Parameters**:

- **InspectionId**: 
    - *Type*: String
    - *Description*: Identifier of inspection in FocalX.

- **Provider**: 
    - *Type*: String
    - *Description*: Customer ID (provided by Client).

- **framenumber**: 
    - *Type*: String
    - *Description*: Framenumber (provided by Client).

- **UserID**: 
    - *Type*: String
    - *Description*: ID of user in Focalx backend.

- **StartTime**: 
    - *Type*: String
    - *Description*: Date-time of start of the inspection.

- **EndTime**: 
    - *Type*: String
    - *Description*: Date-time when the inspection is finished.

- **RegistrationNumber**: 
    - *Type*: String
    - *Description*: Vehicle plate number.

- **Name**: 
    - *Type*: String
    - *Description*: User name.

- **Email**: 
    - *Type*: String
    - *Description*: User email.

- **Phone**: 
    - *Type*: String
    - *Description*: User phone number.

- **Mileage**: 
    - *Type*: String
    - *Description*: Vehicle mileage.

- **MileageImageFilename**: 
    - *Type*: String
    - *Description*: Guid of the picture with the mileage.

- **OrientationResults**: 
    - *Type*: List of OrientationResultItem
    - *Description*: List of beauty shots of the car.

- **vehicleData**: 
    - *Type*: VehicleItem
    - *Description*: Dictionary of vehicle data.

- **metaData**: 
    - *Type*: String
    - *Description*: JSON data in string format received from client.

**OrientationResultItem Details**:

- **Orientation**: 
    - *Type*: String
    - *Description*: Car Position.

- **ImageFileName**: 
    - *Type*: String
    - *Description*: Guid of the picture.

- **ImageFileURL**: 
    - *Type*: String
    - *Description*: Signed Original image URL.

- **ImageFileDrawURL**: 
    - *Type*: String
    - *Description*: Signed URL for draw picture.

- **ColorType**: 
    - *Type*: String
    - *Description*: Color of the car in string format.

- **Luminous**: 
    - *Type*: String
    - *Description*: String with options like clear-image, blur-image, dark-image, night-image.

- **ImageCharacteristic**: 
    - *Type*: String
    - *Description*: String with options like car, partial-car, dirty-car, rainy-car, snow-car, dark-light.

- **ImageView**: 
    - *Type*: String
    - *Description*: String with options like complete-image, obstructing-view, incomplete-image, door-open.

- **Damages**: 
    - *Type*: List of DamageItem
    - *Description*: List of damages.


**VehicleItem Details**:

- **make**: 
    - *Type*: String
    - *Description*: Car make.

- **model**: 
    - *Type*: String
    - *Description*: Model of the car.

- **mileage**: 
    - *Type*: String
    - *Description*: Mileage of the car.

- **carTotalWeight**: 
    - *Type*: Integer
    - *Description*: Total weight of the car.

- **bodyType**: 
    - *Type*: String
    - *Description*: Body type of the car.

- **engineType**: 
    - *Type*: String
    - *Description*: Engine type of the car.

- **vin**: 
    - *Type*: String
    - *Description*: Vehicle Identification Number of the car.

- **registerNumber**: 
    - *Type*: String
    - *Description*: Registration number of the car.

- **technicalWeight**: 
    - *Type*: Integer
    - *Description*: Technical weight of the car.

- **motorKilometerPerLiter**: 
    - *Type*: Integer
    - *Description*: Mileage of the car in kilometers per liter.

- **variant**: 
    - *Type*: String
    - *Description*: Variant of the car.

**DamageItem Details**:

- **DamageNumber**: 
    - *Type*: String
    - *Description*: Identifier of the damage.

- **MarkerPoint**: 
    - *Type*: String
    - *Description*: Damage coordinates.

- **ZoneId**: 
    - *Type*: String
    - *Description*: Code of the part of the car damaged.

- **PartId**: 
    - *Type*: String
    - *Description*: Damage part code.

- **PartName**: 
    - *Type*: String
    - *Description*: Part name in string format in slug.

- **DamageCategoryID**: 
    - *Type*: String
    - *Description*: Client damage category code.

- **DamageCategoryName**: 
    - *Type*: String
    - *Description*: Category of Damage (e.g., K1, K2, K3, K4, K5).

- **DamageTypeCode**: 
    - *Type*: String
    - *Description*: Client damage type code.

- **DamageTypeName**: 
    - *Type*: String
    - *Description*: Damage names like scratch, tear, dent.

- **OtherDamageImages**: 
    - *Type*: List of Strings
    - *Description*: Array of Guids of picture files with the damage.

- **RepairMethodCode**: 
    - *Type*: String
    - *Description*: Repair method ID. The details are:
        1: [Description of Method 1]
        2: [Description of Method 2]
        3: [Description of Method 3]
        4: [Description of Method 4]
        5: [Description of Method 5]

- **CloseUpImageFilename**: 
    - *Type*: String
    - *Description*: Guid of the picture file with the damage.

- **CloseUpImageFileURL**: 
    - *Type*: String
    - *Description*: Signed URL for downloading this close-up image.

    Example:

    .. code-block:: json

         {
            "InspectionId": "72e18833-bbc7-48a4-af5a-f25402e7de12",
            "ProcessId": "M6S5HFQ82CSY",
            "Provider": "264",
            "FrameNumber": "264",
            "UserID": "",
            "StartTime": "2023-12-14 05:19:40.068629+00:00",
            "EndTime": "2023-12-14 22:07:01.033311+00:00",
            "RegistrationNumber": "CTFG18",
            "Name": "",
            "Email": "",
            "Phone": "",
            "Mileage": "12345",
            "MileageImageFilename": "72e18833-bbc7-48a4-af5a-f25402e7de12",
            "OrientationResults": [
               {
                     "Orientation": "1",
                     "Manual": "False",
                     "ImagePositionMasterName": "front",
                     "OrientationName": "front",
                     "Luminious": "clear image",
                     "ImageChracteristic": ["Car"],
                     "ImageViews": [ "Complete Image"],
                     "ColorType": "Grey",
                     "ImageFileName": "547f36c4-f1e0-4b9a-81f6-506d90ac707e",
                     "ImageFileDraw": "547f36c4-f1e0-4b9a-81f6-506d90ac707e",
                     "Damages": [
                        {
                           "DamageNumber": "38dc46e2-b98c-410e-b5e6-e3cbe084536d",
                           "MarkerPoint": "[472.3683782104364, 476.0058620769277, 488.5853111017721, 494.97661376113183]",
                           "DamageCategory": "",
                           "RepairMethod": "6",
                           "Category": "K4",
                           "CloseUpImageFilename": "None",
                           "DamageName": "dent",
                           "PartName": "bumper",
                           "DamageType": "1",
                           "SparePartId": "1",
                           "PartLocation": "1",
                           "ZoneId": "BB21"
                        },
                        {
                           "DamageNumber": "709e7a5b-5bba-46f8-a2c2-68b6cd4f13f2",
                           "MarkerPoint": "None",
                           "DamageCategory": "",
                           "RepairMethod": "6",
                           "CloseUpImageFilename": "None",
                           "DamageType": "1",
                           "SparePartId": "1",
                           "PartLocation": "1",
                           "ZoneId": "BB21"
                        }
                     ]
               }
            ],
            "vehicleData": {
               "Make": "HYUNDAI",
               "Model": "SANTAFE",
               "Mileage": "12345",
               "CarTotalWeight": "None",
               "BodyType": "SUV",
               "BodySize": "medium",
               "Segment": "None",
               "EngineType": "None",
               "Vin": "P22EAD52NDVJCJHWFSFF",
               "RegisterNumber": "CTFG18",
               "TechnicalWeight": "None",
               "MotorKilometerPerLiter": "None",
               "Variant": "None"
            }
         }


Response
--------

**Response Parameters**:

- **Inspection Id**: 
    - *Type*: String
    - *Description*: [Description of the response parameter].

Status Codes
------------

- **2xx**: Success
- **400**: Application Error with response error
- **401**: Application key error
- **5xx**: Server Error

Response Error (when status code is 400)
----------------------------------------

- **error**: 
    - *Type*: String
    - *Description*: This will provide a JSON error indicating that parameters are missing or incorrect.
