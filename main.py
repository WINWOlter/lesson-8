import requests

class City:
  def __init__(self, city):
    r = requests.get("http://geodb-free-service.wirefreethought.com/v1/geo/cities?limit=1&offset=0&namePrefix=" + city)
    res = r.json()
    self.name = res["data"][0]["city"]
    self.lat = res["data"][0]["latitude"]
    self.lon = res["data"][0]["longitude"]
  

c = input("Введіть місто:")
city = City(c)

print(city.name)
print(city.lat)
print(city.lon)