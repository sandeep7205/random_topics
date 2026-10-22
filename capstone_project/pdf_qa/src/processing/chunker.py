def chunk_text(text: str, page_number: int, chunk_size: int = 500, overlap: int = 100) -> list[dict]:
    """
    Split text into smaller chunks with overlapping characters.

    Args:
        text (str): Text to split into chunks.
        page_number (int): Page number associated with the text.
        chunk_size (int): Maximum number of characters per chunk.
            Defaults to 500.
        overlap (int): Number of overlapping characters between
            consecutive chunks. Defaults to 100.

    Returns:
        list[dict]: A list of dictionaries containing:
            - page_number (int): Source page number.
            - chunk_index (int): Sequential chunk number, starting at 1.
            - text (str): Text content of the chunk.
            - char_count (int): Number of characters in the chunk.

        Returns an empty list if the input text is empty.

    Raises:
        ValueError: If overlap is greater than or equal to chunk_size.
    """
    chunk_arr = []
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    if not text:
        return []
    step = chunk_size-overlap
    for index, start in enumerate(range(0, len(text), step)):
        end = start + chunk_size
        chunk = text[start:end]
        chunk_arr.append({"page_number": page_number, "chunk_index":(index + 1), "text":chunk, "char_count": len(chunk)})
    return chunk_arr

if __name__ == "__main__":
    sample_text = (
        "Data engineering is all about building pipelines. "
        "A pipeline takes raw data, cleans it, and loads it into storage. "
        "Chunking breaks big text into small pieces for AI search."
    )
    # Test with small numbers so we can see the overlap easily
    chunks = chunk_text(sample_text, page_number=1, chunk_size=80, overlap=20)
    
    for c in chunks:
        print(f"Chunk {c['chunk_index']} (len {c['char_count']}): {c['text']}")