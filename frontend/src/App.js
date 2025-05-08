import React, { useState } from 'react';

function App() {
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/get-studies');
      const data = await res.json();
      setResponse(JSON.stringify(data, null, 2));
    } catch (err) {
      setResponse('❌ Error fetching data');
    }
    setLoading(false);
  };

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#f9fafb',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: 'system-ui, sans-serif',
      padding: '2rem'
    }}>
      <h1 style={{
        fontSize: '2rem',
        marginBottom: '1rem',
        color: '#333'
      }}>
        Study Fetcher
      </h1>

      <button
        onClick={handleClick}
        disabled={loading}
        style={{
          backgroundColor: '#6366f1',
          color: '#fff',
          padding: '0.5rem 1rem',
          borderRadius: '8px',
          border: 'none',
          cursor: loading ? 'not-allowed' : 'pointer',
          fontSize: '1rem',
          transition: 'background-color 0.2s ease'
        }}
      >
        {loading ? 'Loading...' : 'Fetch Studies'}
      </button>

      <pre style={{
        marginTop: '2rem',
        backgroundColor: '#e5e7eb',
        padding: '1rem',
        borderRadius: '8px',
        width: '100%',
        maxWidth: '600px',
        whiteSpace: 'pre-wrap',
        wordBreak: 'break-word',
        color: '#111',
        fontSize: '0.9rem'
      }}>
        {response}
      </pre>
    </div>
  );
}

export default App;
