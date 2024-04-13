import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Grade from './pages/Grade';
import Registration from './pages/Registration';
import './app/styles/style.scss';
const App: React.FC = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/grade" element={<Grade />} />
        <Route path="/registration" element={<Registration />} />
      </Routes>
    </>
  );
};

export default App;
