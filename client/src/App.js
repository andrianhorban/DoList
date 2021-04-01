import './App.css';
import { BrowserRouter, Route, Switch } from "react-router-dom"
import About from "./Components/About/About";
import Header from "./Components/Header/Header";
import Footer from "./Components/Footer/Footer";
import Index from "./Components/Index/Index";

const App = () => {
    return (
        <div className="App">
            <BrowserRouter>
                <Header/>
                <Switch>
                    <Route exact path='/'>
                        <Index/>
                    </Route>
                    <Route exact path='/about'>
                        <About/>
                    </Route>
                </Switch>
                <Footer/>
            </BrowserRouter>
        </div>
    );
}

export default App;
