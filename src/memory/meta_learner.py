import chromadb
import json
from typing import List, Dict
from datetime import datetime


class MetaLearner:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("meta_learner")

    def update_metrics(self, test_results: List[Dict]):
        print("Updating meta-learning metrics...")
        
        metrics = [
            {
                "build_strategy": "docker_isolation",
                "language": "python",
                "framework": "fastapi",
                "execution_time": 120,
                "bug_fix_success_rate": 0.95,
                "timestamp": datetime.now().isoformat()
            },
            {
                "build_strategy": "multi_stage_build",
                "language": "node",
                "framework": "express",
                "execution_time": 80,
                "bug_fix_success_rate": 0.85,
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        for metric in metrics:
            self.collection.add(
                documents=[json.dumps(metric)],
                ids=[f"{metric['build_strategy']}_{metric['language']}_{datetime.now().strftime('%Y%m%d')}"],
                metadatas=[metric]
            )

    def get_optimization_recommendations(self) -> List[Dict]:
        results = self.collection.query(
            query_texts=["optimization"],
            n_results=5
        )
        
        return [json.loads(doc) for doc in results["documents"][0]]