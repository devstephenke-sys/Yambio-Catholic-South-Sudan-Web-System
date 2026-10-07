# Proposed Information Architecture
## Catholic Diocese of Tombura-Yambio Website

**Date:** October 7, 2026
**Status:** PROPOSAL - Awaiting Diocesan Approval

---

## Executive Summary

This proposed architecture modernizes the existing structure while preserving all important content. Key improvements include:

- Flatter navigation structure
- Individual parish profile pages
- Dedicated Bishop section
- Events calendar
- Site-wide search
- Better CODEP organization
- Document library
- Improved multilingual consistency

---

## Proposed Structure (English)

```
/ (Home)
├── /about/
│   ├── /about/diocese/ (About the Diocese)
│   ├── /about/bishop/ (Bishop Eduardo Hiiboro Kussala)
│   ├── /about/curia/ (Leadership & Curia)
│   ├── /about/history/ (History - extracted from About Us)
│   └── /about/vision-mission/ (Vision, Mission, Values)
│
├── /pastoral/
│   ├── /pastoral/overview/ (About Pastoral Ministry)
│   ├── /pastoral/deaneries/ (Deanery Directory)
│   │   ├── /pastoral/deaneries/[deanery-slug]/ (Individual Deanery)
│   │   └── /pastoral/deaneries/[deanery-slug]/parishes/ (Parish list)
│   ├── /pastoral/parishes/ (Parish Directory - searchable)
│   │   └── /pastoral/parishes/[parish-slug]/ (Individual Parish Profile)
│   ├── /pastoral/youth/ (Youth Ministry)
│   ├── /pastoral/vocations/ (Vocations - NEW)
│   ├── /pastoral/formation/ (Formation programs - NEW)
│   └── /pastoral/institutions/
│       ├── /pastoral/institutions/seminaries/
│       │   ├── /pastoral/institutions/seminaries/philosophicum/
│       │   └── /pastoral/institutions/seminaries/propaedeutic/
│       └── /pastoral/institutions/other/ (Other institutions - NEW)
│
├── /social-development/ (CODEP)
│   ├── /social-development/overview/ (About CODEP)
│   ├── /social-development/programs/
│   │   ├── /social-development/programs/humanitarian/
│   │   ├── /social-development/programs/health/
│   │   ├── /social-development/programs/justice-peace/ (Justice & Peace)
│   │   ├── /social-development/programs/livelihoods/ (Livelihoods)
│   │   ├── /social-development/programs/hiv-aids/ (HIV/AIDS)
│   │   └── /social-development/programs/wash/ (WASH)
│   ├── /social-development/projects/ (Project Directory - NEW)
│   │   └── /social-development/projects/[project-slug]/ (Individual Project)
│   ├── /social-development/departments/
│   │   ├── /social-development/departments/culture/ (Culture, Diversity, Outreach, Sports)
│   │   ├── /social-development/departments/education/
│   │   └── /social-development/departments/finance/
│   └── /social-development/partners/ (Partners - expanded)
│
├── /education/ (Elevated from CODEP for visibility)
│   ├── /education/overview/ (Education Department)
│   ├── /education/schools/ (School Directory - searchable)
│   │   └── /education/schools/[school-slug]/ (Individual School Profile)
│   └── /education/programs/ (Education programs)
│
├── /news/
│   ├── /news/ (News Archive)
│   ├── /news/category/[category]/ (Category pages)
│   └── /news/[article-slug]/ (Individual Article)
│
├── /events/ (NEW)
│   ├── /events/ (Events Calendar)
│   ├── /events/past/ (Past Events)
│   └── /events/[event-slug]/ (Individual Event)
│
├── /sermons/
│   ├── /sermons/ (Sermon Archive)
│   └── /sermons/[sermon-slug]/ (Individual Sermon)
│
├── /multimedia/
│   ├── /multimedia/photos/ (Photo Gallery)
│   ├── /multimedia/videos/ (Video Gallery)
│   └── /multimedia/audio/ (Audio - NEW)
│
├── /resources/ (NEW)
│   ├── /resources/documents/ (Document Library)
│   ├── /resources/publications/ (Publications)
│   └── /resources/forms/ (Downloadable Forms)
│
├── /contact/
│   ├── /contact/ (Contact Form & Information)
│   ├── /contact/offices/ (Office Locations)
│   └── /contact/feedback/ (Feedback Form - NEW)
│
└── /search/ (Search Results)
```

