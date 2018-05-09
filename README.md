# recipes

[![Build Status](https://travis-ci.org/davidmn/recipes.svg?branch=master)](https://travis-ci.org/davidmn/recipes)

## organisation
sorted by meal type currently, as more get added things might group better in another way

## usage
make sure that `mk-recipe.py` is executable then do something like this:
```
./mk-recipe.py --name "Tuna Pasta Puttanesca" --type "main" --serves 4
```
that will create file `main/tuna-pasta-puttanesca.md`

name and type are required arguments while serves is optional

it will not overwrite existing files because
