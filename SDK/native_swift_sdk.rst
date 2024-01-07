Native Swift SDK Integration
==================================

This guide outlines the steps for integrating the Focalx Swift SDK into your native iOS applications.


Prerequisites
-------------

- **Focalx library**:
    -  It will be provided by Focalx.
    -  Focalx.ai supports os versions from iOS 10 and above!


Downloading and Adding the SDK
------------------------------

1. **Download the SDK**:
     - Follow the below link to download the SDK compatible with Swift 5.2 or above: [Download Link](#).

2. **Add the SDK to Your Project**:
     - Unzip the file and drag the `FocalxSDK.xcframework` directory to the "Frameworks" section in your Xcode project tree.

Configuring the Xcode Project
-----------------------------

1. **Select Your Project**:
     - In your Xcode project, select your application project in the Project Navigator (blue project icon) to navigate to the target configuration window.
     - Select the application target under the "Targets" heading in the sidebar.

2. **Add the Framework**:
     - In the General panel tab, click on the "+" button under the "Frameworks, Libraries, and Embedded Content" section.
     - Find `FocalxSDK.xcframework` nested inside the "Frameworks" section.
     - Select `FocalxSDK.xcframework`, click "Add", and ensure you select the "Embed & Sign" option.

Implementing the SDK in Your App
--------------------------------

- **Include the SDK**:
    - In your app, wherever you want to present the damage detection model, include the SDK.
    - For Objective-C: `@import FocalxSDK;`
    - For Swift: `import FocalxSDK`

- **API Token Generation**:
    - Before showing the FocalX.ai damage guide, create a token and supply it to the SDK.
    - Refer to the API documentation for creating a token: [API Token Generation](#).

- **Integration Example**:

    - For Objective-C and Swift, follow the provided code examples to integrate the SDK functionality.

    .. code-block:: objective-c

        // Objective-C Example Code Here
         NSMutableDictionary *dictionary = [NSMutableDictionary dictionaryWithObjectsAndKeys:
                        "token":"SDK token got from backend",
                        "reg_number":"BB423",
                        "vin":"3742394ADCS",
                        "mileage":"122323",
                        "user_hash":"sjkf12324",
                        "customer_num":"erio32133",
                        "frame_num":"343",
                        "process_id":"133",
                        "meta_data":"Dictionary Data",
                        "custom_images":true,
                        "front_image":true, 
                        "front_right_image":true]

        // only token  parameter is Mandatory in above dictionary
        [FocalxSDK showDamageGuideWithParams:self, parameters:dictionary];

        // App (Self object) can implement the call back Delegate / protocol with class name  FocalxcallBackResult, which has following methods.

        - (void)dismissFocalx;   // this method gets invoked, when ever user comes out of the SDK without completing the  inspection.

        - (void)inspectionCompletedWithInspectionID:(NSString *)inspectionID regNumber:(NSString *)regNumber  error:(NSString *)error; // this method gets invoked, when ever user comes out of the SDK after completing the inspection.

        -   **Note**

            self here is the current controller  from where you want to  present DamageGuide


    .. code-block:: swift

                // Swift Example Code Here
                let dictionary = ["token":"SDK token got from backend","reg_number":BB423,"vin":3742394ADCS,"mileage":122323,"user_hash":"sjkf12324","customer_num":"erio32133","frame_num":343,meta_data:"Dictionary Data","custom_images":true,"front_image":true, "front_right_image":true]

                FocalxSDK.showDamageGuideWithParams(caller: self, parameters: dictionary)

                // App (Self object) can implement the call back Delegate/protocol with class name  

                FocalxcallBackResult

                //Has following methods.

                func dismissFocalx()  // this method gets invoked, when ever user comes out of the SDK without completing the  inspection.

                func inspectionCompleted(inspectionID: String,reg_number:String,error:String) //  this method gets invoked, when ever user comes out of the SDK after completing the inspection.
             
                // When you send the custom_images as false you dont need to specify other images that you want to take it will automatically take all 16 images
                // When custom_images is true, we need to pass the image positions that you want user to take

                // Following Custom image parameters you can send when you want to customized which pics user should take
                let front_image = true
                let front_right_image = true
                let right_front_image = true
                let right_rear_image = true
                let rear_right_image = true
                let rear_image = true
                let rear_left_image = true
                let left_rear_image = true
                let left_front_image = true
                let front_left_image = true
                let dashboard_image = true
                let driver_seat_image = true
                let front_passenger_image = true
                let right_rear_passenger_image = true
                let left_rear_passenger_image = true
                let trunck_image = true

- **Custom Image Parameters**:
  - When `custom_images` is set to `false`, all 16 images will be automatically taken.
  - If `true`, you need to specify which images the user should take.

- **App Transport Security (ATS)**:
  - `NSAllowsArbitraryLoads`: This Boolean value is used to disable ATS for domains not listed in `NSExceptionDomains`. 

Remember to follow best practices for secure network connections in your app.
