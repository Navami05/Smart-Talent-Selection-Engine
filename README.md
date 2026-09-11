# Smart Talent Selection Engine

An AI-powered resume screening and job-candidate matching system designed to help recruiters identify suitable candidates based on semantic alignment with a Job Description rather than simple keyword matching.

## Problem Statement

Traditional Applicant Tracking Systems often rely heavily on keyword matching. This can cause qualified candidates to be rejected when they use different terminology, while candidates who repeatedly include relevant keywords may rank higher than candidates with genuinely stronger experience.

The Smart Talent Selection Engine aims to understand the meaning and intent behind resumes and Job Descriptions to produce more meaningful candidate rankings.

## Objectives

- Accept resumes in multiple formats such as PDF, DOCX, JPG, and PNG.
- Extract and understand information from resumes.
- Process Job Descriptions and identify their requirements.
- Compare candidates with Job Descriptions using semantic matching.
- Generate a compatibility score from 0–100.
- Consider the depth and relevance of candidate experience.
- Rank candidates based on their overall suitability.
- Generate a short AI-based "Summary of Fit" for top candidates.

## Planned Features

### 1. Multi-Format Resume Ingestion
- PDF, DOCX, JPG, and PNG support
- Handling of different resume layouts
- File validation and error handling
- Resume organization by job role or batch

### 2. JD-to-Candidate Ranking
- Job Description processing
- Semantic resume-JD matching
- Compatibility scoring
- Experience-depth analysis
- Candidate ranking
- AI-generated "Summary of Fit"

## Planned Technology Stack

### Frontend
- React
- Vite

### Backend
- Python
- FastAPI

### AI / Machine Learning
- Text embeddings
- Semantic similarity
- Natural Language Processing

### Database
- SQLite initially
- PostgreSQL if required

## Project Status

🚧 Currently under development.

## Future Documentation

This README will be expanded as the project develops to include:

- System architecture
- Installation instructions
- Project setup
- API documentation
- AI/ML methodology
- Testing results
- Screenshots
- Limitations
- Future scope

