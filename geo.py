import googlemaps

class Place:
    def __init__(self):
        self.gmaps = None
        self.APIKey = 'AIzaSyBzhe9oVTn0YixpxnGDs4ZnkXar_ivldts'

    def getLoc(self):
        self.gmaps = googlemaps.Client(key=self.APIKey)
        return self.gmaps.geolocate()["location"]

    def getCoords(self):
        loc = self.getLoc()
        return [loc["lat"], loc["lng"]]

    def getPlace(self):
        loc = self.getLoc()
        full_address = self.gmaps.reverse_geocode((loc["lat"], loc["lng"]))[0]["formatted_address"]
        parts = full_address.split(" ")
        place = parts[-2] + " " + parts[-1]
        return place.encode('utf-8')