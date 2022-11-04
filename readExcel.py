import pandas as pd
import requests
import json
import time

def read_excel(filename):
    excel_data = pd.read_excel(filename)

    data = pd.DataFrame(excel_data, columns=['IL', 'ILCE', 'MAHALLE'])
    i = 0
    for row in data.itertuples(index=False):
        str = " ".join([row[0], row[1], row[2]])
        # Запрашиваем полигон
        coord = request_get_polygon(str)
        # Когда полигон найден
        if coord:
            polygons[row[2]] = coord
            time.sleep(5)
            print("{} Polygon {}".format(i, str))
        # Когда не найден - записываем точку в список.
        else:
            points.append(str)
            print("{} Point {}".format(i, str))
        i += 1


def request_get_polygon(Area):
    # URL, на который собираетесь отправлять запрос

    url = 'http://nominatim.openstreetmap.org/search'

    # Параметры запроса
    params = {
        'q': Area,
        'format': 'json',
        'polygon_geojson': '1'
    }

    # Ответ
    response = requests.get(url=url, params=params).json()
    for r in response:
        if r["osm_type"] == "relation":
            coordinates = r["geojson"]["coordinates"]
            return coordinates

    return []

def write_to_file(json_file, file_name):
    with open(file_name + '.json', 'w') as outfile:
        json.dump(json_file, outfile)

if __name__ == "__main__":
    name = "Ant-Izm_Mers"
    polygons = {}
    points = []
    read_excel(name + '.xlsx')
    write_to_file(polygons, "polygons")
    write_to_file(points, "points")

