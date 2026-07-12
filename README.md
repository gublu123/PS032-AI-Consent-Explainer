# 🏥 AI Consent Form Explainer with Multi-LLM Comparison

## Problem Statement

Design a consent-form explainer that translates procedure risks into patient-friendly summaries without changing the legal meaning of the original document.

## Project Overview

Medical consent forms often contain complex medical terminology that can be difficult for patients to understand.

This project uses Artificial Intelligence (AI) and Large Language Models (LLMs) running locally through Ollama to simplify medical consent forms into patient-friendly language while preserving the original legal meaning and medical risks.

The application also compares multiple AI models based on response quality, response time, and risk preservation to help identify the most suitable model for medical consent summarization.

## Objectives

- Extract text from medical consent form PDFs.
- Generate patient-friendly summaries using AI.
- Extract medical risks from consent forms.
- Verify that important risks are preserved in the summary.
- Compare multiple Large Language Models (LLMs).
- Measure response time of different AI models.
- Improve healthcare communication and patient understanding.

## Features Implemented

### 📄 PDF & TXT Processing

- Upload medical consent forms in PDF or TXT format.
- Extract text using **pdfplumber**.
- Supports multiple document formats.

---

### 🤖 AI-Powered Consent Form Simplification

- Simplifies complex medical consent forms into patient-friendly language.
- Preserves the legal meaning and important medical information.
- Generates structured summaries including:
  - Procedure
  - Benefits
  - Risks
  - Recovery

---

### ⚠️ Medical Risk Extraction

- Automatically extracts risks, complications, side effects, and warnings from the original consent form.
- Uses AI-powered risk extraction for improved accuracy.

---

### ✅ Risk Verification

- Compares risks extracted from the original consent form with those present in the generated summary.
- Detects and reports any missing risks to ensure important medical information is not omitted.

---

### 🔍 Multi-LLM Comparison

- Compare multiple Large Language Models simultaneously.
- Supports:
  - Llama 3.2
  - Qwen 3.5
  - Mistral
  - Gemma 3
  - DeepSeek R1

---

### ⏱️ Performance Benchmarking

- Measures response time for each AI model.
- Displays the fastest model automatically.

---

### 🔄 Dynamic Ollama Model Detection

- Automatically detects all installed Ollama models.
- No code modification is required when new models are installed.

---

### 🌐 Interactive Web Interface

- Upload consent forms through a simple web interface.
- Select any installed AI model.
- Compare multiple models using checkboxes.
- Display summaries, extracted risks, missing risks, and performance metrics.

## System Workflow

## System Workflow

Medical Consent Form (PDF/TXT)
            │
            ▼
Text Extraction (pdfplumber)
            │
            ▼
Select AI Model(s)
            │
            ▼
Ollama (Local LLM)
            │
            ▼
Patient-Friendly Summary
            │
     ┌──────┴────────┐
     ▼               ▼
Risk Extraction   Summary Risk Extraction
     │               │
     └──────┬────────┘
            ▼
Risk Verification
            │
            ▼
Compare Multiple Models
            │
            ▼
Performance Analysis
(Response Time • Missing Risks • Fastest Model)

## Technology Stack

### 💻 Programming Language

- Python

---

### ⚙️ Backend Framework

- FastAPI

---

### 🌐 Frontend

- HTML5
- CSS3
- JavaScript

---

### 📚 Python Libraries

- FastAPI
- Uvicorn
- pdfplumber
- requests
- python-multipart

---

### 🤖 Supported AI Models

- Llama 3.2
- Qwen 3.5
- Mistral
- Gemma 3
- DeepSeek R1

---

### 🧠 AI Runtime

- Ollama (Local LLM Runtime)

---

### 🗂 Version Control

- Git
- GitHub

---

### 🖥 Development Environment

- Visual Studio Code

## Project Structure

PS032-AI-Consent-Explainer

├── backend
│   ├── api.py
│   ├── main.py
│   ├── pdf_parser.py
│   ├── summarizer.py
│   ├── risk_extractor.py
│   ├── verifier.py
│
├── frontend
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
├── sample_pdfs
│
├── requirements.txt
│
└── README.md

## Current Results

Successfully implemented:

- PDF and TXT document processing
- AI-powered consent form simplification
- Medical risk extraction
- Missing risk verification
- Multi-LLM comparison
- Dynamic Ollama model detection
- Response time benchmarking
- Fastest model identification
- Local AI processing using Ollama
- Interactive FastAPI web application

## Future Enhancements

- AI-powered semantic risk verification
- Readability score analysis
- Downloadable PDF reports
- Doctor review mode
- Multilingual support (Kannada, Hindi, Bengali)
- Voice-based consent explanation
- Cloud deployment
- User authentication and secure patient records

## Author

Arighna Chowdhury

B.Tech Computer Science and Engineering

Dayananda Sagar University
