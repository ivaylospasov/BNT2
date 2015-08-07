#!/usr/bin/env python3

from sys import argv
from os import path, getcwd
import glob
import subprocess

work_directory = getcwd()
scripts_path = path.dirname(argv[0])
all_doc_files = glob.glob('*.doc*')


def all_grafici_names():
    list_grafici_names = []
    for file in all_doc_files:
        grafik_name, grafik_extension = path.splitext(file)
        list_grafici_names.append(grafik_name)
    list_grafici_names.sort()
    return list_grafici_names


def make_pdf():
    make_pdfs_script = scripts_path + "/" + 'make_pdfs.sh'
    for document in all_doc_files:
        subprocess.call([make_pdfs_script, document])


def all_pdf_grafici(filenames):
    list_pdf_grafici = []
    for filename in filenames:
        pdf_grafik = filename + ".pdf"
        list_pdf_grafici.append(pdf_grafik)
    list_pdf_grafici.sort()
    return list_pdf_grafici


def all_png_grafici(filenames):
    list_png_grafici = []
    for filename in filenames:
        png_grafik = filename + ".png"
        list_png_grafici.append(png_grafik)
    list_png_grafici.sort()
    return list_png_grafici


def resize_pdf():
    all_pdfs = all_pdf_grafici(all_grafici_names())
    resize_pdfs_script = scripts_path + "/" + "resize_pdfs.sh"
    list_resized_pdfs = []
    for pdf_grafik in all_pdfs:
        resized_pdf_name = "resized-" + pdf_grafik
        subprocess.call([resize_pdfs_script, pdf_grafik, resized_pdf_name])
        list_resized_pdfs.append(resized_pdf_name)
    list_resized_pdfs.sort()
    return list_resized_pdfs


def crop_pdfs():
    all_pdfs = glob.glob("*.pdf")
    all_pdfs.sort()
    crop_pdfs_script = scripts_path + "/" + "crop_pdfs.sh"
    for filename in all_pdfs:
        cropped_name = "crop-" + filename
        subprocess.call([crop_pdfs_script, filename, cropped_name])


def convert_to_png():
    all_pdfs = glob.glob("*.pdf")
    convert_to_png_script = scripts_path + "/" + "convert_to_png.sh"
    for filename in all_pdfs:
        final_name_1 = filename.replace("crop-resized-", "")
        final_name_2 = final_name_1.replace(".pdf", ".png")
        subprocess.call([convert_to_png_script, filename, final_name_2])


def main():
    make_pdf()
    resize_pdf()
    crop_pdfs()
    convert_to_png()

if __name__ == '__main__':
    main()
