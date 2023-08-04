import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const url = 'http://localhost:8000/users'; // Replace with your API endpoint URL
      const headers = {
        'Content-Type': 'application/json'
      };

      try {
        const response = await fetch(url, {
          method: 'GET',
          headers: headers,
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const responseData = await response.json();
        setData(responseData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []); // Empty dependency array to ensure the effect runs only once when the component mounts

  return (
    <div>
      <h1>Hello from React</h1>
      <p>Response from FastAPI: {JSON.stringify(data)}</p>
      {data[0]}
    </div>
  );
}

export default App;
