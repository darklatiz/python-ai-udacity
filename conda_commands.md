# Conda Quick Guide

## Using Environments
```shell
conda create -n py2_env python=2
conda create -n py3_env python=3`
```

## Sharing Environments
```shell
conda env export > environment.yaml
```

## Share the List of Dependencies
```shell
pip freeze > requirements.txt
```

Later, you can share this requirements.txt file with other users over Github. Once a user (or yourself) switches to another environment, you can install all the packages mentioned in the requirements.txt file using:
```shell
pip install -r requirements.txt
```

## Installing Conda support for looking at the environments available in Jupyter Notebooks

```shell
conda install nb_conda
```

## To Start Jupyter Notebook
```shell
jupyter notebook
```