# Catholic Diocese of Tombura-Yambio Website Redesign

**Project Start Date:** October 7, 2026
**Status:** Discovery Phase Complete - Awaiting Diocesan Approval

---

## Project Overview

This project aims to completely redesign and rebuild the website for the Catholic Diocese of Tombura-Yambio (CDTY) in South Sudan. The goal is to create a modern, fast, accessible, and maintainable digital platform that serves the Diocese's communication needs while preserving all important existing content.

**Existing Website:** https://www.catholicdioceseoftomburayambio.org/

---

## Discovery Phase - COMPLETE ✅

The discovery phase has been completed. The following documentation has been created:

### Core Documentation

1. **[DISCOVERY-EXECUTIVE-REPORT.md](DISCOVERY-EXECUTIVE-REPORT.md)**
   - Executive summary of findings
   - What exists, what to preserve, what to redesign
   - Recommended architecture and technology
   - Migration risks and timeline
   - **START HERE** for overview

2. **[website-inventory.md](website-inventory.md)**
   - Complete inventory of all pages and content
   - Key statistics and critical issues
   - Content classification (KEEP/UPDATE/REMOVE)
   - Technical notes

3. **[existing-information-architecture.md](existing-information-architecture.md)**
   - Current website structure
   - Navigation analysis
   - Content distribution
   - Strengths and weaknesses

4. **[proposed-information-architecture.md](proposed-information-architecture.md)**
   - Recommended new structure
   - Key improvements explained
   - Navigation menu structure
   - Search and UX improvements

5. **[content-verification-report.md](content-verification-report.md)**
   - Content requiring diocesan verification
   - Critical inconsistencies identified
   - Missing information
   - Verification process and timeline

6. **[technical-audit.md](technical-audit.md)**
   - Current platform analysis (WordPress)
   - Performance assessment
   - Security considerations
   - Recommended technology stack

7. **[design-proposal.md](design-proposal.md)**
   - Visual direction and design philosophy
   - Color palette and typography
   - Layout patterns and components
   - Accessibility and performance considerations

---

## Key Findings Summary

### What Exists
- WordPress-based multilingual site (English, Italian, French)
- 6 deaneries with 35 parishes (inconsistent across languages)
- CODEP (social development wing) with 5 departments
- 2 seminaries, extensive school listings
- 28+ staff members in directory
- News archive (latest from July 2024)
- Copyright shows 2019 (outdated)

### Critical Issues
1. **Inconsistent Data:** Parish counts differ by language (35 vs 27)
2. **Outdated Content:** Copyright 2019, finance objectives (2025), youth plans (2020)
3. **Missing Sections:** No Bishop page, no events, no search, no document library
4. **Poor UX:** Parishes buried in tables, no parish profiles, deep navigation
5. **Empty Sections:** Photo and video galleries have no content
6. **Geographic Uncertainty:** References "former Western Equatoria State" - South Sudan restructured

### What Needs Verification (Before Migration)
- Geographic jurisdiction (current state/county structure)
- Actual parish and deanery counts
- Priest assignments
- Contact information
- Staff directory
- Population statistics
- CODEP program status

---

## Proposed Solution

### New Information Architecture
- Flatter navigation with search functionality
- Individual parish profile pages
- Dedicated Bishop section
- Events calendar
- Document library
- Elevated Education section
- Better CODEP organization

### Recommended Technology
**Primary:** Next.js + Sanity.io (headless CMS)
- Modern, fast, excellent performance
- Great SEO
- Easy for non-technical staff
- Future-proof

**Alternative:** WordPress + Custom Theme
- Familiar to current team
- Lower learning curve
- Less modern but functional

### Visual Direction
- Catholic and dignified
- African and contextual
- Modern and professional
- Colors: Deep green, gold, white
- Typography: Serif headings, sans-serif body

---

## Next Steps

### Immediate Actions Required

1. **Review Discovery Documentation**
   - Read [DISCOVERY-EXECUTIVE-REPORT.md](DISCOVERY-EXECUTIVE-REPORT.md)
   - Review all discovery documents
   - Ask questions or request clarifications

2. **Diocesan Approval Required**
   - Bishop and Curia must approve:
     - Overall project direction
     - Proposed information architecture
     - Technology stack selection
     - Budget approval

3. **Begin Content Verification**
   - Schedule meetings with department heads
   - Verify critical information (geography, parish counts, contact info)
   - Update outdated content
   - Gather missing information (Bishop biography, etc.)

### After Approval

4. **Design Phase** (4-6 weeks)
   - Create wireframes
   - Develop visual design
   - Build design system
   - Design approval

5. **Development Phase** (8-12 weeks)
   - Setup development environment
   - Build components and features
   - Integrate CMS
   - Migrate content

