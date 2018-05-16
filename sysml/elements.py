"""
The `stereotypes` module contains all model elements that are valid for use by the `model` class

---------

Model elements are the building blocks that make up the 9 SysML diagrams
"""

import uuid

# developer notes: to use hidden vs unhidden attributes

class Block(object):
    """This class defines a block

    Parameters
    ----------
    label : string, default None

    values : dict, default None

    parts : list, default None

    references : list, default None

    flowProperties : dict, default None


    Examples
    --------
    >>> warpcore = Block(label='warp core',
    ...                 parts=[antimatterinjector, Dilithiumcrystalchamber],
    ...                 flow={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}})
    ...                 references=[antimatter])
    >>> warpdrive = Block(label='warp drive',
    ...                 values={'class-7'},
    ...                 parts=[antimattercontainment, warpcore, plasmainducer],

    """

    _id_no = 0
    #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, label=None, values=None, parts=None, references=None, flowProperties=None, stereotype=['block']):
        # Label
        if label is None:
            Block._id_no += 1
            self._label = 'Block' + str(Block._id_no)
        elif type(label) is not str:
            raise TypeError(label + " must be a string")
        else:
            self._label = label
        """
        ## Value Property
        if type(values) is dict:
            self._values = values
        else:
            raise TypeError("argument is not a dictionary!")
        ## Part Property
        if parts is None:
            self._parts = []
        elif type(parts) is list: #tk: change to accept block or list of blocks
            self._parts = parts
        else:
            raise TypeError("argument is not a list!")
        ## Reference Property
        if references is None:
            self._references = []
        elif type(references) is list: #tk: change to accept block or list of blocks
            self._references = references
        else:
            raise TypeError("argument is not a list!")
        ## Flow Property
        if flows is None:
            self._flowProperties = {}
        elif type(flowProperties) is dict:
            self._flowProperties = flowProperties
        else:
            raise TypeError("argument is not a dictionary!")
        ## Operations
        self.operations = []
        ## Constraints
        self.constaints = []
        """
    def __repr__(self):
        return "\xabblock\xbb '{}'".format(self._label)

    ## Getters
    @property
    def label(self):
        "Returns block label"
        return self._label

    @property
    def uuid(self):
        "Returns block uuid"
        return self._uuid

    @property
    def parts(self):
        return self._parts

    @property
    def values(self):
        return self._values

    @property
    def references(self):
        return self._references

    @property
    def flows(self):
        return self._flowProperties

    ## Setters
    @label.setter
    def label(self, label):
        "Sets block label"
        if type(label) is not str:
            raise TypeError(label + " must be a string")
        else:
            self._label = label

    @uuid.setter
    def uuid(self, UUID):
        "Sets block uuid"
        if type(UUID) is not str:
            raise TypeError(label + " must be a string")
        else:
            try:
                uuid.UUID(UUID, version=1)
                self._uuid = UUID
            except:
                raise ValueError(UUID + " must be a valid uuid of type, string")

    ## Structural Diagrams
    def bdd(self):
        """Generates a BlockDefinitionDiagram

        A block definition diagram describes the system hierarchy and system/component classifications.
        """
        pass

    def ibd(self):
        """Generates an internal block diagram

        The internal block diagram describes the internal structure of a system in terms of its parts, ports, and connectors.
        """
        pass

    ## Parametric Diagrams
    def par(self):
        """Generates a parametric diagram

        The parametric diagram represents constraints on system property values such as performance, reliability, and mass properties, and serves as a means to integrate the specification and design models with engineering analysis models.
        """
        pass

    # @parts.setter
    # def parts(self, *partv):
    #     """add one or more Blocks to parts
    #
    #     """
    #     for part in partv:
    #         if type(part) is Block:
    #             self._parts.append(part)
    #         else:
    #             raise TypeError("argument is not a 'Block'!")
    # @references.setter
    # def references(self, *referencev):
    #     """add one or more Blocks to references
    #
    #     """
    #     for reference in referencev:
    #         if type(reference) is Block:
    #             self._references.append(reference)
    #         else:
    #             raise TypeError("argument is not a 'Block'!")
    # @values.setter
    # def values(self, values):
    #     """add values dictionary to values
    #
    #     """
    #     if type(values) is dict:
    #         for key in values:
    #             if type(key) is str:
    #                 self.values[key] = values[key]
    #             else:
    #                 raise TypeError("key is not a string!")
    #     else:
    #         raise TypeError("argument is not a dictionary!")
    # @flowProperties.setter
    # def flowProperties(self, flowProperties):
    #     """add flowProperties dictionary to flowProperties
    #
    #     """
    #     if type(flowProperties) is dict:
    #         for flowPort in flowProperties:
    #             if type(flowPort) is str:
    #                 self._flowProperties[flowPort] = flowProperties[flowPort]
    #             else:
    #                 raise TypeError("key is not a string!")
    #     else:
    #         raise TypeError("argument is not a dictionary!")

