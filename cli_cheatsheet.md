# Terminal Cheatsheet – macOS (zsh/bash)

## Verzeichnisse erstellen und navigieren

```bash
cd /Users/danielhopfner/Desktop/python
pwd  # → /Users/danielhopfner/Desktop/python
mkdir u1
mkdir u2
cd u1
mkdir v1
pwd  # → /Users/danielhopfner/Desktop/python/u1
cd v1
pwd  # → /Users/danielhopfner/Desktop/python/u1/v1
cd /Users/danielhopfner/Desktop/python/u2/
```

## Inhalte anzeigen

```bash
ls
ls -a  # zeigt auch . und ..
```

## Versteckten Ordner anlegen und öffnen

```bash
mkdir .desire
ls -a  # zeigt .desire
cd .desire
open .  # öffnet .desire im Finder
```

## Navigation zurück & Kopieren von Ordnern

```bash
cd ../../../u2
cd ../  # zurück zu /python
cp u1 ~/Desktop/  # Fehler: ist ein Ordner
cp -r u1 ~/Desktop/  # mit -r: Ordner rekursiv kopieren
```

## Mit Textdateien arbeiten

```bash
echo "Hallo"  # gibt Hallo aus
echo "Hallo" >> datei.txt  # anhängen
echo "Halloooooo" > datei.txt  # überschreiben
cp datei.txt ~/Desktop
mv datei.txt u2
cp datei.txt /Users/danielhopfner/Desktop
```

## Zurück ins Home-Verzeichnis

```bash
cd ~
pwd  # → /Users/danielhopfner
cd /Users/danielhopfner/Desktop/python
cd ~/Desktop/python
```

## Dateien löschen / verschieben

```bash
rm datei.txt  # Datei löschen
mv -r u1 ~/.Trash/  # ❌ Fehler: mv kennt kein -r
mv u1 ~/.Trash/  # ✅ korrekt
trash u1  # auch gültig (wenn `trash` installiert ist)
```

---

## CLI-Kurzreferenz

### Verzeichnisse

| Befehl         | Beschreibung                                |
| -------------- | ------------------------------------------- |
| `pwd`          | Zeigt den aktuellen Pfad                    |
| `cd <pfad>`    | Wechselt in ein Verzeichnis                 |
| `cd ~`         | Wechselt ins Home-Verzeichnis               |
| `cd ..`        | Eine Ebene nach oben                        |
| `mkdir <name>` | Erstellt ein Verzeichnis                    |
| `ls`           | Listet Inhalte im Verzeichnis               |
| `ls -a`        | Listet alle Inhalte (inkl. .hidden-Dateien) |

### Dateien & Ordner

| Befehl                  | Beschreibung                                      |
|--------------------------|---------------------------------------------------|
| `cp <datei> <ziel>`     | Kopiert eine Datei                                |
| `cp -r <ordner> <ziel>` | Kopiert ein Verzeichnis rekursiv                  |
| `mv <quelle> <ziel>`    | Verschiebt oder benennt Datei/Ordner              |
| `rm <datei>`            | Löscht eine Datei                                 |
| `trash <pfad>`          | Schiebt Datei/Ordner in den Papierkorb (optional) |
| `mv -r`                 | ❌ Ungültig – `mv` braucht kein `-r` für Ordner    |

### Mit Dateien arbeiten

| Befehl                     | Beschreibung                      |
| -------------------------- | --------------------------------- |
| `echo "Text"`              | Gibt "Text" im Terminal aus       |
| `echo "Text" > datei.txt`  | Überschreibt Datei mit "Text"     |
| `echo "Text" >> datei.txt` | Hängt "Text" an eine Datei an     |
| `open .`                   | Öffnet aktuellen Ordner im Finder |

### Versteckte Dateien & Ordner

| Befehl              | Beschreibung                        |
| ------------------- | ----------------------------------- |
| `mkdir .ordnername` | Erstellt versteckten Ordner         |
| `cd .ordnername`    | Wechselt in den versteckten Ordner  |
| `ls -a`             | Zeigt versteckte Dateien und Ordner |

### Sonstiges

| Befehl                   | Beschreibung                        |
| ------------------------ | ----------------------------------- |
| `cp datei.txt ~/Desktop` | Kopiert Datei auf den Desktop       |
| `mv u1 ~/.Trash/`        | Verschiebt Ordner in den Papierkorb |
| `open .`                 | Öffnet aktuellen Ordner im Finder   |
