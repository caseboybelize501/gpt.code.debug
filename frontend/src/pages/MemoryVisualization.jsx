import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MemoryVisualization = () => {
  const [memoryData, setMemoryData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchMemoryData();
  }, []);

  const fetchMemoryData = async () => {
    try {
      // Mock data - in real implementation would call backend API
      setMemoryData({
        repo_dependency_graph: [
          { name: 'project1', language: 'Python' },
          { name: 'project2', language: 'JavaScript' }
        ],
        cross_stack_patterns: [
          { pattern: 'dependency_resolution', language: 'python' },
          { pattern: 'performance_optimization', language: 'node' }
        ],
        sandbox_verification: [
          { repo: 'project1', coverage: 95 },
          { repo: 'project2', coverage: 80 }
        ]
      });
      setLoading(false);
    } catch (error) {
      console.error('Error fetching memory data:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="text-center py-10">Loading...</div>;
  }

  return (
    <div className="memory-visualization">
      <h1>Memory Visualization</h1>
      
      <div className="memory-section">
        <h2>Repository Dependency Graph</h2>
        <div className="graph-container">
          {memoryData.repo_dependency_graph?.map((repo, index) => (
            <div key={index} className="repo-node bg-blue-100 p-3 rounded m-2 inline-block">
              {repo.name} ({repo.language})
            </div>
          ))}
        </div>
      </div>
      
      <div className="memory-section">
        <h2>Cross-Stack Patterns</h2>
        <ul>
          {memoryData.cross_stack_patterns?.map((pattern, index) => (
            <li key={index} className="p-2 bg-green-100 rounded m-2">
              {pattern.pattern} - {pattern.language}
            </li>
          ))}
        </ul>
      </div>
      
      <div className="memory-section">
        <h2>Sandbox Verification</h2>
        <table className="min-w-full bg-white">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b">Repository</th>
              <th className="py-2 px-4 border-b">Coverage (%)</th>
            </tr>
          </thead>
          <tbody>
            {memoryData.sandbox_verification?.map((verification, index) => (
              <tr key={index}>
                <td className="py-2 px-4 border-b">{verification.repo}</td>
                <td className="py-2 px-4 border-b">{verification.coverage}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MemoryVisualization;