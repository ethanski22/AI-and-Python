from mutagen.oggvorbis import OggVorbis

def getOggDuration(file_path):
    audio = OggVorbis(file_path)
    return audio.info.length  # Duration in seconds