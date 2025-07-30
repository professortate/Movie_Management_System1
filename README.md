# Movie Management System

A Python-based movie database management system with HTML interface for comprehensive CRUD operations.

## Technical Overview

This repository implements a **Movie Management System** using Python (64.7%) for backend processing and HTML (35.3%) for the user interface. The system provides a complete set of **CRUD operations** (Create, Read, Update, Delete) for managing movie data through a web-based interface.

## System Requirements

- Python 3.8+
- Web server capability (built-in or external)
- Database engine (SQLite/MySQL/PostgreSQL)
- Browser with HTML5 support
- Dependencies listed in `requirements.txt`

## Technical Architecture

```
┌─────────────────────┐      ┌─────────────────────┐
│ Web Interface (HTML)│◄────►│  Python Controller  │
└─────────────────────┘      └──────────┬──────────┘
                                        │
                                        ▼
                             ┌─────────────────────┐
                             │  Data Access Layer  │
                             └──────────┬──────────┘
                                        │
                                        ▼
                             ┌─────────────────────┐
                             │     Database        │
                             └─────────────────────┘
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/acharyamohan/Movie_Management_System.git
   cd Movie_Management_System
   ```

2. **Set up Python environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
   ```bash
   # Edit config.py or .env file with your database parameters
   python setup_db.py  # If available
   ```

5. **Run the application:**
   ```bash
   python run.py  # Or the appropriate entry point
   ```

## Core CRUD Functionality

### **C**reate Operations
- **Add New Movie**: Insert movie records with title, release year, genre, director, etc.
- **Add Genre/Category**: Manage movie classifications
- **Add Cast/Crew**: Track actors, directors and production staff

### **R**ead Operations
- **Search Movies**: Query by title, genre, year, director, actor
- **View Movie Details**: Access comprehensive information for each entry
- **Generate Reports**: Create custom reports on movie collections

### **U**pdate Operations
- **Edit Movie Details**: Modify any movie attributes
- **Update Categories**: Reclassify movies with different genres
- **Manage Relationships**: Change associations between movies and personnel

### **D**elete Operations
- **Remove Movies**: Delete entries from database
- **Purge Categories**: Remove unused classifications
- **Clean Database**: Maintenance operations for data integrity

