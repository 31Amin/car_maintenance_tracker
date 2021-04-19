# **Holiday Planner** 
<img src="https://t4.ftcdn.net/jpg/00/57/93/05/240_F_57930538_Ytnz8Lk6JnQc1GA1cPfFVJ39o2KBBFUa.jpg">

## Index

- [Introduction](#Introduction)
- [Project Motivation](#Project_Motivation)
- [UX](#UX) 
    - [User Stories](#User_Stories)
    - [Wireframes](#Wireframes)
- [Features](#Features)
    - [Existing Features](#Existing_Features)
    - [Future Enhancements](#Future_Enhancements)
- [Technologies Used](#Technologies_Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)
    - [Content](#Content)
    - [Media](#Media)
    - [Acknowledgements](#Acknowledgements)

- - - -
## **<ins>Introduction</ins>**

## **<ins>Project_Motivation</ins>**



## **<ins>UX</ins>**
Once the concept of the site was developed, as part of the UX design phase I decided to make the site a one page site with distinctive containers for each 
section. The site would have 6 major components,

   - Header
   - Introduction
   - Destinations Information. 
   - Interactive Map
   - Form
   - Footer

Bootstrap was chosen as the main library for the major design elements, it provides the responsiveness required to ensure the site looks good and works well 
across all device sizes. On top of bootstrap, custom CSS was used to provide a unique look and feel and set the site apart. 

**Header**
The header consists of a nav bar, locked to the top of the screen as the page is long the user always has access to the nav bar to jump to the desired 
location. Under that I included a hero image with crisp white text to capture the users attention. 

**Introduction**


### <ins>User_Stories</ins>

**Site User;**
- 1
- 2
- 3
- 4

**Site Owner;**
- A
- B
- C


### <ins>Wireframes</ins>


| Title | Link to Wireframe (pdf) |
| --- | --- |
| Title 1 | add link here |


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


Maintenance Records (tracker.html)
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Check data is reterived and populated from DB| Rsults shoud include all cars registered to a user with list of records for each car listed|Pass|Some UX detailed in UX Testing section|
|Test Details button|Button should launch detailed records page for selected record and populate all data|Pass|None|

Service Record (detailed record.html)
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|All data populates|Validate that all data is populating, the correct data is populating|Pass|None|
|Return Button|Retuen button should take the user back to the main record page|Pass||
|Edit Button|The edit button should take the user to the edit record page and populate the correct record information|Pass|Inital issues, with the two drop down menue, the options were populating but the information from the selected record was now <br> Updated to check the list of the selected data and mark as selected when found|
|Delete Button|Open a modal to confirm deletion|Pass|Note: Delete button does not process and DB action, it onlys launches the modal for confirmation.|
|Confirmation Modal<br>1. Confirm it opens correctly <br> 2. Test No button. <br> 3. Test yes button.<br> 4. Confirm the correct record is deleted and no other record is effected|Selecting No on the confirmation panel should retun the user to the edit screen with no action take <br> selecting yes should initiate the update to the DB to delete the record. The selected record should be removed from the DB.|Pass|Page & functions work as expected|

Add Maintenance Record (addrecord.html)
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Drop down - Cars|Only cars registered to the a user should be shown in the list|Pass||
|Drop down - Garages|Only active garages should show in the list|Pass|One issue to resolve, Garages that were disabled, and should not be selectable where showing in the list. <br> updated to the DB query in Python to only pull records with active flag set.|
|Date Picker|Displays and allows date to be selected|Pass||
|Toggle Switch|Toggles on / off|Pass||
|+ - Buttons|Add / Remove lines from the detailed list section|Pass|Opted to hide the - (remove) button on load, as its only needed if user adds line they then want to remove.|
| Add Record Button|Collects all data & adds new record to the DB|Pass||


Edit Record (edit_record.html)
| Test | Expected outcome | Results | Issues|
| --- | --- | --- | --- |
|Fields Accecpt Data|data can be entered with out issue|Pass|Had to fix issue on service cost field, it was only taking numbers but as filed for cost, it needed to take up to two desimal places if requried. <br> added step=".01" to the field.|
|Data|All record data is correctly entered to the form|Passed|See above for inital issue on reg no & garage fields|
|Ediable|All data fields can be edicated|Pass|All fields where tested to ensure they could be edited|
|Return Button|Returns returns user to detailed record page|Pass||
|+ / - buttons|Ensure buttons work to add remove lines|Pass|Save button, sent the edited data to the DB and updated the correct record|
|Save Chnage Button|Sends the updtes to the DB and saves the updated record|Pass| Initaly failed, <br> the initial page was a copy of the add record and the - (remove button) was hidden, updated JS to not hide on edit page. <br> Due to the way the buttons were coded in the add record page, JS had to be updated to allow them function on edit page.|
|||||
|||||

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