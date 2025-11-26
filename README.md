# Neuronics_GIS_Assignment
The home assignment given to me by Neuronics
My chosen environment is ArcGIS Pro with ArcPy.
A. I loaded and displayed the orthophoto layer “World_Imagery_basemap” in my ArcGIS Pro Project. Source of the orthophoto layer:
https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer
Before:
<img width="940" height="505" alt="image" src="https://github.com/user-attachments/assets/0a8e515a-de0c-4ce2-a688-e424e2862090" />
After:
<img width="940" height="515" alt="image" src="https://github.com/user-attachments/assets/03286270-0781-4fcb-be8d-a4550ddad9c7" />
B. I added the 3 following feature layers on top of the imagery:
1. World_Cities_All: https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Cities/FeatureServer/0
<img width="940" height="371" alt="image" src="https://github.com/user-attachments/assets/27b1337b-85f7-40ce-bbdd-4f77c1b2c879" />
2. World_Countries:
https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Countries/FeatureServer/0
<img width="940" height="523" alt="image" src="https://github.com/user-attachments/assets/a1f9e966-a4df-469c-ac8b-e1e3862cef16" />
3. World_Urban_Areas:
https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Urban_Areas/FeatureServer/0 (In the picture below: a zoom in on Europe)
<img width="940" height="430" alt="image" src="https://github.com/user-attachments/assets/fc469a0b-64fe-45fa-9c88-270b2866f9b5" />
C. I filtered the points in the “World_Cities_All” feature layer with 2 queries:
     Query 1: STATUS = ‘National and provincial capital’, which created a new feature layer “World_Cities_Capitals”
<img width="940" height="390" alt="image" src="https://github.com/user-attachments/assets/04bde47d-0377-4223-a4fb-b1348e2723fb" />
     Query 2: CNTRY_NAME = ‘United States’, which created a new feature layer “World_Cities_United_States”
   <img width="940" height="421" alt="image" src="https://github.com/user-attachments/assets/d49148b8-85c6-4d8a-9add-ae78fc38be4f" />
D. Identify-On-Click: Already a feature of the program.
<img width="804" height="588" alt="image" src="https://github.com/user-attachments/assets/59b8b835-20a6-4647-86f0-5b879d47f121" />
E. Export Filtered Features: I exported the filtered features of World Countries where Shape_Area > 5000000000000 to a shapefile called “Largest_Countries”
<img width="940" height="438" alt="image" src="https://github.com/user-attachments/assets/d25d26b6-eb79-4b50-8c72-ab9bd9fb7bba" />
The total time I spent on this assignment was 3 hours. I completed all the tasks (both the required and optional).
