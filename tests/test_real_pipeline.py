from app.orchestrator.resume_analysis import analyze_resume


def test_real_resume_pipeline():
    candidate = {
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

    job = {
        "job_title": "Generative AI Engineer",
        "company": "Test Company",
        "description": (
            "Build LLM applications using Python, FastAPI, "
            "RAG and vector databases."
        ),
        "required_skills": [
            "Python",
            "FastAPI",
            "LangChain",
            "RAG",
            "Vector Databases"
        ],
        "preferred_skills": [
            "Docker"
        ],
        "required_experience": "1-2 years",
        "responsibilities": [
            "Build LLM applications",
            "Develop REST APIs",
            "Implement RAG pipelines"
        ]
    }

    result = analyze_resume(candidate, job)

    assert result is not None
    assert result.profile_analysis is not None
    assert result.job_analysis is not None
    assert result.match_analysis is not None
    assert result.skill_gaps is not None
    assert result.resume_optimizations is not None
    assert result.final_recommendation is not None