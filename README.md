# 🎬 YouTube Shorts AI System

Ein vollautomatisiertes System zur Erstellung, Bearbeitung und Veröffentlichung von YouTube Shorts mit KI-Stack und 3D-Workflow-Visualisierung.

## 🎯 Was dieses System macht

- **Ideen generieren** → ChatGPT erstellt automatisch Video-Ideen
- **Scripts schreiben** → Claude schreibt das Drehbuch
- **Stimme generieren** → ElevenLabs erstellt eine professionelle Stimme
- **Video erzeugen** → Runway/Pika erstellt automatisch Videos
- **Bearbeiten** → CapCut/Descript optimiert das Video
- **Hochladen** → YouTube API veröffentlicht automatisch
- **Visualisieren** → 3D-Dashboard zeigt den gesamten Prozess live

## 📊 3D-Workflow (Das Herzstück!)

Das System hat ein interaktives 3D-Modell, das zeigt:
- Jeden Schritt des Workflow-Prozesses
- Den Datenfluss zwischen den KI-Tools
- Live-Status jeder laufenden Video-Erstellung
- Erfolgs- und Fehlerrate

```
[Ideenfindung] → [Script] → [Stimme] → [Video] → [Bearbeitung] → [Upload] → [YouTube]
     ↓            ↓         ↓        ↓         ↓              ↓         ↓
   ChatGPT      Claude   ElevenLabs Runway  CapCut      YouTube API  Public
```

## 🛠️ Komponenten

### Backend (Python)
- **Orchestrator**: Verwaltet den gesamten Workflow
- **KI-Handler**: Verbindungen zu OpenAI, ElevenLabs, Runway, YouTube
- **Scheduler**: Plant automatisch neue Videos
- **Database**: Speichert alle Videos und Metadaten

### Frontend (React + 3D)
- **3D-Visualisierung**: Interaktives Workflow-Modell
- **Dashboard**: Statistiken und Live-Monitor
- **Control Panel**: Einstellen von Einstellungen und Parametern

## 🚀 Quick Start

```bash
# 1. Repository klonen
git clone https://github.com/Bosse313/youtube-shorts-ai-system.git
cd youtube-shorts-ai-system

# 2. Dependencies installieren
pip install -r requirements.txt
npm install

# 3. API-Keys hinzufügen (siehe .env.example)
cp .env.example .env
# Bearbeite .env mit deinen API-Keys

# 4. System starten
python backend/main.py
npm run dev

# 5. Dashboard öffnen
# http://localhost:3000
```

## 📋 API-Keys, die du brauchst

1. **OpenAI** (ChatGPT/GPT-4) - Ideenfindung & Scripts
2. **Anthropic** (Claude) - Alternative für Scripts
3. **ElevenLabs** - Sprachgenerierung
4. **Runway** oder **Pika** - Video-Generierung
5. **YouTube Data API** - Automatisches Hochladen
6. **CapCut API** (optional) - Video-Bearbeitung

> Keine Sorge! Im Setup-Guide erklären wir, wie du alle Keys kostenlos oder günstig bekommst.

## 📁 Ordnerstruktur

```
youtube-shorts-ai-system/
├── backend/
│   ├── main.py                 # Hauptserver
│   ├── config.py               # Konfiguration
│   ├── orchestrator.py         # Workflow-Manager
│   ├── handlers/
│   │   ├── openai_handler.py   # ChatGPT Integration
│   │   ├── claude_handler.py   # Claude Integration
│   │   ├── elevenlabs_handler.py
│   │   ├── runway_handler.py
│   │   └── youtube_handler.py
│   ├── models/
│   │   ├── project.py
│   │   └── video.py
│   └── database/
│       └── db.py
├── frontend/
│   ├── components/
│   │   ├── Workflow3D.jsx      # 3D-Visualisierung
│   │   ├── Dashboard.jsx
│   │   └── ControlPanel.jsx
│   └── App.jsx
├── docs/
│   ├── SETUP.md               # Ausführliche Anleitung
│   ├── API_KEYS.md            # Wie man Keys bekommt
│   └── WORKFLOW.md            # So funktioniert es
├── .env.example
├── requirements.txt           # Python Packages
└── package.json              # JavaScript Packages
```

## 📖 Dokumentation

- **[SETUP.md](docs/SETUP.md)** - Schritt-für-Schritt Installation
- **[API_KEYS.md](docs/API_KEYS.md)** - Wie man Keys bekommt
- **[WORKFLOW.md](docs/WORKFLOW.md)** - Wie das System funktioniert
- **[FAQ.md](docs/FAQ.md)** - Häufige Fragen

## 💰 Ziel

**5.000 € Gewinn pro Monat** durch automatisierte YouTube Shorts

Typisches Einkommen:
- YouTube Ads: 1.000-3.000 €/Monat
- Sponsored Content: 2.000-5.000 €/Monat
- Affiliate Links: 500-1.000 €/Monat

## ⚖️ Wichtige Hinweise

- ✅ Alle generierten Videos müssen lizenziert sein
- ✅ YouTube verbietet 100% KI-generierte Inhalte ohne Disclosure
- ✅ Du musst die Nische und Audience selbst wählen
- ✅ Qualitätskontrolle ist wichtig (nicht alles Auto-Upload!)

## 🤝 Support

Bei Fragen schreib ein Issue oder schau in die Docs!

---

**Viel Erfolg! 🚀**