---

## Multilingual Structure

### Recommended Approach
**Subdirectory structure with language prefix:**

```
/en/ (English - default, can be omitted)
/it/ (Italian)
/fr/ (French)
```

### URL Examples
- English: `/about/diocese/` or `/en/about/diocese/`
- Italian: `/it/about/diocese/` or `/it/chi-siamo/` (localized slugs)
- French: `/fr/about/diocese/` or `/fr/qui-sommes-nous/` (localized slugs)

### Language Switching
- Persistent language selector in header
- hreflang tags for SEO
- Language-specific sitemaps

---

## Key Improvements Explained

### 1. Flatter Navigation
**Before:** Homepage → Pastoral Affairs → Deaneries → [Deanery] → Find parish in table
**After:** Homepage → Parishes → [Parish Profile] OR Homepage → Deaneries → [Deanery] → Parishes

**Benefit:** Reduced clicks from 3-4 to 2-3

### 2. Individual Parish Profiles
**Before:** Parishes only listed in deanery tables
**After:** Each parish has its own page with:
- Full details (priest, location, contact, mass times, history)
- Associated quasi-parishes
- Related news
- Photo gallery
- Map location

**Benefit:** Better parish discovery and richer content

### 3. Dedicated Bishop Section
**Before:** Bishop only mentioned on homepage
**After:** Complete bishop page with:
- Biography
- Pastoral letters/messages
- Recent activities
- Photos
- Contact

**Benefit:** Important information easily accessible

### 4. Events Section
**Before:** No events section
**After:** Events calendar with:
- Upcoming events
- Past events archive
- Event categories
- Registration information
- Map locations

**Benefit:** Better communication of diocesan activities

### 5. Site-Wide Search
**Before:** No search functionality
**After:** Search across:
- News
- Sermons
- Parishes
- Schools
- Documents
- Pages

**Benefit:** Users can quickly find information

### 6. CODEP Reorganization
**Before:** Programs listed on About CODEP but not all have pages
**After:** Clear program structure:
- Each program has dedicated page
- Project directory with individual project pages
- Better navigation between programs and departments

**Benefit:** Clearer understanding of CODEP work

### 7. Document Library
**Before:** Documents scattered across departments
**After:** Centralized resource section with:
- Categorized documents
- Downloadable PDFs
- Searchable archive
- Metadata (date, type, size)

**Benefit:** Easy access to official documents

### 8. Education Elevation
**Before:** Education buried under Social Affairs
**After:** Education as top-level section
- School directory with individual school profiles
- Better visibility for educational institutions

**Benefit:** Education gets appropriate prominence

### 9. Vocations & Formation
**Before:** Limited information
**After:** Dedicated sections for:
- Vocations promotion
- Formation programs
- Seminary information enhanced

**Benefit:** Better support for vocations ministry

### 10. Improved Mobile Navigation
**Before:** Assumed poor mobile experience
**After:** Responsive design with:
- Mobile-friendly menu
- Touch-friendly interactions
- Optimized for low bandwidth

**Benefit:** Better experience on mobile devices

---

## Homepage Redesign

### Proposed Sections

1. **Hero**
   - Bishop photo or diocesan image
   - Welcome message
   - Quick navigation buttons

2. **Diocese Overview**
   - Brief introduction
   - Key statistics (parishes, Catholics, counties)
   - Link to About section

3. **Bishop Message**
   - Photo of Bishop
   - Recent message or quote
   - Link to Bishop page

4. **Pastoral Highlights**
   - Featured parish or deanery
   - Recent pastoral activity
   - Link to Pastoral section

5. **Social Development / CODEP**
   - Featured program or project
   - Impact statistics
   - Link to CODEP section

