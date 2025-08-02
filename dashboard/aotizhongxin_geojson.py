# GeoJSON data untuk area Aotizhongxin dan sekitarnya
aotizhongxin_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Aotizhongxin Central",
                "area_id": "area_1"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [116.400, 39.900],
                    [116.410, 39.900],
                    [116.410, 39.910],
                    [116.400, 39.910],
                    [116.400, 39.900]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Aotizhongxin North",
                "area_id": "area_2"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [116.400, 39.910],
                    [116.410, 39.910],
                    [116.410, 39.920],
                    [116.400, 39.920],
                    [116.400, 39.910]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Aotizhongxin East",
                "area_id": "area_3"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [116.410, 39.900],
                    [116.420, 39.900],
                    [116.420, 39.910],
                    [116.410, 39.910],
                    [116.410, 39.900]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Aotizhongxin South",
                "area_id": "area_4"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [116.400, 39.890],
                    [116.410, 39.890],
                    [116.410, 39.900],
                    [116.400, 39.900],
                    [116.400, 39.890]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Aotizhongxin West",
                "area_id": "area_5"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [116.390, 39.900],
                    [116.400, 39.900],
                    [116.400, 39.910],
                    [116.390, 39.910],
                    [116.390, 39.900]
                ]]
            }
        }
    ]
}

# Koordinat titik-titik monitoring dalam area Aotizhongxin
monitoring_points = [
    {"name": "Central Station", "lat": 39.9042, "lon": 116.4074, "area_id": "area_1"},
    {"name": "North Station", "lat": 39.9150, "lon": 116.4050, "area_id": "area_2"},
    {"name": "East Station", "lat": 39.9030, "lon": 116.4150, "area_id": "area_3"},
    {"name": "South Station", "lat": 39.8950, "lon": 116.4060, "area_id": "area_4"},
    {"name": "West Station", "lat": 39.9060, "lon": 116.3950, "area_id": "area_5"}
]
