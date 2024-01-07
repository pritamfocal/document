Native Android SDK Integration
==================================

This guide describes the steps to integrate the FocalxAI SDK into your Android Studio project.


Prerequisites
-------------

- **Focalx library**:
    -  It will be provided by Focalx.
    -  Focalx.ai  supports os versions from Android JellyBean (4.3) API Level 16 to Android 11 API Level 30!


1. Adding the SDK
-----------------

- **Download the SDK**:
   - Download the SDK compatible with your requirements: [Download SDK](#link-to-download).
   - Unzip the file and drag the `focalx-lib.aar` file to the "libs" folder in your Android Studio project.

2. Configuring build.gradle
---------------------------

- **Add FocalX Dependency**:
   - Update the `build.gradle` of your app to include the following dependency:

     .. code-block:: gradle

        implementation(name:'focalx-lib', ext:'aar'){ transitive = true; }

   - Note: If FocalX is already integrated into your project, re-sync the project with Gradle.

3. Starting the FocalX SDK
--------------------------

- **Include the SDK in Your App**:
   - Include the following imports wherever you want to present the damage detection model:

     .. code-block:: kotlin

        import com.focalx.focalxlib.sdk.CameraType
        import com.focalx.focalxlib.sdk.FocalxInspectionCallback
        import com.focalx.focalxlib.sdk.initSDK
        import com.focalx.focalxlib.sdk.startInspection

- **API Token**:
   - Before showing the FocalX.ai damage guide, create a token and supply it as a parameter to the SDK.
   - Check the API documentation for token generation: [API Token Generation](#link-to-api-token-generation).

4. Implementing SDK Dependencies
--------------------------------

- **Add Required Dependencies**:
   - Include the following dependencies in your `build.gradle` file:

     .. code-block:: gradle

        // Add library
        implementation fileTree(dir: "libs", include: ["*.jar", "*.aar"])

        // Images
        implementation 'com.github.bumptech.glide:glide:4.13.2'
        implementation 'io.coil-kt:coil:2.2.1'

       //CameraX
       implementation 'androidx.camera:camera-camera2:1.2.0-beta02'
       implementation 'androidx.camera:camera-core:1.2.0-beta02'
       implementation 'androidx.camera:camera-extensions:1.2.0-beta02'
       implementation 'androidx.camera:camera-lifecycle:1.2.0-beta02'
       implementation 'androidx.camera:camera-view:1.2.0-beta02'

       //Network
       implementation 'com.squareup.retrofit2:converter-moshi:2.9.0'
       implementation 'com.squareup.retrofit2:retrofit:2.9.0'
       implementation 'com.squareup.okhttp3:okhttp:5.0.0-alpha.9'
       implementation 'com.squareup.okhttp3:logging-interceptor:5.0.0-alpha.9'
       implementation "com.squareup.retrofit2:converter-gson:2.9.0"
       implementation 'com.squareup.moshi:moshi:1.14.0'
       implementation 'com.squareup.moshi:moshi-kotlin:1.14.0'
       kapt 'com.squareup.moshi:moshi-kotlin-codegen:1.14.0'

5. Using the SDK in an Activity
-------------------------------

- **Initialize and Start Inspection**:

   - Use the `initSDK` and `startInspection` methods in your activity to start the guiding system.

     .. code-block:: kotlin

        // Kotlin code example for initializing and starting the inspection
        
        initSDK(object : FocalxInspectionCallback {
                override fun onInspectionCompleted(
                    inspectionId: String,
                    registrationNo: String,
                    error: String
                ) {
                    Log.d("TAG", "inspectionId: $inspectionId")
                    Log.d("TAG", "registrationNo: $registrationNo")
                    Log.d("TAG", "error: $error")
                }
         })
        startInspection(activity = this, registrationNo = "BB30945",vin="ADHKSHDSH328973792",mileage="343434",user_hash="jadjkflasjdfsty",frame_num="1","process_id","133",meta_data:"Dictionary Data",hasCustomImages = false, cameraType = arrayListOf(CameraType.CAMERA_POSITION_FRONT))

- **Custom Image Parameters**:
   - When `custom_images` is set to `false`, all 16 images will be automatically taken.
   - If `true`, specify the image positions for the user to take, using parameters such as 
    
     .. code-block:: kotlin
        
           // Following Custom image parameters you can send
            CAMERA_POSITION_FRONT
            CAMERA_POSITION_FRONT_RIGHT
            CAMERA_POSITION_RIGHT_FRONT
            CAMERA_POSITION_RIGHT_REAR
            CAMERA_POSITION_REAR_RIGHT
            CAMERA_POSITION_REAR
            CAMERA_POSITION_REAR_LEFT
            CAMERA_POSITION_LEFT_REAR
            CAMERA_POSITION_LEFT_FRONT
            CAMERA_POSITION_FRONT_LEFT
            CAMERA_POSITION_DASHBOARD
            CAMERA_POSITION_DRIVER_SEAT
            CAMERA_POSITION_FRONT_PASSENGER
            CAMERA_POSITION_LEFT_REAR_PASSENGER
            CAMERA_POSITION_RIGHT_REAR_PASSENGER
            CAMERA_POSITION_TRUNCK

