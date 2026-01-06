# Step-by-Step Debugging for 405 Error

## Step 1: Verify Backend is Running Latest Code

**Check if you've redeployed:**
1. Go to your backend platform (Railway/Render)
2. Check the latest deployment timestamp
3. Verify it's after the code changes
4. If not, **redeploy now**

## Step 2: Test Backend Routes Endpoint

Run this command:
```bash
curl https://your-backend-url/api/routes
```

**Expected Output:**
You should see `/api/enhance-resume` in the routes list with methods including `POST` and `OPTIONS`.

**If you don't see it:**
- Backend code isn't deployed
- There's an import error
- Check backend logs

## Step 3: Test OPTIONS Request Directly

```bash
curl -X OPTIONS https://your-backend-url/api/enhance-resume \
     -H "Origin: https://buildcustomresume.com" \
     -H "Access-Control-Request-Method: POST" \
     -v
```

**Expected:** 200 OK with CORS headers

**If you get 405:**
- Route isn't registered
- Check backend logs for errors

## Step 4: Test POST Request Directly

```bash
curl -X POST https://your-backend-url/api/enhance-resume \
     -F "resume=@test.pdf" \
     -F "job_posting=test" \
     -F "output_format=pdf" \
     -v
```

**Expected:** Either:
- 400 (missing file - but NOT 405)
- 200 (success)
- 500 (processing error - but NOT 405)

**If you get 405:**
- Route definitely not accepting POST
- Check route registration

## Step 5: Check Browser Network Tab

1. Open your website
2. Press F12 → Network tab
3. Clear network log
4. Try to enhance resume
5. Look for the request to `/api/enhance-resume`

**Check:**
- **Request URL:** Should be `https://your-backend-url/api/enhance-resume`
- **Request Method:** Should be `POST`
- **Status Code:** Currently showing 405
- **Request Headers:** Check `Origin` header

**Look for TWO requests:**
1. OPTIONS (preflight) - Should be 200
2. POST - Currently 405

## Step 6: Check Backend Logs

Go to your backend platform and check logs:

**Look for:**
- "Request received: POST /api/enhance-resume"
- "405 Error: Method POST not allowed"
- Any import errors
- Any route registration errors

## Step 7: Verify API URL in Frontend

In browser console, run:
```javascript
console.log('API URL:', process.env.REACT_APP_API_URL);
```

**Check:**
- Is it set?
- Is it correct?
- No trailing slash?
- Includes `/api/enhance-resume` in the full URL?

## Step 8: Test Alternative Endpoint

Try the test endpoint:
```bash
curl -X POST https://your-backend-url/api/test
```

**Expected:** `{"status": "ok", "method": "POST", ...}`

**If this works but `/api/enhance-resume` doesn't:**
- Issue is specific to that route
- Check route registration

## Common Issues & Solutions

### Issue 1: Backend Not Redeployed
**Solution:** Redeploy backend

### Issue 2: Wrong URL
**Symptom:** Request going to wrong endpoint
**Solution:** Check `REACT_APP_API_URL` environment variable

### Issue 3: Route Not Registered
**Symptom:** Route doesn't appear in `/api/routes`
**Solution:** 
- Check backend logs for import errors
- Verify `app.py` is being loaded
- Check if there are syntax errors

### Issue 4: Platform-Specific Routing
**Symptom:** Works locally but not in production
**Solution:**
- Check platform routing rules
- Some platforms require specific route formats
- Check if there's a reverse proxy

### Issue 5: CORS Blocking
**Symptom:** OPTIONS works, POST gets 405
**Solution:**
- Check CORS configuration
- Verify `ALLOWED_ORIGINS` includes your domain

## What to Share for Help

If still getting 405, share:

1. **Output of `/api/routes` endpoint**
2. **Result of OPTIONS curl test**
3. **Result of POST curl test**
4. **Screenshot of Network tab** (showing the failed request)
5. **Backend logs** (last 50 lines)
6. **Frontend console output** (API URL being used)

## Quick Fix Attempt

If nothing else works, try this temporary fix:

**Backend environment variable:**
```
ALLOWED_ORIGINS=*
```

**Then in backend/app.py, change:**
```python
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

This allows all origins temporarily to rule out CORS issues.

## The Updated Code

The backend has been completely rewritten with:
- ✅ Better error handling
- ✅ Detailed logging
- ✅ 405 error handler with debugging info
- ✅ Test endpoints
- ✅ Improved CORS configuration

**Make sure to redeploy!**

