import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [repoJobs, setRepoJobs] = useState([]);
  const [systemScan, setSystemScan] = useState({});
  const [testResults, setTestResults] = useState([]);
  
  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      // Mock data - in real implementation would call backend API
      setRepoJobs([
        { name: 'project1', language: 'Python', stars: 100 },
        { name: 'project2', language: 'JavaScript', stars: 200 }
      ]);
      
      setSystemScan({
        python: ['3.9.0', '3.10.0'],
        node: ['18.0.0']
      });
      
      setTestResults([
        { name: 'python_unit_test', success: true, duration: 2.5 },
        { name: 'node_integration_test', success: false, duration: 3.2 }
      ]);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    }
  };

  return (
    <div className="dashboard">
      <h1>GPT.Code.Debug Dashboard</h1>
      
      <div className="section">
        <h2>Repo Jobs</h2>
        <ul>
          {repoJobs.map((job, index) => (
            <li key={index}>{job.name} ({job.language}) - {job.stars} stars</li>
          ))}
        </ul>
      </div>
      
      <div className="section">
        <h2>System Scan</h2>
        <p>Python versions: {systemScan.python?.join(', ')}</p>
        <p>Node versions: {systemScan.node?.join(', ')}</p>
      </div>
      
      <div className="section">
        <h2>Test Results</h2>
        <ul>
          {testResults.map((result, index) => (
            <li key={index} className={result.success ? 'success' : 'failure'}>
              {result.name}: {result.success ? 'Passed' : 'Failed'} ({result.duration}s)
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;