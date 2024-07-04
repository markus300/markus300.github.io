// App.js
import React from 'react';
import './App.css';
import ProjectSlider from './ProjectSlider';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="title">Portfolio</h1>
        <nav className="menu">
          <ul>
            <li>Home</li>
            <li>About</li>
            <li>Projects</li>
            <li>Contact</li>
          </ul>
        </nav>
      </header>
      <main className="content">
        <ProjectSlider />
      </main>
      <footer className="footer">
        <p>Contact Information: Your Email, Your Phone Number</p>
      </footer>
    </div>
  );
}

export default App;
