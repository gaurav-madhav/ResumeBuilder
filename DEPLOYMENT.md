# Deployment Guide for buildcustomresume.com

This guide will help you deploy your Resume Builder application to your domain `buildcustomresume.com`.

## Deployment Options

You have several options for hosting. Here are the recommended approaches:

### Option 1: Railway (Recommended - Easiest)
- **Pros**: Easy setup, automatic SSL, good free tier
- **Cons**: Limited free tier
- **Cost**: Free tier available, then ~$5/month

### Option 2: Render
- **Pros**: Free tier, easy setup, automatic SSL
- **Cons**: Free tier spins down after inactivity
- **Cost**: Free tier available, then ~$7/month

### Option 3: DigitalOcean App Platform
- **Pros**: Good performance, reasonable pricing
- **Cons**: More configuration needed
- **Cost**: ~$5-12/month

### Option 4: AWS/DigitalOcean VPS
- **Pros**: Full control, scalable
- **Cons**: More complex setup, need to manage SSL
- **Cost**: ~$5-20/month

---

## Recommended: Railway Deployment (Full Stack)

### Step 1: Deploy Backend to Railway

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your repository

3. **Configure Backend Service**
   - Railway will auto-detect Python
   - Set root directory to `backend` (NO leading slash)
   - Add environment variables:
     ```
     FLASK_ENV=production
     ALLOWED_ORIGINS=https://buildcustomresume.com,https://www.buildcustomresume.com
     PORT=5000
     ```

4. **Deploy**
   - Railway will automatically deploy
   - Note the generated domain (e.g., `your-app.railway.app`)

### Step 2: Deploy Frontend to Vercel/Netlify

1. **Build Frontend**
   ```bash
   cd frontend
   npm install
   REACT_APP_API_URL=https://your-backend-url.railway.app npm run build
   ```

2. **Deploy to Vercel**
   - Go to https://vercel.com
   - Sign up with GitHub
   - Import your repository
   - Set root directory to `frontend` (NO leading slash)
   - Add environment variable:
     ```
     REACT_APP_API_URL=https://your-backend-url.railway.app
     ```
   - Deploy

3. **Deploy to Netlify** (Alternative)
   - Go to https://netlify.com
   - Sign up with GitHub
   - Import your repository
   - Build settings:
     - Base directory: `frontend`
     - Build command: `npm install && npm run build`
     - Publish directory: `build`
   - Add environment variable:
     ```
     REACT_APP_API_URL=https://your-backend-url.railway.app
     ```

### Step 3: Configure DNS in Namecheap

1. **Log into Namecheap**
   - Go to https://www.namecheap.com
   - Log in and go to Domain List

2. **Access DNS Settings**
   - Click "Manage" next to `buildcustomresume.com`
   - Go to "Advanced DNS" tab

