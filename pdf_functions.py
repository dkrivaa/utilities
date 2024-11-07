import pymupdf
from PIL import Image
import io
import streamlit as st
from pptx import Presentation


# Merge pdfs and return stream
def merge_files(file_list):
    # Create a new PDF document in memory
    merged_pdf = pymupdf.open()

    for pdf in file_list:
        # Open the uploaded file directly without saving it to disk
        with pymupdf.open(stream=pdf.read(), filetype="pdf") as pdf_file:
            # Insert all pages from the current PDF into the merged PDF
            merged_pdf.insert_pdf(pdf_file)

    # Save the merged PDF to a BytesIO object
    pdf_stream = io.BytesIO()
    merged_pdf.save(pdf_stream)
    merged_pdf.close()

    # Move to the beginning of the BytesIO buffer
    pdf_stream.seek(0)

    return pdf_stream


# Get PDF page count
def get_page_count(pdf):
    with pymupdf.open(stream=pdf, filetype="pdf") as pdf_file:
        page_count = pdf_file.page_count
    return page_count


# Split PDF and return list of streams
def split_file(page_ranges):
    original_pdf = st.session_state['original_file']
    split_files = []
    # Open the uploaded PDF file in memory
    with pymupdf.open(stream=original_pdf, filetype="pdf") as pdf_file:
        for i, (from_page, to_page) in enumerate(page_ranges):
            # Create a new PDF for the specified page range
            split_pdf = pymupdf.open()  # Create an empty PDF

            # Insert the specified pages into the new PDF
            split_pdf.insert_pdf(pdf_file, from_page=from_page - 1, to_page=to_page - 1)

            # Save the split PDF to a BytesIO object
            pdf_stream = io.BytesIO()
            split_pdf.save(pdf_stream)
            split_pdf.close()

            # Move to the beginning of the BytesIO buffer
            pdf_stream.seek(0)

            # Append the file stream and a name for the file
            split_files.append((pdf_stream, f"split_{i + 1}.pdf"))

    return split_files


def pdf_from_image(image_files):
    # Define A4 dimensions at 72 DPI (pixels)
    A4_WIDTH_PX = 595
    A4_HEIGHT_PX = 842

    # If a single image file is passed, wrap it in a list
    if not isinstance(image_files, list):
        image_files = [image_files]

    # Create an in-memory PDF file
    pdf_stream = io.BytesIO()
    pdf_document = pymupdf.open()  # Create a new PDF document

    for image_file in image_files:
        # Open each image using Pillow
        image = Image.open(image_file)

        # Convert the image to RGB if necessary
        if image.mode in ("RGBA", "P"):  # Convert PNG images with transparency
            image = image.convert("RGB")

        # Resize the image to A4 size
        image = image.resize((A4_WIDTH_PX, A4_HEIGHT_PX), Image.LANCZOS)

        # Create a new A4 page in the PDF
        page = pdf_document.new_page(width=A4_WIDTH_PX, height=A4_HEIGHT_PX)

        # Convert the resized image to bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="JPEG")  # Save as JPEG
        image_bytes.seek(0)

        # Insert the image into the PDF page
        rect = pymupdf.Rect(0, 0, A4_WIDTH_PX, A4_HEIGHT_PX)  # Full-page insertion
        page.insert_image(rect, stream=image_bytes.getvalue())

    # Save the PDF document to the in-memory stream
    pdf_document.save(pdf_stream)
    pdf_document.close()

    # Rewind the buffer to the beginning
    pdf_stream.seek(0)
    return pdf_stream


def pdf_from_pptx(pptx_file):
    def slide_to_image(slide):
        # Placeholder image generation logic; replace this with an actual rendering if available
        image = Image.new("RGB", (1280, 720), color="white")
        # Note: This would need to contain rendering logic for each slide
        # if `python-pptx` could render each slide, it would happen here.
        return image

    # Define A4 dimensions at 72 DPI (pixels)
    A4_WIDTH_PX = 595
    A4_HEIGHT_PX = 842

    # Load the PowerPoint presentation
    presentation = Presentation(pptx_file)

    # Create an in-memory PDF file
    pdf_stream = io.BytesIO()
    pdf_document = pymupdf.open()  # Create a new PDF document

    for slide_number, slide in enumerate(presentation.slides):
        # Render each slide to an image
        image_stream = io.BytesIO()
        image = slide_to_image(slide)
        image = image.resize((A4_WIDTH_PX, A4_HEIGHT_PX), Image.LANCZOS)
        image.save(image_stream, format="JPEG")
        image_stream.seek(0)

        # Create a new page in the PDF for each slide
        page = pdf_document.new_page(width=A4_WIDTH_PX, height=A4_HEIGHT_PX)
        rect = pymupdf.Rect(0, 0, A4_WIDTH_PX, A4_HEIGHT_PX)
        page.insert_image(rect, stream=image_stream.getvalue())

    # Save the PDF document to the in-memory stream
    pdf_document.save(pdf_stream)
    pdf_document.close()

    # Rewind the buffer to the beginning
    pdf_stream.seek(0)
    return pdf_stream




