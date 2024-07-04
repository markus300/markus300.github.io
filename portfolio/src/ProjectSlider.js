// ProjectSlider.js
import React, { useEffect, useState } from 'react';
import './ProjectSlider.css';

function ProjectSlider() {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex(prevIndex => (prevIndex + 1) % 3);
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="slider" style={{ transform: `translateX(${-index * 100}%)` }}>
      <div className="slide">Project 1</div>
      <div className="slide">Project 2</div>
      <div className="slide">Project 3</div>
    </div>
  );
}

export default ProjectSlider;
