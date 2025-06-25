MAUI  library Integration
==================================

This guide provides detailed instructions for integrating the Focalx SDK into your .NET MAUI applications.


Prerequisites
-------------

- **Focalx Bindings**:

    Focalx Bindings (provided by Focalx):


    FocalxiOSInspect.csproj


    FocalxAndroidInspect.csproj


Downloading and Adding the SDK
------------------------------

Currently, we support integration via local file paths.
In your MAUI project (e.g., Vascor.csproj), add references to the Focalx libraries as shown below:

.. code-block:: javascript

  <ItemGroup Condition="'$(TargetFramework)' == 'net9.0-ios'">
    <ProjectReference Include="..\FocalxiOSInspect\FocalxiOSInspect.csproj" />
    <!-- Ensure this path points to the FocalxSDK folder -->
  </ItemGroup>

  <ItemGroup Condition="'$(TargetFramework)' == 'net9.0-android'">
    <ProjectReference Include="..\FocalxAndroidInspect\FocalxAndroidInspect.csproj" />
  </ItemGroup>


Usage in the project 
------------------------------

.. code-block:: javascript

    using FocalxiOSInspect;
    using FocalxAndroidInspect;

    const parameters = {
        "auth_token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MzcyMzI4LCJqdGkiOiJjNzY2ZjYzNWUxMzE0MTkxYjlhZWE3ODBiZGQwYjAyZSIsInVzZXJfaWQiOjg0fQ.Ojd4tVmxuR592RYUDBs04WuMBXiQxt-KBnsMYYQMeKc',
        "LocationCode": "LOC34534", 
        "VascorInspectionID": "102938949", 
        "SurveyTypeCode": "04S", 
        "BayLocation": "BAY12", 
        "TransportEquipmentNumber": "CYKS",
        "DeckPositionCode": "DP001" 
    };
        

    FocalxInspect.shared.showFocalx(parameters, (err, result) => {
        // The result will include inspection_id, registration_number, and error (if any)
    });

    //following method gets called when SDK gets dismissed by back button
    func dismissFocalx()  

    //following method gets called when SDK wants to send commands/events to master application
    func inspectionStatus(responceData: String,error:String) 

    //following method gets called when SDK finished scanning the inspections
    func inspectionScanCompleted(responceData: String,error:String) 
        