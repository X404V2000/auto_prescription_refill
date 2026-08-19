# **OpenX Medic**
### auto_prescription_refill

A command-line system for managing patient prescription requests, notifications, and pick-up tracking, backed by a MySQL database. Currently in early development — CLI-first, with a FastAPI web layer planned for later.
---

## Current Status

**In active development.** Core CLI flow and profile creation are wired up; login, prescriptions, and notifications are still placeholders.

+-----------------------------------------------------------+-------------------------------------------------------------------------------+
| Feature                                                   | Status                                                                        |
|-----------------------------------------------------------|-------------------------------------------------------------------------------|
| Main menu / navigation                                    | Working                                                                       |
| Create profile (form → hash password → save to DB)        | Working (pending live DB test)                                                |
| Patient menu (prescriptions, notifications, tracking)     | Placeholder only                                                              |
| Login (credential checking)                               | Not implemented — currently skips straight to patient menu                    |
| Forgot password                                           | Placeholder only                                                              |
| Structured logging                                        | Working                                                                       |
| MySQL connection                                          | Blocked on local root password reset                                          |
| FastAPI web layer                                         | Not started — `FastAPI()` instance exists in `main.py` but has no routes yet  |
+-----------------------------------------------------------+-------------------------------------------------------------------------------+

---

## Project Structure

```
.
├── main.py                    # CLI entry point: menus, navigation, main loop
├── create_profile.py          # create_usr class — profile creation form + DB save
├── dbase_creds.py             # DB credentials + get_db_connection()
├── dbase_table_generator.py   # Drops/creates the medicUsr table
├── db_connection_test.py      # Standalone script to verify DB connectivity
├── apiCall.py                 # Standardized success/error response helpers
├── syslogGenerator.py         # Custom structured logger (SystemLogger)
└── README.md
```

---

## Requirements

```
pip install fastapi bcrypt mysql-connector-python
```

A running MySQL server (tested against MySQL 8.0) with a `medicOpenX` database.

---

## Setup

1. **Configure DB credentials** in `dbase_creds.py` (`host`, `user`, `password`, `database`).
2. **Verify the connection**:
   ```
   python db_connection_test.py
   ```
3. **Generate the `medicUsr` table** (drops and recreates it):
   ```
   python dbase_table_generator.py
   ```
4. **Run the app**:
   ```
   python main.py
   ```

---

## Known Issues / To Do

- `dob` is stored as free-text `VARCHAR`, not a real `DATE` type — the app currently collects it as `DD/MM/YYYY`, which isn't valid MySQL date format as-is.
- Login (option 1) doesn't check credentials yet — it goes straight to the patient menu.
- `dbase_creds.py` currently stores the DB password in plain text. Fine for local dev, but this needs to move to a `.env` file (git-ignored) before the repo goes public.
- FastAPI app instance is created in `main.py` but unused — need to decide whether this stays CLI-only or grows a web API alongside it.
- Prescription request, notifications, and tracking (patient menu options 1–3) are print-statement placeholders with no real logic yet.

---

## Tech Stack

- **Python 3**
- **MySQL** (via 'mysql-connector-python')
- **bcrypt** for password hashing
- **FastAPI** (planned)
