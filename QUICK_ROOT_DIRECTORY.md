# Quick Root Directory Reference

## ⚠️ IMPORTANT: No Leading Slash!

Use: `backend` or `frontend`  
NOT: `/backend` or `/frontend`

---

## 🚂 Railway (Backend)

**Root Directory:** `backend`

**Where to Set:**
1. Railway Dashboard → Your Service → Settings
2. Find "Root Directory" field
3. Enter: `backend`
4. Save and redeploy

---

## ⚡ Vercel (Frontend)

**Root Directory:** `frontend`

**Where to Set:**
1. Vercel Dashboard → Your Project → Settings
2. Go to "General" tab
3. Find "Root Directory"
4. Enter: `frontend`
5. Save and redeploy

**Note:** The `vercel.json` file should work, but if not, set it manually in dashboard.

---

## 🌐 Netlify (Frontend)

**Base Directory:** `frontend`

**Where to Set:**
1. Netlify Dashboard → Your Site → Site settings
2. Go to "Build & deploy"
3. Click "Edit settings"
4. Set "Base directory" to: `frontend`
5. Set "Publish directory" to: `frontend/build`
6. Save

**Note:** The `netlify.toml` file should handle this automatically.

---

## 🎨 Render (Backend)

**Root Directory:** `backend`

**Where to Set:**
1. Render Dashboard → Your Service → Settings
2. Under "Build & Deploy"
3. Find "Root Directory"
4. Enter: `backend`
5. Save

---

## 🎨 Render (Frontend - Static Site)

**Root Directory:** `frontend`

**Where to Set:**
1. Render Dashboard → Your Static Site → Settings
2. Under "Build & Deploy"
3. Find "Root Directory"
4. Enter: `frontend`
5. Set "Publish Directory" to: `build`
6. Save

---

## ☁️ DigitalOcean App Platform

**Backend:**
- **Source Directory:** `backend`

**Frontend:**
- **Source Directory:** `frontend`
- **Output Directory:** `build`

**Where to Set:**
- Set when creating each component in the App Platform

---

## Common Mistakes to Avoid

❌ **Wrong:** `/backend` (leading slash)  
✅ **Correct:** `backend`

❌ **Wrong:** `./backend` (with dot-slash)  
✅ **Correct:** `backend`

❌ **Wrong:** `Backend` (wrong case)  
✅ **Correct:** `backend` (lowercase)

❌ **Wrong:** `backend/` (trailing slash)  
✅ **Correct:** `backend`

---

## How to Verify It's Working

### Backend Verification:
After setting root directory to `backend`, the build should find:
- ✅ `requirements.txt`
- ✅ `app.py`
- ✅ `wsgi.py`

### Frontend Verification:
After setting root directory to `frontend`, the build should find:
- ✅ `package.json`
- ✅ `src/` directory
- ✅ `public/` directory

---

## Still Failing?

1. **Check the build logs** - Look for file path errors
2. **Verify your repo structure** - Make sure `backend/` and `frontend/` folders exist
3. **Double-check spelling** - Must be exactly `backend` or `frontend` (lowercase, no slashes)
4. **Redeploy** - After changing root directory, always redeploy

---

## Quick Test

If you're unsure, try this:
1. Set root directory to `backend` (for backend) or `frontend` (for frontend)
2. Check build logs
3. If you see "Cannot find requirements.txt" or "Cannot find package.json", the root directory is wrong
4. If build starts successfully, you're good! ✅

