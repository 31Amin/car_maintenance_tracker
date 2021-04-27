# **Car Maintenance Tracker** 
<img src="/assets/readmeAssets/car-mtn-tracker.jpg">

## Index

- [Introduction](#Introduction)
- [Project Motivation](#Project_Motivation)
- [UX](#UX) 
    - [User Stories](#User_Stories)
    - [Wireframes](#Wireframes)
- [Database](#Database) 
- [Features](#Features)
    - [Existing Features](#Existing_Features)
    - [Future Enhancements](#Future_Enhancements)
- [Technologies Used](#Technologies_Used)
- [Testing](#Testing)
    - [UX Testin](#UX_Testing)
    - [Functional Testing](#Functional_Testing)
    - [User testin](#User_Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)
    - [Content](#Content)
    - [Media](#Media)
    - [Acknowledgements](#Acknowledgements)

- - - -
## **<ins>Introduction</ins>**
This is the third of my milestone projects, as part of the Code Institute full stack developer course  The project car maintenance tracking tool. It has a front end using Flask framework, 
with Materlize CSS library for the majority of the styling. The project also contains, custom HTMl, CSS & Javascript.

## **<ins>Project_Motivation</ins>**

The car maintenance tracker site is designed to be a application that allows organisations or individuals to record and track maintenance carried out on their vehicles.
The system would have two aspects to it;
1. User Side. <br>
    The user would have the ability to register a car(s) and input maintenance records for the car. 
2. Admin Side. <br>
    The administrator would have the ability to add Garages (which are approved for use) and deactivate them from user view if required. 

The concept was to create an application, that was easy to use, accessible on all devices types and would require minimum training for users. 

## **<ins>UX</ins>**
For the UX, I choose the Materialize CSS library as the primary CSS elements, applying custom CSS where required. The design of the applications, was a basic design on white background. 
As the applications is a functional one I felt the simpler design with minimal graphics was best. The app is used to input data (records), edit and view the records so I don't expect the 
user to be on the site longer than is necessary for them to complete the task. 
In the base HTML, a common header and footer is used, across all the pages, the only element that vaires are the page links depending on the user type and session cookie. 


### <ins>User_Stories</ins>

**Fleet Owner;**
1. Having a fleet of company cars, I want a single tool, where all the maintenance records are logged.
2. Company cars are operated by employees, service & maintenance is arranged by employee, so they system should allow for the employee to input the records & update records.
3. There is a list of approved garages for service and maintenance to be carried out, a list of of the garagges should be available to the employee when entering the record and the list should be able to be updated by the admin. 

**Record Owner;**
1. Simple form when entering data. 
2. Ability to register a car to the system.
3. View of the records entered by me, with the ability to view, edit & delete as required. 

**Site Administrator Owner;**
1. Ability to view all records entered in to the system. 
2. Access to add garages or edit the current list in the DB.
3. Ability to edit or delete records if required from the system.

### <ins>Wireframes</ins>


| Title | Link to Wireframe (pdf) |
| --- | --- |
| Title 1 | add link here |

[Index](#Index)
- - - -
## **<ins>Database</ins>**
The application, would require a databse backend, I chose mongoDB for the project. 
The database has four collections within it;

**Directory;**

The directory collection holds all the suer data, records are created when a user registers on the siet.
Data in the collection;
- Name
- e-mail address
- user Name
- password (stored in hashed format for security)

**Cars;**
The cars collections, holds data on cars registered on the site. Users can register their cars and only registered cars are avilable to create maintenance records for.
Data in the collection;
- Car Registartion
- make
- model
- user
- e-mail
Note: user & e-mail are autopopulated to the DB based on logon user at the time of registration.


**Garage;**
The garages collection has a list of garages that can be used when creating a record. Only the Admin can add or edit the list of gagrages. 
Data in the collection;
- Garage Name
- Garage Contact Name
- Gargage Contact Phone No.
- Garage Status (active, when available for selection by user)


**Maintenance;**
The maintenance collection is populated with the records created by users. 
Data in the collection;
- Car Registartion (user can only selected pre-registered under their username)
- Car make - Populated from Car collection based on reg number selected
- Car Model - same as car make.
- usename - based on the user logged when the record is created
- Service Date - user input as the time of record creation
- Service cost - user input as the time of record creation
- Service Paid - user input as the time of record creation, can be yes / no
- Service Description -  - user input as the time of record creation short description of service
- Odometer Reading  - user input as the time of record creation
- Garage Name - selected from list of active garages in garage collection
- Garage Contact - populated from Garage collection based on reg number selected
- Garage Phone No. - as garage name above
- Service Items - as garage name above

<img src="/assets/readmeAssets/collections_mongoDB.jpg">

[Index](#Index)
- - - -
## **<ins>Features</ins>**

### <ins>Existing_Features</ins>
- 1
- 2
- 3
- 4



### <ins>Future_Enhancements</ins>


[Index](#Index)
- - - -
## <ins>Technologies_Used</ins>
**Balsamiq**    https://balsamiq.com/wireframes/
- Basamiq was used in the design phase to create wireframes of the proposed web site.

**Github** https://github.com/
- Github is the repository used for version control & storage of the project.
- Github pages was used for the deployment of the site.

**Gitpod** https://www.gitpod.io/
- Gitpod was the IDE used for the development throughout the project.

**Bootstrap** https://getbootstrap.com/
- Bootstrap library was chosen for the initial layout & to provide responsiveness across devices sizes, layout was customised on top of bootstrap.

**Google Maps API** https://cloud.google.com/maps-platform/
- Google Maps API to create the map
- plotting the locations based on location data.

**Google Fonts** https://fonts.google.com/
- Google fonts provided fonts for the project (Roboto Condensed & Serrat)

**Font Awesome** https://fontawesome.com/
- Icons used through the web site are sourced from Font Awesome

**W3C Validation Service** https://validator.w3.org/
- HTML & CSS code was checked on W3C validator at the end of the project.

**HTML Formatter** https://webformatter.com/html
- HTML code was run through HTML formatter to fix any indentation issues.

**ami.responsivedesign** http://ami.responsivedesign.is/#
- The project was tested on ami.responsivedesign
- image used in readme file was taken from ami.responsivedesign site

**w3schools** https://www.w3schools.com
- For addtional code explanations & features to use.


[Index](#Index)
- - - -
## <ins>Testing</ins>


### <ins>UX_Testing</ins>
As part of the UX testing all pages were tested for the following criteria;
1. Pages renders on the device, with now obvious distortion.
2. All colours and text is consistent and displays well to the user
3. All links within the page work as expected
4. All fields, that should be accessible for editing / adding data work as expected
5. Any buttons on the page are accessible and displayed appropriately for the screen size.
6. Any other issues the tester sees related to UX. 

| Page | Desktop | Tablet | Mobile | Issues |
| --- | --- | --- | --- | --- |
|register|Pass|Pass|Pass|Link below register box failed on live site, link was for git pot test site.|
|login|Pass|Pass|Pass|Link below register box failed on live site, link was for git pot test site.||
|tracker|Pass|Pass|Pass|Some modifications were made to better display the lists. One column was removed from the lits of records for display on mobile to iprove the lay out|
|detailed information|Pass|Pass|Pass|The cards on the top of the page, were differnt sizes depending on the data from the record, set a min height to ensure they all remain the same height.|
|add record|Pass|Pass|Pass||
|edit record|Pass|Pass|Pass||
|manage garages|Pass|Pass|Pass||
|add car|Pass|Pass|Pass|spelling error on text above form.|
|user profile|Pass|Pass|Pass||

**Note:** Early in testing, it was obvious that there were issues with the site on a table devise. 
Testing was suspended and all pages were updated with addtionl size for medium devices to improve the layout on a tablet device. 
Testing, was resumed after this fix was applied to all pages. 

[Index](#Index)
### <ins>Functional_Testing</ins>

**Register (register.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Fields are accesable|Fields should accecp data and validate for min requirements set. |Pass||
|Register Button|Button should collect data from from and create an account.<br> Data should be validated with DB to ensure userid does not already exist|Pass||

**Login (login.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Fields are accesable| The username and password accecpt data from the user|Pass||
|login Button|Button logs user on and prsents message if there is an issue. Redirects user to profile page upon longin|Pass||

**User profile (userprofile.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Data Check|All data is correct for the logged in user|Pass||

**Maintenance Records (tracker.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Check data is reterived and populated from DB| Rsults shoud include all cars registered to a user with list of records for each car listed|Pass|Some UX detailed in UX Testing section|
|Test Details button|Button should launch detailed records page for selected record and populate all data|Pass|None|

**Service Record (detailed record.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|All data populates|Validate that all data is populating, the correct data is populating|Pass|None|
|Return Button|Retuen button should take the user back to the main record page|Pass||
|Edit Button|The edit button should take the user to the edit record page and populate the correct record information|Pass|Inital issues, with the two drop down menue, the options were populating but the information from the selected record was now <br> Updated to check the list of the selected data and mark as selected when found|
|Delete Button|Open a modal to confirm deletion|Pass|Note: Delete button does not process and DB action, it onlys launches the modal for confirmation.|
|Confirmation Modal<br>1. Confirm it opens correctly <br> 2. Test No button. <br> 3. Test yes button.<br> 4. Confirm the correct record is deleted and no other record is effected|Selecting No on the confirmation panel should retun the user to the edit screen with no action take <br> selecting yes should initiate the update to the DB to delete the record. The selected record should be removed from the DB.|Pass|Page & functions work as expected|

**Add Maintenance Record (addrecord.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Drop down - Cars|Only cars registered to the a user should be shown in the list|Pass||
|Drop down - Garages|Only active garages should show in the list|Pass|One issue to resolve, Garages that were disabled, and should not be selectable where showing in the list. <br> updated to the DB query in Python to only pull records with active flag set.|
|Date Picker|Displays and allows date to be selected|Pass||
|Toggle Switch|Toggles on / off|Pass||
|+ - Buttons|Add / Remove lines from the detailed list section|Pass|Opted to hide the - (remove) button on load, as its only needed if user adds line they then want to remove.|
| Add Record Button|Collects all data & adds new record to the DB|Pass||


**Edit Record (edit_record.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Fields Accecpt Data|data can be entered with out issue|Pass|Had to fix issue on service cost field, it was only taking numbers but as filed for cost, it needed to take up to two desimal places if requried. <br> added step=".01" to the field.|
|Data|All record data is correctly entered to the form|Passed|See above for inital issue on reg no & garage fields|
|Ediable|All data fields can be edicated|Pass|All fields where tested to ensure they could be edited|
|Return Button|Returns returns user to detailed record page|Pass||
|+ / - buttons|Ensure buttons work to add remove lines|Pass|Save button, sent the edited data to the DB and updated the correct record|
|Save Chnage Button|Sends the updtes to the DB and saves the updated record|Pass| Initaly failed, <br> the initial page was a copy of the add record and the - (remove button) was hidden, updated JS to not hide on edit page. <br> Due to the way the buttons were coded in the add record page, JS had to be updated to allow them function on edit page.|

**Edit Add Car (addcar.html)**
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Fields are accessable & function||||
|Drops downs are populated with correct data<br> User should see onl cars register to there userid. <br>only garages marked as active should be avaliable for slection|Pass|||
|+ / - Buttons|Buttons should add or remoove lines from the Form.|Pass||
|Add record Button|Button should colleect the data from the form and create a new record in the DB and take the user to the maintenance record page|Pass||

**Manage Garages Record (add_garage.html)**
Manage Garage pages has two functions, 
1. Add a new garage to the DB
2. Update existing garages to activate or deactive them.
    (With only active garages being avaliable for slection by users. )

| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Add garage form, fields are accessable|Fields are accessable and can be filled out.|Pass||
|Button|Button collects data from Form and creates a record in the DB.|Pass||
|List of Garages is displayed and accessable|List canb be read and button shows|Pass|Initaly, the list was not working on mobile and table, it was not responsive and the button was off the phone screen<br> updated the table to a responsive class table from Materlize.|
|Activate / Deactivate Button|The button should toggle the status of the garage and reload the page|Pass||

[Index](#Index)

### <ins>User_Testing</ins>

[Index](#Index)
- - - -

## <ins>Deployment</ins>
The project was developed using GitHub as the repository and I choose to deploy the live project on GitHub Pages,
The live site can be accessed at https://meltaylor78.github.io/holiday_planner/

**Important Note**
The main data for the locations and data that drives the interactive map are contained in the location.js file.
This file drives the menus for the map. Ensure this file remains correctly linked if you deploy the site or make a local copy of the repo.

**To complete the deployment;**
- From the Github repository 
- Navigate to the settings tab on the top of the repository page
- Scroll down to the section GitHub Pages. 
- In this GitHub Pages section, complete the deployment selection;
- Select the Branch to deploy from the first menu
    -	Select the folder from the second menu
    -	Save the settings
Further updates can be made, such as custom domain and enforce HTTPS. I did not opt for a custom domain but did select to enforce HTTPS 
for the additional security it offers. 

GitHub also provides the option to clone the repository, cloning allows you to make a local copy of the repository on your machine. 
You can complete this using the code drop down menu to get details to clone the repositor. You can find more information on how to clone a 
repository on GitHub Docs [Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)


[Index](#Index)
- - - -

## <ins>Credits</ins>
The developers of the Holiday Planner site would like to thank all those who contributed directly or indirectly to the development of the site, or 
through providing media and content for the site.

- - - -

| Details | Site | Link |
| --- | --- | --- |
| Discover Ireland images & video | Discover Ireland | https://www.discoverireland.ie/ |

In addtion to the list aboved, see the [Technologies Used](#Technologies_Used) and the [Acknowledgements](#Acknowledgements) section for others that we would like 
to extend our thanks and apperication to.

[Index](#Index)
- - - -

### <ins>Media</ins>

| Details | Site | Link |
| --- | --- | --- |
| Google Maps | Google Maps API | https://cloud.google.com/maps-platform/ |
| Video - Ireland – a luxury destination |  Discover Ireland - YouTube | https://www.youtube.com/watch?v=rvSdyIhpdrM&feature=youtu.be |
| Images | Discover Ireland | https://www.discoverireland.ie/ |


[Index](#Index)
- - - -

### <ins>Acknowledgements</ins>
| Name | Acknowledgement | Acknowledgement |
| --- | --- | --- |
| Rahul Lakhanpal | Project Mentor | Rahul provided the advice & input needed to develop the site. He also guided me with the layout and ascetics to ensure a modern look and feel. |
| Caroline Taylor | Content Provider | Helped to source images and content for the site. Reviewed included text|
| Caroline Taylor | User Acceptance Testing | Provided user functional testing and user acceptance testing |
| Discover Ireland | Content | For images and video content included |

[Index](#Index)
- - - -