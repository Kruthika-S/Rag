from app.document_processor import extract_text, create_chunks

text = extract_text("backend/uploads/sample.pdf")

chunks = create_chunks(text)

print("Chunks:", len(chunks))
print(chunks[0])
