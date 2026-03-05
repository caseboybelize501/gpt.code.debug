import docker
import subprocess
from typing import Dict, List
import time

class SandboxRunner:
    def __init__(self):
        self.docker_client = docker.from_env()
        
    def run_in_sandbox(self, container_name: str, command: str) -> Dict:
        try:
            # Create and start container
            container = self.docker_client.containers.run(
                image="python:3.9",
                command=command,
                detach=True,
                name=container_name
            )
            
            # Wait for completion
            result = container.wait()
            logs = container.logs().decode('utf-8')
            
            # Clean up
            container.remove()
            
            return {
                "success": result["StatusCode"] == 0,
                "exit_code": result["StatusCode"],
                "logs": logs
            }
        except Exception as e:
            print(f"Error running in sandbox: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def run_multiple_tests(self, test_cases: List[Dict]) -> List[Dict]:
        results = []
        
        for test_case in test_cases:
            result = self.run_in_sandbox(
                container_name=test_case["name"],
                command=test_case["command"]
            )
            result["test_name"] = test_case["name"]
            results.append(result)
        
        return results

    def resolve_dependencies(self, project_path: str) -> bool:
        try:
            # Mock dependency resolution
            print(f"Resolving dependencies for {project_path}")
            return True
        except Exception as e:
            print(f"Error resolving dependencies: {e}")
            return False