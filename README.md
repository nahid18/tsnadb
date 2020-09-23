# TSNAdb Downloader

A command line interface downloader tool for Tumor-Specific NeoAntigen database (TSNAdb) developed for Cambridge Bioinformatics Hackathon 2020


### Installation

Create a conda environment first, and then install required packages:
```sh
conda install -c conda-forge argparse
conda install -c conda-forge python-wget
```
To download all tumors:
```sh
python tsnadb.py -t all -o output
```

To download Bladder tumors for both NetMHCpan 2.8 and NetMHCpan 4.0:
```sh
python tsnadb.py -t bladder -o output
```

To get help, run
```sh
python tsnadb.py -h
```
License
----

GNU General Public License


