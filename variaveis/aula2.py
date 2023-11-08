#Sua empresa
lat = '-22.005320'
lon = '-47.891040'

#Startup adquirida
latlon = '-22.005320;-47.891040'

#Manipulando as strings
indexPontoVirgula = latlon.find(';')
startupLat = latlon[0:10]
startupLon = latlon[11:len(latlon)]

#Exibindo resultado
print(f'Latitude: {startupLat} Longitude: {startupLon}')
