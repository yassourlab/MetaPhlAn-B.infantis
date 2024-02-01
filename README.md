# MetaPhlAn-B.infantis
MetaPhlAn database that allows quantification of _Bifidobacterium longum_ subspecies (_Bifidobacterium longum_ subsp. _infantis_ and _Bifidobacterium longum_ subsp. _longum_) from metagenomic data. 
This tool is based on the standard MetaPhlAn4 database. After running it MetaPhlAn4 can re ran as usual with the flags `--index` and `--bowtie2db` specifying the new custom database. 

If you use this tool please cite: 
Ennis, D., Shmorak, S., Jantscher-Krenn, E., & Yassour, M. (2024). Longitudinal quantification of Bifidobacterium longum subsp. infantis reveals late colonization in the infant gut independent of maternal milk HMO composition. Nature Communications, 15(1), 894.

## Installation and requirements
* Clone the repository using `git clone`.
* Make sure you have the following dependencies (excpet for click they are all included in the MetaPhlAn conda environment):
  * bowtie2
  * python3 packages: click, pickle, bz2, subprocess, os
 
## Running
To add _B. longum_ subspecies specific markers to the metaphlan database run
`metaphlan_longum_markers.py --mpa-db-directory <PATH TO METAPHLAN ORIGINAL DATABASE>`

Optional arguments:  
`--db_name`   The name of the original database without a suffix. Default :'mpa_vOct22_CHOCOPhlAnSGB_202212'  
`--output`    The directory in which to save the new database. Default: current directory

Note that since the MetaPhlAn bowtie database is inspected and rebuilt,  this process needs time and memory (~3 hours, 32g, 12 CPUs) 
