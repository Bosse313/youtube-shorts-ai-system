from datetime import datetime


def get_trends():
    return [
        {
            "id": "brainrot-001",
            "title": "AI-Chatbot wird zum Lebensberater",
            "niche": "brainrot",
            "hook": "Wenn dein Chef dich im Chatbot-Design findet",
            "why_now": "Humoristische Alltagsszenarien mit Tech-Referenz performen stark.",
            "format": "3-6 Sekunden Hook + schnelle Wiederholungen",
            "tone": "absurd, witzig, schnell",
            "trend_score": 94,
        },
        {
            "id": "brainrot-002",
            "title": "Katzen übernehmen das Büro",
            "niche": "animals",
            "hook": "Die Katze hat heute den Statusbericht geschrieben",
            "why_now": "Tier-Meme mit Büro-Kontext sind extrem starke Shorts-Motive.",
            "format": "Schnelle Bildwechsel, Text Overlay, absurd",
            "tone": "süß + absurd",
            "trend_score": 90,
        },
        {
            "id": "brainrot-003",
            "title": "Bester Freund = falscher Roboter",
            "niche": "tech-humor",
            "hook": "Der Roboter ist immer online, aber nie ehrlich",
            "why_now": "KI-Humor und Roboter-Meme ziehen konstant Aufmerksamkeit an.",
            "format": "Text-Overlay + Screaming Cuts",
            "tone": "dystopisch, humorvoll",
            "trend_score": 91,
        },
        {
            "id": "brainrot-004",
            "title": "Frustrierter Manager 2.0",
            "niche": "office-humor",
            "hook": "Das Meeting war kurz - aber der Stress blieb länger",
            "why_now": "Office-Memes bleiben hoch, wenn sie mit absurdem Twist kombiniert sind.",
            "format": "Jump-Cut, aggressive Sounds, schnelle Wiederholungen",
            "tone": "chaotisch, ernst + absurd",
            "trend_score": 88,
        },
        {
            "id": "brainrot-005",
            "title": "Mein PC hat besseres Timing als ich",
            "niche": "tech-life",
            "hook": "Der Computer reagiert schneller als ich bei Entscheidungen",
            "why_now": "Alltag + Technik + Frust ist ein sehr starkes Content-Muster.",
            "format": "Quick cuts, captions, starker Punchline",
            "tone": "realistisch, humorvoll",
            "trend_score": 87,
        },
    ]


def find_trend(trend_id):
    for trend in get_trends():
        if trend["id"] == trend_id:
            return trend
    return get_trends()[0]
