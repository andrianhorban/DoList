import React from "react";
import s from './style.module.css';
import NavItem from './NavItem/NavItem'

const Navbar = () => {
    return (
        <div className={s.navbar}>
            <NavItem path="/" text='Список справ' />

            <NavItem path="/about" text='Про застосунок' />

        </div>
    );
};

export default Navbar;