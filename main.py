import geopandas
import xml.etree.cElementTree as ET

data = geopandas.read_file("geopackage/trampelpfade.gpkg")

root = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
doc = ET.SubElement(root, "Document")
ET.SubElement(doc, "name").text = "Trampelpfade am Uetliberg"

styles = {
    "weg": {"color": "AA1461FF", "width": 9},
    "pfad": {"color": "AA1400FF", "width": 6},
    "pfadspur": {"color": "501400FF", "width": 5},
    "alpin": {"color": "AAF02814", "width": 6},
    "alpinspur": {"color": "50F02814", "width": 5},
    "biketrail": {"color": "AA143C00", "width": 6},
    "illegalbiketrail": {"color": "AA780078", "width": 6},
}
for id, attributes in styles.items():
    style = ET.SubElement(doc, "Style", id=id)
    linestyle = ET.SubElement(style, "LineStyle")
    for attribute, value in attributes.items():
        ET.SubElement(linestyle, attribute).text = str(value)


for index, item in data.iterrows():
    name = item["Name"]
    style = "#weg"
    if name == "Trampelpfad":
        style = "#pfad"
    elif name == "Trampelpfad (vague)":
        style = "#pfadspur"
    elif name == "Trampelpfad (alpine)":
        style = "#alpin"
    elif name == "Trampelpfad (alpine, vague)":
        style = "#alpinspur"
    elif name == "Official bike trail":
        style = "#biketrail"
    elif name == "Illegal bike trail":
        style = "#illegalbiketrail"

    for line in item["geometry"].geoms:
        placemark = ET.SubElement(doc, "Placemark")
        ET.SubElement(placemark, "styleUrl").text = style
        ET.SubElement(placemark, "name").text = name
        ET.SubElement(placemark, "description").text = item["description"]
        linestring = ET.SubElement(placemark, "LineString")
        ET.SubElement(linestring, "altitudeMode").text = "clampToGround"
        ET.SubElement(linestring, "tesselate").text = "1"
        coords = " ".join([f"{x},{y}" for x, y in line.coords])
        ET.SubElement(linestring, "coordinates").text = coords

# print(ET.tostring(root, encoding='unicode', xml_declaration=True))

tree = ET.ElementTree(root)
tree.write("kml/trampelpfade.kml", encoding='utf-8', xml_declaration=True)



data = geopandas.read_file("geopackage/uto869.gpkg")

root = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
doc = ET.SubElement(root, "Document")
ET.SubElement(doc, "name").text = "Uto869's routes on Hikr"

style = ET.SubElement(doc, "Style", id="uto")
linestyle = ET.SubElement(style, "LineStyle")
ET.SubElement(linestyle, "color").text = "32000000"
ET.SubElement(linestyle, "width").text = "16"

for index, item in data.iterrows():
    name = item["Name"]
    style = "#uto"

    for line in item["geometry"].geoms:
        placemark = ET.SubElement(doc, "Placemark")
        ET.SubElement(placemark, "styleUrl").text = style
        ET.SubElement(placemark, "name").text = name
        ET.SubElement(placemark, "description").text = item["description"]
        linestring = ET.SubElement(placemark, "LineString")
        ET.SubElement(linestring, "altitudeMode").text = "clampToGround"
        ET.SubElement(linestring, "tesselate").text = "1"
        coords = " ".join([f"{x},{y}" for x, y in line.coords])
        ET.SubElement(linestring, "coordinates").text = coords

tree = ET.ElementTree(root)
tree.write("kml/uto869.kml", encoding='utf-8', xml_declaration=True)
