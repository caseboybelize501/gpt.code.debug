import subprocess
import os
from typing import List, Dict
import docker


class StackBuilder:
    def __init__(self):
        self.docker_client = docker.from_env()
        
    def build_environments(self, repo_jobs: List[Dict], toolchain_map: Dict[str, List[Dict]]):
        print("Building environments for missing projects...")
        
        languages = ["python", "node", "go", "java", "cpp", "rust", "swift"]
        
        for job in repo_jobs:
            language = job.get("language", "unknown")
            if language.lower() in languages:
                self.build_language_environment(language, job)
            else:
                print(f"Unsupported language: {language}")

    def build_language_environment(self, language: str, repo_job: Dict):
        try:
            # Mock implementation - would actually build Docker containers
            print(f"Building environment for {language} project: {repo_job['name']}")
            
            # Create Dockerfile
            dockerfile_content = self.generate_dockerfile(language)
            with open("Dockerfile", "w") as f:
                f.write(dockerfile_content)
            
            # Build image
            print(f"Building Docker image for {language}...")
            
        except Exception as e:
            print(f"Error building environment for {language}: {e}")

    def generate_dockerfile(self, language: str) -> str:
        dockerfiles = {
            "python": "FROM python:3.9\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD [\"python\", \"main.py\"]",
            "node": "FROM node:18\nWORKDIR /app\nCOPY package.json .\nRUN npm install\nCOPY . .\nCMD [\"npm\", \"start\"]",
            "go": "FROM golang:1.19\nWORKDIR /app\nCOPY go.mod .\nRUN go mod download\nCOPY . .\nCMD [\"go\", \"run\", \"main.go\"]",
            "java": "FROM openjdk:17\nWORKDIR /app\nCOPY pom.xml .\nRUN mvn dependency:copy-dependencies\nCOPY . .\nCMD [\"java\", \"-cp\", \"target/classes:target/dependency/*\", \"Main\"]",
            "cpp": "FROM gcc:11\nWORKDIR /app\nCOPY . .\nRUN g++ -o main main.cpp\nCMD [\"./main\"]",
            "rust": "FROM rust:1.60\nWORKDIR /app\nCOPY Cargo.toml .\nRUN cargo build\nCOPY . .\nCMD [\"cargo\", \"run\"]",
            "swift": "FROM swift:5.7\nWORKDIR /app\nCOPY Package.swift .\nRUN swift package resolve\nCOPY . .\nCMD [\"swift\", \"run\"]"
        }
        
        return dockerfiles.get(language, "FROM alpine:latest\nWORKDIR /app\nCOPY . .\nCMD [\"echo\", \"Hello World\"]")