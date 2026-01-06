# Frontend Deployment Fix

## The Problem

The error `cd: frontend: No such file or directory` occurs when:
- The root directory is set to `frontend` in your deployment platform
- But the build command tries to `cd frontend` again
- Since you're already in `frontend`, there's no `frontend` subdirectory

## ✅ Solution

### For Vercel

**Option 1: Set Root Directory to `frontend` (Recommended)**

1. Go to Vercel Dashboard → Your Project → Settings
2. Go to **General** tab
3. Set **Root Directory** to: `frontend`
4. The `vercel.json` has been updated to work with this setting
5. Build command will be: `npm install && npm run build`
6. Output directory will be: `build`

**Option 2: Keep Root Directory Empty**

If you keep root directory empty, update `vercel.json` build command to:
```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/build"
}
```

### For Netlify

**Set Root Directory to `frontend`**

1. Go to Netlify Dashboard → Your Site → Site settings
2. Go to **Build & deploy**
3. Set **Base directory** to: `frontend`
4. Set **Publish directory** to: `build`
5. The `netlify.toml` has been updated to work with this setting

### For Render (Static Site)

**Set Root Directory to `frontend`**

1. Go to Render Dashboard → Your Static Site → Settings
2. Under **Build & Deploy**
3. Set **Root Directory** to: `frontend`
4. Set **Build Command** to: `npm install && npm run build`
5. Set **Publish Directory** to: `build`

## Updated Configuration Files

### vercel.json
- ✅ Removed `cd frontend` from build command
- ✅ Changed output directory from `frontend/build` to `build`
- ✅ Assumes root directory is set to `frontend`

### netlify.toml
- ✅ Updated publish directory from `frontend/build` to `build`
- ✅ Added `npm install` to build command
- ✅ Assumes base directory is set to `frontend`

## Quick Fix Checklist

- [ ] Set **Root Directory** to `frontend` in your platform
- [ ] Verify **Build Command** is: `npm install && npm run build`
- [ ] Verify **Output/Publish Directory** is: `build`
- [ ] Add environment variable: `REACT_APP_API_URL` (your backend URL)
- [ ] Redeploy

## Environment Variables

Don't forget to set:
```
REACT_APP_API_URL=https://your-backend-url.railway.app
```
(or whatever your backend URL is)

## Verification

After deploying, check:
- ✅ Build completes without "No such file or directory" errors
- ✅ Build output shows "Creating an optimized production build..."
- ✅ Build succeeds with "Compiled successfully!"
- ✅ Site is accessible and API calls work

## Common Issues

### Issue: "Cannot find package.json"
**Solution:** Make sure root directory is set to `frontend`

### Issue: "Build output not found"
**Solution:** Make sure publish directory is set to `build` (not `frontend/build`)

### Issue: "API calls failing"
**Solution:** Verify `REACT_APP_API_URL` environment variable is set correctly

## Still Having Issues?

1. **Check build logs** - Look for the exact error message
2. **Verify file structure** - Make sure `frontend/package.json` exists
3. **Check root directory** - Must be exactly `frontend` (lowercase, no slashes)
4. **Try manual build** - Run `npm install && npm run build` locally in `frontend/` directory

