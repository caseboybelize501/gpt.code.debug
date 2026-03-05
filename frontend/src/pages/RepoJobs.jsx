import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RepoJobs = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchRepoJobs();
  }, []);

  const fetchRepoJobs = async () => {
    try {
      // Mock data - in real implementation would call backend API
      setJobs([
        { name: 'project1', language: 'Python', stars: 100, status: 'queued' },
        { name: 'project2', language: 'JavaScript', stars: 200, status: 'in_progress' },
        { name: 'project3', language: 'Go', stars: 50, status: 'completed' }
      ]);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching repo jobs:', error);
      setLoading(false);
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'queued': return 'bg-yellow-500';
      case 'in_progress': return 'bg-blue-500';
      case 'completed': return 'bg-green-500';
      default: return 'bg-gray-500';
    }
  };

  if (loading) {
    return <div className="text-center py-10">Loading...</div>;
  }

  return (
    <div className="repo-jobs">
      <h1>Repository Jobs</h1>
      
      <div className="jobs-grid">
        {jobs.map((job, index) => (
          <div key={index} className="job-card bg-white p-4 rounded shadow">
            <h3>{job.name}</h3>
            <p>Language: {job.language}</p>
            <p>Stars: {job.stars}</p>
            <div className="status">
              <span className={`inline-block w-3 h-3 rounded-full ${getStatusColor(job.status)}`}></span>
              <span className="ml-2">{job.status}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RepoJobs;