from src.ingestion.extractor import extract_pdf
from src.processing.cleaner import clean_page
from src.processing.chunker import chunk_text

from dotenv import load_dotenv
import os
import json

def run_pipeline(file_path) -> dict:
    """
    Extract, clean, and split PDF text into chunks.

    Extracts PDF metadata and page-level text, cleans the text,
    splits non-empty pages into smaller chunks, and stores the
    resulting chunks alongside the file metadata.

    Args:
        file_path (Path): Path to the PDF file.

    Returns:
        dict: A dictionary containing:
            - file_path (str): Absolute path to the PDF file.
            - file_name (str): Name of the PDF file.
            - file_size (int): File size in bytes.
            - file_hash (str): SHA-256 hash of the file.
            - page_count (int): Total number of pages in the PDF.
            - chunks (list): List of text chunks with their associated
              page numbers.

    Raises:
        FileNotFoundError: If the PDF file does not exist or is not
            a regular file.
    """

    all_chunks = []

    extract_data = extract_pdf(file_path)

    for i, raw_text in enumerate(extract_data['pages']):
        clean_data = clean_page(raw_text['text'])
        if clean_data:
            chunk_texts = chunk_text(clean_data, raw_text['page_number'], 500, 100)
            all_chunks.extend(chunk_texts)

    del extract_data['pages']
    extract_data['chunks'] = all_chunks
    
    return extract_data


if __name__ == "__main__":
    try:
        load_dotenv()
        input_file = os.getenv("FILE_PATH")

        result = run_pipeline(input_file)

        print(json.dumps(result, indent=4))
    except FileNotFoundError as e:
        print(f"Error: {e}")