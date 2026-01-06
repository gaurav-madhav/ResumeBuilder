# Namecheap DNS Configuration Guide

This guide will help you configure your DNS records in Namecheap to point `buildcustomresume.com` to your hosting provider.

## Quick Setup Steps

### 1. Access Namecheap DNS Settings

1. Log into your Namecheap account at https://www.namecheap.com
2. Go to **Domain List** from the left sidebar
3. Find `buildcustomresume.com` and click **Manage**
4. Navigate to the **Advanced DNS** tab

### 2. DNS Records Configuration

The exact records depend on your hosting provider. Here are common configurations:

---

## Configuration A: Vercel/Netlify (Frontend) + Railway (Backend)

### Frontend Records (Vercel/Netlify will provide exact values):

**A Record:**
- Type: `A Record`
- Host: `@`
- Value: `[IP provided by Vercel/Netlify]` (usually `76.76.21.21` for Vercel)
- TTL: `Automatic`

**CNAME Record for www:**
- Type: `CNAME Record`
- Host: `www`
- Value: `[CNAME provided by Vercel/Netlify]` (e.g., `cname.vercel-dns.com`)
- TTL: `Automatic`

### Backend Records (Railway):

**CNAME Record for API subdomain:**
- Type: `CNAME Record`
- Host: `api`
- Value: `[Your Railway app].railway.app` (e.g., `resume-builder-production.railway.app`)
- TTL: `Automatic`

**Example:**
```
Type    Host    Value                                    TTL
A       @       76.76.21.21                             Automatic
CNAME   www     cname.vercel-dns.com                     Automatic
CNAME   api     resume-builder-production.railway.app   Automatic
```

---

## Configuration B: Render (Full Stack)

### Frontend Records:

**CNAME Record:**
- Type: `CNAME Record`
- Host: `@`
- Value: `[Your Render static site].onrender.com`
- TTL: `Automatic`

**CNAME Record for www:**
- Type: `CNAME Record`
- Host: `www`
- Value: `[Your Render static site].onrender.com`
- TTL: `Automatic`

### Backend Records:

**CNAME Record for API:**
- Type: `CNAME Record`
- Host: `api`
- Value: `[Your Render web service].onrender.com`
- TTL: `Automatic`

**Note:** Render may require A records instead. Check Render's domain setup instructions.

---

## Configuration C: DigitalOcean App Platform

### Frontend Records:

**CNAME Record:**
- Type: `CNAME Record`
- Host: `@`
- Value: `[Your DigitalOcean app].ondigitalocean.app`
- TTL: `Automatic`

**CNAME Record for www:**
- Type: `CNAME Record`
- Host: `www`
- Value: `[Your DigitalOcean app].ondigitalocean.app`
- TTL: `Automatic`

### Backend Records:

**CNAME Record for API:**
- Type: `CNAME Record`
- Host: `api`
- Value: `[Your backend app].ondigitalocean.app`
- TTL: `Automatic`

---

## Important Notes

### 1. Remove Default Records
- Remove any default A records pointing to parking pages
- Remove any default CNAME records you don't need

### 2. DNS Propagation
- Changes can take **24-48 hours** to fully propagate
- Usually works within **1-2 hours**
- Check propagation status: https://dnschecker.org

### 3. TTL Settings
- Use **Automatic** TTL for most records
- Lower TTL (300-600) if you plan to change records frequently

### 4. Subdomain Setup
- The `api` subdomain is optional but recommended
- You can also use the same domain for both frontend and backend
- If using same domain, configure your hosting provider's reverse proxy

### 5. SSL Certificates
- Most hosting providers (Vercel, Netlify, Railway, Render) provide automatic SSL
- Ensure your domain is properly configured in the hosting provider's dashboard
- SSL will activate automatically once DNS propagates

---

## Verification Steps

### 1. Check DNS Records
```bash
# Check A record
dig buildcustomresume.com

# Check CNAME records
dig www.buildcustomresume.com
dig api.buildcustomresume.com
```

### 2. Test Domain Resolution
```bash
# Test main domain
ping buildcustomresume.com

# Test API subdomain
ping api.buildcustomresume.com
```

### 3. Test HTTPS
- Visit https://buildcustomresume.com
- Check that SSL certificate is valid
- Browser should show a lock icon

### 4. Test API Endpoint
```bash
curl https://api.buildcustomresume.com/api/health
```

---

## Common Issues

### Issue: Domain not resolving
**Solution:**
- Wait 24-48 hours for DNS propagation
- Verify records are correct in Namecheap
- Check with https://dnschecker.org

### Issue: SSL certificate not working
**Solution:**
- Ensure domain is added in hosting provider dashboard
- Wait for DNS propagation
- Some providers need 24-48 hours to issue SSL

### Issue: CNAME conflicts with A record
**Solution:**
- You cannot have both A and CNAME for the same host
- Use A record for root domain (@)
- Use CNAME for subdomains (www, api)

### Issue: www subdomain not working
**Solution:**
- Ensure CNAME record for www is set
- Verify value points to correct hosting provider
- Check hosting provider supports www subdomain

---

## Quick Reference: Namecheap DNS Interface

When adding records in Namecheap:

1. Click **Add New Record**
2. Select record type (A, CNAME, etc.)
3. Fill in:
   - **Host**: `@` for root, `www` for www, `api` for api subdomain
   - **Value**: IP address (A) or domain (CNAME)
   - **TTL**: Select "Automatic"
4. Click **Save**

---

## Support

If you need help:
1. Check your hosting provider's DNS documentation
2. Contact Namecheap support for DNS issues
3. Use DNS checker tools to verify propagation
4. Check hosting provider logs for domain verification status

---

## Example: Complete DNS Setup for Railway + Vercel

```
Record Type    Host    Value                                    TTL
A Record       @       76.76.21.21                             Automatic
CNAME Record   www     cname.vercel-dns.com                     Automatic
CNAME Record   api     resume-builder-production.railway.app   Automatic
```

This setup:
- Points `buildcustomresume.com` → Vercel (frontend)
- Points `www.buildcustomresume.com` → Vercel (frontend)
- Points `api.buildcustomresume.com` → Railway (backend)

Good luck! 🚀

