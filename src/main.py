import os
import sys
from dotenv import load_dotenv
from bootstrap.repo_scanner import RepoScanner
from bootstrap.system_scanner import SystemScanner
from bootstrap.stack_builder import StackBuilder
from bootstrap.sandbox_runner import SandboxRunner
from bootstrap.test_runner import TestRunner
from bootstrap.dependency_resolver import DependencyResolver
from agents.deploy_agent import DeployAgent
from agents.learn_agent import LearnAgent
from memory.repo_dependency_graph import RepoDependencyGraph
from memory.cross_stack_patterns import CrossStackPatterns
from memory.sandbox_verification import SandboxVerification
from memory.meta_learner import MetaLearner

class GPTCodeDebug:
    def __init__(self):
        load_dotenv()
        self.repo_scanner = RepoScanner()
        self.system_scanner = SystemScanner()
        self.stack_builder = StackBuilder()
        self.sandbox_runner = SandboxRunner()
        self.test_runner = TestRunner()
        self.dependency_resolver = DependencyResolver()
        self.deploy_agent = DeployAgent()
        self.learn_agent = LearnAgent()
        self.repo_dependency_graph = RepoDependencyGraph()
        self.cross_stack_patterns = CrossStackPatterns()
        self.sandbox_verification = SandboxVerification()
        self.meta_learner = MetaLearner()

    def run(self):
        print("Starting GPT.Code.Debug Autonomous Agent")
        
        # Phase 1: Repo Scan
        print("Phase 1: Repo Scan")
        repo_jobs = self.repo_scanner.scan_github_repos()
        
        # Phase 2: System Scan
        print("Phase 2: System Scan")
        toolchain_map = self.system_scanner.scan_system_drives()
        
        # Phase 3: Stack Build & Sandbox
        print("Phase 3: Stack Build & Sandbox")
        self.stack_builder.build_environments(repo_jobs, toolchain_map)
        
        # Phase 4: Test & Verification
        print("Phase 4: Test & Verification")
        test_results = self.test_runner.run_tests()
        
        # Phase 5: Memory & RAG
        print("Phase 5: Memory & RAG")
        self.repo_dependency_graph.update(repo_jobs)
        self.cross_stack_patterns.extract_and_store(test_results)
        self.sandbox_verification.store_results(test_results)
        self.meta_learner.update_metrics(test_results)
        
        # Phase 6: Deployment & SaaS
        print("Phase 6: Deployment & SaaS")
        self.deploy_agent.package_frameworks()
        
        # Phase 7: Feedback Loop
        print("Phase 7: Feedback Loop")
        self.learn_agent.monitor_and_update()
        
        print("Agent completed all phases successfully.")

if __name__ == "__main__":
    agent = GPTCodeDebug()
    agent.run()