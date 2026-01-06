# Fix: ModuleNotFoundError: No module named 'main'

This error occurs when the deployment platform tries to import a module that doesn't exist. Here are the solutions:

## Solution 1: Update Start Command (Recommended)

The issue is likely with how gunicorn is being called. Use one of these commands depending on your root directory setting:

### If Root Directory is NOT set (running from repo root):
```bash
gunicorn --config backend/gunicorn_config.py backend.wsgi:app
```

### If Root Directory IS set to `backend`:
```bash
gunicorn --config gunicorn_config.py wsgi:app
```

## Solution 2: Platform-Specific Fixes

### Railway

**Option A: Set Root Directory to `backend`**
1. Go to Railway Dashboard → Your Service → Settings
2. Set Root Directory to: `backend`
3. Update Start Command to:
   ```
   gunicorn --config gunicorn_config.py wsgi:app
   ```

**Option B: Keep Root Directory Empty**
1. Keep Root Directory empty (default)
2. Update Start Command to:
   ```
   gunicorn --config backend/gunicorn_config.py backend.wsgi:app
   ```

### Render

**Option A: Set Root Directory to `backend`**
1. Go to Render Dashboard → Your Service → Settings
2. Set Root Directory to: `backend`
3. Update Start Command to:
   ```
   gunicorn --config gunicorn_config.py wsgi:app
   ```

**Option B: Keep Root Directory Empty**
1. Keep Root Directory empty
2. Update Start Command to:
   ```
   gunicorn --config backend/gunicorn_config.py backend.wsgi:app
   ```

### Heroku

The Procfile has been updated. If using Heroku, make sure your Procfile contains:
```
web: gunicorn --config backend/gunicorn_config.py backend.wsgi:app
```

## Solution 3: Alternative - Use app.py Directly

If the above doesn't work, you can run gunicorn directly on app.py:

### If Root Directory is `backend`:
```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

### If Root Directory is empty:
```bash
gunicorn backend.app:app --bind 0.0.0.0:$PORT
```

## Solution 4: Create a Simple Start Script

Create `backend/start.sh`:
```bash
#!/bin/bash
cd "$(dirname "$0")"
gunicorn --config gunicorn_config.py wsgi:app
```

Then use as start command:
```bash
bash backend/start.sh
```

## Verification

After updating, check the logs. You should see:
- ✅ Gunicorn starting successfully
- ✅ No "ModuleNotFoundError" errors
- ✅ Application binding to port

## Common Causes

1. **Wrong root directory**: If root directory is set incorrectly, Python can't find modules
2. **Wrong import path**: Using `wsgi:app` when should use `backend.wsgi:app` (or vice versa)
3. **Missing __init__.py**: The `backend/__init__.py` file has been added to make it a package
4. **Auto-detection**: Some platforms auto-detect and look for `main.py` - we don't have one, so we need to specify the command

## Quick Fix Checklist

- [ ] Check what your root directory is set to
- [ ] Update start command to match root directory setting
- [ ] Verify `backend/wsgi.py` exists and imports correctly
- [ ] Verify `backend/app.py` exists
- [ ] Check that `backend/__init__.py` exists (just created)
- [ ] Redeploy and check logs

## Still Not Working?

If you're still getting the error:

1. **Check the exact error message** - it might give clues about which module it's looking for
2. **Check build logs** - see what files are being found
3. **Try the alternative command** - use `gunicorn app:app` directly
4. **Verify file structure** - make sure all files are in the right place

The most common fix is ensuring the start command matches your root directory setting!

