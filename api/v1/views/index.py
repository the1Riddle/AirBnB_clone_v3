#!/usr/bin/python3
"""connects to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


hbnbText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """info"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """more info"""
    return_dict = {}
    for key, value in hbnbText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)

if __name__ == "__main__":
    pass