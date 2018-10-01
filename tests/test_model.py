import sysml
import pytest
import uuid
from pint import UnitRegistry


@pytest.fixture(scope="module")
def model():
    """Create a model object that will also serve as the root directory for all
    other model elements"""
    model = sysml.Model('Constitution-class Starship')
    return model


def test_model(model):
    # assert repr(model) == "\xabmodel\xbb Constitution-class Starship"
    # assert repr(type(model)) == "<class 'sysml.system.Model'>"

    assert model.stereotype == "\xabmodel\xbb"

    with pytest.raises(TypeError) as info:
        model = sysml.Model(47)
        assert "must be a string" in str(info.value)
    with pytest.raises(TypeError) as info:
        model = sysml.ModelElement()
        assert "Can't instantiate abstract class base" in str(info.value)


def test_valueType():
    kesselrun = sysml.ValueType(12, 'parsec')
    # assert repr(kesselrun) == "\xabvalueType\xbb 12 parsec"
    assert kesselrun.magnitude == 12
    assert kesselrun.units == 'parsec'
    assert kesselrun.name == '12 parsec'

    oneparsec = sysml.ValueType(1, 'parsec')
    assert oneparsec.magnitude == 1
    assert str(oneparsec.units) == 'parsec'

    lightyear = sysml.ValueType(1, 'lightyear')
    assert lightyear.magnitude == 1
    assert str(lightyear.units) == 'light_year'
    # parsectolightyear = oneparsec.ito('lightyear')
    distToProximaCentari = sysml.ValueType(0.98144, 'lightyear') + oneparsec
    assert round(distToProximaCentari.magnitude, 3) == 4.243
    assert str(distToProximaCentari.units) == 'light_year'

    distToProximaCentari = oneparsec + sysml.ValueType(0.98144, 'lightyear')
    assert round(distToProximaCentari.magnitude, 3) == 1.301
    assert distToProximaCentari.units == 'parsec'

    distToProximaCentari.ito('lightyear')
    assert round(distToProximaCentari.magnitude, 3) == 4.243
    assert str(distToProximaCentari.units) == 'light_year'

    distToProximaCentari.ito('parsec')
    assert round(distToProximaCentari.magnitude, 3) == 1.301
    assert distToProximaCentari.units == 'parsec'
    # isDroidsWeAreLookingFor = sysml.ValueType(False)
    # # assert repr(isDroidsWeAreLookingFor) == "\xabvalueType\xbb False bool"
    # assert isDroidsWeAreLookingFor.magnitude is False
    # assert isDroidsWeAreLookingFor.units == 'dimensionless'
    # assert isDroidsWeAreLookingFor.name == 'False bool'

    c = 2.99792458*10**8
    warpfactor1 = sysml.ValueType(c, 'meters/second')
    warpfactor2 = warpfactor1 + sysml.ValueType(7*c, 'meters/second')
    warpfactor5 = 125*warpfactor1
    warpfactor3 = warpfactor5 - sysml.ValueType(98*c, 'meters/second')
    warpfactor6 = sysml.ValueType(217*c, 'meters/second') - warpfactor1
    warpfactor4 = warpfactor5/2
    assert warpfactor1.magnitude == c
    assert warpfactor2.magnitude == 8*c
    assert warpfactor3.magnitude == 27*c
    assert warpfactor5.magnitude == 125*c
    assert warpfactor4.magnitude == warpfactor5.magnitude/2
    assert warpfactor6.magnitude == 216*c

    with pytest.raises(Exception) as info:
        fluxcapacitor = sysml.ValueType(1.21, 'JiggaWatts')
        assert "is not defined in the unit registry" in str(info.value)


