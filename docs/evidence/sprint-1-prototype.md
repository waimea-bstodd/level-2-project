# Sprint 1 - Developing a DB and UI Prototype

V1 

First UI concept

https://design.penpot.app/#/view?file-id=6f06cb60-262a-804c-8008-6c67ea606676&page-id=6f06cb60-262a-804c-8008-6c67ea606677&section=interactions&index=0&share-id=1f0b307d-0f2e-41c2-877d-2d7881282a73

V2

V2 is a more simplified concept of V1 after working on the app. Stuff like the bottom buttons were changged and the home page was also changed a lot with also other smaller things were changed 
 https://design.penpot.app/#/view?file-id=52a5041f-08a1-80f1-8008-c3285ac1d6ba&page-id=6f06cb60-262a-804c-8008-6c67ea606677&section=interactions&index=0&share-id=195aa835-355f-45d3-91c0-9fb8081a49c0

## Sprint Goals

Develop a design for the database and a UI prototype that simulates the key functionality of the system. Test and refine the UI so that it can serve as the model for the next phase of development in Sprint 2.

### Specific Goals

**Edit these goals as needed**

- Design the database:
    - Tables
    - Fields / types
    - Primary keys
    - Default / nullable values
    - Relationships (foreign keys)
- Design the UI
    - Key pages
    - User interactions and 'flow'
    - Page layouts / features
    - Colour palette
    - Etc.


## Initial Database Design

Replace this text with notes regarding the DB design.

![DB Design](screenshots/Screenshot%202026-08-17%20102610.png)


### Required Data Input

Audio Files uploaded by the user through the upload form
Track metadata. Tracks should get nammed by the file name and then can be edited by users. Users can also name the artist or album but is optional
playlist data. Users need to be able to name their playlists and also be able to add tracks to them
searching. Users can enter keywords to search for spefcic songs, albums or artists to find what they want to listen to faster

### Required Data Output

Home page. The home page will show recently added songs
Libary page. This will show all songs and playlists
Search results. A way to find spefcic songs, albums or artists

### Required Data Processing

The system securely saves uploaded audio files using unique UUID prefixes, automatically strips extensions to create clean song titles, sanitizes text inputs and runs SQL queries for search and playlist linking.

## UI 'Flow'

The first stage of prototyping was to explore how the UI might 'flow' between states, based on the required functionality.

This Figma demo shows the initial design for the UI 'flow':

**FIGMA FLOW - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT**

https://design.penpot.app/#/view?file-id=6f06cb60-262a-804c-8008-6c67ea606676&page-id=6f06cb60-262a-804c-8008-6c67ea606677&section=interactions&index=0&share-id=1f0b307d-0f2e-41c2-877d-2d7881282a73

### Testing

Checked the layout of song lists on smaller mobile widths to ensure it stayed readable.
### Changes / Improvements

Changed padding sizes so track list doesnt feel squized on diffreant mobile devices 
*IMPROVED FIGMA FLOW - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT*


## Initial UI Prototype

The next stage of prototyping was to develop the layout for each screen of the UI.

This Figma demo shows the initial layout design for the UI:

*FIGMA PROTOTYPE - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT*

### Testing

Replace this text with notes about what you did to test the UI flow and the outcome of the testing.

### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

*FIGMA IMPROVED PROTOTYPE - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT*


## Refined UI Prototype

Having established the layout of the UI screens, the prototype was refined visually, in terms of colour, fonts, etc.

This Figma demo shows the UI with refinements applied:

*FIGMA REFINED PROTOTYPE - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT*

### Testing

Replace this text with notes about what you did to test the UI flow and the outcome of the testing.

### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

*FIGMA IMPROVED REFINED PROTOTYPE - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT*


## Sprint Review

I think that this sprint went well. I manged to make a good enough prototype and tried to follow what I made in penpot. I think working on the css didnt go that well as I dont think im that good at css and the app will look different to the penpot design.
