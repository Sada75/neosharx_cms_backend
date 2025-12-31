import uuid
from django.core.files.uploadedfile import UploadedFile
from common.supabase import supabase


def upload_to_supabase(file: UploadedFile, folder="covers") -> str:
    """
    Uploads a file to Supabase Storage and returns public URL
    """
    filename = f"{folder}/{uuid.uuid4()}-{file.name}"

    supabase.storage.from_("media").upload(
        filename,
        file.read(),
        {"content-type": file.content_type}
    )

    public_url = supabase.storage.from_("media").get_public_url(filename)
    return public_url
