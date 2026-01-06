# Quick Fix for 405 Error

## Most Likely Causes

### 1. Backend Not Redeployed
**Fix:** Redeploy your backend with the updated code

### 2. CORS Configuration Issue
**Fix:** The code has been updated with better CORS handling. Redeploy.

### 3. Wrong API URL
**Check:** In browser console, verify the API URL being used

## Immediate Steps

### Step 1: Test Backend Routes
```bash
curl https://your-backend-url/api/routes
```

This will show all registered routes. Look for `/api/enhance-resume` with methods including `POST` and `OPTIONS`.

### Step 2: Test OPTIONS Request
```bash
curl -X OPTIONS https://your-backend-url/api/enhance-resume -v
```

Should return 200 OK.

### Step 3: Check Browser Network Tab

1. Open DevTools (F12) → Network tab
2. Try to enhance resume
3. Look for:
   - OPTIONS request (should be 200)
   - POST request (should NOT be 405)

### Step 4: Verify Environment Variables

**Backend:**
- `ALLOWED_ORIGINS` should include your frontend domain

**Frontend:**
- `REACT_APP_API_URL` should be your backend URL (no trailing slash)

## What Changed

1. ✅ Improved CORS configuration
2. ✅ Added explicit OPTIONS handling
3. ✅ Added route for trailing slash
4. ✅ Added test endpoint at `/api/test`
5. ✅ Better error handling

## Next Steps

1. **Redeploy backend** with the updated code
2. **Test the routes endpoint** to verify routes are registered
3. **Check browser console** for the exact error
4. **Test with curl** to isolate if it's a CORS issue

## If Still Getting 405

Share:
- Output of `curl https://your-backend-url/api/routes`
- Screenshot of Network tab showing the failed request
- Backend deployment logs

The updated code should fix the 405 error. Make sure to redeploy!