class Requirement(object):
    """This class defines a requirement"""

    stereotype = "\xabrequirement\xbb"
    _id_no = 0
    #tk: need to fix id_no state; store all existing id_no's in a list?

    def __init__(self, label=None, txt=None, id_no=None, satisfy=None, verify=None, refine=None):
        # ID no.
        if id_no is None:
            Requirement._id_no += 1
            self._id_no = 'ID' + str(Requirement._id_no).zfill(3)
        elif type(id_no) in [int,float]:
            self._id_no = 'ID' + str(id_no).zfill(3)
        else:
            raise TypeError("argument is not int or float!")
        # Label
        if label is None:
            self._label = 'Requirement' + str(self._id_no)
        elif type(label) is str:
            self.label = label
        else:
            raise TypeError("argument is not a string!")
        # Text
        if txt is None:
            self.txt = ''
        elif type(label) is str:
            self.txt = txt
        else:
            raise TypeError("argument is not a string!")
        # Satisfy
        if satisfy is None:
            self._satisfy = []
        elif type(satisfy) is []: #tk: change to accept block or list of blocks
            self._satisfy = satisfy
        # Verify
        if verify is None:
            self._verify = []
        elif type(verify) is []: #tk: change to accept block or list of blocks
            self._verify = verify
        # Refine
        if refine is None:
            self.refine = []
        elif type(refine) is []: #tk: change to accept block or list of blocks
            self._refine = refine
        # Trace
        if trace is None:
            self.trace = []
        elif type(trace) is []: #tk: change to accept block or list of blocks
            self._trace = trace
    def __repr__(self):
        return "\xabrequirement\xbb {self.name}"
    ## Set requirement relations
    def satisfiedBy(self, *sourcev):
        for source in sourcev:
            self._satisfy.append(source)
    def refinedBy(self, *sourcev):
        for source in sourcev:
            self._refine.append(source)
    def verifiedBy(self, *sourcev):
        for source in sourcev:
            self._verify.append(source)

    def req(self):
        """Generates a requirement diagram

        The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relationships allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements.
        """
        pass


class Package(object):
    """This class defines a package"""
    stereotype = "package"

    def __init__(self, label=None):
        self._label = label
    def __repr__(self):
        return "\xab" + self.stereotype + "\xbb '{}'".format(self._label)

    ## Structural Diagrams
    def bdd(self):
        """Generates a BlockDefinitionDiagram

        A block definition diagram describes the system hierarchy and system/component classifications.
        """
        pass

    def pkg(self):
        """Generates a package diagram

        The package diagram is used to organize the model.
        """
        pass

    ## Behavior
    def uc(self):
        """Generates a use case diagram

        A use-case diagram provides a high-level description of functionality that is achieved through interaction among systems or system parts.
        """
        pass

    ## Requirement Diagram
    def req(self):
        """Generates a requirement diagram

        The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relationships allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements.
        """
        pass

class StateMachine(object):
    """This class defines a state"""

    def __init__(self):
        pass

    def stm(self):
        """Generates a state machine diagram for a valid model element key

        The state machine diagram describes the state transitions and actions that a system or its parts perform in response to events.
         """
        pass

class Activity(object):
    """This class defines a activity"""

    def __init__(self):
        pass

    ## Behavioral Diagrams
    def act(self):
        """Generates an activity diagram for a valid model element key

        The activity diagram represents the flow of data and control between activities.
        """
        pass

class Interaction(object):
    """This class defines an interaction"""

    def __init__(self):
        pass

    ## Behavioral Diagrams
    def sd(self):
        """Generates a sequence diagram

        A sequence diagram represents the interaction between collaborating parts of a system.
        """
        pass

class ConstraintBlock(object):
    """This class defines a constraint"""

    def __init__(self):
        pass

    ## Structural Diagrams
    def bdd(self):
        """Generates a BlockDefinitionDiagram

        A block definition diagram describes the system hierarchy and system/component classifications.
        """
        pass

    ## Parametric Diagrams
    def par(self):
        """Generates a parametric diagram

        The parametric diagram represents constraints on system property values such as performance, reliability, and mass properties, and serves as a means to integrate the specification and design models with engineering analysis models.
        """
        pass
