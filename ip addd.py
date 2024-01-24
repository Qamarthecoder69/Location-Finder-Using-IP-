import geocoder,folium

ip=geocoder.ip("me")
adress=ip.latlng
mymap=folium.Map(location=adress,zoom_start=12)
folium.Circle(adress,radius=500).add_to(mymap)
mymap.save("mymap.html")