def test_package(model):
    """Create a package, labeled 'Structure', within model which will serve as
    namespace for the system structure

    Note: Model and Package objects can be thought of as a dict-like container
    for returning stereotyped model elements
    """

    with pytest.raises(TypeError) as info:
        model.add()
        assert "missing 1 required positional argument" in str(info.value)

    package_type = "<class 'sysml.element.Package'>"

    holodeck = sysml.Package('Holodeck')

    assert holodeck.stereotype == "\xabpackage\xbb"

    model.add('holodeck', holodeck)

    # assert repr(model['holodeck']) == "\xabpackage\xbb Holodeck"
    # assert repr(type(model['holodeck'])) == package_type
    assert uuid.UUID(model['holodeck'].uuid, version=1)
    # assert repr(model.elements) == "{'holodeck': \xabpackage\xbb Holodeck}"

    model.remove('holodeck')

    with pytest.raises(KeyError) as info:
        model['holodeck']
        assert "holodeck" in str(info.value)

    starship_block = sysml.Block('Constitution-class Starship')

    structure = sysml.Package('structure', {'starship': starship_block})

    model.add('structure', structure)

    with pytest.raises(TypeError) as info:
        model['structure'].add()
        assert "missing 1 required positional argument" in str(info.value)

    # model['structure'].add(starship_block)

    assert starship_block is model['structure']['starship']

    # assert repr(model['structure']) == "\xabpackage\xbb structure"
    # assert repr(type(model['structure'])) == package_type
    assert uuid.UUID(model['structure'].uuid, version=1)

    with pytest.raises(AttributeError) as info:
        model['structure'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['structure'].uuid = "47"
        assert "can't set attribute" in str(info.value)


def test_block(model):
    """Add block elements to package objects using built-in add_part()
    method"""

    starship_block = sysml.Block('Constitution-class Starship')

    assert starship_block.name == "Constitution-class Starship"
    assert starship_block.stereotype == "\xabblock\xbb"
    assert starship_block.multiplicity == 1
    assert uuid.UUID(starship_block.uuid, version=1)

    l1 = "name: Constitution-class Starship\n"
    l2 = "stereotype: \xabblock\xbb\n"
    l3 = "parts: []\n"
    l4 = "references: []\n"
    l5 = "values: []\n"
    l6 = "constraints: []\n"
    l7 = "flows: []\n"
    l8 = "multiplicity: {}\n".format(starship_block.multiplicity)
    l9 = "uuid: {}".format(starship_block.uuid)

    # assert repr(starship_block) == l1+l2+l3+l4+l5+l6+l7+l8+l9
    assert repr(type(starship_block)) == "<class 'sysml.element.Block'>"

    with pytest.raises(AttributeError) as info:
        starship_block.uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        starship_block.uuid = "47"
        assert "can't set attribute" in str(info.value)


@pytest.mark.skip('Deprecated')
def test_block_stereotype():
    """Test block stereotype"""
    # Note: needs to be rewritten such that users can write derived classes,
    # using block as base class, as a means to extend stereotype

    # enterprise = sysml.Block('NCC-1701',stereotype='constitutionClass')
    # enterpriseD = sysml.Block(
    #     'NCC-1701-D',stereotype=['galaxyClass','flagship'])
    #
    # assert enterprise.stereotype == ['block', 'constitutionClass']
    # assert enterpriseD.stereotype == ['block', 'galaxyClass', 'flagship']
    #
    # with pytest.raises(TypeError) as info:
    #     enterpriseD = sysml.Block('NCC-1701-D',stereotype=47)
    #     assert "must be a string or set of strings" in str(info.value)


def test_block_partProperty(model):
    """Add block elements as parts to parent blocks using add_part() method

    Parts added to a block element are dictionary-callable via the 'parts'
    attribute"""

    starship_block = sysml.Block('Constitution-class Starship')

    starship_block.add_part('saucer section', sysml.Block('Primary Hull'))
    starship_block['engineering'] = sysml.Block('Secondary Hull')

    with pytest.raises(TypeError) as info:
        starship_block.add_part()
        assert "missing 1 required positional argument" in str(info.value)

    with pytest.raises(TypeError) as info:
        starship_block[47]
        assert "must be a string" in str(info.value)

    with pytest.raises(TypeError) as info:
        starship_block[47] = '47'
        assert "must be a string" in str(info.value)

    with pytest.raises(TypeError) as info:
        starship_block['47'] = '47'
        assert "must be a Block" in str(info.value)

    with pytest.raises(KeyError) as info:
        starship_block['47']
        assert "not contained in" in str(info.value)

    primaryhull = starship_block.parts['saucer section']
    engineeringhull = starship_block.parts['engineering']

    assert primaryhull is starship_block['saucer section']
    assert engineeringhull is starship_block['engineering']

    assert starship_block.name == "Constitution-class Starship"
    assert starship_block.stereotype == "\xabblock\xbb"
    assert starship_block.multiplicity == 1
    assert uuid.UUID(starship_block.uuid, version=1)

    l1 = "name: Constitution-class Starship\n"
    l2 = "stereotype: \xabblock\xbb\n"
    l3 = "parts: \n"
    l4 = "\tsaucer section: \xabblock\xbb Primary Hull\n"
    l5 = "\tengineering: \xabblock\xbb Secondary Hull\n"
    l6 = "references: []\n"
    l7 = "values: []\n"
    l8 = "constraints: []\n"
    l9 = "flows: []\n"
    l10 = "multiplicity: {}\n".format(starship_block.multiplicity)
    l11 = "uuid: {}".format(starship_block.uuid)

    # assert repr(starship_block) == l1 + l2+l3+l4+l5+l6+l7+l8+l9+l10+l11
    assert repr(type(starship_block)) == "<class 'sysml.element.Block'>"

    assert repr(type(primaryhull)) == "<class 'sysml.element.Block'>"
    assert repr(type(engineeringhull)) == "<class 'sysml.element.Block'>"
    assert uuid.UUID(primaryhull.uuid, version=1)
    assert uuid.UUID(engineeringhull.uuid, version=1)

    starship_block.add_part('cloak', sysml.Block('Cloaking device'))
    cloaking_device = starship_block.parts['cloak']
    starship_block.remove_part('cloak')

    with pytest.raises(KeyError) as info:
        model['Cloaking device']
        assert 'Cloaking device' in str(info.value)

    with pytest.raises(KeyError) as info:
        starship_block['cloak']
        assert 'cloak' in str(info.value)

    with pytest.raises(AttributeError) as info:
        primaryhull.uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        primaryhull.uuid = "47"
        assert "can't set attribute" in str(info.value)

    assert primaryhull.multiplicity == 1
    assert engineeringhull.multiplicity == 1

    with pytest.raises(TypeError) as info:
        primaryhull.multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        engineeringhull.multiplicity = -1
        assert "must be a positive int" in str(info.value)


def test_block_partProperty_withMultiplicity(model):
    """Add block elements as parts to parent blocks, with multiplicity, using
    add_part() method"""
    # notes: need to redesign multiplicity constructor and setter

    starship_block = model['structure']['starship']

    starship_block.add_part('nacelle', sysml.Block('Nacelle', multiplicity=2))
    starship_block.add_part('pylons', sysml.Block('Pylon', multiplicity=2))

    nacelle = starship_block.parts['nacelle']
    pylon = starship_block.parts['pylons']

    # assert repr(nacelle) == "\xabblock\xbb Nacelle"
    # assert repr(pylon) == "\xabblock\xbb Pylon"

    # assert repr(type(nacelle)) == "<class 'sysml.element.Block'>"
    # assert repr(type(pylon)) == "<class 'sysml.element.Block'>"

    assert nacelle.multiplicity == 2
    assert pylon.multiplicity == 2

    with pytest.raises(TypeError) as info:
        pylon.multiplicity = 'mayonnaise'
        assert "must be a positive int" in str(info.value)
    with pytest.raises(ValueError) as info:
        pylon.multiplicity = -1
        assert "must be a positive int" in str(info.value)


@pytest.mark.skip('WIP')
def test_block_valueProperty(model):
    pass


@pytest.mark.skip('WIP')
def test_block_referenceProperty(model):
    pass


@pytest.mark.skip('WIP')
def test_block_constraintProperty(model):
    pass


@pytest.mark.skip('WIP')
def test_block_port(model):
    pass


@pytest.mark.skip('WIP')
def test_interaction(model):
    """Create an interaction, stereotyped as a test case, to be used to verify
    a requirement"""
    # model.add(sysml.Package('Analysis'))
    # model['Analysis'].add(sysml.TestCase('Warp Field Analysis'))


def test_requirements(model):
    """Create a package, labeled 'Requirements', within model which will serve
    as namespace for the system

    Define two requirement elements, passing in a string name and text field as
    its constructor arguments
    """

    model['requirements'] = sysml.Package('Requirements')

    package_type = "<class 'sysml.element.Package'>"

    # assert repr(model['requirements']) == "\xabpackage\xbb Requirements"
    # assert repr(type(model['requirements'])) == package_type

    assert uuid.UUID(model['requirements'].uuid, version=1)

    with pytest.raises(AttributeError) as info:
        model['requirements'].uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        model['requirements'].uuid = "47"
        assert "can't set attribute" in str(info.value)

    # with pytest.raises(TypeError) as info:
    #     model['requirements'].add(sysml.Requirement())
    #     assert "missing 2 required positional argument" in str(info.value)

    top_lvl_req = sysml.Requirement(
        'Top-level',
        """A constitution-class starship shall provide a 5-year mission
        capability to explore strange new worlds, to seek out new life and new
        civilizations, and to boldly go where no one has gone before.""")
    functional_req = sysml.Requirement(
        'Functional',
        """A constitution-class starship shall be able to travel at warp 8 or
        higher""")
    model['requirements']['top-level'] = top_lvl_req
    model['requirements']['functional'] = functional_req

    assert top_lvl_req is model['requirements']['top-level']
    assert functional_req is model['requirements']['functional']
    # assert repr(top_lvl_req) == "\xabrequirement\xbb Top-level"
    # assert repr(functional_req) == "\xabrequirement\xbb Functional"

    requirement_type = "<class 'sysml.element.Requirement'>"
    # assert repr(type(top_lvl_req)) == requirement_type
    # assert repr(type(functional_req)) == requirement_type

    assert top_lvl_req.stereotype == "\xabrequirement\xbb"

    assert uuid.UUID(top_lvl_req.uuid, version=1)
    assert uuid.UUID(functional_req.uuid, version=1)

    with pytest.raises(AttributeError) as info:
        top_lvl_req.uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        top_lvl_req.uuid = "47"
        assert "can't set attribute" in str(info.value)


def test_derive_requirement(model):
    """Define a dependency relationship, of stereotype «derive», between two
    requirements"""

    # with pytest.raises(TypeError) as info:
    #     model['requirements'].add(sysml.Dependency())
    #     assert "missing 3 required positional arguments" in str(info.value)

    client = model['requirements']['functional']
    supplier = model['requirements']['top-level']
    deriveReqt = sysml.DeriveReqt(client, supplier)
    model['requirements']['deriveReqt1'] = deriveReqt

    assert deriveReqt is model['requirements']['deriveReqt1']

    # assert repr(deriveReqt.client) == "\xabrequirement\xbb Functional"
    # assert repr(deriveReqt.supplier) == "\xabrequirement\xbb Top-level"

    requirement_type = "<class 'sysml.element.Requirement'>"
    derivereqt_type = "<class 'sysml.element.DeriveReqt'>"

    # assert repr(type(deriveReqt)) == derivereqt_type

    # assert repr(type(deriveReqt.client)) == requirement_type
    # assert repr(type(deriveReqt.supplier)) == requirement_type
    assert deriveReqt.stereotype == "\xabderiveReqt\xbb"

    assert uuid.UUID(deriveReqt.uuid, version=1)

    with pytest.raises(AttributeError) as info:
        deriveReqt.uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        deriveReqt.uuid = "47"
        assert "can't set attribute" in str(info.value)


@pytest.mark.skip('WIP')
def test_refine_requirement(model):
    pass
    # instantiate use case
    # add dependency where requirement is supplier node (i.e., "supplier") and
    # use case is client node (i.e., "client")
    # assert dependency supplier is of type(requirement)
    # assert dependency client is of type(use case)
    # assert dependency stereotype is "refine"


def test_satisfy_requirement(model):
    """Define a dependency relationship, of stereotype «satisfy», between a
    requirement and block"""

    starship_block = model['structure']['starship']

    warpdrive = sysml.Block('Class-7 Warp Drive')
    starship_block.add_part('warpdrive', warpdrive)

    reqt1 = model['requirements']['functional']
    satisfy = sysml.Satisfy(warpdrive, reqt1)
    model['requirements'].add('satisfy1', satisfy)

    assert satisfy is model['requirements']['satisfy1']

    # assert repr(warpdrive) == "\xabblock\xbb Class-7 Warp Drive"
    # assert repr(reqt1) == "\xabrequirement\xbb Functional"

    assert satisfy.stereotype == "\xabsatisfy\xbb"

    assert satisfy.name == satisfy.name
    assert satisfy.stereotype == "\xabsatisfy\xbb"

    # assert repr(satisfy.client) == "\xabblock\xbb Class-7 Warp Drive"
    # assert repr(satisfy.supplier) == "\xabrequirement\xbb Functional"

    satisfy_type = "<class 'sysml.element.Satisfy'>"
    block_type = "<class 'sysml.element.Block'>"
    requirement_type = "<class 'sysml.element.Requirement'>"

    # assert repr(type(satisfy)) == satisfy_type
    # assert repr(type(satisfy.client)) == block_type
    # assert repr(type(satisfy.supplier)) == requirement_type

    assert uuid.UUID(satisfy.uuid, version=1)

    with pytest.raises(AttributeError) as info:
        satisfy.uuid = 47
        assert "can't set attribute" in str(info.value)
    with pytest.raises(AttributeError) as info:
        satisfy.uuid = "47"
        assert "can't set attribute" in str(info.value)


@pytest.mark.skip('WIP')
def test_verify_requirement(model):
    pass
    # instantiate test case
    # add dependency where requirement is supplier node (i.e., "supplier")
    # and test case is client node (i.e., "client")
    # assert dependency supplier is of type(Requirement)
    # assert dependency client stereotype is a «testCase»
    # assert dependency stereotype is "verify"


if __name__ == '__main__':
    print(__doc__)
    pytest.main(args=['-v'])
