file_name = input("Name of the file: ").strip().lower()

file_extensions = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

file_extension = None
for extension in file_extensions:
    if file_name.endswith(extension):
        file_extension = extension
        break

if file_extension:
    mime_type = file_extensions[file_extension]
    print(mime_type)
else:
    print("application/octet-stream")