6. **Latest News**
   - 3-4 most recent news articles
   - Thumbnail images
   - Link to News archive

7. **Upcoming Events**
   - Next 3-5 events
   - Date, time, location
   - Link to Events calendar

8. **Featured Sermon**
   - Most recent sermon
   - Audio/video if available
   - Link to Sermons

9. **Quick Links**
   - Find a Parish
   - Contact Us
   - Donate (if applicable)
   - Newsletter signup

10. **Partners**
    - Partner logos
    - Link to Partners page

11. **Contact Preview**
    - Main office contact
    - Social media links
    - Link to Contact page

12. **Footer**
    - Full navigation
    - Office locations
    - Social media
    - Legal links

---

## Navigation Menu Structure

### Primary Navigation (Desktop)

```
Home | About | Pastoral | Social Development | Education | News | Resources | Contact
```

### Secondary Navigation (Dropdowns)

**About:**
- Diocese
- Bishop
- Leadership
- History
- Vision & Mission

**Pastoral:**
- Deaneries
- Parishes
- Youth Ministry
- Vocations
- Formation
- Institutions

**Social Development (CODEP):**
- About CODEP
- Programs
- Projects
- Departments
- Partners

**Education:**
- Overview
- Schools
- Programs

**News:**
- Latest News
- Categories
- Events

**Resources:**
- Documents
- Publications
- Multimedia
- Sermons

**Contact:**
- Contact Form
- Offices
- Feedback

---

## Search Functionality

### Search Index
- Pages
- News articles
- Sermons
- Parishes
- Schools
- Projects
- Documents

### Search Filters
- Content type
- Date range
- Category
- Language

### Search Results Display
- Relevance ranking
- Content type indicators
- Snippets
- Pagination

---

## Parish Directory UX

### Browse by Deanery
- List of deaneries with parish counts
- Click deanery → list of parishes → click parish → parish profile

### Search Parishes
- Search by name
- Filter by deanery
- Filter by county
- Filter by status (parish/quasi-parish)

### Parish Profile Page
- Basic information (name, deanery, county, location)
- Priest information
- Contact details
- Mass times (if available)
- History
- Associated quasi-parishes
- Map
- Photo gallery
- Related news
- Related events

---

## CODEP Project Directory

### Project Page Structure
- Project title
- Program category
- Location
- Beneficiaries
- Objectives
- Activities
- Results/Impact
- Partners
- Timeline
- Budget (if public)
- Photos
- Documents
- Related news
- Contact

### Browse Projects
- Filter by program
- Filter by location
- Filter by status (active/completed)
- Search by name

---

## News System

### News Article Page
- Title
- Date
- Author
- Category
- Featured image
- Body content
- Tags
- Related articles
- Share buttons
- Print option

### News Archive
- Featured story
- Latest news
- Category filtering
- Search
- Pagination
- Archive by year/month

---

## Events System

### Event Page
- Title
- Date and time
- Location (with map)
- Description
- Organizer
- Image
- Registration information
- Contact
- Related events

### Events Calendar
- Month view
- List view
- Filter by category
- Filter by location
- Upcoming vs past events

---

## Document Library

### Document Categories
- Pastoral documents
- CODEP reports
- Annual reports
- Financial reports (public)
- Educational materials
- Forms
- Policies
- Publications

### Document Metadata
- Title
- Description
- Date
- Category
- File type
- File size
- Download count
- Language

### Browse
- Filter by category
- Filter by date
- Filter by type
- Search

---

## SEO Considerations

### URL Structure
- Clean, descriptive URLs
- Hyphen-separated words
- Lowercase
- No trailing slashes (configurable)

### SEO Elements
- Unique title tags
- Meta descriptions
- H1 hierarchy
- Canonical URLs
- Open Graph tags
- Twitter Card tags
- Schema.org structured data
- Breadcrumbs
- XML sitemap
- Robots.txt

### Multilingual SEO
- hreflang tags
- Language-specific sitemaps
- Alternate language links
- Localized meta tags

---

## Accessibility Considerations

