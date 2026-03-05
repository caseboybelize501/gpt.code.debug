import os
import subprocess
from typing import Dict, List
import platform

class SystemScanner:
    def __init__(self):
        self.system = platform.system()
        
    def scan_system_drives(self) -> Dict[str, List[Dict]]:
        print("Scanning system drives...")
        
        # Mock implementation - would scan C:/ and D:/ drives
        toolchain_map = {
            "python": [
                {"version": "3.9.0", "path": "/usr/bin/python3", "license_ok": True},
                {"version": "3.10.0", "path": "/usr/local/bin/python3.10", "license_ok": True}
            ],
            "node": [
                {"version": "18.0.0", "path": "/usr/bin/node", "license_ok": True}
            ]
        }
        
        # Deduplicate stacks
        deduplicated = self.deduplicate_stacks(toolchain_map)
        
        # Save to file
        with open("toolchain_map.json", "w") as f:
            import json
            json.dump(deduplicated, f, indent=2)
        
        return deduplicated

    def deduplicate_stacks(self, toolchain_map: Dict[str, List[Dict]]) -> Dict[str, List[Dict]]:
        # Mock implementation - would actually deduplicate based on version and path
        return toolchain_map

    def scan_docker_images(self) -> List[Dict]:
        try:
            result = subprocess.run(["docker", "images", "--format", "json"], 
                                  capture_output=True, text=True)
            images = json.loads(result.stdout)
            return images
        except Exception as e:
            print(f"Error scanning Docker images: {e}")
            return []