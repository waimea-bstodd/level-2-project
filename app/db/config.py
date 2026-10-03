class TrackTable:
    NAME = "tracks"
    SCHEMA = """
        CREATE TABLE tracks (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            title    TEXT NOT NULL,
            artist   TEXT NOT NULL,
            album    TEXT,
            filename TEXT NOT NULL,
            created  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    SEED_DATA = None

class PlaylistTable:
    NAME = "playlists"
    SCHEMA = """
        CREATE TABLE playlists (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT NOT NULL,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    SEED_DATA = None

class PlaylistTrackTable:
    NAME = "playlist_tracks"
    SCHEMA = """
        CREATE TABLE playlist_tracks (
            playlist_id INTEGER NOT NULL,
            track_id    INTEGER NOT NULL,
            FOREIGN KEY(playlist_id) REFERENCES playlists(id),
            FOREIGN KEY(track_id) REFERENCES tracks(id),
            PRIMARY KEY(playlist_id, track_id)
        )
    """
    SEED_DATA = None

TABLES = [
    TrackTable,
    PlaylistTable,
    PlaylistTrackTable
]