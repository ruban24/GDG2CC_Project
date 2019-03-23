import json
import urllib.request
import turtle
url = 'http://api.open-notify.org/astros.json'
get = urllib.request.urlopen(url)
result = json.loads(get.read())
print('People in Space: ', result['number'])
astro = result['people']
for a in astro:
    print(a['name'], ' in ', a['craft'])
    
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.register_shape('space_station.gif')
url = 'http://api.open-notify.org/iss-now.json'
get = urllib.request.urlopen(url)
result = json.loads(get.read())
location = result['iss_position']
latitude = location['latitude']
longitude = location['longitude']
print('Latitude: ', latitude)
print('Longitude: ', longitude)


screen.bgpic('nasa.gif')
iss = turtle.Turtle()
iss.shape('space_station.gif')
iss.setheading(90)
iss.penup()
iss.goto(float(longitude), float(latitude))
turtle.done()
