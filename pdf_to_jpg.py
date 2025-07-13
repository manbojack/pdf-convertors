#!/usr/bin/env python3
import argparse
from pdf2image import convert_from_path
import os

def pdf_to_jpg(pdf_path):
    images = convert_from_path(pdf_path, dpi=300)
    base_dir = os.path.dirname(pdf_path)
    base_filename = os.path.splitext(os.path.basename(pdf_path))[0]

    for i, image in enumerate(images):
        suffix = f"_page_{i+1}" if len(images) > 1 else ""
        output_path = os.path.join(base_dir, f"{base_filename}{suffix}.jpg")
        image.save(output_path, 'JPEG')
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to JPG (same name as input file).")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    args = parser.parse_args()

    pdf_to_jpg(args.pdf_file)
