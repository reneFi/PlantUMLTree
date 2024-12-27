""" This file contains all classes needed for representing a statemachine"""
class NamedObject:
    """ This class is the base for all named objects within the state machine representation"""
    def __init__(self, name):
        self.set_name(name)  # Set the name of the object

    def set_name(self, name):
        """Set the name of the state machine."""
        self.name = name

    def get_name(self):
        """
        This method returns the name of the object
        """
        return self.name

class State(NamedObject):
    """ This class represents a state in a statemachine """

class StateMachine(NamedObject):
    """ 
    This class conains the statemachine 
    """
    def __init__(self, name):
        super().__init__(name)
        self.initial_state = None

    def get_initial_state(self):
        """
        This method returns the initial state as starting point for traversing the statemachine
        """
        return self.initial_state

    def insert_state(self,state):
        """
        This function changes the initial state of the state machine. 
        As usual, only one initial state is allowed.
        """
        self.initial_state = state
