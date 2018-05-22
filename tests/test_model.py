import sysml
import pytest
import uuid

# Notes: block elements with starting property attributes should be broken down into granular blocks and assigned id's & relationships upon assimilation into model.
@pytest.fixture
def model():
    "Create a SysML model instance"
    model = sysml.Model()
    return model

@pytest.fixture
def add_package(model):
    """Add element(s) to model using built-in 'add_elements()' method
    Note: model keys are internally generated"""
    model.add_package('Structure')
    return model

def test_add_package(add_package):
    model = add_package
    assert repr(model['Structure']) == "\xabpackage\xbb 'Structure'"

def test_package_has_valid_uuid(add_package):
    "Model elements should be assigned a uuid upon assimilation into model"
    model = add_package
    assert uuid.UUID(model['Structure'].uuid, version=1)

@pytest.fixture
def add_block_to_package(add_package):
    """ add block elements as parts to parent blocks using `add_block` the method"""
    model = add_package
    model['Structure'].add_block('Constitution-class starship')
    return model

def test_add_block_to_package(add_block_to_package):
    """ add block elements as parts to parent blocks using `add_block` the method"""
    model = add_block_to_package
    assert repr(model['Structure']['Constitution-class starship']) == "\xabblock\xbb 'Constitution-class starship'"

def test_block_has_valid_uuid(add_block_to_package):
    "Model elements should be assigned a uuid upon assimilation into model"
    model = add_block_to_package
    assert uuid.UUID(model['Structure']['Constitution-class starship'].uuid, version=1)

@pytest.fixture
def add_parts_to_block(add_block_to_package):
    model = add_block_to_package
    model['Structure']['Constitution-class starship'].add_part('Primary Hull')
    model['Structure']['Constitution-class starship'].add_part('Engineering Hull')
    return model

def test_add_parts_to_block(add_parts_to_block):
    "Parts added to a block element are callable by index via the 'parts' attribute"
    model = add_parts_to_block
    assert repr(model['Structure']['Constitution-class starship'].parts['Primary Hull']) == "\xabblock\xbb 'Primary Hull'"
    assert repr(model['Structure']['Constitution-class starship'].parts['Engineering Hull']) == "\xabblock\xbb 'Engineering Hull'"

def test_block_part_has_valid_uuid(add_parts_to_block):
    "Model elements should be assigned a uuid upon assimilation into model"
    model = add_parts_to_block
    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['Primary Hull'].uuid, version=1)
    assert uuid.UUID(model['Structure']['Constitution-class starship'].parts['Engineering Hull'].uuid, version=1)

@pytest.mark.skip('WIP')
def test_bdd(add_parts_to_block):
    "methods can also be called on package objects for generating 'diagram objects' for the 9 SysML diagrams"
    model = add_parts_to_block
    model['Structure'].bdd() # generates a block-definition diagram object on the 'Structure' package
    model['Structure'].show() # show diagrams generated for package, 'Structure'
    # Need some way to test diagram was generated

@pytest.fixture
def add_requirements(model):
    model.add_package('Requirements') # creates a package, labeled 'Requirements', within model for storing model requirements
    model['Requirements'].add_requirement('Top-level', 'A constitution-class starship shall be able to boldly go where no one has gone before')
    model['Requirements'].add_requirement('Functional-1', 'A constitution-class starship shall be able to travel at warp 8 or higher')
    return model

def test_add_requirements(add_requirements):
    model = add_requirements
    assert repr(model['Requirements']['Top-level']) == "\xabrequirement\xbb 'Top-level'"
    assert repr(model['Requirements']['Functional-1']) == "\xabrequirement\xbb 'Functional-1'"

def test_requirement_valid_uuid(add_requirements):
    "Model elements should be assigned a uuid upon assimilation into model"
    model = add_requirements
    assert uuid.UUID(model['Requirements']['Top-level'].uuid, version=1)
    assert uuid.UUID(model['Requirements']['Functional-1'].uuid, version=1)

@pytest.fixture
def add_relation_between_requirements(add_requirements):
    "adds relation to 'Requirements' package consisting of source-target pair and relationship type as arguments."
    model = add_requirements
    model['Requirements'].add_relation(model['Requirements']['Functional 1'], model['Requirements']['Top-level'], 'deriveReqt')

@pytest.mark.skip('WIP')
def test_add_relation_between_requirements(add_relation_between_requirements):
    model = add_relation_between_requirements
    assert repr(model['Requirements'].relations['deriveReqt']['source']) == "\xabrequirement\xbb 'Functional-1'"
    assert repr(model['Requirements'].relations['deriveReqt']['target']) == "\xabrequirement\xbb 'Top-level'"
    assert repr(model['Requirements'].relations['deriveReqt']['type']) == "\xabrequirement\xbb 'Top-level'"
