import chromadb
import json
from typing import List, Dict
from datetime import datetime


class SandboxVerification:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("sandbox_verification")

    def store_results(self, test_results: List[Dict]):
        print("Storing sandbox verification results...")
        
        for result in test_results:
            doc = {
                "repo": result["name"],
                "test_suite": "unit_integration",
                "coverage": result.get("coverage", 0.0),
                "regressions": [],
                "resource_metrics": {
                    "cpu_usage": 0.5,
                    "memory_usage": 128,
                    "disk_usage": 50
                },
                "timestamp": datetime.now().isoformat()
            }
            
            self.collection.add(
                documents=[json.dumps(doc)],
                ids=[f"{result['name']}_{datetime.now().strftime('%Y%m%d')}"],
                metadatas=[doc]
            )

    def get_verification_report(self, repo_name: str) -> Dict:
        results = self.collection.query(
            query_texts=[repo_name],
            n_results=1
        )
        
        if results["documents"] and len(results["documents"][0]) > 0:
            return json.loads(results["documents"][0][0])
        
        return {}