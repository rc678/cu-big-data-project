import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('/users') // Assuming FastAPI is running on default port 8000
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      <h1>Hello from React</h1>
      <p>Response from FastAPI: {JSON.stringify(data)}</p>
    </div>
  );
}

export default App;
