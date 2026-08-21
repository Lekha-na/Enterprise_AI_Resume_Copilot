import pytest

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
            "skills": [""],
            "experience": [],
            "projects": [""],
            "education": "",
            "certifications": []
        },
        "job": {
            "job_title": "Generative AI Engineer",
            "company": "ABC Technologies",
            "description": "Build LLM Applications",
            "required_skills": [
                "Python"
            ],
            "preferred_skills": [],
            "required_experience": "1-2 Years",
            "responsibilities": [
                "Build LLM Applications"
            ]
        }
    }

    response = client.post("/analyze", json=payload)

    assert response.status_code == 422

def test_analyze_rejects_invalid_job():
    payload = {
        "candidate": {
            "name": "Lekhana",
            "skills": ["Python"],
            "experience": [],
            "projects": ["AI Resume Copilot"],
            "education": "B.Tech in Electronics and Communication Engineering",
            "certifications": []
        },
        "job": {
            "job_title": "",
            "company": "",
            "description": "",
            "required_skills": [],
            "preferred_skills": [],
            "required_experience": "",
            "responsibilities": []
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
        "app.orchestrator.resume_analysis.analyze_profile_agent",
        mock_profile
    )

    monkeypatch.setattr(
        "app.orchestrator.resume_analysis.analyze_job_agent",
        mock_job
    )

    monkeypatch.setattr(
        "app.orchestrator.resume_analysis.match_candidate",
        mock_match
    )

    monkeypatch.setattr(
        "app.orchestrator.resume_analysis.analyze_skill_gap",
        mock_skill_gap
    )

    monkeypatch.setattr(
        "app.orchestrator.resume_analysis.optimize_resume",
        mock_resume
    )

    monkeypatch.setattr(
        "app.orchestrator.resume_analysis.generate_final_recommendation",
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

def test_analyze_handles_ai_service_error(monkeypatch, caplog):

    def mock_profile(candidate):
        raise RuntimeError(
            "AI service temporarily unavailable. "
            "Please try again later."
        )

    monkeypatch.setattr(
        "app.orchestrator.resume_analysis.analyze_profile_agent",
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

    with caplog.at_level("ERROR"):
       response = client.post(
        "/analyze",
        json=payload
    )

    assert response.status_code == 503

    data = response.json()

    assert data["error"] == "AI service unavailable"

    assert "RuntimeError while processing POST /analyze" in caplog.text

    assert "temporarily unavailable" in data["message"]

def test_match_analysis_rejects_invalid_percentage():

    with pytest.raises(ValueError):
        MatchAnalysis(
            matched_skills=["Python"],
            missing_skills=["RAG"],
            match_percentage=150,
            overall_assessment="Invalid match."
        )

def test_final_recommendation_rejects_invalid_percentage():

    with pytest.raises(ValueError):
        FinalRecommendation(
            overall_match=150,
            application_recommendation="Invalid",
            key_strengths=["Python"],
            major_gaps=["RAG"],
            priority_improvements=["Learn RAG"]
        )

        def test_analyze_endpoint(monkeypatch):
            from app.main import app
            from fastapi.testclient import TestClient

            client = TestClient(app)

            def mock_analyze_resume(candidate, job):
                return {
                    "profile_analysis": {
                        "candidate_level": "Entry-Level",
                        "primary_domain": "Artificial Intelligence",
                        "years_experience": 0,
                        "key_skills": ["Python", "FastAPI", "LangChain"],
                        "project_summary": "Developed AI Resume Copilot.",
                        "education_summary": "B.Tech in Electronics and Communication Engineering",
                       "certification_summary": "None"
            },
            "job_analysis": {
                "required_skills": [
                    "Python",
                    "FastAPI",
                    "LangChain",
                    "RAG"
                ],
                "preferred_skills": ["Docker"],
                "required_experience": "1-2 years",
                "responsibilities": [
                    "Build LLM applications",
                    "Develop REST APIs"
                ]
            },
            "match_analysis": {
                "matched_skills": [
                    "Python",
                    "FastAPI",
                    "LangChain"
                ],
                "missing_skills": ["RAG", "Docker"],
                "match_percentage": 60,
                "overall_assessment": "Partial match."
            },
            "skill_gaps": [
                {
                    "skill": "RAG",
                    "importance": "High",
                    "reason": "Required for the job.",
                    "recommendation": "Build an end-to-end RAG project."
                }
            ],
            "resume_optimizations": [
                {
                    "section": "Projects",
                    "current_issue": "Project details are brief.",
                    "recommendation": "Expand project details.",
                    "reason": "Demonstrates practical skills."
                }
            ],
            "final_recommendation": {
                "overall_match": 60,
                "application_recommendation": "Apply after upskilling",
                "key_strengths": [
                    "Python",
                    "FastAPI",
                    "LangChain"
                ],
                "major_gaps": [
                    "RAG",
                    "Docker"
                ],
                "priority_improvements": [
                    "Build an end-to-end RAG project"
                ]
            }
        }

            monkeypatch.setattr(
   "app.main.analyze_resume", 
     mock_analyze_resume
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
        "company": "Test Company",
        "description": "Build LLM applications",
        "required_skills": [
                "Python",
                "FastAPI",
                "LangChain",
                "RAG"
            ],
            "preferred_skills": ["Docker"],
            "required_experience": "1-2 years",
            "responsibilities": [
                "Build LLM applications",
                "Develop REST APIs"
            ]
     }
}
            response = client.post(
                       "/analyze",
                        json=payload
                )
            assert response.status_code == 200

            data = response.json() 
            assert "profile_analysis" in data
            assert "job_analysis" in data
            assert "match_analysis" in data
            assert "skill_gaps" in data
            assert "resume_optimizations" in data
            assert "final_recommendation" in data

            assert data["match_analysis"]["match_percentage"] == 60