### WCAG 2.1 AA Compliance
- Semantic HTML
- Keyboard navigation
- ARIA labels (where needed)
- Alt text for images
- Color contrast (4.5:1)
- Focus indicators
- Skip navigation link
- Accessible forms
- Screen reader compatibility
- Resizable text

### Performance
- Core Web Vitals optimization
- Lazy loading images
- Optimized images (WebP/AVIF)
- Minimal JavaScript
- Code splitting
- CDN for static assets
- Browser caching

---

## Mobile-First Design

### Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

### Mobile Features
- Hamburger menu
- Touch-friendly targets (44px minimum)
- Stacked layouts
- Simplified navigation
- Optimized images
- Reduced animations
- Offline-capable (service worker)

---

## Content Management

### CMS Requirements
- Easy content editing
- Image upload/management
- Document upload
- Multi-language support
- User roles (admin, editor, author)
- Version control
- Draft/publish workflow
- Scheduled publishing

### Content Types
- Pages
- News articles
- Events
- Sermons
- Parishes
- Schools
- Projects
- Documents
- Staff profiles

### Custom Fields for Key Content Types

**Parish:**
- Name
- Slug
- Deanery (relationship)
- County
- Location/Address
- Priest
- Contact (phone, email)
- Mass times
- Creation date
- Status
- Description
- History
- Images
- Map coordinates

**News:**
- Title
- Slug
- Excerpt
- Content
- Featured image
- Author
- Category
- Tags
- Published date
- Status
- Language

**Event:**
- Title
- Slug
- Date/time
- Location
- Description
- Image
- Category
- Registration info
- Status

**Project:**
- Title
- Slug
- Program
- Location
- Beneficiaries
- Objectives
- Activities
- Results
- Partners
- Timeline
- Status

---

## Migration Strategy

### Phase 1: Core Content
- Homepage
- About pages
- Bishop page (new)
- Contact page
- Basic navigation

### Phase 2: Pastoral Content
- Deanery pages
- Parish profiles (new)
- Seminary pages
- Youth ministry

### Phase 3: Social Development
- CODEP overview
- Program pages
- Department pages
- Project profiles (new)

### Phase 4: Dynamic Content
- News system
- Events system (new)
- Sermons
- Multimedia

### Phase 5: Resources
- Document library (new)
- Publications
- Forms

### Phase 6: Multilingual
- Italian translation
- French translation
- Language consistency

---

## Technical Recommendations

### Framework Options
1. **Next.js + Headless CMS** (Recommended)
   - Modern, fast
   - Great SEO
   - Easy multilingual
   - Static generation where possible

2. **WordPress + Custom Theme**
   - Familiar to current team
   - Good CMS
   - Plugin ecosystem
   - May require more maintenance

3. **Static Site Generator + CMS**
   - Hugo, Jekyll, or similar
   - Very fast
   - Simple hosting
   - May limit dynamic features

### Database (if needed)
- PostgreSQL or MySQL
- Normalized schema
- Relationships for parishes, deaneries, projects, etc.

### Hosting
- Vercel, Netlify, or similar (for Next.js)
- Traditional hosting (for WordPress)
- CDN for static assets
- SSL certificate
- Backup strategy

---

## Success Metrics

### User Experience
- Reduced average clicks to find information
- Improved search usage
- Increased time on site
- Lower bounce rate

### Content
- Increased news publication frequency
- More parish profiles with complete information
- Regular event updates
- Growing document library

### Technical
- Improved Core Web Vitals
- Faster page load times
- Better mobile experience
- Higher accessibility scores

### Engagement
- Increased contact form submissions
- More newsletter signups (if added)
- Better social media engagement
- Increased return visitors

---

## Approval Required

This proposed architecture requires approval from:
1. Bishop Eduardo Hiiboro Kussala
2. Diocesan Curia
3. CODEP leadership
4. Department heads

Questions for approval:
1. Is the proposed structure appropriate?
2. Are there missing sections?
3. Should any sections be prioritized differently?
4. Are there content sensitivities to consider?
5. Who will be responsible for content updates?
6. What is the preferred technology stack?
7. What is the timeline for implementation?
8. What is the budget?
