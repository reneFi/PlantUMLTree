# PlantUMLTree

This is PlantUML parser based on the Proof-of-Concept PlantUML parser (https://github.com/pjcuadra/plantuml-parser/blob/master/README.md). The parser now supports:

* class diagrams
* state diagrams 

PlantUML is being parsed using LARK and described in EBNF.

## Usage

```
python plantuml-tree.py -i <plantuml-file>
```

## TODOs

* Finish Supporting all diagram features for state and class diagrams 

* Add support for other diagrams;

  * Sequence Diagram
  * Usecase Diagram
  * Activity Diagram
  * Component Diagram
  * State Diagram
  * Object Diagram
  * Deployment Diagram
  * Timing Diagram
