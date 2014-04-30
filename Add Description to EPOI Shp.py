#this file adds a field to the epoi shapefile that gives a desctiption of the type of building that it happens to be

import arcpy
import NAICS_DICT
#Set Workspace

#Set input shapefile
fc =  arcpy.GetParameterAsText(0)


#Create fields in Attribute tab
arcpy.AddField_management(fc,"DESC_1","TEXT")
arcpy.AddField_management(fc,"DESC_2","TEXT")
arcpy.AddField_management(fc,"DESC_3","TEXT")
arcpy.AddField_management(fc,"DESC_4","TEXT")
arcpy.AddField_management(fc,"DESC_5","TEXT")

fieldarray = [["NAICS_1","DESC_1"], ["NAICS_2","DESC_2"], ["NAICS_3","DESC_3"], ["NAICS_4","DESC_4"], ["NAICS_5","DESC_5"]]

#Update Each Table
index = 0
for index in range(0,5):
        cursor = arcpy.da.UpdateCursor(fc, fieldarray[index])
        for row in cursor:
                if NAICS_DICT.naics_1.get(row[0]):
                        row[1] =  NAICS_DICT.naics_1[row[0]]                      
                else:
                        row[1] = "ERROR - INCORRECT NAICS"
                cursor.updateRow(row)
        del cursor, row
        index = index + 1
del fieldarray, index
arcpy.RefreshTOC()
