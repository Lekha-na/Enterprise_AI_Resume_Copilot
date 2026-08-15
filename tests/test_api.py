from fastapi.testclient import TestClient

from app.main import app
from app.models.profile import ProfileAnalysis
from app.models.job import JobAnalysis
from app.models.match import MatchAnalysis
from app.models.skill_gap import SkillGap
from app.models.resume_optimization import ResumeOptimization
from app.models.recommendation import FinalRecommendation

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Enterprise AI Resume Copilot is running"

def test_analyze_rejects_invalid_candidate():
    payload = {
        "candidate": {
            "name": "",
            "skills": [],
            "experience": [],
            "projects": [],
            "education": "",
            "certifications": []
        },
        "job": {
            "job_title": "Generative AI Engineer",
            "company": "ABC Technologies",
            "description": "Build LLM applications",
            "required_skills": [
                "Python"
            ],
            "preferred_skills": [],
            "required_experience": "1-2 years",
            "responsibilities": [
                "Build LLM applications"
            ]
        }
    }

    response = client.post("/analyze", json=payload)

    assert response.status_code == 422

def test_analyze_valid_request(monkeypatch):

    def mock_profile(candidate):
        return ProfileAnalysis(
            candidate_level="Entry-level",
            primary_domain="Artificial Intelligence",
            years_experience=0,
            key_skills=["Python", "FastAPI", "LangChain"],
            project_summary="Developed AI Resume Copilot.",
            education_summary="B.Tech in Electronics and Communication Engineering",
            certification_summary="None"
        )

    def mock_job(job):
        return JobAnalysis(
            required_skills=[
                "Python",
                "FastAPI",
                "LangChain",
                "RAG",
                "Vector Databases"
            ],
            preferred_skills=["Docker", "AWS"],
            required_experience="1-2 years",
            responsibilities=[
                "Build LLM applications",
                "Develop REST APIs",
                "Implement RAG pipelines",
                "Work with AI systems"
            ]
        )

    def mock_match(profile, job):
        return MatchAnalysis(
            matched_skills=[
                "Python",
                "FastAPI",
                "LangChain"
            ],
            missing_skills=[
                "RAG",
                "Vector Databases",
                "Docker",
                "AWS"
            ],
            match_percentage=42.86,
            overall_assessment="Partial match."
        )

    def mock_skill_gap(missing_skills, job):
        return [
            SkillGap(
                skill="RAG",
                importance="High",
                reason="Required for the job.",
                recommendation="Build an end-to-end RAG project."
            )
        ]

    def mock_resume(profile, job):
        return [
            ResumeOptimization(
                section="Projects",
                current_issue="Project details are brief.",
                recommendation="Expand the project details.",
                reason="Shows practical technical skills."
            )
        ]

    def mock_recommendation(
        profile,
        job,
        match,
        skill_gaps,
        resume_optimizations
    ):
        return FinalRecommendation(
            overall_match=42.86,
            application_recommendation="Do Not Apply Yet",
            key_strengths=[
                "Python",
                "FastAPI",
                "LangChain"
            ],
            major_gaps=[
                "RAG",
                "Vector Databases"
            ],
            priority_improvements=[
                "Build an end-to-end RAG project"
            ]
        )

    monkeypatch.setattr(
        "app.main.analyze_profile_agent",
        mock_profile
    )

    monkeypatch.setattr(
        "app.main.analyze_job_agent",
        mock_job
    )

    monkeypatch.setattr(
        "app.main.match_candidate",
        mock_match
    )

    monkeypatch.setattr(
        "app.main.analyze_skill_gap",
        mock_skill_gap
    )

    monkeypatch.setattr(
        "app.main.optimize_resume",
        mock_resume
    )

    monkeypatch.setattr(
        "app.main.generate_final_recommendation",
        mock_recommendation
    )

    payload = {
        "candidate": {
            "name": "Lekhana",
            "skills": [
                "Python",
                "FastAPI",
                "LangChain"
            ],
            "experience": [],
            "projects": [
                "AI Resume Copilot"
            ],
            "education": "B.Tech in Electronics and Communication Engineering",
            "certifications": []
        },
        "job": {
            "job_title": "Generative AI Engineer",
            "company": "ABC Technologies",
            "description": "Build LLM applications",
            "required_skills": [
                "Python",
                "FastAPI",
                "LangChain",
                "RAG",
                "Vector Databases"
            ],
            "preferred_skills": [
                "Docker",
                "AWS"
            ],
            "required_experience": "1-2 years",
            "responsibilities": [
                "Build LLM applications",
                "Develop REST APIs",
                "Implement RAG pipelines",
                "Work with AI systems"
            ]
        }
    }

    response = client.post("/analyze", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "profile_analysis" in data
    assert "job_analysis" in data
    assert "match_analysis" in data
    assert "skill_gaps" in data
    assert "resume_optimizations" in data
    assert "final_recommendation" in data

    assert data["match_analysis"]["match_percentage"] == 42.86

def test_analyze_profile(monkeypatch):

    def mock_profile(candidate):
        return ProfileAnalysis(
            candidate_level="Entry-level",
            primary_domain="Artificial Intelligence",
            years_experience=0,
            key_skills=["Python", "FastAPI", "LangChain"],
            project_summary="Developed AI Resume Copilot.",
            education_summary="B.Tech in Electronics and Communication Engineering",
            certification_summary="None"
        )

    monkeypatch.setattr(
        "app.main.analyze_profile_agent",
        mock_profile
    )

    payload = {
        "name": "Lekhana",
        "skills": [
            "Python",
            "FastAPI",
            "LangChain"
        ],
        "experience": [],
        "projects": [
            "AI Resume Copilot"
        ],
        "education": "B.Tech in Electronics and Communication Engineering",
        "certifications": []
    }

    response = client.post(
        "/analyze-profile",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["candidate_level"] == "Entry-level"
    assert data["primary_domain"] == "Artificial Intelligence"
    assert data["years_experience"] == 0

def test_analyze_job(monkeypatch):

    def mock_job(job):
        return JobAnalysis(
            required_skills=[
                "Python",
                "FastAPI",
                "LangChain",
                "RAG",
                "Vector Databases"
            ],
            preferred_skills=[
                "Docker",
                "AWS"
            ],
            required_experience="1-2 years",
            responsibilities=[
                "Build LLM applications",
                "Develop REST APIs",
                "Implement RAG pipelines",
                "Work with AI systems"
            ]
        )

    monkeypatch.setattr(
        "app.main.analyze_job_agent",
        mock_job
    )

    payload = {
        "job_title": "Generative AI Engineer",
        "company": "ABC Technologies",
        "description": "Build LLM applications",
        "required_skills": [
            "Python",
            "FastAPI",
            "LangChain",
            "RAG",
            "Vector Databases"
        ],
        "preferred_skills": [
            "Docker",
            "AWS"
        ],
        "required_experience": "1-2 years",
        "responsibilities": [
            "Build LLM applications",
            "Develop REST APIs",
            "Implement RAG pipelines",
            "Work with AI systems"
        ]
    }

    response = client.post(
        "/analyze-job",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "required_skills" in data
    assert "preferred_skills" in data
    assert "required_experience" in data
    assert "responsibilities" in data

    assert "Python" in data["required_skills"]
    assert data["required_experience"] == "1-2 years"

def test_analyze_match(monkeypatch):

    def mock_profile(candidate):
        return ProfileAnalysis(
            candidate_level="Entry-level",
            primary_domain="Artificial Intelligence",
            years_experience=0,
            key_skills=["Python", "FastAPI", "LangChain"],
            project_summary="Developed AI Resume Copilot.",
            education_summary="B.Tech in Electronics and Communication Engineering",
            certification_summary="None"
        )

    def mock_job(job):
        return JobAnalysis(
            required_skills=[
                "Python",
                "FastAPI",
                "LangChain",
                "RAG",
                "Vector Databases"
            ],
            preferred_skills=["Docker", "AWS"],
            required_experience="1-2 years",
            responsibilities=[
                "Build LLM applications",
                "Develop REST APIs",
                "Implement RAG pipelines",
                "Work with AI systems"
            ]
        )

    def mock_match(profile, job):
        return MatchAnalysis(
            matched_skills=[
                "Python",
                "FastAPI",
                "LangChain"
            ],
            missing_skills=[
                "RAG",
                "Vector Databases",
                "Docker",
                "AWS"
            ],
            match_percentage=42.86,
            overall_assessment="Partial match."
        )

    monkeypatch.setattr(
        "app.main.analyze_profile_agent",
        mock_profile
    )

    monkeypatch.setattr(
        "app.main.analyze_job_agent",
        mock_job
    )

    monkeypatch.setattr(
        "app.main.match_candidate",
        mock_match
    )

    payload = {
        "candidate": {
            "name": "Lekhana",
            "skills": [
                "Python",
                "FastAPI",
                "LangChain"
            ],
            "experience": [],
            "projects": [
                "AI Resume Copilot"
            ],
            "education": "B.Tech in Electronics and Communication Engineering",
            "certifications": []
        },
        "job": {
            "job_title": "Generative AI Engineer",
            "company": "ABC Technologies",
            "description": "Build LLM applications",
            "required_skills": [
                "Python",
                "FastAPI",
                "LangChain",
                "RAG",
                "Vector Databases"
            ],
            "preferred_skills": [
                "Docker",
                "AWS"
            ],
            "required_experience": "1-2 years",
            "responsibilities": [
                "Build LLM applications",
                "Develop REST APIs",
                "Implement RAG pipelines",
                "Work with AI systems"
            ]
        }
    }

    response = client.post(
        "/analyze-match",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["match_percentage"] == 42.86

    assert "Python" in data["matched_skills"]

    assert "RAG" in data["missing_skills"]

    assert "overall_assessment" in data

def test_analyze_handles_ai_service_error(monkeypatch):

    def mock_profile(candidate):
        raise RuntimeError(
            "AI service temporarily unavailable. "
            "Please try again later."
        )

    monkeypatch.setattr(
        "app.main.analyze_profile_agent",
        mock_profile
    )

    payload = {
        "candidate": {
            "name": "Lekhana",
            "skills": [
                "Python",
                "FastAPI",
                "LangChain"
            ],
            "experience": [],
            "projects": [
                "AI Resume Copilot"
            ],
            "education": "B.Tech in Electronics and Communication Engineering",
            "certifications": []
        },
        "job": {
            "job_title": "Generative AI Engineer",
            "company": "ABC Technologies",
            "description": "Build LLM applications",
            "required_skills": [
                "Python",
                "FastAPI",
                "LangChain"
            ],
            "preferred_skills": [],
            "required_experience": "1-2 years",
            "responsibilities": [
                "Build LLM applications"
            ]
        }
    }

    response = client.post(
        "/analyze",
        json=payload
    )

    assert response.status_code == 503

    data = response.json()

    assert data["error"] == "AI service unavailable"

    assert "temporarily unavailable" in data["message"]