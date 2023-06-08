import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_base_model_initialization(self):
        # Test model initialization
        model = BaseModel()
        
        # Verify that the model attributes are set correctly
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        
    def test_base_model_to_dict(self):
        # Test conversion of model to dictionary
        model = BaseModel()
        model.name = "Test Model"
        model.age = 25
        
        model_dict = model.to_dict()
        
        # Verify that the converted dictionary has the expected keys and values
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        self.assertEqual(model_dict['name'], model.name)
        self.assertEqual(model_dict['age'], model.age)
        
    def test_base_model_from_dict(self):
        # Test creation of model from dictionary
        model_data = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00',
            'updated_at': '2022-01-01T12:30:00',
            'name': 'Test Model',
            'age': 25
        }
        
        model = BaseModel.from_dict(model_data)
        
        # Verify that the model attributes are set correctly from the dictionary
        self.assertEqual(model.id, model_data['id'])
        self.assertEqual(model.created_at.isoformat(), model_data['created_at'])
        self.assertEqual(model.updated_at.isoformat(), model_data['updated_at'])
        self.assertEqual(model.name, model_data['name'])
        self.assertEqual(model.age, model_data['age'])
        
if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""Test for required behaviour and documentation"""
import unittest
