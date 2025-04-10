App in app Documentation
=====================

This section covers the communication between application to application or deeplinking

Integration 
-------------------------------

- **API Token Generation**:

    - Before showing the FocalX.ai application guide, generate a token and supply it to the application using Deeplinking.
    - Refer to the API documentation for token generation: Authentication API.

- **Expected Parameters**:

    - The Deeplinking expects the following parameters:

For iOS

    .. code-block:: 


        com.focalx.auto://deeplinkingapp?reg_number=BB20972&vin=TMBJH65JXB3105096&mileage=1323232&token=Vivsui5Ik&user_hash=89A18CD&customer_num=81&frame_num=275&callbackURl=com.customerapp.com://&browser_type=chrome

For Android

    .. code-block:: 

        com.focalx.inspection://deeplinkingapp?reg_number=BB20972&vin=TMBJH65JXB3105096&mileage=1323232&token=Vivsui5Ik&user_hash=89A18CD&customer_num=81&frame_num=275&callbackURl=https://linkforcustomerawebsite&browser_type=chrome

For browser

    .. code-block:: 

        com.focalx.auto://deeplinkingapp?reg_number=BB20972&vin=TMBJH65JXB3105096&mileage=1323232&token=Vivsui5Ik&user_hash=89A18CD&customer_num=81&frame_num=275&callbackURl=https://linkforcustomerawebsite&browser_type=chrome
  

- **Parameters Description**:

    -  token: Token that you get from focalx backend, its mandaotry to pass.
    -  numberPlate: Number plate of the car its mandatory to pass.
    -  baseUrl: Based on this url developer can change the environment of the SDK.Developer will get this from focalx
    -  call_back_url: This is the callback url that our application will use for opening your application

