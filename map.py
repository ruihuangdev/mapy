import folium

# create map object
m = folium.Map(location=[40.6971494, -74.2598655], zoom_start=12)

#global tooltip
tooltip = 'Click for more info'

# create markers
folium.Marker([40.7208063, -74.0021247],
              popup="<p>NikeLab 21 Mercer</p>", tooltip=tooltip).add_to(m),
folium.Marker([40.7579353, -73.9861885],
              popup="<p>Line Store NYC</p>", icon=folium.Icon(icon="cloud")).add_to(m)
folium.Marker([40.7190145, -74.0008184],
              popup="<p>Boba Guys SOHO</p>", icon=folium.Icon(color="pink")).add_to(m)
folium.Marker([40.7618261, -73.9793211],
              popup="<p>Halal Guys</p>", icon=folium.Icon(color="green", icon="leaf")).add_to(m)

# gen map
m.save('test.html')
