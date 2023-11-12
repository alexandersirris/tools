# run pip install pikepdf in terminal

import pikepdf
from pathlib import Path
import os

def split_pdf(input_pdf_path, max_size_mb=25):
    input_pdf = pikepdf.Pdf.open("") # add file to split
    total_pages = len(input_pdf.pages)
    output_pdf = pikepdf.Pdf.new()
    output_filename = f"split_0.pdf"
    file_counter = 0

    for i in range(total_pages):
        output_pdf.pages.append(input_pdf.pages[i])
        temp_filename = f"temp_split.pdf"
        output_pdf.save(temp_filename)

        if os.path.getsize(temp_filename) > max_size_mb * 1024 * 1024: # select max file size to split
            # Remove last added page
            del output_pdf.pages[-1]
            output_pdf.save(output_filename)
            print(f"Saved {output_filename}")
            file_counter += 1
            output_filename = f"split_{file_counter}.pdf"
            output_pdf = pikepdf.Pdf.new()
            output_pdf.pages.append(input_pdf.pages[i])  # Add the page to new split

    # Save the last split file
    if len(output_pdf.pages) > 0:
        output_pdf.save(output_filename)
        print(f"Saved {output_filename}")

    # Clean up temporary file
    if os.path.exists(temp_filename):
        os.remove(temp_filename)

# Example usage
split_pdf("") #add file destination and anme
