"""
Diagrams

---------

SysML includes 9 types of diagrams, some of which are taken from UML.

-Block definition diagram
-Internal block diagram
-Package diagram
-Use case diagram
-Requirement diagram
-Activity diagram
-Sequence diagram
-State diagram
-Parametric diagram
"""

## Structure
class BlockDefinitionDiagram(object):
    """This class defines a block definition diagram
    
    A block definition diagram describes the system hierarchy and system/component classifications. 
    """
    
    def __init__(self):
        pass

class InternalBlockDiagram(object):
    """This class defines an internal block diagram
    
    The internal block diagram describes the internal structure of a system in terms of its parts, ports, and connectors.
    """
    
    def __init__(self):
        pass

class PackageDiagram(object):
    """This class defines a package diagram

    The package diagram is used to organize the model.
    """

    def __init__(self):
        pass

## Behavior
class SequenceDiagram(object):
    """This class defines a sequence diagram

    A sequence diagram represents the interaction between collaborating parts of a system.
    """

    def __init__(self):
        pass

class StateDiagram(object):
    """This class defines a state machine diagram

    The state machine diagram describes the state transitions and actions that a system or its parts perform in response to events.
     """

    def __init__(self):
        pass

class ActivityDiagram(object):
    """This class defines an activity diagram

    The activity diagram represents the flow of data and control between activities.
    """

    def __init__(self):
        pass

class UseCaseDiagram(object):
    """This class defines a use case diagram

    A use-case diagram provides a high-level description of functionality that is achieved through interaction among systems or system parts.
    """

    def __init__(self):
        pass

## Requirements
class RequirementDiagram(object):
    """This class defines a requirement diagram

    The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relationships allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements.
    """

    def __init__(self):
        pass

## Parametrics
class ParametricDiagram(object):
    """This class defines a parametric diagram

    The parametric diagram represents constraints on system property values such as performance, reliability, and mass properties, and serves as a means to integrate the specification and design models with engineering analysis models.
    """

    def __init__(self):
        pass

