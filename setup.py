from setuptools import setup
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "Abhiraj_Mayuri_Kanishka"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/mayuri41/bookRecommendationSystem.git",
    author_email="surwasemayuri41@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)