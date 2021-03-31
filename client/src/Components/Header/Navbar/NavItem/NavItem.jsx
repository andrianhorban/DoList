import React from "react";
import s from './style.module.css';


const NavItem = () => {
    return (
        <div>
            <NavItem path="/" text='Головна' />

            <NavItem path="/about" text='Про нас' />
        </div>
    );
};

export default NavItem;