6. **Testing and Launch** (3-4 weeks)
   - Comprehensive testing
   - Bug fixes
   - Deployment
   - Go live

**Total Timeline:** 5-7 months after approval

---

## Budget Estimate

### Development (One-time)
- Discovery: $3,000 - $5,000 ✅ Complete
- Design: $5,000 - $10,000
- Development: $10,000 - $20,000
- Content Migration: $2,000 - $5,000
- Testing: $2,000 - $4,000
- Training: $1,000 - $2,000

**Total: $23,000 - $46,000**

### Ongoing Annual
- Hosting: $500 - $2,000
- CMS: $0 - $1,200
- Maintenance: $3,000 - $6,000 (optional)

**Total: $3,515 - $9,715/year**

---

## File Structure

```
St Yambio Catholic Website/
├── README.md (this file)
├── DISCOVERY-EXECUTIVE-REPORT.md
├── website-inventory.md
├── existing-information-architecture.md
├── proposed-information-architecture.md
├── content-verification-report.md
├── technical-audit.md
├── design-proposal.md
└── [Additional documentation to be created]
```

---

## Critical Decision Points

### Decision 1: Project Approval
**Question:** Does the Diocese approve proceeding with the website redesign?
**Needed:** Bishop and Curia approval
**Timeline:** Immediate

### Decision 2: Information Architecture
**Question:** Is the proposed information architecture appropriate?
**Needed:** Stakeholder review and approval
**Timeline:** After project approval

### Decision 3: Technology Stack
**Question:** Which technology stack should be used?
**Options:**
- Next.js + Sanity.io (recommended)
- WordPress + Custom Theme (alternative)
- Other (to be discussed)
**Needed:** Technical decision and budget approval
**Timeline:** After architecture approval

### Decision 4: Budget
**Question:** Is the budget acceptable?
**Range:** $23,000 - $46,000 (one-time)
**Needed:** Finance Secretary approval
**Timeline:** After technology decision

---

## Content Verification Priority

### CRITICAL (Must Complete Before Development)
1. Geographic jurisdiction (South Sudan state structure)
2. Parish count (resolve 35 vs 27 inconsistency)
3. Deanery count (resolve 6 vs 4 inconsistency)
4. Bishop information (complete biography)
5. Priest assignments (all deaneries)
6. Contact information (all offices)

### HIGH (Complete Before Development)
7. Population statistics
8. Staff directory
9. CODEP programs
10. Health department status

### MEDIUM (Complete During Development)
11. Seminary information
12. School listings
13. Partners
14. Vision/Mission/Values

---

## Team and Responsibilities

### Diocesan Team
- **Bishop Eduardo Hiiboro Kussala** - Overall approval, Bishop information
- **Vicar General** - Content verification, leadership information
- **Curia Secretary** - Administrative coordination
- **CODEP Director** - CODEP content verification
- **Education Secretary** - School information verification
- **Finance Secretary** - Budget approval
- **Pastoral Coordinator** - Parish/deanery information
- **Department Heads** - Content verification for respective sections

### Development Team
- **Project Manager** - Overall coordination
- **UX/UI Designer** - Design and user experience
- **Frontend Developer** - Implementation
- **Backend Developer** - CMS integration
- **Content Specialist** - Content migration
- **QA Tester** - Testing and quality assurance

---

## Communication Plan

### Weekly Updates
- Progress report to Bishop and Curia
- Demo of completed work
- Review of any issues or blockers

### Milestone Reviews
- Design approval
- Development progress
- Testing results
- Launch readiness

### Documentation
- All decisions documented
- Change requests tracked
- Status updates shared

---

## Risks and Mitigation

### High Risk
- **Data loss during migration** → Complete backups, staging environment
- **SEO ranking drop** → 301 redirects, preserve URLs
- **Content inconsistency** → Verification before migration

### Medium Risk
- **Performance issues** → Performance testing, optimization
- **Staff training** → Comprehensive training, user-friendly CMS
- **Scope creep** → Clear requirements, phased approach

---

## Success Criteria

The project will be considered successful when:

1. All important existing content is migrated
2. New information architecture is implemented
3. Site is fast (Core Web Vitals green)
4. Site is accessible (WCAG AA compliant)
5. Site is mobile-responsive
6. Search functionality works
7. Diocesan staff can update content
8. SEO is maintained or improved
9. No data loss occurred
10. Stakeholders are satisfied with the result

---

## Contact

For questions about this project:

**Project Manager:** [To be assigned]
**Email:** [To be provided]
**Phone:** [To be provided]

---

## License and Usage

This documentation is confidential property of the Catholic Diocese of Tombura-Yambio. Do not distribute without permission.

---

**Last Updated:** October 7, 2026
**Document Version:** 1.0
