FROM jupyter/minimal-notebook

LABEL maintainer="André Roque Matheus <amatheus@mac.com"

USER $NB_UID

RUN conda install --quiet --yes 'spacy==2.0.11' 'tabulate==0.8.2'

RUN python -m spacy download en; python -m spacy download pt