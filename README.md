# 🎬 YouTube Shorts AI System

Ein lokales, transparentes Starter-Projekt für ein KI-gestütztes YouTube-Shorts-System mit:
- Trend-Analyse
- automatischer Video-Idee und Script-Erzeugung
- 3D-Workflow-Visualisierung
- manueller Freigabe vor dem Upload
- vollständiger Kontrolle über jeden Schritt

## Projektziel

Dieses Projekt ist bewusst als kontrollierbare Grundversion gebaut. Du bekommst ein Dashboard, in dem du jede Phase nachvollziehen, prüfen und bei Bedarf anpassen kannst. Es ist kein Black-Box-System, sondern ein durchsichtiger Workflow.

## Kernprinzip

- Das System erkennt Trends und Muster
- Aus einem Trend wird ein Video-Konzept erstellt
- Ein Script und eine Stimmrichtung werden vorbereitet
- Der Workflow wird in einer 3D-Ansicht sichtbar gemacht
- Du prüfst alles und genehmigst erst dann den Upload

## Verzeichnisstruktur

```text
youtube-shorts-ai-system/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── trending_analyzer.py
│   └── video_generator.py
├��─ frontend/
│   ├── index.html
│   └── workflow3d.html
├── .env.example
├── README.md
├── requirements.txt
├── start.sh
└── .venv/   # wird lokal beim Start erzeugt
```

## Voraussetzungen

- Python 3.10+
- Git
- optional: Visual Studio Code

## Installation

1. Repository klonen

```bash
git clone https://github.com/Bosse313/youtube-shorts-ai-system.git
cd youtube-shorts-ai-system
```

2. Abhängigkeiten installieren

```bash
python3 -m venv .venv
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

Danach öffnest du im Browser:
- http://localhost:5000
- http://localhost:5000/workflow3d

## So funktioniert das System

### 1) Trend-Analyse
Das System liefert Beispiel-Trends, die du mit deinen eigenen Ideen, Nischen und Hashtags erweitern kannst.

### 2) Workflow-Erzeugen
Aus einem gewählten Trend wird automatisch ein Video-Plan erzeugt, inklusive:
- Titel
- Hook
- Script
- Voice-over
- Shot-Plan
- Bearbeitungs-Schritte
- Freigabe-Status

### 3) 3D-Visualisierung
Auf der 3D-Seite siehst du die einzelnen Zustände des Workflows als visuelle Karten in einer räumlichen Darstellung.

### 4) Menschliche Kontrolle
Du hast volle Kontrolle:
- Trends prüfen
- Script lesen
- Voice-over anpassen
- Video vor Upload freigeben oder ablehnen

## Wichtige Hinweise

- Das ist ein lokaler Starter-Workflow, keine vollständig automatisierte KI-Produktionspipeline
- Für echte Videoproduktionen brauchst du später echte APIs wie OpenAI, ElevenLabs, Runway, Pika oder YouTube
- Die Grundversion ist bewusst transparent und kontrollierbar gebaut

## Nächste Erweiterungen

- echte OpenAI-Integration
- echte ElevenLabs-TTS-Integration
- echte Video-Generierung via Runway/Pika
- echte YouTube-Upload-API
- Vorschau-Funktion mit FFmpeg
- automatischer Scheduler

## Datenschutz und Kontrolle

Das System ist bewusst so aufgebaut, dass du in jedem Schritt die Transparenz behältst. Du musst nichts blind akzeptieren.

---

Wenn du möchtest, kann ich als Nächstes die nächste Stufe bauen:
- echte OpenAI-API-Integration
- echte TTS-Integration
- echte YouTube-Upload-Funktionen
- ein größeres Dashboard mit Logs und Review-Funktion
