"""Test execution for plantuml parser"""

# Copyright 2024 René Fischer - renefischer@fischer-homenet.de
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from src.output.statemachine.statemachine import StateMachine
from src.output.statemachine.statemachine import State

def test_statemachine_name():
    """Fuction for testing all plantuml class diagrams located in class_diagram folder"""

    statemachine = StateMachine("TestStatemachine")
    assert statemachine.get_name() == "TestStatemachine"

def test_statemachine_empty():
    """Fuction for testing all plantuml class diagrams located in class_diagram folder"""

    statemachine = StateMachine("test")
    assert statemachine.get_initial_state() is None

def test_statemachine_insert_state_should_return_the_state():
    """Fuction for testing all plantuml class diagrams located in class_diagram folder"""

    statemachine = StateMachine("test")
    statemachine.insert_state(State("State1"))
    assert statemachine.get_initial_state().get_name() == "State1"

def test_statemachine_insert_second_state_should_return_the_last_state():
    """Fuction for testing all plantuml class diagrams located in class_diagram folder"""

    statemachine = StateMachine("test")
    statemachine.insert_state(State("State1"))
    statemachine.insert_state(State("State2"))
    assert statemachine.get_initial_state().get_name() == "State2"