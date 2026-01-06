# Deployment Checklist for buildcustomresume.com

Use this checklist to ensure a smooth deployment process.

## Pre-Deployment

- [ ] Code is committed to GitHub repository
- [ ] All tests pass locally
- [ ] Environment variables documented
- [ ] Production configurations reviewed

## Step 1: Deploy Backend

### Railway (Recommended)
- [ ] Create Railway account
- [ ] Connect GitHub repository
- [ ] Create new project
- [ ] Set root directory to `/backend`
- [ ] Add environment variables:
  - [ ] `FLASK_ENV=production`
  - [ ] `ALLOWED_ORIGINS=https://buildcustomresume.com,https://www.buildcustomresume.com`
  - [ ] `PORT=5000`
- [ ] Deploy and note the URL (e.g., `your-app.railway.app`)
- [ ] Test backend: `curl https://your-app.railway.app/api/health`

### Render (Alternative)
- [ ] Create Render account
- [ ] Create Web Service
- [ ] Configure build and start commands
- [ ] Add environment variables
- [ ] Deploy and note the URL

## Step 2: Deploy Frontend

### Vercel (Recommended)
- [ ] Create Vercel account
- [ ] Import GitHub repository
- [ ] Set root directory to `/frontend`
- [ ] Add environment variable:
  - [ ] `REACT_APP_API_URL=https://your-backend-url.railway.app`
- [ ] Deploy
- [ ] Note the Vercel URL

### Netlify (Alternative)
- [ ] Create Netlify account
- [ ] Import GitHub repository
- [ ] Configure build settings
- [ ] Add environment variable
- [ ] Deploy

## Step 3: Configure Custom Domain

### In Hosting Provider (Vercel/Netlify)
- [ ] Add custom domain: `buildcustomresume.com`
- [ ] Add custom domain: `www.buildcustomresume.com`
- [ ] Follow domain verification steps
- [ ] Note DNS configuration requirements

## Step 4: Configure DNS in Namecheap

- [ ] Log into Namecheap account
- [ ] Go to Domain List → Manage → Advanced DNS
- [ ] Remove default/parking records
- [ ] Add A record for root domain (@)
- [ ] Add CNAME record for www subdomain
- [ ] Add CNAME record for api subdomain (if using subdomain)
- [ ] Save all changes
- [ ] Wait for DNS propagation (check with dnschecker.org)

## Step 5: Update Backend CORS

- [ ] Update `ALLOWED_ORIGINS` in backend environment variables:
  - [ ] `https://buildcustomresume.com`
  - [ ] `https://www.buildcustomresume.com`
- [ ] Redeploy backend if needed

## Step 6: Testing

- [ ] Test main domain: https://buildcustomresume.com
- [ ] Test www subdomain: https://www.buildcustomresume.com
- [ ] Test SSL certificate (should show lock icon)
- [ ] Test backend API: `curl https://api.buildcustomresume.com/api/health`
- [ ] Test file upload functionality
- [ ] Test resume enhancement
- [ ] Test download functionality
- [ ] Check browser console for errors
- [ ] Test on mobile device
- [ ] Test with different browsers

## Step 7: Post-Deployment

- [ ] Monitor error logs
- [ ] Set up monitoring/alerts (optional)
- [ ] Update any hardcoded URLs
- [ ] Test all features end-to-end
- [ ] Document any custom configurations
- [ ] Share the live URL!

## Troubleshooting

If something doesn't work:

1. **DNS Issues**
   - [ ] Check DNS propagation: https://dnschecker.org
   - [ ] Verify records in Namecheap match hosting provider requirements
   - [ ] Wait 24-48 hours if recently changed

2. **SSL Issues**
   - [ ] Ensure domain is added in hosting provider dashboard
   - [ ] Wait for SSL certificate issuance (can take up to 24 hours)
   - [ ] Verify DNS is fully propagated

3. **CORS Issues**
   - [ ] Verify `ALLOWED_ORIGINS` includes your domain
   - [ ] Check frontend is using correct API URL
   - [ ] Ensure no trailing slashes in URLs

4. **Backend Not Starting**
   - [ ] Check logs in hosting platform
   - [ ] Verify all environment variables are set
   - [ ] Ensure `gunicorn` is in requirements.txt

5. **Frontend Build Fails**
   - [ ] Verify `REACT_APP_API_URL` is set
   - [ ] Check build logs for errors
   - [ ] Ensure all dependencies are in package.json

## Success Criteria

Your deployment is successful when:
- ✅ Domain resolves correctly
- ✅ SSL certificate is active (HTTPS works)
- ✅ Frontend loads without errors
- ✅ Backend API responds correctly
- ✅ File upload works
- ✅ Resume enhancement works
- ✅ Download works
- ✅ No CORS errors in console

## Next Steps (Optional Enhancements)

- [ ] Set up error tracking (Sentry, etc.)
- [ ] Set up analytics (Google Analytics, etc.)
- [ ] Configure CDN for static assets
- [ ] Set up automated backups
- [ ] Configure rate limiting
- [ ] Add monitoring/uptime checks
- [ ] Set up CI/CD pipeline

---

**Congratulations!** Your website should now be live at https://buildcustomresume.com 🎉

