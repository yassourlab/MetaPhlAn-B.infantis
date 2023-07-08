# MetaPhlAn-B.infantis
MetaPhlAn database that allows quantification of _Bifidobacterium longum_ subspecies (_Bifidobacterium longum_ subsp. _infantis_ and _Bifidobacterium longum_ subsp. _longum_) from metagenomic data. 

If you use this tool please cite: 

## Installation and requirements
* Clone the repository using `git clone`.
* Make sure you have the following dependencies:
  - check that tehese are all in the mpa conda env
  * bowtie2
  * python3 packages: click, pickle, bz2, subprocess, os
 
## Running
To add B. longum subspecies specific markers to the metaphlan database run
`metaphlan_longum_markers.py --mpa-db-directory <PATH TO METAPHLAN ORIGINAL DATABASE>`

Optional arguments:  
`--db_name`   The name of the database without a suffix. Default :'mpa_vOct22_CHOCOPhlAnSGB_202212'  
`--output`    The directory in which to save the new database. Default: current directory

Note that since the MetaPhlAn bowtie database is inspected and rebuilt this can take time an memory (~3 hours, 32g, 12 CPUs) 
