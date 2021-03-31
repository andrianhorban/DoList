import React from "react";
import s from './style.module.css';
import NavItem from 'NavItem/NavItem'

const Navbar = () => {
    return (
        <div>
            <NavItem path="/" text='Головна' />

            <NavItem path="/about" text='Про нас' />
        </div>
    );
};

export default Navbar;