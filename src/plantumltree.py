"""Modulefor parsing plantuml diagrams to an AST"""

# Copyright 2024 René Fischer - renefischer@fischer-homenet.de
#
# Copyright 2018 Pedro Cuadra - pjcuadra@gmail.com
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
from sys import argv
import sys
import os
import logging
from lark import Lark, Tree


def getopts(argvalues):
    """Function parsing command line options"""
    opts = {}  # Empty dictionary to store key-value pairs.
    while argvalues:  # While there are arguments left to parse...
        if argvalues[0][0] == '-':  # Found a "-name value" pair.
            if len(argvalues) > 1:
                if argvalues[1][0] != '-':
                    opts[argvalues[0]] = argvalues[1]
                else:
                    opts[argvalues[0]] = True
            elif len(argvalues) == 1:
                opts[argvalues[0]] = True

        # Reduce the argument list by copying it starting from index 1.
        argvalues = argvalues[1:]
    return opts

def print_tree(node, level=0):
    """ Print the current node with indentation based on the level """
    print("  " * level + f"{node.data}")

    # Recursively print each child
    for child in node.children:
        if isinstance(child, Tree):
            print_tree(child, level + 1)  # Recur with increased level
        else:
            print("  " * (level + 1) + str(child))  # Terminal node (e.g., literal)


def in_order_traversal(node):
    """ Print the tree in in order traversal """
    if len(node.children) == 2:  # Binary operator case
        if isinstance(node.children[0], Tree):
            in_order_traversal(node.children[0])
        else:
            print(node.children[0], end=" ")

        print(node.data, end=" ")
    
        if isinstance(node.children[1], Tree):
            in_order_traversal(node.children[1])
        else:
            print(node.children[1], end=" ")

# Function to recursively traverse the tree
def traverse_tree(tree):
    """ Print the tree by recursively traversing the tree """
    print(f"Node: {tree.data}")

    # If the node has children, recursively traverse them
    if tree.children:
        for child in tree.children:
            if isinstance(child, Tree):  # If child is a Tree node, recursively traverse it
                traverse_tree(child)
            else:
                print(f"Terminal: {child}")

if __name__ == '__main__':
    myargs = getopts(argv)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    grammar_file_path = os.path.join(dir_path, "grammar", "grammar.ebnf")
    with open(grammar_file_path, encoding="utf-8") as grammar_file:
        parser = Lark(grammar_file.read())

        if '-i' in myargs:
            with open(myargs['-i'], encoding="utf-8") as puml:
                ast = parser.parse(puml.read())
                traverse_tree(ast)
                print("********************************Print tree")
                print_tree(ast)
                print("********************************In order traversal")
                in_order_traversal(ast)
                print (type(ast))
        else:
            sys.exit(1)

    if '-v' in myargs:
        logging.basicConfig(level=logging.INFO)
