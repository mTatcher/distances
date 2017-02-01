#  ReadMe
This project is a test problem which involves graphs.

## Requirements
This program was tested on python 3.6, so execution is guaranteed on this version

## Installation

```
git clone {this repo name}
pip install -r requirements.txt
```

## Usage
in terminal, type
```
python distance.py ${path/to/file} ${city_a} ${city_b}
```
for example,
```
python distance.py ~/my_file.txt Washington "Los Angeles"
```
The output will be a dictionary of 3 keys:

* shortest path: The path from city_a to city_b
* shortest path length: length of the path
* cut size: number of edges to be removed from graph to separate it in 2 (almost) equal parts

## Assumptions
* no empty lines inbetween and no quotes surrounding lines are allowed, and each line of the input file has the following format:
```
city_a, city_b, distance
```
third value in line must be an integer, for example
```
New York, Washington, 1
```
* the graph is connected, i.e. any node is reachable from any other node