3. **Configure DNS Records**

   **For Frontend (Vercel/Netlify):**
   - Add A Record:
     - Type: A
     - Host: @
     - Value: [Vercel/Netlify IP - they'll provide this]
     - TTL: Automatic
   
   - Add CNAME Record:
     - Type: CNAME
     - Host: www
     - Value: [Vercel/Netlify domain]
     - TTL: Automatic

   **For Backend (Railway):**
   - Add CNAME Record:
     - Type: CNAME
     - Host: api
     - Value: [Railway domain, e.g., your-app.railway.app]
     - TTL: Automatic

   **Example DNS Records:**
   ```
   Type    Host    Value                          TTL
   A       @       76.76.21.21                   Auto
   CNAME   www     cname.vercel-dns.com          Auto
   CNAME   api     your-app.railway.app          Auto
   ```

4. **Wait for DNS Propagation**
   - Can take 24-48 hours, usually much faster
   - Check with: https://dnschecker.org

### Step 4: Configure Custom Domain in Vercel/Netlify

1. **In Vercel:**
   - Go to your project settings
   - Click "Domains"
   - Add `buildcustomresume.com` and `www.buildcustomresume.com`
   - Follow verification steps

2. **In Netlify:**
   - Go to Site settings
   - Click "Domain management"
   - Add custom domain `buildcustomresume.com`
   - Follow verification steps

### Step 5: Update Backend CORS

Update the `ALLOWED_ORIGINS` environment variable in Railway:
```
ALLOWED_ORIGINS=https://buildcustomresume.com,https://www.buildcustomresume.com
```

---

## Alternative: Render Deployment (Full Stack)

### Step 1: Deploy Backend to Render

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - Name: `resume-builder-backend`
     - Environment: Python 3
     - Build Command: `cd backend && pip install -r requirements.txt`
     - Start Command: `cd backend && gunicorn --config gunicorn_config.py wsgi:app`
     - Root Directory: `backend`

3. **Add Environment Variables**
   ```
   FLASK_ENV=production
   ALLOWED_ORIGINS=https://buildcustomresume.com,https://www.buildcustomresume.com
   ```

4. **Deploy**
   - Render will provide a URL like `your-app.onrender.com`

### Step 2: Deploy Frontend to Render

1. **Create Static Site**
   - Click "New +" → "Static Site"
   - Connect your GitHub repository
   - Configure:
     - Name: `resume-builder-frontend`
     - Build Command: `cd frontend && npm install && REACT_APP_API_URL=https://your-backend.onrender.com npm run build`
     - Publish Directory: `frontend/build`
     - Root Directory: `frontend`

2. **Add Environment Variable**
   ```
   REACT_APP_API_URL=https://your-backend.onrender.com
   ```

3. **Add Custom Domain**
   - In Static Site settings, go to "Custom Domains"
   - Add `buildcustomresume.com` and `www.buildcustomresume.com`
   - Render will provide DNS instructions

### Step 3: Configure DNS

Follow Render's DNS instructions, which typically include:
- CNAME records pointing to Render's servers
- A records if needed

---

## Alternative: DigitalOcean App Platform

### Step 1: Create App

1. Go to https://cloud.digitalocean.com
2. Create App → GitHub
3. Select your repository

### Step 2: Configure Backend Component

- Component Type: Web Service
- Source Directory: `backend` (NO leading slash)
- Build Command: `pip install -r requirements.txt`
- Run Command: `gunicorn --config gunicorn_config.py wsgi:app`
- Environment Variables:
  ```
  FLASK_ENV=production
  ALLOWED_ORIGINS=https://buildcustomresume.com,https://www.buildcustomresume.com
  ```

### Step 3: Configure Frontend Component

- Component Type: Static Site
- Source Directory: `frontend` (NO leading slash)
- Build Command: `npm install && REACT_APP_API_URL=$API_URL npm run build`
- Output Directory: `build`
- Environment Variables:
  ```
  REACT_APP_API_URL=https://your-backend-app.ondigitalocean.app
  ```

### Step 4: Add Custom Domain

- In App settings, go to "Domains"
- Add `buildcustomresume.com`
- Follow DNS configuration instructions

---

## Testing Your Deployment

1. **Test Backend API**
   ```bash
   curl https://api.buildcustomresume.com/api/health
   ```
   Should return: `{"status":"healthy"}`

2. **Test Frontend**
   - Visit https://buildcustomresume.com
   - Try uploading a resume and enhancing it

3. **Check CORS**
   - Open browser console
   - Should not see CORS errors

---

## SSL/HTTPS

All recommended platforms (Railway, Render, Vercel, Netlify, DigitalOcean) provide automatic SSL certificates via Let's Encrypt. No additional configuration needed!

---

## Troubleshooting

### DNS Not Working
- Wait 24-48 hours for full propagation
- Check DNS with: https://dnschecker.org
- Verify records in Namecheap match platform requirements

### CORS Errors
- Verify `ALLOWED_ORIGINS` includes your domain
- Check that frontend is using correct API URL
- Ensure no trailing slashes in URLs

### Backend Not Starting
- Check logs in your hosting platform
- Verify all environment variables are set
- Ensure `gunicorn` is in requirements.txt

### Frontend Build Fails
- Verify `REACT_APP_API_URL` is set
- Check that build command includes environment variable
- Review build logs for errors

---

## Post-Deployment Checklist

- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] DNS configured correctly
- [ ] Custom domain working
- [ ] SSL certificate active (HTTPS)
- [ ] CORS configured correctly
- [ ] Test file upload works
- [ ] Test resume enhancement works
- [ ] Test download works
- [ ] Monitor error logs

---

## Support

If you encounter issues:
1. Check platform-specific documentation
2. Review application logs
3. Verify all environment variables
4. Test API endpoints directly

Good luck with your deployment! 🚀

