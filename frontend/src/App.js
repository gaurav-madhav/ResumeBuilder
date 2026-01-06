import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobPosting, setJobPosting] = useState('');
  const [outputFormat, setOutputFormat] = useState('pdf');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const validTypes = ['application/pdf', 'application/msword', 
                         'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
      if (validTypes.includes(file.type) || file.name.endsWith('.pdf') || 
          file.name.endsWith('.doc') || file.name.endsWith('.docx')) {
        setResumeFile(file);
        setError('');
      } else {
        setError('Please upload a PDF, DOC, or DOCX file');
        setResumeFile(null);
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess(false);
    setLoading(true);

    if (!resumeFile) {
      setError('Please select a resume file');
      setLoading(false);
      return;
    }

    if (!jobPosting.trim()) {
      setError('Please enter job posting or responsibilities');
      setLoading(false);
      return;
    }

    try {
      const formData = new FormData();
      formData.append('resume', resumeFile);
      formData.append('job_posting', jobPosting);
      formData.append('output_format', outputFormat);

      // Use environment variable for API URL, fallback to relative path
      const apiUrl = process.env.REACT_APP_API_URL || '';
      const response = await axios.post(`${apiUrl}/api/enhance-resume`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob',
      });

      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `enhanced_resume.${outputFormat}`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);

      setSuccess(true);
      setResumeFile(null);
      setJobPosting('');
      document.getElementById('resume-upload').value = '';
    } catch (err) {
      console.error('Error details:', err);
      console.error('Error response:', err.response);
      console.error('API URL:', process.env.REACT_APP_API_URL || 'Not set');
      
      let errorMessage = 'An error occurred while processing your resume';
      
      if (err.response) {
        // Server responded with error
        if (err.response.data) {
          // Try to parse error message from blob or JSON
          if (err.response.data instanceof Blob) {
            const reader = new FileReader();
            reader.onload = () => {
              try {
                const errorData = JSON.parse(reader.result);
                setError(errorData.error || errorMessage);
              } catch {
                setError(`Server error (${err.response.status}): ${err.response.statusText}`);
              }
            };
            reader.readAsText(err.response.data);
            return; // Exit early, error will be set in reader.onload
          } else if (typeof err.response.data === 'object') {
            errorMessage = err.response.data.error || err.response.data.message || errorMessage;
          } else {
            errorMessage = `Server error (${err.response.status}): ${err.response.statusText}`;
          }
        } else {
          errorMessage = `Server error (${err.response.status}): ${err.response.statusText}`;
        }
      } else if (err.request) {
        // Request was made but no response received
        errorMessage = 'Unable to connect to server. Please check your internet connection and ensure the backend is running.';
        console.error('No response received:', err.request);
      } else if (err.code === 'ERR_NETWORK' || err.message.includes('Network Error')) {
        errorMessage = 'Network error: Cannot reach the server. Please check if the backend API is accessible.';
      } else if (err.message) {
        errorMessage = err.message;
      }
      
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="top-header">
        <div className="top-header-content">
          <div className="logo">BuildCustomResume</div>
        </div>
      </div>
      <div className="container">
        <header className="header">
          <h1>AI-Powered Resume Enhancer</h1>
          <p>Optimize your resume with targeted keywords from job descriptions. Get noticed by ATS systems and hiring managers.</p>
        </header>

        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label htmlFor="resume-upload" className="label">
              Upload Your Resume
            </label>
            <input
              id="resume-upload"
              type="file"
              accept=".pdf,.doc,.docx"
              onChange={handleFileChange}
              className="file-input"
            />
            {resumeFile && (
              <p className="file-name">Selected: {resumeFile.name}</p>
            )}
          </div>

          <div className="form-group">
            <label htmlFor="job-posting" className="label">
              Job Posting or Responsibilities
            </label>
            <textarea
              id="job-posting"
              value={jobPosting}
              onChange={(e) => setJobPosting(e.target.value)}
              placeholder="Paste the job description, requirements, or key responsibilities here..."
              className="textarea"
              rows="8"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="output-format" className="label">
              Output Format
            </label>
            <select
              id="output-format"
              value={outputFormat}
              onChange={(e) => setOutputFormat(e.target.value)}
              className="select"
            >
              <option value="pdf">PDF</option>
              <option value="docx">DOCX</option>
            </select>
          </div>

          {error && <div className="error-message">{error}</div>}
          {success && (
            <div className="success-message">
              Resume enhanced successfully! Your download should start shortly.
            </div>
          )}

          <button
            type="submit"
            className="submit-button"
            disabled={loading}
          >
            {loading ? 'Processing...' : 'Enhance My Resume'}
          </button>
        </form>

        <div className="info-section">
          <h2>How It Works</h2>
          <ul>
            <li>Upload your existing resume in PDF, DOC, or DOCX format</li>
            <li>Paste the job description or key responsibilities</li>
            <li>Our AI analyzes and extracts relevant keywords automatically</li>
            <li>Download your optimized, ATS-friendly resume instantly</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;

