#  ReadMe
This project is a shortest path finding algorithm implementation

## Requirements
This program was tested on python 3.6, so execution is guaranteed on this version

## Installation

```
git clone {this repo name}
```

## Usage
in terminal, type
```
python distance.py ${path/to/file} ${node_a} ${node_b}
```
for example,
```
python distance.py ~/my_file.txt Moscow "St. Petersburg"
```

## Assumptions
* no empty lines inbetween and no quotes surrounding lines are allowed, and each line of the input file has the following format:
```
city_a, city_b, distance
```
* distance must be an non-negative integer, for example
```
New York, Washington, 1
```
