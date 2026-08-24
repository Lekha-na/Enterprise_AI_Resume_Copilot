# 🚀 Enterprise AI Resume Copilot

### AI-Powered Resume Analysis & Job Matching System

Enterprise AI Resume Copilot is a **Generative AI-powered application** that analyzes candidate profiles and job descriptions, evaluates candidate-job compatibility, identifies skill gaps, provides resume optimization suggestions, and generates actionable career recommendations.

The application is built with **Python, FastAPI, Google Gemini, LangChain, Pydantic, and Uvicorn**, and is deployed as a production API on **Render**.

---

## 🌐 Live Demo

### 🚀 Production API

**https://enterprise-ai-resume-copilot.onrender.com**

### 📚 Interactive API Documentation

**https://enterprise-ai-resume-copilot.onrender.com/docs**

The Swagger UI provides an interactive interface for testing all available API endpoints.

---

## ✨ Key Features

* 🤖 AI-powered candidate profile analysis
* 📄 Intelligent job description analysis
* 🎯 Candidate-job matching
* 📊 Match percentage calculation
* 🔍 Skill gap identification
* 📝 AI-powered resume optimization
* 💡 Final career recommendations
* 🔗 REST API using FastAPI
* 📚 Interactive Swagger/OpenAPI documentation
* 🧩 Modular AI-agent architecture
* 🧪 Automated testing with Pytest
* 📈 Code coverage analysis
* ☁️ Cloud deployment using Render

---

## 🏗️ System Architecture

![Enterprise AI Resume Copilot Architecture](docs/screenshots/Architecture.png)

The system follows a modular AI-analysis architecture.

```text
                    ┌────────────────────────┐
                    │    Candidate Profile   │
                    │ Skills / Experience    │
                    │ Projects / Education   │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │      FastAPI API       │
                    │        Layer           │
                    └───────────┬────────────┘
                                │
                                ▼
             ┌────────────────────────────────────┐
             │        AI ANALYSIS PIPELINE         │
             │                                    │
             │  ┌──────────────────────────────┐  │
             │  │      Profile Analyzer        │  │
             │  └──────────────┬───────────────┘  │
             │                 ▼                  │
             │  ┌──────────────────────────────┐  │
             │  │        Job Analyzer          │  │
             │  └──────────────┬───────────────┘  │
             │                 ▼                  │
             │  ┌──────────────────────────────┐  │
             │  │        Job Matcher            │  │
             │  └──────────────┬───────────────┘  │
             │                 ▼                  │
             │  ┌──────────────────────────────┐  │
             │  │      Skill Gap Analyzer      │  │
             │  └──────────────┬───────────────┘  │
             │                 ▼                  │
             │  ┌──────────────────────────────┐  │
             │  │      Resume Optimizer        │  │
             │  └──────────────┬───────────────┘  │
             │                 ▼                  │
             │  ┌──────────────────────────────┐  │
             │  │     Final Recommender        │  │
             │  └──────────────┬───────────────┘  │
             └─────────────────┼──────────────────┘
                               │
                               ▼
                    ┌────────────────────────┐
                    │    Google Gemini LLM   │
                    │    Service             │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ Comprehensive Analysis │
                    │        Report          │
                    └────────────────────────┘
```

---

## 🔄 Workflow

The complete AI Resume Copilot workflow consists of six major stages.

### 1️⃣ Profile Analysis

The Profile Analyzer processes the candidate information and extracts:

* Candidate level
* Primary domain
* Years of experience
* Key skills
* Project information
* Education
* Certifications

### 2️⃣ Job Analysis

The Job Analyzer processes the target job description and extracts:

* Required skills
* Preferred skills
* Experience requirements
* Job responsibilities
* Key job requirements

### 3️⃣ Candidate-Job Matching

The Job Matcher compares the candidate profile against the analyzed job requirements.

It identifies:

* Matching skills
* Missing skills
* Candidate-job match percentage

### 4️⃣ Skill Gap Analysis

The Skill Gap Analyzer identifies the skills that the candidate needs to improve to better qualify for the target role.

### 5️⃣ Resume Optimization

The Resume Optimizer generates AI-powered suggestions to improve the candidate's resume and align it more closely with the target job.

### 6️⃣ Final Recommendation

The Final Recommender combines all analysis results and produces:

* Overall recommendation
* Candidate suitability
* Improvement areas
* Suggested action plan

---

## 🧠 AI Pipeline

```text
Candidate Profile
        │
        ▼
Profile Analyzer
        │
        ▼
Job Description ──────► Job Analyzer
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
                   Final AI Recommendation
```

---

## 🛠️ Technology Stack

