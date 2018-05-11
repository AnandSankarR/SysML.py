"""
The `Model` class is used to instantiate a central namespace for a SysML model by subsuming stereotypes into mode elements or model relationships.

---------

Model elements and relationships are the building blocks that make up the 9 SysML diagrams
"""
from sysml.stereotypes import *
import re
import uuid

# developer notes: to use hidden vs unhidden attributes

class Model(object):
    """This class defines a SysML model for subsuming stereotypes into model elements or relationships.
    """

    # Dictionary of valid model elements. key: stereotype [string], value: stereotype [class]
    _validElements = {
        "block":Block,
        "requirement":Requirement,
        "constraint":Constraint,
        "package":Package
    }

    # Dictionary of valid model relationships. key: stereotype [string], value: valid stereotype nodes [list of classes]
    _validRelationships = {
        "containment":{
            "source":[Block],
            "target":[Block]},
        "inheritance":{
            "source":[Block],
            "target":[Block]},
        "association":{
            "source":[Block],
            "target":[Block]},
        "generalization":{
            "source":[Block],
            "target":[Block]},
        "partProperty":{
            "source":[Block],
            "target":[Block]},
        "valueProperty":{
            "source":[Block],
            "target":[Block]},
        "referenceProperty":{
            "source":[Block],
            "target":[Block]},
        "flowProperty":{
            "source":[Block],
            "target":[Block]}
    }

    def __init__(self, label=None, elements={}, relationships={}):
        # Model label
        self._label = label
        # All model elements stored as a dictionary of key-value pairs
        self._elements = elements
        # All model relationships stored as a dictionary of key-value pairs
        self._relationships = relationships

    def __setitem__(self, key, stereotype):
        "Sets/overwrites stereotype-valid model element or relationship into model"
        if self._isValidElementKey(key):
            self._setElement(key, stereotype)
        elif self._isValidRelationshipKey(key):
            self._setRelationship(key, stereotype)
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'partProperty-42' ")

    def __getitem__(self, key):
        "Returns data for key-specified model element or relationship"
        if key in self._elements.keys():
            return self._elements[key]
        elif key in self._relationships.keys():
            return self._relationships[key]
        else:
            raise ValueError(repr(key) + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'partProperty-42' ")

    def add_elements(self, *stereotypev):
        "Sets/overwrites stereotype-valid model element or relationship into model"
        for stereotype in stereotypev:
            key = self._generateKey(stereotype, 9999)
            self._setElement(key, stereotype)

    @property
    def elements(self):
        "Returns dictionary of model elements"
        return self._elements

    @property
    def relationships(self):
        "Returns dictionary of relationships"
        return self._relationships

    @elements.setter
    def elements(self, elements):
        """Sets/rewrites model elements for entire model by passing model elements as key-value pairs.

        Note: model elements must be valid stereotypes.
        """
        if type(elements) is not dict:
            raise TypeError(repr(elements) + " must be a dictionary.")
        else:
            for key in elements.keys():
                self._setElements(key, elements[key])

    @relationships.setter
    def relationships(self, relationships):
        """Sets relationships to user-defined dictionary.

        Note: model relationships must be valid stereotypes.
        """
        if type(relationships) is not dict:
            raise TypeError(repr(relationships) + " must be a dictionary.")
        for key in relationships.keys():
            stereotypeName, id_no = key.split('-')
            if not self._isValidRelationshipKey(key):
                raise ValueError(key + " is not a valid key. Keys should be a string containing a dash-separated stereotype and integer, e.g., 'partProperty-42' ")
            else:
                self._setRelationship(key, relationships[key])

    def _generateKey(self, stereotype, maxId_no):
        if self._isValidElement(stereotype):
            for validElement in self._validElements.keys():
                if isinstance(stereotype, self._validElements[validElement]):
                    for id_no in range(1, maxId_no+1):
                        newKey = validElement + "-" + str(id_no)
                        if newKey not in self._elements.keys():
                            return newKey
        elif self._isValidRelationship(stereotype):
            for validRelationship in self._validRelationships.keys():
                if stereotype["relationshipType"] is validRelationship:
                    for id_no in range(1, maxId_no+1):
                        newKey = validRelationship + "-" + str(id_no)
                        if newKey not in self._relationships.keys():
                            return newKey
        else:
            raise TypeError(stereotype + " is not a valid stereotype.")

    def _setElement(self, key, stereotype):
        if key is None:
            key = _generateKey(stereotype)
        if not self._isValidElement(stereotype):
            raise TypeError(repr(stereotype) + " is not a valid stereotype.")
        else:
            self._elements[key] = stereotype
            self._elements[key].uuid = str(uuid.uuid1())

    def _setRelationship(self, key, relationship):
        if relationship["source"] not in self._elements.keys():
            raise TypeError(relationships[key]["source"] + " does not exist in model.")
        if relationship["target"] not in self._elements.keys():
            raise TypeError(relationship["target"] + " does not exist in model.")
        if not self._isValidRelationship(relationship):
            raise TypeError(relationship["source"] + " and " + relationships["target"] + " are not a valid source-target pair for " + stereotypeName)
        else:
            self._relationships[key] = relationship
            # if not hasattr(self._relationships[key], 'uuid'):
            #     self._relationships[key].uuid = str(uuid.uuid1())

    def _isValidRelationship(self, relationship):
        source = self._elements[relationship["source"]]
        target = self._elements[relationship["target"]]
        relationshipType = relationship["relationshipType"]
        return type(source) in self._validRelationships[relationshipType]['source'] and type(target) in self._validRelationships[relationshipType]['target']

    @classmethod
    def _isValidElementKey(cls, key):
        elementName, id_no = key.split('-')
        return elementName in cls._validElements.keys() and isinstance(int(id_no),int)

    @classmethod
    def _isValidElement(cls, stereotype):
        return type(stereotype) in cls._validElements.values()

    @classmethod
    def _isValidRelationshipKey(cls, key):
        relationship, id_no = key.split('-')
        return relationship in cls._validRelationships.keys() and isinstance(int(id_no),int)

    # @classmethod
    # def _isValidSource(cls, relationship, source):
    #     return source in cls._validRelationships[relationship]['source']
    #
    # @classmethod
    # def _isValidTarget(cls, relationship, target):
    #     return target in cls._validRelationships[relationship]['target']
