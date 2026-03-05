import chromadb
import json
from typing import List, Dict
from datetime import datetime


class RepoDependencyGraph:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("repo_dependency_graph")

    def update(self, repos: List[Dict]):
        print("Updating repository dependency graph...")
        
        for repo in repos:
            doc = {
                "repo_name": repo["name"],
                "language": repo["language"],
                "dependencies": [],
                "last_build_status": "success",
                "known_issues": [],
                "timestamp": datetime.now().isoformat()
            }
            
            self.collection.add(
                documents=[json.dumps(doc)],
                ids=[repo["name"]]
            )

    def get_repo_info(self, repo_name: str) -> Dict:
        results = self.collection.query(
            query_texts=[repo_name],
            n_results=1
        )
        
        if results["documents"] and len(results["documents"][0]) > 0:
            return json.loads(results["documents"][0][0])
        
        return {}

    def find_similar_repos(self, repo_name: str, limit: int = 5) -> List[Dict]:
        results = self.collection.query(
            query_texts=[repo_name],
            n_results=limit
        )
        
        return [json.loads(doc) for doc in results["documents"][0]]