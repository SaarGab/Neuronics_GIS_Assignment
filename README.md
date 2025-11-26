# Neuronics_GIS_Assignment
The home assignment given to me by Neuronics.

My chosen environment is ArcGIS Pro with ArcPy.

Important note: Please create a new ArcGIS Pro Project from scratch, and then inside it create a Map (it's one of the options). Afterwards, change the values of the 2 following variables in the code (called the_actual_code.py, it's in this repository):

APRX_PATH - Should contain the path to your ArcGIS Pro project's .aprx file (e.g. r"C:\Users\Saar\Documents\ArcGIS\Projects\MyProject\MyProject.aprx").

OUT_FOLDER - Should contatin the path to your ArcGIS Pro project folder, which you must have write access to (e.g. r"C:\Users\Saar\Documents\ArcGIS\Projects\MyProject").

Afterwards, please SAVE AND CLOSE the project and then run the code attached (that is, the_actual_code.py, which is in this repository).

The code does the following:

A. Loads and displays the orthophoto layer “World_Imagery_basemap” in the ArcGIS Pro Project. Source of the orthophoto layer:
https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer.

Before and After images:

<img width="940" height="505" alt="image" src="https://github.com/user-attachments/assets/0a8e515a-de0c-4ce2-a688-e424e2862090" />
<img width="940" height="515" alt="image" src="https://github.com/user-attachments/assets/03286270-0781-4fcb-be8d-a4550ddad9c7" />

B. Adds the 3 following feature layers on top of the imagery:
1. World_Cities_All: https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Cities/FeatureServer/0
<img width="940" height="371" alt="image" src="https://github.com/user-attachments/assets/27b1337b-85f7-40ce-bbdd-4f77c1b2c879" />

2. World_Countries:
https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Countries/FeatureServer/0
<img width="940" height="523" alt="image" src="https://github.com/user-attachments/assets/a1f9e966-a4df-469c-ac8b-e1e3862cef16" />

3. World_Urban_Areas:
https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Urban_Areas/FeatureServer/0 (In the picture below: a zoom in on Europe)
<img width="940" height="430" alt="image" src="https://github.com/user-attachments/assets/fc469a0b-64fe-45fa-9c88-270b2866f9b5" />

C. Filters the points in the “World_Cities_All” feature layer with 2 queries:

     Query 1: STATUS = ‘National and provincial capital’, which creates a new feature layer “World_Cities_Capitals”
<img width="940" height="390" alt="image" src="https://github.com/user-attachments/assets/04bde47d-0377-4223-a4fb-b1348e2723fb" />

     Query 2: CNTRY_NAME = ‘United States’, which creates a new feature layer “World_Cities_United_States”
   <img width="940" height="421" alt="image" src="https://github.com/user-attachments/assets/d49148b8-85c6-4d8a-9add-ae78fc38be4f" />
   
D. Identify-On-Click: Already a feature of every ArcGIS Pro project.
<img width="978" height="715" alt="image" src="https://github.com/user-attachments/assets/116b13ff-6824-4fdb-a223-2510f8d9edeb" />

E. Filters the features of the feature layer World_Countries where Shape_Area > 5000000000000 and then exports them to a shapefile called “Largest_Countries”
<img width="940" height="438" alt="image" src="https://github.com/user-attachments/assets/d25d26b6-eb79-4b50-8c72-ab9bd9fb7bba" />

The total time I spent on this assignment was 4 hours. I completed all the tasks (both the required and optional).
