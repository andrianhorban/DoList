import React from "react";
import s from './style.module.css';
import Navbar from  './Navbar/Navbar'

const Header = () => {
    return (
       <div className={s.header}>
            <Navbar />
       </div>
    );
};

export default Header;