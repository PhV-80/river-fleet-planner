# river-fleet-planner

**Logistics planning demo for river fleet management (Django + Angular)**

Demo-Projekt für mein Vorstellungsgespräch als Fachinformatiker Anwendungsentwicklung.

---

## 🎯 Projektziel

Zeigen, dass ich:
- Geschäftslogik modellieren kann (Domain-Driven Design)
- Sauberen, testbaren Code schreibe
- Mit modernen Web-Technologien arbeite (Django, Angular)
- Git-Workflows verstehe (Feature-Branches, Pull Requests)

---

## 🚢 Features (V1)

### Backend (Django REST Framework)
- **Ship-Management**: Schiffe anlegen (Name, Kapazität, Status)
- **Voyage-Management**: Fahrten planen (Start-/Zielhafen, Zeitfenster)
- **Konflikt-Check**: Schiff darf nicht doppelt gebucht sein (automatische Validierung)

### Frontend (Angular)
- Ship-Liste + Formular
- Voyage-Liste + Formular
- Konflikt-Anzeige (rot markieren bei Überschneidung)

---

## 🛠️ Tech-Stack

| Komponente | Technologie                        |
|------------|------------------------------------|
| Backend | Django 5.1 + Django REST Framework |
| Frontend | Angular 21                         |
| Datenbank | SQLite (lokal), PostgreSQL (Prod)  |
| Testing | Django Unit Tests                  |
| Deployment | Docker → Proxmox HomeLab           |

---

## 📦 Setup (lokal)

### Backend
```bash
# Venv aktivieren
python -m venv venv
venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -r requirements.txt

# Datenbank migrieren
python manage.py migrate

# Admin-User anlegen
python manage.py createsuperuser

# Server starten
python manage.py runserver
```

### Frontend
```bash
# Angular-CLI installieren (global)
npm install -g @angular/cli

# Dependencies installieren
cd frontend
npm install

# Dev-Server starten
ng serve
```

---

## 🧪 Tests ausführen

```bash
python manage.py test logistics
```

**Aktueller Status:** 6 Tests ✅ (alle grün)

---

## 📅 Projekt-Status

| Tag | Feature | Status | PR                                                         |
|-----|---------|--------|------------------------------------------------------------|
| **Tag 1** | Django-Setup, Models, Tests | ✅ Fertig | [#1](https://github.com/PhV-80/river-fleet-planner/pull/1) |
| **Tag 2** | REST API (CRUD-Endpunkte) | ✅ Fertig | [#2](https://github.com/PhV-80/river-fleet-planner/pull/2)                                                     |
| **Tag 3** | Angular-Setup + erste Komponenten | ➡️ Entfallen | -                                                          |
| **Tag 4** | Angular-UI (vollständig) | 🚧 In Arbeit | -                                                          |
| **Tag 5** | Deployment (Docker + HomeLab) | 📅 Geplant | -                                                          |

---

## 🔗 Live-Demo (nach Tag 5)

[https://fleet-planner.phasev80.de](https://fleet-planner.phasev80.de) (noch nicht deployed)

---

## 📝 Lizenz

Dieses Projekt ist ein Demo-Projekt für Bewerbungszwecke und hat keine formale Lizenz.

---

## 👤 Autor

**PhaseV80**
GitHub: [@PhV-80](https://github.com/PhV-80)
```