# Root Directory Configuration Guide

This guide shows the exact root directory settings for each deployment platform.

## Project Structure

```
ResumeBuilder/          ← Repository Root
├── backend/            ← Backend Root Directory
│   ├── app.py
│   ├── wsgi.py
│   ├── requirements.txt
│   └── ...
└── frontend/           ← Frontend Root Directory
    ├── package.json
    ├── src/
    └── ...
```

---

## Platform-Specific Root Directory Settings

### 🚂 Railway (Backend)

**Root Directory:** `backend`

**How to Set:**
1. In Railway dashboard, go to your service
2. Click on "Settings"
3. Under "Source", find "Root Directory"
4. Set to: `backend`
5. Save

**Alternative (via railway.json):**
The `railway.json` file should work, but if it doesn't, set it manually in the dashboard.

---

### ⚡ Vercel (Frontend)

**Root Directory:** `frontend`

**How to Set:**
1. In Vercel dashboard, go to your project
2. Click "Settings"
3. Go to "General" → "Root Directory"
4. Set to: `frontend`
5. Save and redeploy

**Or via vercel.json:**
The `vercel.json` should handle this, but you can also set it in dashboard.

---

### 🌐 Netlify (Frontend)

**Root Directory:** `frontend`

**How to Set:**
1. In Netlify dashboard, go to your site
2. Click "Site settings"
3. Go to "Build & deploy" → "Edit settings"
4. Set:
   - **Base directory:** `frontend`
   - **Build command:** `npm run build`
   - **Publish directory:** `frontend/build`
5. Save

**Or via netlify.toml:**
The `netlify.toml` file should handle this automatically.

---

### 🎨 Render (Backend)

**Root Directory:** `backend` (or leave empty if using render.yaml)

**How to Set:**
1. In Render dashboard, go to your service
2. Click "Settings"
3. Under "Build & Deploy", find "Root Directory"
4. Set to: `backend`
5. Save

**Or via render.yaml:**
The `render.yaml` should work, but you may need to set root directory in dashboard if it's not working.

---

### 🐳 Render (Frontend - Static Site)

**Root Directory:** `frontend`

**How to Set:**
1. In Render dashboard, go to your static site
2. Click "Settings"
3. Under "Build & Deploy", find "Root Directory"
4. Set to: `frontend`
5. Set **Publish Directory:** `build`
6. Save

---

### ☁️ DigitalOcean App Platform

**Backend Service:**
- **Root Directory:** `backend`
- **Build Command:** `pip install -r requirements.txt`
- **Run Command:** `gunicorn --config gunicorn_config.py wsgi:app`

**Frontend Service:**
- **Root Directory:** `frontend`
- **Build Command:** `npm install && npm run build`
- **Output Directory:** `build`

---

### 🚀 Heroku (Backend)

**Root Directory:** Leave empty (root of repo)

**Note:** Heroku uses the `Procfile` at the root, which already has `cd backend && ...`

If you want to set root directory:
1. Create a `project.toml` file (or use Heroku CLI)
2. Or set `PROJECT_ROOT=backend` in config vars

---

## Common Issues & Solutions

### Issue: "Cannot find requirements.txt"
**Solution:** Set root directory to `backend`

### Issue: "Cannot find package.json"
**Solution:** Set root directory to `frontend`

### Issue: "Build command failed"
**Solution:** 
- Verify root directory is correct
- Check that build commands use relative paths from root directory
- Ensure all files exist in the specified root directory

### Issue: "Module not found"
**Solution:**
- For backend: Ensure root directory is `backend` and `requirements.txt` is there
- For frontend: Ensure root directory is `frontend` and `package.json` is there

---

## Quick Reference Table

| Platform | Service Type | Root Directory | Notes |
|----------|-------------|----------------|-------|
| Railway | Backend | `backend` | Set in Settings → Root Directory |
| Vercel | Frontend | `frontend` | Set in Settings → Root Directory |
| Netlify | Frontend | `frontend` | Set in Build settings → Base directory |
| Render | Backend | `backend` | Set in Settings → Root Directory |
| Render | Frontend | `frontend` | Set in Settings → Root Directory |
| DigitalOcean | Backend | `backend` | Set when creating component |
| DigitalOcean | Frontend | `frontend` | Set when creating component |
| Heroku | Backend | (empty) | Uses Procfile at root |

---

## Verification Steps

After setting root directory:

1. **Backend:**
   - Verify `requirements.txt` is found
   - Verify `app.py` or `wsgi.py` is found
   - Check build logs for successful dependency installation

2. **Frontend:**
   - Verify `package.json` is found
   - Verify `src/` directory is found
   - Check build logs for successful npm install and build

---

## Still Having Issues?

If deployment is still failing after setting root directory:

1. **Check Build Logs:**
   - Look for file path errors
   - Check if files are being found in the right location

2. **Verify File Structure:**
   - Ensure your repository structure matches the expected layout
   - Check that all necessary files exist

3. **Platform-Specific:**
   - Railway: Check Nixpacks detection
   - Vercel: Check build output logs
   - Render: Check build and deploy logs
   - Netlify: Check deploy logs

4. **Common Mistakes:**
   - Using `/backend` instead of `backend` (no leading slash)
   - Using `./backend` instead of `backend`
   - Case sensitivity: `Backend` vs `backend` (use lowercase)

---

## Example: Railway Configuration

If Railway is not detecting correctly:

1. Go to Railway dashboard
2. Select your service
3. Settings → Root Directory
4. Enter: `backend` (no slash, no dot)
5. Save
6. Redeploy

The build should now find:
- `backend/requirements.txt` ✓
- `backend/app.py` ✓
- `backend/wsgi.py` ✓

---

## Example: Vercel Configuration

If Vercel is not building correctly:

1. Go to Vercel dashboard
2. Select your project
3. Settings → General → Root Directory
4. Enter: `frontend` (no slash, no dot)
5. Save
6. Redeploy

The build should now find:
- `frontend/package.json` ✓
- `frontend/src/` ✓
- `frontend/public/` ✓

---

Need help? Check the deployment logs for specific error messages!

