# TSNAdb Downloader

A command line interface downloader tool for Tumor-Specific NeoAntigen database (TSNAdb) developed for Cambridge Bioinformatics Hackathon 2020.
Check the database here: http://biopharm.zju.edu.cn/tsnadb/


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

To download only for Bladder tumors for both NetMHCpan 2.8 and NetMHCpan 4.0:
```sh
python tsnadb.py -t bladder -o output
```

To download only for Head and Neck tumors only for NetMHCpan 2.8:
```sh
python tsnadb.py -t head -o output --v2
```

To get help, run
```sh
python tsnadb.py -h
```

### Citations

[1]. Wu J, Zhao W, Zhou B, Su Z, Gu X, Zhou Z*, Chen S*. TSNAdb: a database for tumor-specific neoantigens from immunogenomics data analysis. Genomics  Proteomics Bioinformatics. 2018, 16(4),276–282. DOI: 10.1016/j.gpb.2018.06.003

[2]. Zhou Z#, Lyu X#, Wu J, Yang X, Wu S, Zhou J, Gu X, Su Z*, Chen S*. TSNAD: an integrated software for cancer somatic mutation and tumour-specific neoantigen detection. R Soc Open Sci. 2017, 4: 170050. DOI: 10.1098/rsos.170050 

License
----

GNU General Public License


