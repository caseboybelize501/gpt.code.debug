import requests
from typing import List, Dict
import json


class RepoScanner:
    def __init__(self):
        self.github_token = "your_github_token"
        self.headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def scan_github_repos(self) -> List[Dict]:
        print("Scanning GitHub repositories...")
        
        # Mock data - in real implementation, this would call GitHub API
        repos = [
            {
                "name": "project1",
                "last_commit": "2023-01-01T00:00:00Z",
                "language": "Python",
                "stars": 100,
                "url": "https://github.com/user/project1"
            },
            {
                "name": "project2",
                "last_commit": "2023-02-01T00:00:00Z",
                "language": "JavaScript",
                "stars": 200,
                "url": "https://github.com/user/project2"
            }
        ]
        
        # Compare with already_in_progress_repos
        already_in_progress = self.get_already_in_progress()
        missing_repos = [repo for repo in repos if repo["name"] not in already_in_progress]
        
        # Write RepoJobQueue
        self.write_repo_job_queue(missing_repos)
        
        return missing_repos

    def get_already_in_progress(self) -> List[str]:
        # Mock implementation - would read from database or file
        return ["existing_project"]

    def write_repo_job_queue(self, repos: List[Dict]):
        with open("repo_job_queue.json", "w") as f:
            json.dump(repos, f, indent=2)
        print(f"Wrote {len(repos)} jobs to queue")