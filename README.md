# Enterprise AI Resume Copilot

An AI-powered resume analysis and job-matching system that analyzes a candidate's profile against a job description, identifies skill gaps, evaluates job fit, and provides actionable resume and career recommendations.

## 🚀 Overview

**Enterprise AI Resume Copilot** is a modular Generative AI application built with Python, FastAPI, and Google's Gemini API.

The system uses multiple specialized AI agents to analyze:

- Candidate profiles
- Job descriptions
- Candidate-job matching
- Skill gaps
- Resume optimization opportunities
- Final application recommendations

The project follows a modular architecture so that each analysis component can be developed, tested, and improved independently.

---

## ✨ Key Features

### 👤 Candidate Profile Analysis

Analyzes candidate information including:

- Technical skills
- Education
- Experience
- Projects
- Certifications
- Career level
- Primary technical domain

### 💼 Job Description Analysis

Extracts important information from a job description:

- Required skills
- Preferred skills
- Required experience
- Job responsibilities

### 🎯 Candidate-Job Matching

Compares candidate skills with job requirements and determines:

- Matched skills
- Missing skills
- Match percentage
- Overall job-fit assessment

### 📊 Skill Gap Analysis

Identifies missing or insufficient skills required for the target position and provides improvement suggestions.

### 📝 Resume Optimization

Generates recommendations for improving the candidate's resume based on the target job description.

### 🤖 Final Recommendation

Produces an overall recommendation containing:

- Overall match score
- Application recommendation
- Key strengths
- Major gaps
- Priority improvements

---

## 🏗️ System Architecture

The project follows a modular agent-based architecture:

```text
                    ┌──────────────────────┐
                    │      Candidate       │
                    │       Profile        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Profile Analyzer    │
                    │        Agent         │
                    └──────────┬───────────┘
                               │
                               │
                    ┌──────────▼───────────┐
                    │      Job Analyzer     │
                    │        Agent          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Job Matcher       │
                    │        Agent          │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
       ┌──────────────────┐       ┌──────────────────┐
       │   Skill Gap      │       │ Resume Optimizer │
       │    Analyzer      │       │                  │
       └────────┬─────────┘       └────────┬─────────┘
                │                          │
                └────────────┬─────────────┘
                             ▼
                  ┌──────────────────────┐
                  │ Final Recommendation │
                  │        Agent         │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Final Analysis     │
                  └──────────────────────┘
```

---

## 📁 Project Structure

```text
Enterprise_AI_Resume_Copilot/
│
├── app/
│   ├── main.py
│   │
│   ├── agents/
│   │   ├── profile_analyzer.py
│   │   ├── job_analyzer.py
│   │   ├── job_matcher.py
│   │   ├── skill_gap_analyzer.py
│   │   ├── resume_optimizer.py
│   │   └── final_recommender.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── logging_config.py
│   │   └── settings.py
│   │
│   ├── models/
│   │   ├── profile.py
│   │   ├── job.py
│   │   ├── match.py
│   │   ├── match_request.py
│   │   ├── skill_gap.py
│   │   ├── resume_optimization.py
│   │   ├── recommendation.py
│   │   └── analyze_response.py
│   │
│   ├── orchestrator/
│   │   └── resume_analysis.py
│   │
│   └── services/
│       ├── llm_service.py
│       └── llm_models.py
│
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_llm_service.py
│   ├── test_orchestrator.py
│   └── test_real_pipeline.py
│
├── .env
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── README.md
```

> **Note:** `.env` should never be committed to Git because it contains the Gemini API key.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API framework |
| Pydantic | Data validation and structured models |
| Google Gemini | Generative AI / LLM |
| python-dotenv | Environment variable management |
| Uvicorn | ASGI application server |
| Pytest | Automated testing |
| HTTPX | API testing |
| Git | Version control |

---

## 🔑 Environment Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

Never upload the actual API key to GitHub.

