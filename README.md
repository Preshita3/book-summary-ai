 AI Book Summary Generator

An AI-powered web application that generates structured, high-quality book summaries in seconds using Large Language Models (LLMs).

 Overview
 This project allows users to enter the name of any book and instantly receive a detailed summary (~1000 words) including:

 Overview
 Core concepts
 Key lessons
 Real-life applications
 Final takeaway

 Built as a hands-on project to understand how real-world AI applications are developed, integrated, and deployed.

 Features
 Input any book name (e.g., Atomic Habits – James Clear)
 Instant AI-generated summaries
 Structured and easy-to-understand output
 Clean and simple user interface
 Secure API key handling (no hardcoded secrets)
 Tech Stack
 Python
 Streamlit (Frontend + App framework)
 LLM API (via OpenRouter)
 Create an environment variable:
 Windows:
 setx OPENROUTER_API_KEY "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"
 4. Run the app
 streamlit run app.py

Key Learnings
Integrating LLM APIs into real applications
Handling API errors, rate limits, and model issues
Prompt engineering for better output quality
Managing environment variables securely
Building end-to-end AI products

 Future Improvements
 Multi-language support (Hindi / Marathi)
 Download summary as PDF
 Custom summary length (500 / 1000 words)
 Improved UI/UX
 Book auto-suggestions
