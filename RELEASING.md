# Releasing the dataset

## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_hochstetler2004sociolinguistic.py
```


## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_hochstetler2004sociolinguistic.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_hochstetler2004sociolinguistic.py
cldfbench zenodo --communities glottography cldfbench_hochstetler2004sociolinguistic.py
cldfbench readme cldfbench_hochstetler2004sociolinguistic.py
```


## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
17      valid features
18      valid speaker areas
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| ampa1238 | 0.30 | False | 1 |
| bang1363 | 0.00 | True | 1 |
| bond1248 | 0.00 | True | 1 |
| dogu1235 | 0.00 | True | 1 |
| donn1239 | 0.00 | True | 1 |
| jams1239 | 0.00 | False | 1 |
| momb1254 | 0.01 | False | 1 |
| nang1261 | 0.28 | False | 1 |
| tebu1239 | 0.05 | False | 1 |
| tene1248 | 0.00 | True | 1 |
| tomm1242 | 0.00 | True | 1 |
| tomo1243 | 0.00 | True | 1 |
| toro1252 | 0.00 | True | 1 |
| toro1253 | 0.00 | False | 1 |


## Release

Commit and push all changes.

Run
```
cldfbench glottography.release cldfbench_hochstetler2004sociolinguistic.py vX.Y
```
and follow the instructions given in the output of the command.