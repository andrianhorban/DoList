import React from "react";
import s from './style.module.css';
import Navbar from  './Navbar/Navbar'

const Header = () => {
    return (
       <div className={s.header}>
            <div className={`${s.header__block} ${s.header__title}`}>
                DoList
            </div>
           <Navbar />


       </div>
    );
};

export default Header;