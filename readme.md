# json-inspect

[![PyPI version](https://badge.fury.io/py/json-inspect.svg)](https://badge.fury.io/py/json-inspect)
[![PyPI license](https://img.shields.io/pypi/l/json-inspect.svg?maxAge=2592000)](https://github.com/JohnMurray/json-inspect/blob/master/LICENSE)

A command-line tool for inspecting and working with JSON files. Current sub-commands supported include

__Table of Contents__

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Installation](#installation)
- [Sub-Commands](#sub-commands)
  - [histo](#histo)
  - [ext](#ext)
- [Planned Improvements](#planned-improvements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation

You an simply install with the normal method for Python utils, such as

```sh
pip install json-inspect
```

## Sub-Commands

Each sub-command has it's own help file and options and serves different purposes. Please be sure to read the
docs for each command as it may not work like the others. To see the most up-to-date documentation on all available
sub-commands, run the utility with the `-h` options without providing a sub-command.

```text
$ json-inspect -h
usage: json-inspect [-h] [-f FILE] {histo,ext,validate,format} ...

Utility for inspecting JSON files/input

positional arguments:
  {histo,ext,validate,format}
    histo               Create histograms from JSON values
    ext                 Extract values from JSON
    validate            Validate text input as JSON
    format              Nicely format JSON input

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  JSON file to read in. If not provided STDIN will be
                        used
```

Note that there are some global options. The main thing here is that some sort of JSON input is required
for this utility to work. This is defined with the global `-f` option, or by providing input via `STDIN`.

### histo

If you are processing a large number of JSON objects/arrays, then it may be useful to know what fields are present,
what values they contain, and the frequency of both. Starting off with the help file

```text
usage: json-inspect histo [-h] [-p PREFIX] [-c] paths [paths ...]

Generate a histogram based on values found using a JSON search expression

positional arguments:
  paths                 search paths to create histograms for, prefixed with
                        optional value from the --prefix option

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        String to prefix all search-paths with
  -c, --conflate        Conflate non-empty responses to the same value
```

* The `-p` option will allow you to prefix all of your search paths. This is useful if you are performing
multiple searches that have a common prefix for deeply nested JSON searches.
* The `-c` option will conflate your histogram to two values, `__none__` and `__some__`. The first meaning
that no key/value was found for a given lookup in your search path and the latter meaning that _a_ value was
found. This is useful if you only care about the frequency of presence.

A search path is a dot-delimited expression used for traversing JSON objects. An example to get us started is

```text
[].*.user.demographic.regions.[].name
```

To start, note that search expressions contain 3 types of tokens

* `[]` - indicates an array. Each item in the array is collected and will be processed by the next token
* `*` - indicates an object in which all fields should be collected and will be processed by the next token
* `TOKEN` - a field-value of an object. It's value will be collected and processed by the next token

For our example above, it would be satisfied by the following JSON document

```json
[
 {
   "facebook": {
     "user": {
       "demographic": {
         "regions": [ {"name": "US"}, {"name": "Kentucky"}, {"name": "Louisville"} ]
       }
     }
   },
   "google": {
     "user": {
       "demographic": {
         "regions": [ {"name": "US"}, {"name": "Kentucky"}, {"name": "Highland Heights"} ]
       }
     }
   }
 },
 {
   "twitter": {
     "user": {
       "demographic": {
         "regions": [ {"name": "UK"}, {"name": "Wales"} ]
       }
     }
   }
 }
]
```

Running the `histo` sub-command, we would get output such as

```sh
cat test.json | json-inspect histo '[].*.user.demographic.regions.[].name'

[].*.user.demographic.regions.[].name:
Highland Heig   | #########################                          | (1)
US              | ################################################## | (2)
Louisville      | #########################                          | (1)
Kentucky        | ################################################## | (2)
UK              | #########################                          | (1)
Wales           | #########################                          | (1)
```

The bar-chart represents the number found relative to the max found with a total count of finds per-element
in the rightmost column.


### ext

The `ext`, extraction command, is used for pulling data out of JSON files. It supports the
same prefix and search expressions as `histo` along with a few other options for value output.

```
$ json-inspect ext -h
usage: json-inspect ext [-h] [-p PREFIX] [-d DELIM] [-F] paths [paths ...]

Extract values from JSON using a JSON search expression

positional arguments:
  paths                 search paths to return values for

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        String to prefix all search-paths with
  -d DELIM, --delimiter DELIM
                        String to delimit all results by
  -F, --flatten         Flatten array and object values. For objects, only the
                        values (not the keys) are retained in the falttened
                        values
```

Using the same input test JSON file from the `histo` command, we can see an example of
output

```
$ cat test.json | json-inspect ext "[].*.user.demographic.regions.[].*"
Louisville,Kentucky,US,Highland Heights,Kentucky,US,Wales,UK

$ cat test.json | json-inspect ext -d '|' "[].*.user.demographic.regions.[].*"
Louisville|Kentucky|US|Highland Heights|Kentucky|US|Wales|UK
```

## Planned Improvements

[ ] Refactor code to be testable (maybe write some test)
[ ] Add support for `**`
