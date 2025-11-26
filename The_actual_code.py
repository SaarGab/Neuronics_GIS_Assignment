"""
ArcPy script to reproduce tasks in README.md:
  A. Add World Imagery (orthophoto)
  B. Add 3 vector layers (World_Cities, World_Countries, World_Urban_Areas)
  C. Create two filtered city layers:
       - STATUS = 'National and provincial capital'
       - CNTRY_NAME = 'United States'
  D. (Identify-on-click is built into ArcGIS Pro — no code needed)
  E. Export World_Countries features where Shape_Area > 5000000000000
       to a shapefile named 'Largest_World_Countries.shp'

See README: README.md. :contentReference[oaicite:1]{index=1}
"""

import arcpy
import os
import sys

# ------------ USER CONFIG ------------
# If running the script from inside ArcGIS Pro use "CURRENT".
# If running externally, put the full path to your .aprx, e.g. r"C:\Users\you\Documents\Project.aprx"
APRX_PATH = r"C:\Users\Saar\Documents\ArcGIS\Projects\MyProject\MyProject.aprx"

# Target map name (None->use first map in project)
TARGET_MAP_NAME = None  # or e.g. "Map"

# Where to write exported shapefile (a folder)
OUT_FOLDER = r"C:\Users\Saar\Documents\ArcGIS\Projects\MyProject"  # <-- change this to a folder you have write access to

# Output shapefile name (no path)
OUT_SHAPE_NAME = "Largest_World_Countries.shp"

# Overwrite outputs
arcpy.env.overwriteOutput = True
# -------------------------------------

# Service URLs (from your README)
IMAGERY_URL = r"https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer"
CITIES_URL = r"https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Cities/FeatureServer/0"
COUNTRIES_URL = r"https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Countries/FeatureServer/0"
URBAN_AREAS_URL = r"https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Urban_Areas/FeatureServer/0"

# Definition queries (as in your README)
QUERY_CAPITALS = "STATUS = 'National and provincial capital'"
QUERY_US = "CNTRY_NAME = 'United States'"

# Where clause for largest countries (as in your README)
COUNTRIES_WHERE = "Shape_Area > 5000000000000"

# Ensure output folder exists
if not os.path.isdir(OUT_FOLDER):
    raise SystemExit(f"Output folder does not exist: {OUT_FOLDER}")

# Open ArcGIS Project
aprx = arcpy.mp.ArcGISProject(APRX_PATH)
# choose map
if TARGET_MAP_NAME:
    maps = [m for m in aprx.listMaps() if m.name == TARGET_MAP_NAME]
    if not maps:
        raise SystemExit(f"Map named '{TARGET_MAP_NAME}' not found in {APRX_PATH}")
    m = maps[0]
else:
    maps = aprx.listMaps()
    if not maps:
        # create a map if none exists
        m = aprx.createMap("Map")
    else:
        m = maps[0]

print(f"Using project: {APRX_PATH!r}, map: {m.name!r}")

# ------------------------
# A. Add imagery (orthophoto)
# ------------------------
print("Adding World Imagery (orthophoto)...")
try:
    imagery_layer = m.addDataFromPath(IMAGERY_URL)
    # set a friendly name
    imagery_layer.name = "World_Imagery_basemap"
    print("Added imagery layer:", imagery_layer.name)
except Exception as e:
    print("Failed to add imagery layer:", e)
    raise

# ------------------------
# B. Add vector layers
# ------------------------
print("Adding vector layers...")

try:
    cities_layer = m.addDataFromPath(CITIES_URL)
    cities_layer.name = "World_Cities_All"
    print("Added:", cities_layer.name)
except Exception as e:
    print("Failed to add World_Cities:", e)
    raise

try:
    countries_layer = m.addDataFromPath(COUNTRIES_URL)
    countries_layer.name = "World_Countries"
    print("Added:", countries_layer.name)
except Exception as e:
    print("Failed to add World_Countries:", e)
    raise

try:
    urban_layer = m.addDataFromPath(URBAN_AREAS_URL)
    urban_layer.name = "World_Urban_Areas"
    print("Added:", urban_layer.name)
except Exception as e:
    print("Failed to add World_Urban_Areas:", e)
    raise

# ------------------------
# C. Filtering - create two filtered city layers
#    Approach: add the same service again and set different definitionQuery
# ------------------------
print("Creating filtered city layers...")

# Add second copy for capitals
capitals_layer = m.addDataFromPath(CITIES_URL)
capitals_layer.name = "World_Cities_Capitals"
# assign definitionQuery
try:
    capitals_layer.definitionQuery = QUERY_CAPITALS
    print(f"Applied definitionQuery to {capitals_layer.name}: {QUERY_CAPITALS}")
except Exception as e:
    print("Failed to set definitionQuery on capitals_layer:", e)
    # continue

# Add third copy for US cities
us_layer = m.addDataFromPath(CITIES_URL)
us_layer.name = "World_Cities_United_States"
try:
    us_layer.definitionQuery = QUERY_US
    print(f"Applied definitionQuery to {us_layer.name}: {QUERY_US}")
except Exception as e:
    print("Failed to set definitionQuery on us_layer:", e)
    # continue

# OPTIONAL: reorder layers so imagery is at bottom
try:
    # move imagery to bottom
    m.moveLayer(m.listLayers()[0], imagery_layer, "AFTER")  # best-effort
except Exception:
    pass




# ------------------------
# E. Export Filtered Features (World_Countries where Shape__Area > ...)
# ------------------------

print("Exporting filtered World_Countries to shapefile...")

COUNTRIES_WHERE = "Shape__Area > 5000000000000"   # <-- valid field

try:
    # Use the LAYER OBJECT, not the URL
    desc = arcpy.Describe(countries_layer)
    fc = desc.catalogPath  # internal featureclass handle

    arcpy.management.MakeFeatureLayer(fc, "Largest_Countries_tmp", COUNTRIES_WHERE)

    arcpy.conversion.FeatureClassToFeatureClass(
        in_features="Largest_Countries_tmp",
        out_path=OUT_FOLDER,
        out_name=os.path.splitext(OUT_SHAPE_NAME)[0]
    )

    print("Export completed successfully.")

    # ---- Add exported shapefile to the map ----
    exported_fc_path = os.path.join(OUT_FOLDER, OUT_SHAPE_NAME)
    print("Adding exported layer to the map:", exported_fc_path)

    new_layer = m.addDataFromPath(exported_fc_path)
    new_layer.name = "Largest_Countries"
    print("Successfully added exported layer to the map.")

except Exception as e:
    print("Export failed:", e)
    raise


# Save the project (if not CURRENT) or offer to save if CURRENT
try:
    if APRX_PATH != "CURRENT":
        aprx.save()
        print("Saved project to", APRX_PATH)
    else:
        # If running inside Pro and using CURRENT, explicitly save the .aprx on disk if needed:
        # ask user if they want to save - we will save programmatically (uncomment to auto-save)
        # aprx.save()
        print("Running with 'CURRENT' ArcGISProject - changes are available in the open project.")
except Exception as e:
    print("Warning: could not save project:", e)

    
print("Script finished successfully.")
