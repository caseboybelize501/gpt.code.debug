import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TestReports = () => {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTestReports();
  }, []);

  const fetchTestReports = async () => {
    try {
      // Mock data - in real implementation would call backend API
      setReports([
        { name: 'python_unit_test', success: true, duration: 2.5, coverage: 95 },
        { name: 'node_integration_test', success: false, duration: 3.2, coverage: 80 },
        { name: 'go_unit_test', success: true, duration: 1.8, coverage: 90 }
      ]);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching test reports:', error);
      setLoading(false);
    }
  };

  const getSuccessColor = (success) => {
    return success ? 'text-green-600' : 'text-red-600';
  };

  if (loading) {
    return <div className="text-center py-10">Loading...</div>;
  }

  return (
    <div className="test-reports">
      <h1>Test Reports</h1>
      
      <div className="reports-table">
        <table className="min-w-full bg-white">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b">Test Name</th>
              <th className="py-2 px-4 border-b">Status</th>
              <th className="py-2 px-4 border-b">Duration (s)</th>
              <th className="py-2 px-4 border-b">Coverage (%)</th>
            </tr>
          </thead>
          <tbody>
            {reports.map((report, index) => (
              <tr key={index}>
                <td className="py-2 px-4 border-b">{report.name}</td>
                <td className={`py-2 px-4 border-b ${getSuccessColor(report.success)}`}>
                  {report.success ? 'Passed' : 'Failed'}
                </td>
                <td className="py-2 px-4 border-b">{report.duration}</td>
                <td className="py-2 px-4 border-b">{report.coverage}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TestReports;