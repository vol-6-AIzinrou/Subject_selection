import React, { useState } from 'react';
import './App.css';
import axios from 'axios';
import angryImage from './angry.png';

const AngryImage = () => (
  <img src={angryImage} alt="angry face" style={{width: '30%', height: 'auto'}}/>
);

const ChatApp = () => {
  const [selectedOption, setSelectedOption] = useState('');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleSendOption = () => {
    if (selectedOption !== '') {
      const payload = {
        option: selectedOption,
      };
      axios.post('http://localhost:5000/selectedOption', payload)
        .then(response => console.log(response))
        .catch(error => console.log(error));
    }
  };

  return (
    <div className="App">
      <h2>AIに人間だと気づかれるな...</h2>
      <select value={selectedOption} onChange={handleOptionChange}>
        <option value=""></option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </select>
      <button onClick={handleSendOption}>お題選択</button>
      <div className="angry-images">
        <AngryImage />
        <AngryImage />
        <AngryImage />
        <AngryImage />
        <AngryImage />
        <AngryImage />
      </div>
    </div>
  );
};

export default ChatApp;
