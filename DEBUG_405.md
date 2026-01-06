# Debugging 405 Error - Step by Step

## Quick Diagnostic Steps

### Step 1: Verify Backend is Deployed with Latest Code

1. **Check if backend has the updated code:**
   - Go to your backend platform (Railway/Render)
   - Check the latest deployment
   - Verify it includes the OPTIONS handler

2. **Force a new deployment:**
   - Make a small change (add a comment)
   - Commit and push
   - Or manually trigger redeploy

### Step 2: Test Backend Directly

**Test 1: Health Check**
```bash
curl https://your-backend-url/api/health
```
Expected: `{"status":"healthy"}`

**Test 2: List Routes**
```bash
curl https://your-backend-url/api/routes
```
Expected: Should show `/api/enhance-resume` with methods `['POST', 'OPTIONS', 'HEAD']`

**Test 3: Test OPTIONS (Preflight)**
```bash
curl -X OPTIONS https://your-backend-url/api/enhance-resume \
     -H "Origin: https://buildcustomresume.com" \
     -H "Access-Control-Request-Method: POST" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -v
```
Expected: 200 OK with CORS headers

**Test 4: Test POST**
```bash
curl -X POST https://your-backend-url/api/enhance-resume \
     -H "Content-Type: multipart/form-data" \
     -F "resume=@test.pdf" \
     -F "job_posting=test" \
     -F "output_format=pdf" \
     -v
```
Expected: Should NOT return 405

### Step 3: Check Browser Network Tab

1. Open browser DevTools (F12)
2. Go to Network tab
3. Try to enhance resume
4. Look for TWO requests:
   - **First:** OPTIONS request to `/api/enhance-resume`
     - Status should be 200
     - Check Response Headers for CORS headers
   - **Second:** POST request to `/api/enhance-resume`
     - Status should be 200 (not 405)

### Step 4: Check API URL

In browser console, check:
```javascript
console.log('API URL:', process.env.REACT_APP_API_URL);
```

Verify:
- URL is correct
- No trailing slash
- Includes `/api/enhance-resume` (not just `/enhance-resume`)

### Step 5: Check CORS Configuration

**Backend Environment Variable:**
```
ALLOWED_ORIGINS=https://buildcustomresume.com,https://www.buildcustomresume.com
```

**Verify in backend logs:**
- Check if CORS is being applied
- Look for any CORS-related errors

## Common Causes & Fixes

### Cause 1: Backend Not Redeployed
**Fix:** Redeploy backend with latest code

### Cause 2: Wrong URL
**Symptom:** Request going to wrong endpoint
**Fix:** Verify `REACT_APP_API_URL` is set correctly

### Cause 3: CORS Preflight Failing
**Symptom:** OPTIONS request returns 405
**Fix:** 
- Check CORS configuration
- Verify `ALLOWED_ORIGINS` includes your domain
- Check backend logs

### Cause 4: Route Not Registered
**Symptom:** Route doesn't appear in `/api/routes`
**Fix:** 
- Check backend logs for import errors
- Verify `app.py` is being loaded correctly

### Cause 5: Proxy/Load Balancer
**Symptom:** Works with curl but not from browser
**Fix:** 
- Check if platform has proxy settings
- May need to configure platform-specific CORS

## Platform-Specific Checks

### Railway
1. Check deployment logs
2. Verify environment variables are set
3. Check service is running
4. Test direct API call

### Render
1. Check build logs
2. Verify start command
3. Check service logs
4. Verify environment variables

## Quick Fix: Test with curl

If curl works but browser doesn't:
- Issue is likely CORS
- Check CORS configuration
- Verify frontend domain is in ALLOWED_ORIGINS

If curl also returns 405:
- Issue is with backend route
- Check route registration
- Check backend logs
- Verify deployment

## Still Not Working?

Share:
1. **Backend logs** - Latest deployment logs
2. **Network tab screenshot** - Show the failed request
3. **Routes endpoint result** - Output of `/api/routes`
4. **Curl test results** - Results of OPTIONS and POST tests

