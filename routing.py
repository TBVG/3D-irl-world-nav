

import osrm

client = osrm.Client(host='http://router.project-osrm.org')

def get_route(start, end):
    response = client.route(start, end)
    return response["routes"][0]["geometry"]