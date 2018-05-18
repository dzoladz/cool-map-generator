import folium
import pandas as pd

df = pd.read_csv('data.csv', sep=",")
df.columns = ["LAT", "LONG", "NAME", "WEBSITE", "ICON"]

my_map = folium.Map(location=[40.33, -82.99],
                    # tiles='OpenStreetMap',
                    # tiles='Mapbox Control Room',
                    # tiles='Stamen Terrain',
                    # tiles='Stamen Toner',
                    # tiles='Stamen Watercolor',
                    # tiles='Mapbox Bright',
                    tiles='CartoDB Positron',
                    zoom_start=7,
                    width=600,
                    height=500)

for index, row in df.iterrows():
    library_website = folium.Html('<a href="http://' + row["WEBSITE"] + '"target="_blank">' + row["NAME"] + '</a>', script=True)
    folium.Marker(location=[row["LONG"], row["LAT"]],
                  popup=folium.Popup(html=library_website),
                  icon=folium.features.CustomIcon(row["ICON"],
                                                  popup_anchor=(9, -19))).add_to(my_map)

#Export Map: '/Users/Derek/Desktop/map.html'
path = 'map.html'

my_map.save(path)
