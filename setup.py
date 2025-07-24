# setup.py
from setuptools import setup, find_packages

setup(
    name="agno-qa-pipeline",  # nome do seu projeto/pacote
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "agno",
        "duckduckgo-search",
        "langchain",
        "pypdf",
        "unstructured",
        "python-docx",
        "faiss-cpu"
    ],
    include_package_data=True,
    description="Pipeline QA com Groq, FAISS e LangChain",
    author="Tobias Santos",
    author_email="seu-email@exemplo.com",
)
