import React from 'react';
import styles from './Profile.module.scss';
const Profile: React.FC = () => {
  return (
    <div className={styles.profile}>
      <span className={styles.avatar}></span>
      <a className={styles.name} href="">
        Profile Name, grade
      </a>
    </div>
  );
};

export default Profile;
