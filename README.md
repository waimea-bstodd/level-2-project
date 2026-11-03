# Music Player

By Ben Todd

## Project Description

This is a app that lets users stream their downloaded music across multiple devices on the same wifi without needing duplicate files on every device. It acts as a local media server where users can upload music files, manage user made playlists, and stream audio directly through a web browser interface accross multiple devices

This project contains demo music that was downloaded from https://pixabay.com/ and all files used are copyright free

The app has the following key features:
- Play local music across multiple devices connected to the same Wifi
- Multi file audio uploads with metadata editing for titles, artists, and albums
- Searching. Users can search for specific tracks, artists, or albums
- Playlists. Users can create, view, and delete playlists
- Track management. Users can delete individual tracks
- Clean and simple layout with a consistent navigation across all pages



## Live Site

The site is hosted at Render at [this link](https://level-2-project-dnzb.onrender.com/)


## Supporting Documents

*For easier reading, the docs are hosted as a [GH Pages site](https://waimea-bstodd.github.io/level-2-project/)*

Task Instructions:
- [Instruction documents](docs/instructions/)

Project Evidence
- [Sprint 0: Project Requirements](docs/evidence/sprint-0-requirements.md)
- [Sprint 1: Prototype Development](docs/evidence/sprint-1-prototype.md)
- [Sprint 2: Database](docs/evidence/sprint-2-database.md)
- [Sprint 3: MVP Development](docs/evidence/sprint-3-mvp.md)
- [Sprint 4: Final System Development](docs/evidence/sprint-4-final.md)
- [Review: Project Final Review](docs/evidence/system-review.md)


## Technologies Used

- [Flask](https://flask.palletsprojects.com/) as the web framework
- [Python](https://www.python.org/) as the programming language used
- [SQLite](https://sqlite.org/) for the database
- [Jinja2](https://jinja.palletsprojects.com/templates/) for page templating


## Project Structure

```
├── README.md            # Project README
│
├── requirements.txt     # Python modules required
│
├── app/                 # Flask application
│   │
│   ├── __init__.py      # Routes and app logic
│   │
│   ├── .env             # Environment values
│   │
│   ├── templates/       # Jinja2 templates
│   │   ├── pages/       # Full page templates
│   │   └── partials/    # Reusable template parts
│   │
│   ├── static/          # Files to be served directly
│   │   ├── css/         # CSS stylesheets
│   │   ├── images/      # Images
│   │   └── js/          # Javascript files
│   │
│   ├── db/              # Database files
│   │   ├── config.py    # Database schema & seed data
│   │   └── data.sqlite  # SQLite database
│   │
│   └── helpers/         # Helper files (don't modify)
│
└── docs/                # Project documentation
    ├── guides/          # Helpful guides
    ├── instructions/    # Task instructions
    └── evidence/        # Project evidence
```
