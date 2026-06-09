# AI-Powered Consent Form Explainer

## Problem Statement

Design a consent-form explainer that translates procedure risks into patient-friendly summaries without changing the legal meaning of the original document.

## Project Overview

Medical consent forms often contain complex terminology that can be difficult for patients to understand. This project uses Artificial Intelligence and Natural Language Processing (NLP) to convert medical consent forms into simple, patient-friendly language while preserving the original intent and risks.

## Objectives

* Extract text from medical consent form PDFs.
* Simplify medical terminology using a Large Language Model (LLM).
* Generate patient-friendly summaries.
* Improve healthcare communication and accessibility.
* Support future enhancements such as risk extraction and multilingual explanations.

## Features Implemented

### PDF Text Extraction

* Upload and process medical consent forms.
* Extract text using PDF parsing techniques.

### AI-Based Simplification

* Uses Llama 3 running locally through Ollama.
* Converts complex medical language into easy-to-understand summaries.

### Patient-Friendly Output

* Presents information in a structured format.
* Maintains the original meaning of the consent form.

## System Workflow

Consent Form PDF
↓
Text Extraction (pdfplumber)
↓
Llama 3 (Ollama)
↓
Patient-Friendly Summary

## Technology Stack

### Programming Language

* Python

### Libraries

* pdfplumber
* requests

### AI Model

* Llama 3

### AI Runtime

* Ollama

### Version Control

* Git
* GitHub

## Project Structure

PS032-AI-Consent-Explainer

├── backend
│   ├── main.py
│   ├── pdf_parser.py
│   └── summarizer.py

├── frontend

├── docs

├── sample_pdfs

├── requirements.txt

└── README.md

## Current Results

Successfully implemented:

* PDF text extraction
* Llama 3 integration
* Consent form simplification
* Local AI processing

## Future Enhancements

* Risk Extraction Module
* Risk Verification System
* Readability Score Analysis
* Multilingual Support (Kannada, Hindi, Bengali)
* FastAPI Backend
* React Frontend Dashboard
* Voice-Based Consent Explanation

## Author

Arighna Chowdhury

B.Tech Computer Science and Engineering

Dayananda Sagar University
