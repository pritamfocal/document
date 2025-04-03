Inspection Portal and its feature
==================================

This guide outlines the inspection portal functionality and its feature


Inspection portal Overview
-------------

- **Portal Overview**:

     Portal contails the features where it shows all the features that inspection portal support. 
     It supports following types of feature
    -  Dashboard: The dashboard provides a comprehensive view of client inspection statistics, including key metrics such as "Inspection Performed," "Inspected Vehicles," "Users Added," and "Sites Added" within a specified date range. Additionally, it displays overall AI-detected damages and rejected damages for a clear assessment of inspection outcomes.

.. raw:: html

    <iframe src="https://www.loom.com/embed/fab1553283524edfb6d5074a36426363?sid=066e7557-0e78-43ec-8325-7eff9edd63d1"
          style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>


     

Dashboard 
------------------------------

-  **Inspection**:
     - The inspection statistics are presented in a graphical format for the specified date range, displaying the number of inspections "Created" and "Closed"

-  **Damage stats**:
     - The damage statistics are represented in a pie chart format, differentiating the counts for "AI Detected," "Added," and "Rejected" damages


.. raw:: html

    <iframe src="https://www.loom.com/embed/63be0dc7448646089f81f7ffb34210d1?sid=60515f41-bf41-4d91-80c6-93bbc535bd5f"
           style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>

Inspection views
------------------------------

1. **Inspection view and search**:
     - The inspection screen displays all inspections, regardless of the user. It includes a global search feature that allows users to find inspections by entering a registration number.
Additionally, inspections can be viewed based on different timeframes, including Daily, Weekly, and Monthly.
A key feature of this screen is the Advanced Search, which enables users to efficiently filter inspections using various criteria such as Number Plate, VIN, Status, Damage Category, Damage Status, Body Type, Occurrence, and Created By, within a specified date range.

.. raw:: html

    <iframe src="https://www.loom.com/embed/978c137f60804bbfbad4e79049eea413?sid=3da1cc8a-b157-49d0-98cc-9f04ee593ea0"
           style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>

2. **Inspection Report**:
     - The Screen provides inspection report details, how to export pdf report and dynamic form. 

.. raw:: html

    <iframe src="https://www.loom.com/embed/4f8fbbd3fcf44074b60f2f1edbd3a31f?sid=084d8b90-37b0-4e61-ae59-1e54536a0f49"
           style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>

3. **Archive**:
     - The Archive Screen provides access to deleted inspections while ensuring that no inspection data is permanently lost. It allows users to restore deleted inspections by moving them back to the Inspection Screen whenever needed, ensuring easy retrieval of past records.

.. raw:: html

    <iframe src="https://www.loom.com/embed/28c1967d310340099747c1a80f4ef013?sid=eeb5c964-7fc0-4449-9144-ac34da23227a"
            style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>



User views
------------------------------

1. **Creating user**:
     - The User Screen displays user details associated with the specific client account currently logged in. It also provides the functionality to create new users to expand the workforce.
There are two methods for creating a user:
By Official Email ID – Creating a user with login credentials.
One-Time User – Adding a user without login credentials, intended for temporary access.

.. raw:: html

    <iframe src="https://www.loom.com/embed/9f5d7089de1a4eb497c7544aa13fc247?sid=bd010a44-6b60-401a-b755-9aa48d4c7f23"
            style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>

2. **One time link creation**:
     - The One-Time Link user creation process is a simple and efficient method for granting temporary access. By entering the user's email ID, the system generates and sends a login link to their email. The user can then access the application with a single click from the email, without requiring login credentials.
This feature is primarily designed for trial purposes, allowing users to explore the application effortlessly.

.. raw:: html

    <iframe src="https://www.loom.com/embed/3689164416f24819b7e10738a56f4194?sid=fae9323d-71c8-49e8-8a0f-b969d3ffe984"
            style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>


Settings views
------------------------------

1. **Customer settings**:
     - The Settings Page serves as the central hub for configuring all client-specific settings. It allows customization and management of various system preferences to align with the client's requirements.

2. **Submit report**:
     - The Submit Report Setting is a security-focused feature that generates a unique API security key for each client. This ensures that the client’s dashboard remains secure and accessible only to authorized users.

3. **Custom images**:
     - The system includes predefined exterior and interior car images for capturing inspection photos. However, if a customer requires additional specific images beyond the predefined set, they have the flexibility to customize and add "Custom Images" as per their needs.

4. **Create inspection**:
     - When creating an inspection, the client needs to collect essential vehicle details such as Registration Number, Make, Model, etc.
The Car Information Settings allow clients to customize the required fields by enabling or disabling options such as: Registration Number, VIN, Make, Model, Mileage, Body Type, Year.
This ensures that only the necessary vehicle details are requested during the inspection process.
         
5. **Custom workflow**:
     - The Workflow provides a structured and simplified approach to managing inspections by allowing users to:
Capture images efficiently.
Answer required inspection questions.
Review AI-detected damages in the Damage Detail Screen.
All these functionalities are configurable within the Workflow Settings, where users can enable or disable the following options:
AI Guide – Controls the image capturing screen.
Dynamic Form – Manages checklist-related questions.
Damage Detail Screen – Enables reviewing of AI-detected damages.
This flexibility allows clients to tailor the workflow according to their inspection requirements.

6. **Dynamic form and check list**:
     - The Dynamic Form serves as a checklist-based interactive form where users can respond to questions configured by the client.
We support five types of question formats to enhance flexibility in data collection:
True or False
Single Answer Selection
Multiple Answer Selection
Comment Only
Single Image Capturing
Multiple Image Capturing
Additionally, for image-related question types, a comment box can be configured, allowing users to provide additional details along with the captured images.

7. **Personal information on inspection**:
     - The Personal Information setting allows clients to configure whether user details should be collected during the inspection process.
Clients can enable or disable the following fields based on their requirements:
Name
Email
Contact
This ensures flexibility in gathering necessary user information as needed.

8. **Report showing options**:
     - The Report Display Setting is a key feature that allows clients to generate a PDF report containing all relevant details of an inspected vehicle, including detected damages. This report helps clients easily validate inspection results.
Additionally, the PDF report is configurable, enabling clients to customize the information displayed. The configurable settings include:
Source of Damage
Damage Type
Severity
As an added benefit, clients can also enable or disable the option to download damaged images and car images within the PDF report, ensuring flexibility based on their reporting needs.

9. **Bucket storage information**:
     - We have predefine car image positions like `right-front`	
      if you to add taking different image than the specified position that you want inspector to take then you will add custome images


.. raw:: html

    <iframe src="https://www.loom.com/embed/815a1859ee7b4cdbbde3aeea99f49eac?sid=2ba073c5-c15d-492a-ad6c-7fc1c0dabc9c"
            style="margin-top: 40px; margin-bottom: 20px;"
            width="640"
            height="360"
            frameborder="0"
            webkitallowfullscreen
            mozallowfullscreen
            allowfullscreen></iframe>

