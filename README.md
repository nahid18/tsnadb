# TSNAdb Downloader

A command line interface downloader tool for Tumor-Specific NeoAntigen database (TSNAdb) developed for Cambridge Bioinformatics Hackathon 2020.
Check the database here: http://biopharm.zju.edu.cn/tsnadb/


### Installation

Create a conda environment first, and then install required packages:
```sh
conda install -c conda-forge python-wget
```
To download all tumors for both NetMHCpan versions:
```sh
python tsnadb.py -t all -o output
```

To download all tumors for specific NetMHCpan version:
```sh
python tsnadb.py -t all -o output --v4
```

To download specific tumors for both NetMHCpan versions:
```sh
python tsnadb.py -t bladder -o output
```

To download specific tumors for a specific NetMHCpan version:
```sh
python tsnadb.py -t head -o output --v2
```

To get help, run
```sh
python tsnadb.py -h
```

All available tumors:
```sh
bladder
brain
breast
cervix
colorectal
head
kidney
liver
lung
ovary
pancreas
prostate
skin
stomach
thyroid
uterus
```

### Citations

[1]. Wu J, Zhao W, Zhou B, Su Z, Gu X, Zhou Z*, Chen S*. TSNAdb: a database for tumor-specific neoantigens from immunogenomics data analysis. Genomics  Proteomics Bioinformatics. 2018, 16(4),276–282. DOI: 10.1016/j.gpb.2018.06.003

[2]. Zhou Z#, Lyu X#, Wu J, Yang X, Wu S, Zhou J, Gu X, Su Z*, Chen S*. TSNAD: an integrated software for cancer somatic mutation and tumour-specific neoantigen detection. R Soc Open Sci. 2017, 4: 170050. DOI: 10.1098/rsos.170050 

License
----

GNU General Public License


