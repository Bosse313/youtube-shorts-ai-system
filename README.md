# 🎬 YouTube Shorts AI System

Ein lokales Starter-Projekt für ein KI-gestütztes YouTube-Shorts-System mit:
- Trend-Analyse
- automatischer Video-Idee und Script-Erzeugung
- 3D-Workflow-Visualisierung
- manuelle Freigabe vor dem Upload
- vollständiger Kontrolle über jeden Schritt

## Projektziel

Dieses Projekt ist bewusst als transparente, kontrollierbare Grundversion gebaut. Du bekommst nicht nur ein "Black-Box"-System, sondern ein Dashboard, in dem du jede Phase nachvollziehen, prüfen und bei Bedarf anpassen kannst.

## Kernprinzip

- Das System schaut sich Trends an und erkennt Muster
- Basierend auf einem Trend wird ein Video-Konzept erstellt
- Ein Script und eine Stimme werden vorbereitet
- Der Workflow wird in einer 3D-Ansicht sichtbar gemacht
- Du prüfst alles und genehmigst erst dann den Upload

## Verzeichnisstruktur

```text
youtube-shorts-ai-system/
├── backend/
│   ├── main.py
│   ├── trending_analyzer.py
│   └── video_generator.py
├── frontend/
│   ├── index.html
│   └── workflow3d.html
├── .env.example
├── README.md
├── requirements.txt
└── start.sh
```

## Voraussetzungen

- Python 3.10+
- Git
- Visual Studio Code (optional, aber empfohlen)

## Installation

1. Repository klonen

```bash
git clone https://github.com/Bosse313/youtube-shorts-ai-system.git
cd youtube-shorts-ai-system
```

2. Abhängigkeiten installieren

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Umgebungsvariablen anlegen

```bash
cp .env.example .env
```

4. Starten

```bash
bash start.sh
```

Dann öffnest du im Browser:
- http://localhost:5000
- http://localhost:5000/workflow3d

## So funktioniert das System

### 1) Trend-Analyse
Das System liefert Beispiel-Trends, die du mit deinen eigenen aktuellen Nischen, Hashtags oder Ideen erweitern kannst.

### 2) Workflow-Erzeugen
Aus einem ausgewählten Trend wird automatisch ein Video-Plan erzeugt, inklusive:
- Titel
- Hook
- Script
- Voice-over
- Shot-Plan
- Bearbeitungs-Schritte
- Freigabe-Status

### 3) 3D-Visualisierung
Auf der 3D-Seite siehst du die einzelnen Zustände des Workflows als Karten, die in einer räumlichen Darstellung angezeigt werden.

### 4) Menschliche Kontrolle
Du hast volle Kontrolle:
- Trends prüfen
- Script lesen
- Voice-over anpassen
- Video vor Upload freigeben oder ablehnen

## Wichtige Hinweise

- Dies ist ein lokaler Starter-Workflow, keine komplette KI-Produktionspipeline mit echten API-Uploads
- Für echte Videos müsstest du später echte APIs wie OpenAI, ElevenLabs, Runway oder YouTube verbinden
- Du kannst dieses Projekt nach Bedarf erweitern und genau dort steuern, wo du Kontrolle brauchst

## Nächste Erweiterungen

- echte OpenAI-Integration
- echte ElevenLabs-TTS-Integration
- echte Video-Generierung per Runway/Pika
- echte YouTube-Upload-API
- Vorschau-Funktion mit FFmpeg
- automatische Scheduler-Tasks

## Datenschutz und Kontrolle

Das System ist bewusst so aufgebaut, dass du in jedem Schritt die Transparenz behältst. Du musst nichts blind akzeptieren.

---

Wenn du möchtest, kann ich als Nächstes eine zweite Stufe bauen:
- echte OpenAI-API-Integration
- echte TTS-Integration
- echte YouTube-Upload-Funktionen
- ein größeres Dashboard mit Automatisierung und Filterung
