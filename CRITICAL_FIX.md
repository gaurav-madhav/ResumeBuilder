# CRITICAL FIX: ModuleNotFoundError: No module named 'main'

## The Problem

Your deployment platform is trying to import a module called `main` which doesn't exist. This happens when:
1. The platform auto-detects Python and looks for `main.py`
2. The start command isn't being used correctly
3. There's a mismatch between root directory and start command

## ✅ IMMEDIATE FIX

### Step 1: Update Start Command in Your Platform

Go to your deployment platform (Railway/Render/etc.) and update the **Start Command** to:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

**This directly imports the Flask app from `app.py`, bypassing any auto-detection issues.**

### Step 2: Verify Root Directory

Make sure your **Root Directory** is set to: `backend`

### Step 3: Redeploy

After updating the start command, redeploy your application.

---

## Alternative Commands (If Above Doesn't Work)

### Option 1: Use main.py (I've created this file)
```bash
gunicorn main:app --bind 0.0.0.0:$PORT --workers 2
```

### Option 2: Use wsgi.py
```bash
gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2
```

### Option 3: Use start script
```bash
bash backend/start.sh
```

---

## Platform-Specific Instructions

### Railway

1. Go to Railway Dashboard
2. Select your service
3. Go to **Settings** tab
4. Scroll to **Deploy** section
5. Find **Start Command**
6. Set to: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
7. Verify **Root Directory** is set to: `backend`
8. Click **Save**
9. Go to **Deployments** tab and trigger a new deployment

### Render

1. Go to Render Dashboard
2. Select your web service
3. Go to **Settings** tab
4. Scroll to **Build & Deploy**
5. Find **Start Command**
6. Set to: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
7. Verify **Root Directory** is set to: `backend`
8. Click **Save Changes**
9. Manually deploy or wait for auto-deploy

### Heroku

Update your `Procfile`:
```
web: gunicorn app:app --bind 0.0.0.0:$PORT --workers 2
```

Then commit and push:
```bash
git add Procfile
git commit -m "Fix start command"
git push heroku main
```

---

## Why This Works

- `app:app` directly references the Flask app instance from `app.py`
- No intermediate imports that could fail
- Works regardless of auto-detection
- Simple and reliable

---

## Files Created/Updated

1. ✅ Created `backend/main.py` - Fallback entry point
2. ✅ Created `backend/start.sh` - Startup script
3. ✅ Updated `railway.json` - Start command
4. ✅ Updated `render.yaml` - Start command

---

## Verification

After deploying, check the logs. You should see:
- ✅ Gunicorn starting successfully
- ✅ "Listening at: http://0.0.0.0:5000"
- ✅ No "ModuleNotFoundError" errors
- ✅ Workers booting successfully

---

## Still Not Working?

If you're still getting errors:

1. **Check the exact error message** - It might give more clues
2. **Verify file structure** - Make sure `backend/app.py` exists
3. **Check root directory** - Must be exactly `backend` (lowercase, no slashes)
4. **Try the alternative commands** - Use `main:app` or `wsgi:app`
5. **Check build logs** - See if dependencies are installing correctly

---

## Quick Test Locally

To test if the command works locally:

```bash
cd backend
gunicorn app:app --bind 0.0.0.0:5000 --workers 2
```

If this works locally, it will work in production!