| Technology      | Purpose                     |
| --------------- | --------------------------- |
| 🐍 Python       | Core programming language   |
| ⚡ FastAPI       | REST API framework          |
| ✨ Google Gemini | Generative AI / LLM         |
| 🔗 LangChain    | LLM application framework   |
| 📦 Pydantic     | Data validation and schemas |
| 🚀 Uvicorn      | ASGI application server     |
| 🧪 Pytest       | Automated testing           |
| 📈 pytest-cov   | Code coverage               |
| 🐙 GitHub       | Version control             |
| ☁️ Render       | Cloud deployment            |

---

## 📁 Project Structure

```text
Enterprise_AI_Resume_Copilot/
│
├── app/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── profile_analyzer.py
│   │   ├── job_analyzer.py
│   │   ├── job_matcher.py
│   │   ├── skill_gap_analyzer.py
│   │   ├── resume_optimizer.py
│   │   └── final_recommender.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── logging_config.py
│   │   └── settings.py
│   │
│   ├── models/
│   │   ├── analyze_response.py
│   │   ├── job.py
│   │   ├── match.py
│   │   ├── match_request.py
│   │   ├── profile.py
│   │   ├── recommendation.py
│   │   ├── resume_optimization.py
│   │   └── skill_gap.py
│   │
│   ├── orchestrator/
│   │   └── resume_analysis.py
│   │
│   ├── services/
│   │   └── llm_service.py
│   │
│   └── main.py
│
├── tests/
│
├── docs/
│   └── screenshots/
│       ├── architecture.png
│       ├── swagger.png
│       ├── render-deployment.png
│       └── analysis-response.png
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Lekha-na/Enterprise_AI_Resume_Copilot.git
cd Enterprise_AI_Resume_Copilot
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

**Important:** Never upload your actual API key to GitHub.

Make sure `.env` is included in `.gitignore`.

## 6. Run the Application

```bash
uvicorn app.main:app --reload
```

The local API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoints

## Health Check

```http
GET /
```

Checks whether the API is running.

---

## Analyze Candidate Profile

```http
POST /analyze-profile
```

Analyzes candidate information and generates structured profile insights.

---

## Analyze Job Description

```http
POST /analyze-job
```

Analyzes a job description and extracts important job requirements.

---

## Analyze Candidate-Job Match

```http
POST /analyze-match
```

Compares candidate skills against job requirements and generates matching information.

---

## Complete Resume Analysis

```http
POST /analyze
```

Runs the complete AI Resume Copilot pipeline.

```text
Profile Analysis
       ↓
Job Analysis
       ↓
Job Matching
       ↓
Skill Gap Analysis
       ↓
Resume Optimization
       ↓
Final Recommendation
```

---

# 📊 Example API Request

The `/analyze` endpoint accepts candidate and job information.

```json
{
  "candidate": {
    "name": "Alex Johnson",
    "skills": [
      "Python",
      "FastAPI",
      "LangChain",
      "RAG",
      "Google Gemini",
      "Prompt Engineering"
    ],
    "experience": [
      "Developed AI-powered applications using Python and FastAPI"
    ],
    "projects": [
      "Enterprise AI Resume Copilot"
    ],
    "education": "B.Tech in Electronics and Communication Engineering",
    "certifications": [
      "Generative AI Certification"
    ]
  },
  "job": {
    "job_title": "Generative AI Engineer",
    "company": "Tech Innovations",
    "description": "Develop and deploy AI-powered applications using modern LLM technologies.",
    "required_skills": [
      "Python",
      "FastAPI",
      "LangChain",
      "RAG"
    ],
    "preferred_skills": [
      "Google Gemini",
      "Vector Databases",
      "Prompt Engineering"
    ],
    "required_experience": "0-2 years",
    "responsibilities": [
      "Develop LLM-powered applications",
      "Build RAG pipelines",
      "Develop REST APIs",
      "Optimize AI workflows"
    ]
  }
}
```

---

# 📤 API Response

The complete analysis response contains:

```text
Profile Analysis
├── Candidate Level
├── Primary Domain
├── Years of Experience
├── Key Skills
└── Project Summary

Job Analysis
├── Required Skills
├── Preferred Skills
├── Experience Requirements
└── Responsibilities

Match Analysis
├── Match Percentage
├── Matched Skills
└── Missing Skills

Skill Gap Analysis
├── Missing Skills
└── Improvement Areas

Resume Optimization
└── Resume Improvement Suggestions

