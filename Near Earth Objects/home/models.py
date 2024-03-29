"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str
import math
import datetime


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object
    , such as its primary designation (required, unique), IAU name
    (optional), diameter in kilometers (optional - sometimes unknown),
    and whether it's marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied
        to the constructor.
        """
        self.designation = info.get("pdes")
        self.name = info.get("name")
        if not self.name:
            self.name = None
        self.diameter = info.get("diameter")
        if not self.diameter:
            self.diameter = float("nan")
        self.hazardous = info.get("pha")

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return f"{self.designation} ({self.name})"
        return f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        is_hazardous = "is" if self.hazardous else "is not"
        if not math.isnan(self.diameter):
            return f"A NearEarthObject {self.fullname} has \
        a diameter of {self.diameter:.3f} km and {is_hazardous} \
        potentially hazardous."
        return f"A NearEarthObject {self.fullname}, {is_hazardous} \
        potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string\
        representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, \
                name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")

    def serialize(self):
        """Return a dict representation of self attributes.

        Returns:
            [dict]: Keys associated with self attributes.
        """
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous,
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the
    NEO's close approach to
    Earth, such as the date and time (in UTC) of closest
    approach, the nominal
    approach distance in astronomical units, and the
    relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to
        the constructor.
        """
        self._designation = info.get("des")
        if not self._designation:
            self._designation = None

        self.time = info.get("cd")

        if self.time:
            self.time = cd_to_datetime(self.time)
            assert isinstance(self.time, datetime.datetime), "Date"
            "should be a datetime object"
        else:
            self.time = None

        self.distance = info.get("dist")
        if not self.distance:
            self.distance = float("nan")
        self.velocity = info.get("v_rel")
        if not self.velocity:
            self.velocity = float("nan")

        assert isinstance(self.distance, float), "Distance should be a float"
        assert isinstance(self.velocity, float), "Velocity should be a float"

        # Create an attribute for the referenced NEO, originally None.
        self.neo = info.get("neo")
        if not self.neo:
            self.neo = None

    @property
    def designation(self):
        """Get designation.

        Returns:
            [str]: Returns self._designation
        """
        return self._designation

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s\
        approach time.

        The value in `self.time` should be a Python `datetime` object.
        While a `datetime` object has a string representation, the
        default representation includes seconds - significant figures
        that don't exist in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        if self.time:
            return datetime_to_str(self.time)
        return "Unknown Time"

    def __str__(self):
        """Return `str(self)`."""
        return f"A CloseApproach at {self.time_str}, '{self.neo.fullname}' \
        approaches Earth at a distance of {self.distance:.2f} au and a \
        velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation\
        of this object."""
        return (f"CloseApproach(time={self.time_str!r}, \
        distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def serialize(self):
        """Return a dict representation of self attributes.

        Returns:
            [dict]: Keys associated with self attributes.
        """
        return {
            "datetime_utc": datetime_to_str(self.time),
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
        }
