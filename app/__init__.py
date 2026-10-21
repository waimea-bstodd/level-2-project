#===========================================================
# Music Player
# Ben Todd
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import os
import html
import uuid
from app.helpers import *


# Create the app
app = Flask(__name__)


# Set up the folder where uploaded music files will be stored
UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show recent tracks
#-----------------------------------------------------------
@app.get("/")
def home():
    # Fetch the 10 most recently added tracks from the database
    with connect_db() as db:
        sql = "SELECT * FROM tracks ORDER BY created DESC LIMIT 10"
        tracks = db.execute(sql).fetchall()

    return render_template("pages/home.jinja", tracks=tracks)


#-----------------------------------------------------------
# Search page - Lets people search for songs, artists, albums
#-----------------------------------------------------------
@app.get("/search")
def search():
    query = request.args.get('query', '').strip()
    tracks = []
    
    # If a search term was entered, query the database using LIKE filters
    if query:
        search_term = f"%{query}%"
        with connect_db() as db:
            sql = "SELECT * FROM tracks WHERE title LIKE ? OR artist LIKE ? OR album LIKE ?"
            params = (search_term, search_term, search_term)
            tracks = db.execute(sql, params).fetchall()
            
    return render_template("pages/search.jinja", tracks=tracks, query=query)


#-----------------------------------------------------------
# Library page - Show all tracks and playlists
#-----------------------------------------------------------
@app.get("/library")
def library():
    # Retrieve all tracks sorted by artist/title and all playlists sorted by name
    with connect_db() as db:
        tracks = db.execute("SELECT * FROM tracks ORDER BY artist, title").fetchall()
        playlists = db.execute("SELECT * FROM playlists ORDER BY name").fetchall()

    return render_template("pages/library.jinja", tracks=tracks, playlists=playlists)


#-----------------------------------------------------------
# Upload pages - For uploading music to the app
#-----------------------------------------------------------
@app.get("/upload")
def upload_form():
    return render_template("pages/upload.jinja")


@app.post("/upload")
def upload_track():
    audio_files = request.files.getlist('audio')
    
    # Validate that files were actually selected
    if not audio_files or audio_files[0].filename == '':
        flash("Please select at least one audio file.", "error")
        return redirect("/upload")

    success_count = 0

    with connect_db() as db:
        # Loop through each uploaded file and its custom form inputs using enumerate
        for index, audio_file in enumerate(audio_files):
            if audio_file.filename:
                form_title = request.form.get(f'title_{index}', '').strip()
                form_artist = request.form.get(f'artist_{index}', '').strip()
                form_album = request.form.get(f'album_{index}', '').strip()
                
                # Fallback to filename if title is blank
                if not form_title:
                    form_title, _ = os.path.splitext(audio_file.filename)
                
                # Sanitize inputs and apply default values if needed
                title = html.escape(form_title)
                artist = html.escape(form_artist) if form_artist else "Unknown Artist"
                album = html.escape(form_album) if form_album else "Unknown Album"
                
                # Secure the filename and save the audio file to disk
                filename = secure_filename(audio_file.filename)
                unique_filename = f"{uuid.uuid4().hex[:8]}_{filename}"
                filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
                audio_file.save(filepath)

                # Insert track metadata into the database
                sql = "INSERT INTO tracks (title, artist, album, filename) VALUES (?, ?, ?, ?)"
                params = (title, artist, album, unique_filename)
                db.execute(sql, params)
                
                success_count += 1
                
    return redirect("/library")


#-----------------------------------------------------------
# Playlist pages - lets people make playlists and view them
#-----------------------------------------------------------
@app.get("/playlist/new")
def new_playlist_form():
    with connect_db() as db:
        tracks = db.execute("SELECT * FROM tracks ORDER BY title").fetchall()

    return render_template("pages/playlist_new.jinja", tracks=tracks)


@app.post("/playlist")
def create_playlist():
    name = html.escape(request.form.get('name', '').strip())
    track_ids = request.form.getlist('tracks')
    
    # Ensure playlist name is provided
    if not name:
        flash("Playlist name is required.", "error")
        return redirect("/playlist/new")

    with connect_db() as db:
        # Insert new playlist and get its ID
        sql = "INSERT INTO playlists (name) VALUES (?)"
        result = db.execute(sql, (name,))
        playlist_id = result.lastrowid
        
        # Link selected tracks to the playlist via junction table
        for tid in track_ids:
            db.execute("INSERT INTO playlist_tracks (playlist_id, track_id) VALUES (?, ?)", (playlist_id, tid))
            
    return redirect("/library")


@app.get("/playlist/<int:id>")
def view_playlist(id):
    with connect_db() as db:
        playlist = db.execute("SELECT * FROM playlists WHERE id=?", (id,)).fetchone()
        sql = """
            SELECT t.* FROM tracks t
            JOIN playlist_tracks pt ON t.id = pt.track_id
            WHERE pt.playlist_id = ?
        """
        tracks = db.execute(sql, (id,)).fetchall()
        
    return render_template("pages/playlist.jinja", playlist=playlist, tracks=tracks)


#-----------------------------------------------------------
# Delete - Remove tracks and playlists
#-----------------------------------------------------------
@app.post("/track/<int:id>/delete")
def delete_track(id):
    with connect_db() as db:
        # Remove the physical audio file from disk
        track = db.execute("SELECT filename FROM tracks WHERE id=?", (id,)).fetchone()
        if track:
            filepath = os.path.join(UPLOAD_FOLDER, track['filename'])
            if os.path.exists(filepath):
                os.remove(filepath)
            
            # Remove track references from playlists and delete the track record
            db.execute("DELETE FROM playlist_tracks WHERE track_id=?", (id,))
            db.execute("DELETE FROM tracks WHERE id=?", (id,))
            
    return redirect("/library")


@app.post("/playlist/<int:id>/delete")
def delete_playlist(id):
    with connect_db() as db:
        # Remove playlist track connections and delete the playlist record
        db.execute("DELETE FROM playlist_tracks WHERE playlist_id=?", (id,))
        db.execute("DELETE FROM playlists WHERE id=?", (id,))
        
    return redirect("/library")


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)