Final Recommendation
├── Recommendation
└── Action Plan
```

---

# 🧪 Testing

The application is tested using **Pytest**.

## Test Execution

```bash
pytest
```

### Test Result

```text
15 passed, 1 warning in 18.77s
```

## Code Coverage

The project currently achieves **87% overall code coverage**.

```text
TOTAL    242 statements
MISSED    32 statements
COVERAGE  87%
```

### Coverage Summary

| Component             | Coverage |
| --------------------- | -------: |
| Profile Analyzer      |      69% |
| Settings              |      90% |
| LLM Service           |      90% |
| API Routes            |       0% |
| Other core components |     100% |
| **Overall**           |  **87%** |

The automated test suite successfully passed all **15 tests**.

---

# ☁️ Deployment

The application is deployed on **Render** as a production FastAPI web service.

## Production URL

https://enterprise-ai-resume-copilot.onrender.com

## Swagger Documentation

https://enterprise-ai-resume-copilot.onrender.com/docs

## Deployment Flow

```text
GitHub Repository
        │
        ▼
      Render
        │
        ▼
Python / FastAPI Application
        │
        ▼
     Uvicorn
        │
        ▼
Google Gemini API
        │
        ▼
AI Resume Analysis
        │
        ▼
     JSON Response
```

---

# 📸 Screenshots

## 🏗️ System Architecture

![Enterprise AI Resume Copilot Architecture](docs/screenshots/architecture.png)

---

## 📚 Swagger API Documentation

![Swagger API Documentation](docs/screenshots/swagger.png)

The Swagger interface allows users to interactively test the available API endpoints.

---

## ☁️ Render Deployment

![Render Deployment](docs/screenshots/render-deployment.png)

The application has been successfully deployed and is accessible through the production URL.

---

## 🤖 Complete AI Resume Analysis

![AI Resume Analysis Response](docs/screenshots/analysis-response.png)

The `/analyze` endpoint returns the complete AI-generated resume and job analysis.

---

# 🔐 Environment Variables

The application requires the following environment variable:

| Variable         | Description           |
| ---------------- | --------------------- |
| `GEMINI_API_KEY` | Google Gemini API key |

For security:

* Never commit `.env` to GitHub.
* Never expose API keys in source code.
* Use Render Environment Variables for production secrets.

---

# 🎯 Project Objectives

The main objective of Enterprise AI Resume Copilot is to automate the resume-to-job analysis process using Generative AI.

The system addresses several common challenges faced by job seekers:

* Understanding complex job descriptions
* Comparing resumes against job requirements
* Identifying missing technical skills
* Optimizing resumes for specific positions
* Generating personalized recommendations

---

# 🌟 Key Benefits

### 🎯 Accurate Job Matching

Evaluates how closely a candidate's profile aligns with a target job.

### 🔍 Skill Gap Identification

Identifies missing skills and potential improvement areas.

### 📝 Resume Optimization

Provides AI-powered suggestions for improving resume alignment.

### ⚡ Automated Analysis

Combines multiple analysis stages into a single API workflow.

### 💡 Actionable Recommendations

Provides a final recommendation and suggested next steps.

---

# 🔮 Future Enhancements

Planned or potential improvements include:

* 📄 Resume PDF upload and parsing
* 🔗 Job description URL extraction
* 🎯 ATS score prediction
* 🔄 Multiple job comparison
* 📚 Personalized learning recommendations
* 👤 User authentication
* 💾 Persistent candidate profiles
* 🧠 Advanced vector database semantic search
* 📑 Resume version management
* 📊 Analytics dashboard
* 🖥️ Dedicated frontend application
* 🔐 API authentication and authorization

---

# 📈 Future Architecture

```text
                    ┌──────────────────┐
                    │  Web Dashboard   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     FastAPI      │
                    │    REST API      │
                    └────────┬─────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       ┌──────────────┐             ┌──────────────┐
       │ AI Agents    │             │ Vector DB    │
       └──────┬───────┘             └──────┬───────┘
              │                             │
              └──────────────┬──────────────┘
                             ▼
                    ┌──────────────────┐
                    │  Google Gemini   │
                    │       LLM        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Career Insights  │
                    │ & Recommendations│
                    └──────────────────┘
```

---

# 🧩 Design Principles

The application follows several software engineering principles:

* **Modular architecture**
* **Separation of concerns**
* **Reusable AI agents**
* **Structured Pydantic models**
* **RESTful API design**
* **Environment-based configuration**
* **Automated testing**
* **Cloud deployment**
* **Secure API key management**

---

# 👩‍💻 Author

## Lekhana

**B.Tech — Electronics & Communication Engineering**

### Areas of Interest

* Generative AI
* Large Language Models
* Prompt Engineering
* AI Engineering
* Python
* FastAPI
* RAG
* LLM Applications

---

# 📄 License

This project is intended for **educational, portfolio, and demonstration purposes**.

---

## ⭐ If You Find This Project Interesting

Feel free to explore the repository, test the live API, and experiment with the AI-powered resume analysis workflow.
