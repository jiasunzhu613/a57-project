import googlemaps
import pandas as pd
from datetime import datetime

file = input("Give me yo file name: ")
skiprows = int(input("How many bad lines to skip: "))

df = pd.read_excel(f"../data/{file}.xlsx", skiprows=skiprows)
gmaps = googlemaps.Client(key="AIzaSyAuKfWc9z1gsqQUXiPhNK8pvcRFHRr5OAs")
df.rename(columns=df.iloc[1])
df["Latitude"] = 0
df["Longitude"] = 0
print(df)

memo = {}

for idx, row in df.iterrows():
    """if idx <= 3:
    continue"""
    # print(row)
    address = row["Location"] + ", " + row["City"]
    if address in memo:
        long_lat = memo[address]
        lat = long_lat[0]
        lng = long_lat[1]
        print(f"from memo: {lat}, {lng}")
        df.loc[idx, "Latitude"] = lat
        df.loc[idx, "Longitude"] = lng
        continue

    geocode_result = gmaps.geocode(row["Location"] + ", " + row["City"])
    try:
        long_lat = geocode_result[0]["geometry"]["location"]
        # print(f"{long_lat["lat"]}, {long_lat["lng"]}")
        lat = long_lat["lat"]
        lng = long_lat["lng"]
        print(f"{lat}, {lng}")
        df.loc[idx, "Latitude"] = lat
        df.loc[idx, "Longitude"] = lng

        memo[address] = (lat, lng)
    except:
        print(f"Error: {idx}")
        print(row)
    # df.to_excel("../data/NOX_LL.xlsx")
    print()

print(df)
print(df.columns)

df.to_excel(f"../data/{file}_LL.xlsx")
# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

""" # Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions(
    "Sydney Town Hall", "Parramatta, NSW", mode="transit", departure_time=now
)

# Validate an address with address validation
addressvalidation_result = gmaps.addressvalidation(
    ["1600 Amphitheatre Pk"],
    regionCode="US",
    locality="Mountain View",
    enableUspsCass=True,
)

# Get an Address Descriptor of a location in the reverse geocoding response
address_descriptor_result = gmaps.reverse_geocode(
    (40.714224, -73.961452), enable_address_descriptor=True
) """
