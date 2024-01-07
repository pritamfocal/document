Web SDK Documentation
=====================

This section covers the integration of the Focalx Web SDK/plugin.

Integration via Manual Download
-------------------------------

- **Downloading the Package**:
  - The package is available on the npm repository and can be downloaded from: 
    `https://www.npmjs.com/package/focalxaiinspection`

- **Adding the Package**:
  - Include the following line in your `package.json` file:

    .. code-block:: json

        "focalxaiinspection": "^0.1.0",

- **API Token Generation**:
    - Before showing the FocalX.ai damage guide, generate a token and supply it to the SDK.
    - Refer to the API documentation for token generation: Authentication API.

Integration Process with Package Manager
----------------------------------------

- **Expected Parameters**:
    - The SDK expects the following parameters:

    .. code-block:: javascript

        const carData = {
                    token: accessToken, //Mandatory
                    numberPlate: "Number Plate", //Mandatory
                    carBodyType: "suv",  //optional
                    vin: "3742394ADCS", //optional
                    make: "Make", //optional
                    model: "Model", //optional
                    year: "1919", //optional
                    mileage: "12121222", //optional
                    reg_number: "BB423", //optional
                    user_hash: "sjkf12324", //optional
                    customer_num: "erio32133", //optional
                    frame_num: "343", //optional
                    process_id: "133", //optional
                    meta_data: "Dictionary Data", //optional
                    baseUrl: baseUrl, //Mandatory
                    call_back_url: "https://www.zoomcar.com?success=true&inspectionID=someInspectiondID&registrationNumber=BB2092&error=nil" //Mandatory
        }

- **Parameters Description**:

    -  token: Token that you get from focalx backend, its mandaotry to pass.
    -  numberPlate: Number plate of the car its mandatory to pass.
    -  baseUrl: Based on this url developer can change the environment of the SDK.Developer will get this from focalx
    -  call_back_url: This is the callback url that SDK will call once user finishes the inspection

Usage of Web SDK
----------------

- **Importing and Configuring the SDK**:

  - Import `FocalxAI` from 'focalxaiinspection' and set up the `carData` object as shown in the example.

    .. code-block:: javascript

        import FocalxAI from 'focalxaiinspection';

        const carData = {
            numberPlate: "Number Plate",
            carBodyType: "suv",
            vin: "3742394ADCS",
            make: "Make",
            model: "Model",
            year: "1919",
            mileage: "12121222",
            token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzOTY0NzkxLCJqdGkiOiI0NTIzZmI2NDg2OGY0ZDA0YTU1ZmY0MjBmODI2NDk3ZiIsInVzZXJfaWQiOjV9.ZbhE-w6Ca6jCb4bTZ-dHgVsznktKepbWVwRLQDtjkQk",
            reg_number: "BB423",
            user_hash: "sjkf12324",
            customer_num: "erio32133",
            frame_num: "343",
            process_id: "133",
            meta_data: "Dictionary Data",
            baseUrl: "preprod.backend.focalx.tk",
            call_back_url: "https://www.zoomcar.com/in/mumbai"
        }
        sessionStorage.setItem("carInformation", JSON.stringify(carData));

        function App() {
        return (
            <div className="App">
            <FocalxAI />
            </div>
        );
        }

        export default App;