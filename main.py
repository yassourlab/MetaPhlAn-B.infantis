#!/bin/python3
# update the pkl file to recognize the new markers
# change the longum SGB to be species level and add subspsecies longum and infantis

import click
import pickle
import bz2
import subprocess
import os
import sys
sys.path.append(os.getcwd())


@click.command()
@click.option('--mpa-db-directory', required=True, help="The directory where the original MetaPhlAn database is saved",
              type=click.Path(exists=True), default = sys.path.append(os.path.dirname(__file__)))
@click.option('--db_name', required=False, default="mpa_vOct22_CHOCOPhlAnSGB_202212",
              help="The name of the database without a suffix")
@click.option('--output', '-o', required=False, default=os.path.dirname(__file__),
              help="The directory in which to save the new database")
def run_all(db_name, mpa_db_directory, output):
    db_name_no_suffix = db_name.split(".")[0]
    pkl_file = mpa_db_directory + "/" + db_name_no_suffix + ".pkl"
    output_dir_pkl = output + "/" + "mpa_vOct22_CHOCOPhlAnSGB_lon_subsp_190423.pkl"
    db_file_no_suffix = mpa_db_directory + "/" + db_name_no_suffix
    output_dir_db = output
    # add_markers(db_file_no_suffix, output_dir_db)
    update_pkl_file(pkl_file, output_dir_pkl)
    end_message(output_dir_db)




def add_markers(db_file, output_dir):
    subprocess.run(f"bowtie2-inspect {db_file} > {output_dir}/mpa_vOct22_CHOCOPhlAnSGB_202212_markers.fasta")
    subprocess.run(
        f"cat {output_dir}/mpa_vOct22_CHOCOPhlAnSGB_202212_markers.fasta infantis_ref_markers_panphlan_190423.fa longum_subsp_ref_markers_panphlan_190423.fa > "
        f"{output_dir}/mpa_vOct22_CHOCOPhlAnSGB_202212__markers_lon_subsp.fasta")
    subprocess.run(f"bowtie2-build {output_dir}/mpa_vOct22_CHOCOPhlAnSGB_202212__markers_lon_subsp.fasta "
                   f"{output_dir}/mpa_vOct22_CHOCOPhlAnSGB_lon_subsp")


def update_pkl_file(pkl_file, output_dir):
    # open pkl file
    db = pickle.load(bz2.open(pkl_file, 'r'))

    # add infantis and longum taxonomy
    db['taxonomy']['k__Bacteria|p__Actinobacteria|c__Actinomycetia|o__Bifidobacteriales|f__Bifidobacteriaceae' \
                   '|g__Bifidobacterium|s__Bifidobacterium_longum|t__subsp.infantis'] = (
        '2|201174|1760|85004|31953|1678|216816|', 2832748)
    db['taxonomy']['k__Bacteria|p__Actinobacteria|c__Actinomycetia|o__Bifidobacteriales|f__Bifidobacteriaceae' \
                   '|g__Bifidobacterium|s__Bifidobacterium_longum|t__subsp.longum'] = (
        '2|201174|1760|85004|31953|1678|216816|', 2422247)

    # add infantis genes
    infantis_genes = open("infantis_ref_markers_panphlan_190423_names.txt", 'r').read().split('\n')[:-1]
    gene_len_inf = open("length_infantis_ref_markers_panphlan_190423.txt", 'r').read().split('\n')[:-1]
    i = 0
    for gene in infantis_genes:
        db['markers'][gene] = {'clade': 't__subsp.infantis',
                               'ext': [],
                               'len': float(gene_len_inf[i]),
                               'taxon': 'k__Bacteria|p__Actinobacteria|c__Actinobacteria|o__Bifidobacteriales|f__Bifidobacteriaceae|g__Bifidobacterium|s__Bifidobacterium_longum|t__subsp.infantis'
                               }
        i += 1

    # add longum genes
    longum_genes = open("longum_subsp_ref_markers_panphlan_190423_names.txt", 'r').read().split('\n')[:-1]
    gene_len_lon = open("length_longum_subsp_ref_markers_panphlan_190423.txt", 'r').read().split('\n')[:-1]
    i = 0
    for gene in longum_genes:
        db['markers'][gene] = {'clade': 't__subsp.longum',
                               'ext': [],
                               'len': float(gene_len_lon[i]),
                               'taxon': 'k__Bacteria|p__Actinobacteria|c__Actinobacteria|o__Bifidobacteriales|f__Bifidobacteriaceae|g__Bifidobacterium|s__Bifidobacterium_longum|t__subsp.longum'
                               }
        i += 1

    # remove "t__" from regular longum
    db['taxonomy'][
        'k__Bacteria|p__Actinobacteria|c__Actinomycetia|o__Bifidobacteriales|f__Bifidobacteriaceae|g__Bifidobacterium|s__Bifidobacterium_longum'] = \
        db['taxonomy'].pop(
            'k__Bacteria|p__Actinobacteria|c__Actinomycetia|o__Bifidobacteriales|f__Bifidobacteriaceae|g__Bifidobacterium|s__Bifidobacterium_longum|t__SGB17248')

    for gene in list(db['markers'].keys()):
        if db['markers'][gene][
            'taxon'] == "k__Bacteria|p__Actinobacteria|c__Actinomycetia|o__Bifidobacteriales|f__Bifidobacteriaceae|g__Bifidobacterium|s__Bifidobacterium_longum|t__SGB17248":
            db['markers'][gene][
                'taxon'] = "k__Bacteria|p__Actinobacteria|c__Actinomycetia|o__Bifidobacteriales|f__Bifidobacteriaceae|g__Bifidobacterium|s__Bifidobacterium_longum"
            db['markers'][gene]['clade'] = "s__Bifidobacterium_longum"

    # Save the new mpa_pkl file
    with bz2.BZ2File(output_dir, 'w') as ofile:
        pickle.dump(db, ofile, pickle.HIGHEST_PROTOCOL)


def end_message(output_dir):
    print(f"MetaPhlAn database updated successfully.\n"
          f"The database is saved under {output_dir}/mpa_vOct22_CHOCOPhlAnSGB_lon_subsp\n"
          f"To run Metaphlan with this database add these flags:\n"
          f"--bowtie2db {output_dir}\n"
          f"--index mpa_vOct22_CHOCOPhlAnSGB_lon_subsp_190423")


if __name__ == "__main__":
    run_all()

