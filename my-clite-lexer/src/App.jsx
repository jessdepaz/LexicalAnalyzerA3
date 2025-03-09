import React from 'react';
import './App.css';  // Make sure to include the CSS file for styling
import Lexer from './Lexer';  // Import Lexer component

const App = () => {
  return (
    <div className="App">
      <h1> Group 1: Lexical Analyzer Assignment 3</h1>
      {/* Render the Lexer component */}
      <Lexer />
    </div>
  );
};

export default App;