def process_incoming_document(file_text):
    # Secure: Sanitize and validate input before LLM interaction
    sanitized_input = validate_and_sanitize(file_text)  # Implement validation logic
    
    prompt = f"Summarize this document for the user: {sanitized_input}"
    return prompt