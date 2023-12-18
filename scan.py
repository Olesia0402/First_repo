import sys
from pathlib import Path


images_files = list()
documents_files = list()
audio_files = list()
video_files = list()
archives = list()
others = list()
unknown = set()
extensions = set()

registered_extensions = {
    'JPEG': images_files,
    'PNG': images_files,
    'JPG': images_files,
    'SVG': images_files,
    'DOC': documents_files,
    'DOCX': documents_files,
    'TXT': documents_files,
    'PDF': documents_files,
    'XLSX': documents_files,
    'PPTX': documents_files,
    'MP3': audio_files,
    'OGG': audio_files,
    'WAV': audio_files,
    'AMR': audio_files,
    'AVI': video_files,
    'MP4': video_files,
    'MOV': video_files,
    'MKV': video_files,
    'TAR': archives,
    'GZ': archives,
    'ZIP': archives
}

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in registered_extensions.keys():
                scan(item)
            continue
        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)

if __name__ is '__main__':
    path = sys.argv[1]
    print(f'Start in {path}')

    folder = Path(path)

    scan(folder)

    print(f'images: {images_files}')
    print(f'documents: {documents_files}')
    print(f'audio: {audio_files}')
    print(f'video: {video_files}')
    print(f'archives: {archives}')
    print(f'unknown: {others}')
    print(f'All extensions: {extensions}')
    print(f'Unknown extensions: {unknown}')