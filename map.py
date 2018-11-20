import folium

#create map object
m = folium.Map(location=[40.6971494,-74.2598655], zoom_start=12)

#gen map
m.save('test.html')