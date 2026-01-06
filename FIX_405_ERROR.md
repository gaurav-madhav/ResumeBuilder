# Fix: Server Error (405) - Method Not Allowed

## The Problem

A 405 error means the server received the request but the HTTP method (POST) is not allowed for that endpoint. This can happen due to:

1. **CORS preflight failure** - OPTIONS request failing
2. **Route configuration issue** - Method not properly registered
3. **Proxy/load balancer** - Blocking POST requests
4. **URL mismatch** - Wrong endpoint being called

## ✅ Solutions

### Solution 1: CORS Preflight (Most Common)

The backend has been updated to explicitly handle OPTIONS requests. Make sure:

1. **Backend is redeployed** with the updated code
2. **CORS is properly configured** - Check `ALLOWED_ORIGINS` environment variable

### Solution 2: Verify the API URL

Check that the frontend is calling the correct URL:

1. **Open browser console** (F12)
2. **Look for the API URL** - Should show: `API URL: https://your-backend-url`
3. **Check the full request URL** in Network tab
4. **Verify it's:** `https://your-backend-url/api/enhance-resume`
   - Not: `https://your-backend-url/enhance-resume` (missing /api/)
   - Not: `https://your-backend-url/api/enhance-resume/` (trailing slash)

### Solution 3: Check Backend Route

Verify the backend route is registered:

1. **Test health endpoint:**
   ```bash
   curl https://your-backend-url/api/health
   ```
   Should return: `{"status":"healthy"}`

2. **Test enhance-resume with OPTIONS (preflight):**
   ```bash
   curl -X OPTIONS https://your-backend-url/api/enhance-resume \
        -H "Origin: https://buildcustomresume.com" \
        -H "Access-Control-Request-Method: POST" \
        -v
   ```
   Should return 200 OK

3. **Test enhance-resume with POST:**
   ```bash
   curl -X POST https://your-backend-url/api/enhance-resume \
        -F "resume=@test.pdf" \
        -F "job_posting=test" \
        -F "output_format=pdf" \
        -v
   ```
   Should not return 405

### Solution 4: Check Platform-Specific Issues

#### Railway

Railway should work fine, but check:
1. **No reverse proxy blocking POST** - Railway doesn't add one by default
2. **Environment variables set correctly**
3. **Backend logs** - Check for any routing errors

#### Render

Render might have issues with:
1. **Custom domains** - May need additional CORS configuration
2. **Health checks** - Make sure they're not interfering

### Solution 5: Debug Steps

1. **Check Network Tab:**
   - Open DevTools → Network
   - Try the request
   - Look for:
     - First request: OPTIONS (preflight) - Should be 200
     - Second request: POST - Should be 200 (not 405)

2. **Check Request Headers:**
   - Verify `Content-Type: multipart/form-data`
   - Verify `Origin` header matches your frontend domain

3. **Check Response Headers:**
   - Look for CORS headers in OPTIONS response
   - Should include: `Access-Control-Allow-Methods: POST, OPTIONS`

### Solution 6: Temporary Workaround

If CORS is the issue, temporarily allow all origins (for testing only):

**Backend environment variable:**
```
ALLOWED_ORIGINS=*
```

**Then update backend/app.py:**
```python
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

**⚠️ Warning:** Only for testing! Remove after fixing.

## Updated Code

The backend has been updated to:
1. ✅ Explicitly handle OPTIONS requests
2. ✅ Configure CORS with proper methods
3. ✅ Allow Content-Type header
4. ✅ Support credentials

## Verification Checklist

- [ ] Backend redeployed with updated code
- [ ] OPTIONS request returns 200 (check Network tab)
- [ ] POST request doesn't return 405
- [ ] API URL is correct (no trailing slash, includes /api/)
- [ ] CORS headers are present in response
- [ ] `ALLOWED_ORIGINS` includes your frontend domain
- [ ] Browser console shows no CORS errors

## Still Getting 405?

If you're still getting 405 after the above:

1. **Check backend logs** - Look for routing errors
2. **Test with curl** - See if POST works directly
3. **Verify route registration** - Check if route is being registered
4. **Check for middleware** - Any middleware blocking POST?

The code has been updated to handle OPTIONS and configure CORS properly. Redeploy the backend and try again!

