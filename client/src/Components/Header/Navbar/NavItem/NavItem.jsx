import React from "react";
import s from './style.module.css';
import {NavLink} from "react-router-dom";


const NavItem = ({path, text}) => {
    return (
        <NavLink
            exact
            to={path}>
            {text}

        </NavLink>
    );
};

export default NavItem;