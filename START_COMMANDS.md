# Start Commands for Different Configurations

Use the appropriate start command based on your root directory setting.

## If Root Directory is Set to `backend`

When root directory is `backend`, you're already in the backend folder, so use:

```bash
gunicorn --config gunicorn_config.py wsgi:app
```

Or simpler (without config file):
```bash
gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2
```

Or even simpler (direct app import):
```bash
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2
```

## If Root Directory is NOT Set (Empty/Default)

When root directory is empty, you're in the repo root, so use:

```bash
gunicorn --config backend/gunicorn_config.py backend.wsgi:app
```

Or simpler (without config file):
```bash
gunicorn backend.wsgi:app --bind 0.0.0.0:$PORT --workers 2
```

Or even simpler (direct app import):
```bash
gunicorn backend.app:app --bind 0.0.0.0:$PORT --workers 2
```

## Recommended: Simplest Command (Works Either Way)

The simplest command that should work regardless of root directory:

```bash
gunicorn backend.app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

This directly imports the app from `backend.app` module, which should work whether root directory is set or not.

## Platform-Specific Recommendations

### Railway
- **Root Directory:** `backend`
- **Start Command:** `gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2`

### Render
- **Root Directory:** `backend`
- **Start Command:** `gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2`

### Heroku
- **Root Directory:** (empty)
- **Procfile:** `web: gunicorn backend.app:app --bind 0.0.0.0:$PORT --workers 2`

## Testing Locally

To test which command works for you:

1. **If testing from repo root:**
   ```bash
   cd /Users/gauravmadhav/ResumeBuilder
   gunicorn backend.app:app --bind 0.0.0.0:5000
   ```

2. **If testing from backend directory:**
   ```bash
   cd /Users/gauravmadhav/ResumeBuilder/backend
   gunicorn app:app --bind 0.0.0.0:5000
   ```

Both should work!

