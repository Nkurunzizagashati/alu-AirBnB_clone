import unittest
from models.state import State


class TestState(unittest.TestCase):
    state = State()
    state.name = "Rwanda"
    state.assertIsInstance(state, State)
    state.assertIsInstance(state.name, str)
    state.assertEqual(state.name, "Rwanda")
