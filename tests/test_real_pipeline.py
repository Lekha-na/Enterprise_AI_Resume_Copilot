from app.orchestrator.resume_analysis import analyze_resume


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

print("\n========== PROFILE ANALYSIS ==========")
print(result.profile_analysis)

print("\n========== JOB ANALYSIS ==========")
print(result.job_analysis)

print("\n========== MATCH ANALYSIS ==========")
print(result.match_analysis)

print("\n========== SKILL GAPS ==========")
print(result.skill_gaps)

print("\n========== RESUME OPTIMIZATIONS ==========")
print(result.resume_optimizations)

print("\n========== FINAL RECOMMENDATION ==========")
print(result.final_recommendation)