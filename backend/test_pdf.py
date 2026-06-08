from app.document_processor import extract_text, create_chunks

text = extract_text("uploads/Cloud.pdf")

chunks = create_chunks(text)

print("Chunks:", len(chunks))
print(chunks[0])
