from app.models.profile import CandidateProfile,ProfileAnalysis
from app.services.llm_service import ask_gemini

def build_profile_analysis_prompt(profile: CandidateProfile) -> str:
    return f"""
You are a professional resume profile analyzer.

Analyze the following candidate profile:

Name: {profile.name}

Skills:
{profile.skills}

Experience:
{profile.experience}

Projects:
{profile.projects}

Education:
{profile.education}

Certifications:
{profile.certifications}

Determine:
1. The candidate's career level.
2. The candidate's primary professional domain.
3. Estimated years of professional experience.
4. The candidate's most important skills.
5. A concise summary of the projects.
6. A concise summary of the education.
7. A concise summary of certifications.

Return only the structured information requested.
Do not return Markdown.
Do not add headings, explanations, or commentary outside the requested fields.ss
"""
def analyze_profile(profile: CandidateProfile):
    prompt = build_profile_analysis_prompt(profile)

    result = ask_gemini(prompt, ProfileAnalysis)

    return result

if __name__ == "__main__":
    test_profile = CandidateProfile(
        name="Test Candidate",
        skills=["Python", "FastAPI", "LangChain"],
        experience=[],
        projects=["AI Resume Copilot"],
        education="B.Tech in Electronics and Communication Engineering",
        certifications=[]
    )

    analysis = analyze_profile(test_profile)

    print("\n--- PROFILE ANALYSIS ---")
    print(analysis)
