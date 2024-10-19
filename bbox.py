import json

with open("geoBoundariesCGAZ_ADM0.geojson", "r") as file:
    geojson_data = json.loads(file.read())


def calculate_bbox(coordinates):
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)
    max_x = max(coord[0] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates)
    return [min_x, min_y, max_x, max_y]


def extract_bboxes(geojson):
    bbox_dict = {}
    print(type(geojson))

    for feature in geojson["features"]:
        shape_group = feature["properties"]["shapeGroup"]
        geometry_type = feature["geometry"]["type"]

        if geometry_type == "Polygon":
            coordinates = feature["geometry"]["coordinates"][0]
            bbox = calculate_bbox(coordinates)
            bbox_dict[shape_group] = bbox

        elif geometry_type == "MultiPolygon":
            all_coords = [
                coord
                for polygon in feature["geometry"]["coordinates"]
                for coord in polygon[0]
            ]
            bbox = calculate_bbox(all_coords)
            bbox_dict[shape_group] = bbox

    return bbox_dict


bboxes = extract_bboxes(geojson_data)
output_json = json.dumps(bboxes, indent=4)


with open("bbox.json", "w") as outfile:
    outfile.write(output_json)
