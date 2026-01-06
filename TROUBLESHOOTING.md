# Troubleshooting Production Issues

## Error: "An error occurred while processing your resume"

This generic error can have several causes. Follow these steps to diagnose and fix:

### Step 1: Check Browser Console

1. Open your website in a browser
2. Press `F12` or right-click → "Inspect" → "Console" tab
3. Try to enhance a resume again
4. Look for error messages in red
5. Check for:
   - CORS errors
   - Network errors
   - 404 errors (API not found)
   - 500 errors (server error)

### Step 2: Verify API URL Configuration

**Check Frontend Environment Variable:**

1. In Vercel/Netlify dashboard:
   - Go to your project → Settings → Environment Variables
   - Verify `REACT_APP_API_URL` is set
   - Value should be your backend URL (e.g., `https://your-backend.railway.app`)
   - **Important:** No trailing slash!

2. **Rebuild frontend** after setting environment variable:
   - Environment variables are only available at build time
   - You must redeploy after adding/changing them

### Step 3: Test Backend API Directly

Test if your backend is accessible:

```bash
# Test health endpoint
curl https://your-backend-url.railway.app/api/health

# Should return: {"status":"healthy"}
```

If this fails:
- Backend is not accessible
- Check backend deployment status
- Check backend logs for errors

### Step 4: Check CORS Configuration

**Verify Backend CORS Settings:**

1. Check your backend environment variables:
   - `ALLOWED_ORIGINS` should include your frontend domain
   - Example: `https://buildcustomresume.com,https://www.buildcustomresume.com`

2. Test CORS:
   - Open browser console
   - Look for CORS errors like:
     ```
     Access to XMLHttpRequest at '...' from origin '...' has been blocked by CORS policy
     ```

3. **Fix CORS:**
   - Update `ALLOWED_ORIGINS` in backend to include your frontend domain
   - Redeploy backend

### Step 5: Check Backend Logs

**Railway:**
1. Go to Railway Dashboard → Your Service
2. Click "Deployments" tab
3. Click on latest deployment → "View Logs"
4. Look for error messages

**Render:**
1. Go to Render Dashboard → Your Service
2. Click "Logs" tab
3. Look for error messages

**Common Backend Errors:**
- `ModuleNotFoundError` - Missing Python dependencies
- `FileNotFoundError` - Missing files or directories
- `PermissionError` - File permission issues
- `ImportError` - Import issues

### Step 6: Verify File Upload

**Check:**
1. File size limits (should be under 10MB)
2. File format (PDF, DOC, DOCX only)
3. Backend has write permissions for uploads directory

### Step 7: Common Issues & Solutions

#### Issue: "Network Error" or "ERR_NETWORK"
**Cause:** Frontend can't reach backend
**Solution:**
- Verify `REACT_APP_API_URL` is set correctly
- Check backend is running and accessible
- Test backend URL directly in browser

#### Issue: CORS Error
**Cause:** Backend not allowing frontend origin
**Solution:**
- Update `ALLOWED_ORIGINS` in backend environment variables
- Include your frontend domain (with https://)
- Redeploy backend

#### Issue: 404 Not Found
**Cause:** API endpoint not found
**Solution:**
- Verify backend is running
- Check API URL is correct
- Ensure route `/api/enhance-resume` exists

#### Issue: 500 Internal Server Error
**Cause:** Backend processing error
**Solution:**
- Check backend logs for specific error
- Verify all dependencies are installed
- Check file permissions
- Verify uploads directory exists

#### Issue: "Cannot read property 'error' of undefined"
**Cause:** Error response format issue
**Solution:**
- Check backend error handling
- Verify error responses are JSON

### Step 8: Enable Detailed Error Messages

The frontend code has been updated to show more detailed error messages. After redeploying, you should see:
- Network errors with specific messages
- Server errors with status codes
- Connection errors with helpful messages

### Step 9: Test Locally

Test the connection locally:

1. **Start backend locally:**
   ```bash
   cd backend
   source venv/bin/activate
   python app.py
   ```

2. **Update frontend to use local backend:**
   - Temporarily set `REACT_APP_API_URL=http://localhost:5000`
   - Rebuild and test

3. **If local works but production doesn't:**
   - Issue is with production configuration
   - Check environment variables
   - Check CORS settings
   - Check network/firewall settings

### Step 10: Quick Checklist

- [ ] `REACT_APP_API_URL` is set in frontend environment variables
- [ ] Frontend was rebuilt after setting environment variable
- [ ] Backend is running and accessible
- [ ] `ALLOWED_ORIGINS` includes frontend domain
- [ ] Backend logs show no errors
- [ ] Browser console shows specific error (not generic)
- [ ] CORS is configured correctly
- [ ] File uploads are working
- [ ] Backend dependencies are installed

### Getting More Information

**Enable Debug Mode:**

1. Open browser console
2. The updated code now logs:
   - Error details
   - API URL being used
   - Response status
   - Network errors

**Check Network Tab:**

1. Open browser DevTools → Network tab
2. Try to enhance resume
3. Look for the API request
4. Check:
   - Request URL (is it correct?)
   - Request status (200, 404, 500, etc.)
   - Response body (what error message?)

### Still Not Working?

If you've tried all the above:

1. **Share the exact error from browser console**
2. **Share backend logs**
3. **Share your environment variable settings** (without sensitive data)
4. **Test backend health endpoint** and share result

The frontend code has been updated to provide better error messages. Redeploy the frontend to see more detailed errors!

