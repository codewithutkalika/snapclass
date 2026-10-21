# SnapClass: Intelligent AI Attendance

A face and voice recognition attendance app for classrooms. Teachers take attendance from classroom photos or a voice recording, and the app marks each enrolled student Present or Absent. Students enroll in subjects with a subject code and track their own attendance.

Team project. Built with Python, Streamlit and Supabase (PostgreSQL)

## Features

**Students**
- Sign up with a face photo and a voice sample
- Enroll in a subject using the code given by the teacher, and unenroll later
- Dashboard with a card per subject showing total classes and classes attended

**Teachers**
- Create subjects and share the subject code with students
- Take attendance by uploading or capturing classroom photos (face recognition) or by recording audio (voice recognition)
- Review results (Present or Absent per student) before saving
- Attendance records table with time, subject, subject code and attendance stats

## How it works

1. When a student signs up, their face and voice are converted into numeric embeddings (face_recognition and dlib for faces, Resemblyzer for voices) and stored in Supabase.
2. For attendance, faces or voices in the uploaded media are converted to embeddings and matched against the enrolled students of the selected subject using a scikit-learn classifier.
3. Matched students are marked Present, everyone else Absent, and the result is saved to the attendance log.

## Tech stack

| Area | Technology |
|---|---|
| Language | Python 3.12 |
| Web app / UI | Streamlit, custom CSS |
| Database | Supabase (PostgreSQL) |
| Face recognition | face_recognition (dlib), scikit-learn |
| Voice recognition | Resemblyzer, librosa, PyTorch |
| Security | bcrypt password hashing, secrets kept out of the repo |
| Data handling | pandas, NumPy, Pillow |
| Other | segno (QR codes), Git and GitHub |

## Project structure

```
snapclass/
├── app.py
├── requirements.txt
├── assets/              # images and screenshots
└── src/
    ├── screens/         # home, student and teacher screens
    ├── components/      # dialogs and reusable UI
    ├── database/        # Supabase client and queries
    ├── pipelines/       # face and voice recognition
    └── ui/              # styling
```

## Database tables

students, teachers, subjects, subjects_students (enrollments) and attendance_logs.

## Run locally

1. Install Python 3.12 and Git.
2. Clone the repo and create a virtual environment:

```
git clone https://github.com/<your-username>/snapclass.git
cd snapclass
python -m venv venv312
venv312\Scripts\activate
```

3. Install the packages:

```
python -m pip install -r requirements.txt
```

If dlib or webrtcvad fail to build on Windows, install the pre-built versions instead:

```
python -m pip install dlib-bin
python -m pip install face_recognition --no-deps
python -m pip install face_recognition_models Click numpy pillow "setuptools<81"
python -m pip install resemblyzer --no-deps
python -m pip install webrtcvad-wheels torch
```

4. Create `.streamlit/secrets.toml` with your own Supabase credentials (this file is git-ignored and never committed):

```
SUPABASE_URL = "https://<your-project>.supabase.co"
SUPABASE_KEY = "<your-anon-or-publishable-key>"
```

5. Run the app:

```
python -m streamlit run app.py
```

## Notes

- Use test data only. This is a learning project and its database policies are permissive, so it is not meant for real student data.
- Never commit your Supabase keys.

## Team

- Anita Sharma
- Aashna Mahadik
- Sneha Sharma
- Utkalika Nayak
