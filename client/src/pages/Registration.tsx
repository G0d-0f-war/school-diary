import React, { useContext, useEffect } from 'react';
import { Context } from '../main';
import { observer } from 'mobx-react';
import { useNavigate } from 'react-router-dom';
import Auth from '../modules/Registration/components/Auth/Auth';

const Registration: React.FC = () => {
  const { store } = useContext(Context);
  useEffect(() => {
    if (localStorage.getItem('token')) {
      store.checkAuth();
    }
  }, []);
  const navigate = useNavigate();

  if (store.isAuth) {
    navigate('/home');
  }
  return (
    <div className="registration">
      <Auth />
    </div>
  );
};

export default observer(Registration);
