import React from 'react';
import ReactDOM from 'react-dom/client'; // Ensure you're importing from 'react-dom/client'
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root')); // Ensure this element exists

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
