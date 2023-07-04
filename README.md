# MetaPhlAn-B.infantis
MetaPhlAn database that allows quantification of _Bifidobacterium longum_ subspecies (_Bifidobacterium longum_ subsp. _infantis_ and _Bifidobacterium longum_ subsp. _longum_) from metagenomic data. 

# Installation and requirements
* Clone the repository using `git clone`.
* Make sure you have the following dependencies:
  * bowtie2
  * python3 packages: click, pickle, bz2, subprocess, os, sys
 
# Running
To add B. longum subspoecies specific markers to the metaphlan database run
`XXX --mpa-db-directory <PATH TO METAPHLAN ORIGINAL DATABASE>`

Optional arguments:
`--db_name  The name of the database without a suffix. default :'mpa_vOct22_CHOCOPhlAnSGB_202212'
--output    The directory in which to save the new database. default: current directory`

Note that since the MetaPhlAn bowtie database is inspected and rebuilt this can take time an memory (~12 hours, 16g) 
