import chromadb
import json
from typing import List, Dict
from datetime import datetime


class CrossStackPatterns:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("cross_stack_patterns")

    def extract_and_store(self, test_results: List[Dict]):
        print("Extracting and storing cross-stack patterns...")
        
        patterns = [
            {
                "language": "python",
                "pattern_type": "dependency_resolution",
                "dependency_resolve": "pipenv",
                "fix_applied": "resolved version conflicts",
                "runtime_gain": 0.2,
                "timestamp": datetime.now().isoformat()
            },
            {
                "language": "node",
                "pattern_type": "performance_optimization",
                "dependency_resolve": "caching",
                "fix_applied": "reduced response time",
                "runtime_gain": 0.3,
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        for pattern in patterns:
            self.collection.add(
                documents=[json.dumps(pattern)],
                ids=[f"{pattern['language']}_{pattern['pattern_type']}_{datetime.now().strftime('%Y%m%d')}"],
                metadatas=[pattern]
            )

    def find_optimization_patterns(self, language: str) -> List[Dict]:
        results = self.collection.query(
            query_texts=[language],
            n_results=5
        )
        
        return [json.loads(doc) for doc in results["documents"][0]]