Make sure `.env` is included in `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
.pytest_cache/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Enterprise_AI_Resume_Copilot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

---

## 🔌 API Endpoints

The application currently exposes five main analysis endpoints.

### 1. Analyze Profile

```text
POST /analyze-profile
```

Analyzes candidate information and generates a structured profile analysis.

### 2. Analyze Job

```text
POST /analyze-job
```

Analyzes a job description and extracts important job requirements.

### 3. Analyze Match

```text
POST /analyze-match
```

Compares a candidate profile against job requirements.

### 4. Analyze Skill Gap

```text
POST /analyze-skill-gap
```

Identifies missing skills and provides improvement recommendations.

### 5. Complete Resume Analysis

```text
POST /analyze
```

Runs the complete resume analysis pipeline.

The complete pipeline combines:

```text
Profile Analysis
       ↓
Job Analysis
       ↓
Candidate-Job Matching
       ↓
Skill Gap Analysis
       ↓
Resume Optimization
       ↓
Final Recommendation
```

---

## 🧪 Testing

The project includes automated tests for the API, LLM service, individual components, and the complete pipeline.

Run all tests with:

```bash
pytest
```

Current test status:

```text
15 passed
```

This confirms that the current implementation passes the project's automated test suite.

---

## 🧠 AI Pipeline

The core orchestration is handled by the resume analysis pipeline.

Conceptually:

```text
Candidate + Job
      │
      ▼
Profile Analyzer
      │
      ▼
Job Analyzer
      │
      ▼
Job Matcher
      │
      ▼
Skill Gap Analyzer
      │
      ▼
Resume Optimizer
      │
      ▼
Final Recommender
      │
      ▼
Structured AI Recommendation
```

Each agent has a focused responsibility instead of forcing one large LLM prompt to perform every task.

---

## 📌 Example Use Case

A candidate provides:

```text
Skills:
Python
FastAPI
LangChain

Experience:
Entry-level

Project:
AI Resume Copilot
```

A company provides a job requiring:

```text
Python
FastAPI
LangChain
RAG
Docker
```

The system can identify:

```text
Matched Skills:
Python
FastAPI
LangChain

Missing Skills:
RAG
Docker
```

The system can then recommend improvements such as:

```text
Priority Improvements:
- Develop practical RAG experience
- Learn Docker fundamentals
- Add RAG/Docker projects to the resume
```

---

## 🔐 Error Handling

The API includes error handling for situations such as:

- Invalid request data
- Invalid model responses
- LLM service failures
- Invalid match percentages
- Missing configuration
- Unexpected processing errors

When the Gemini service is unavailable, the API can return an appropriate service-unavailable response rather than exposing internal errors to the client.

---

## 🧩 Design Principles

The project follows several software engineering principles:

### Modular Architecture

Each AI capability is isolated into a separate module.

### Separation of Concerns

API routes, business logic, AI services, models, and orchestration are separated.

### Structured Outputs

Pydantic models are used to validate and structure AI-generated results.

### Testability

Individual components and API endpoints are covered by automated tests.

### Configuration Management

Sensitive configuration is stored using environment variables rather than hard-coded credentials.

### Extensibility

New agents and analysis capabilities can be added without redesigning the entire application.

---

## 🚧 Future Improvements

Potential future enhancements include:

- Resume PDF upload and parsing
- Job description PDF parsing
- DOCX resume support
- Resume-to-job similarity scoring
- Vector database integration
- RAG-based career recommendations
- Resume section rewriting
- ATS compatibility scoring
- Frontend dashboard
- Authentication and user accounts
- Persistent resume/job history
- Deployment to a cloud platform
- Monitoring and observability
- CI/CD pipeline

---

## 🎯 Project Goals

The main objective of Enterprise AI Resume Copilot is to demonstrate how Generative AI can be integrated into a real-world software application to provide structured, explainable, and actionable career recommendations.

The project combines:

```text
Generative AI
+
LLM Engineering
+
FastAPI
+
Agent-based Architecture
+
Pydantic
+
REST APIs
+
Automated Testing
```

---

## 👩‍💻 Author

**Lekhana**

B.Tech – Electronics and Communication Engineering

Interested in:

- Generative AI
- LLM Applications
- AI Engineering
- Python
- FastAPI
- Agentic AI
- RAG
- Prompt Engineering

---

## 📄 License

This project is intended for educational, portfolio, and demonstration purposes.
