
# MASHUP

## Assignment 7

## Overview

This assignment consists of two independent programs:

* **Program 1:** Command-line based mashup generator
* **Program 2:** Web-based mashup generator using FastAPI and deployed on Render

Both programs generate an audio mashup by downloading songs of a given singer from YouTube, trimming them to a fixed duration, and concatenating them into a single audio file.

---

# Program 1 – Command Line Mashup Generator

## Objective

To build a Python script that:

1. Searches YouTube for songs of a given singer
2. Downloads a specified number of audio files
3. Trims each audio clip to a fixed duration
4. Concatenates all clips into one mashup file

---

## Methodology

The workflow of Program 1 is as follows:

### Step 1: Input Parameters

The user provides:

* Singer name
* Number of videos (n)
* Duration per clip (d seconds)

Constraints:

* n > 10
* d > 20 seconds

---

### Step 2: Downloading Audio

* The `yt-dlp` library is used to search YouTube with:

  `ytsearch{n}:<singer> songs`

* Only best available audio format is downloaded.

* Files are stored temporarily in the `downloads/` directory.

---

### Step 3: Audio Processing

* The `pydub` library is used.
* Each audio file is:

  * Loaded
  * Trimmed to `d` seconds
* Trimmed clips are appended sequentially into a single `AudioSegment`.

---

### Step 4: Mashup Generation

* The final merged audio is exported as:

  `output/mashup.mp3`



## Observations

* Download speed depends on internet bandwidth.
* Audio length consistency depends on availability of full-length songs.
* `yt-dlp` may occasionally skip unavailable videos.

---

# Program 2 – Web-Based Mashup Generator

## Objective

To extend Program 1 into a web service where:

* User submits inputs via browser
* Mashup is generated on the server
* Final mashup is sent to the user's email

---

## Technology Stack

* FastAPI (backend framework)
* Jinja2 (HTML templating)
* Uvicorn (ASGI server)
* yt-dlp (audio download)
* pydub (audio processing)
* SMTP (email delivery)
* Render (deployment)

---

## Methodology

### Step 1: Web Interface

User enters:

* Singer name
* Number of videos
* Duration per clip
* Email address

Input validation:

* Number of videos > 10
* Duration > 20

If invalid, error message is displayed (no JSON shown to user).

---

### Step 2: Backend Processing

When form is submitted:

1. FastAPI receives POST request.
2. Inputs are validated.
3. `create_mashup()` is called.
4. Mashup is generated using same logic as Program 1.

---

### Step 3: Email Delivery

* After successful mashup generation:

  * The file is attached to an email
  * Sent using Gmail SMTP
* Credentials are stored securely using environment variables.

---

### Step 4: Deployment

The application is deployed on Render:

* Root directory: `Program_2`
* Python version specified in `runtime.txt`
* Dependencies listed in `requirements.txt`
* Start command:

  `uvicorn main:app --host 0.0.0.0 --port 10000`

Live URL:

[https://mashup-pdk9.onrender.com/](https://mashup-pdk9.onrender.com/)


