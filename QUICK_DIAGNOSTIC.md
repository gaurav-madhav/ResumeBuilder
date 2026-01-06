# Quick Diagnostic Guide

## Error: "An error occurred while processing your resume"

### Immediate Checks (5 minutes)

1. **Open Browser Console**
   - Press `F12` → Console tab
   - Try the action again
   - Look for red error messages
   - **Share the exact error message**

2. **Check API URL**
   - In browser console, you should see: `API URL: [your-backend-url]`
   - If it says "Not set", the environment variable is missing
   - **Fix:** Set `REACT_APP_API_URL` in Vercel/Netlify and rebuild

3. **Test Backend Health**
   - Open: `https://your-backend-url.railway.app/api/health`
   - Should show: `{"status":"healthy"}`
   - If it fails, backend is down

4. **Check Network Tab**
   - Press `F12` → Network tab
   - Try the action
   - Find the `/api/enhance-resume` request
   - Check:
     - Status code (200 = good, 404/500 = bad)
     - Response body (error message)

### Most Common Issues

#### 1. Missing REACT_APP_API_URL
**Symptom:** Console shows "API URL: Not set"
**Fix:**
- Vercel: Settings → Environment Variables → Add `REACT_APP_API_URL`
- Value: `https://your-backend-url.railway.app` (no trailing slash)
- **Important:** Rebuild frontend after adding

#### 2. CORS Error
**Symptom:** Console shows "CORS policy" error
**Fix:**
- Backend: Update `ALLOWED_ORIGINS` environment variable
- Include: `https://buildcustomresume.com,https://www.buildcustomresume.com`
- Redeploy backend

#### 3. Backend Not Running
**Symptom:** Network error or 502/503
**Fix:**
- Check backend deployment status
- Check backend logs for errors
- Restart backend service

#### 4. Network Error
**Symptom:** "Network Error" or "ERR_NETWORK"
**Fix:**
- Verify backend URL is correct
- Check backend is accessible
- Test backend health endpoint

### Quick Test Commands

```bash
# Test backend health
curl https://your-backend-url.railway.app/api/health

# Test from frontend domain (check CORS)
curl -H "Origin: https://buildcustomresume.com" \
     https://your-backend-url.railway.app/api/health
```

### What to Share for Help

1. **Browser Console Error** (exact message)
2. **Network Tab Details** (status code, response)
3. **Backend Logs** (from Railway/Render)
4. **Environment Variables** (names only, not values)
5. **Backend Health Check Result**

The frontend has been updated to show more detailed errors. Redeploy to see better error messages!

