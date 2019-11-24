import React from 'react'
import { Provider } from 'react-redux';
import Home from '../home/Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';


export default function App (props) {
  return(
    <Provider store={props.store}>
      <Router history={props.history}>
        <Switch>
          <Route exact path='/' component={Home} />
        </Switch>
      </Router>
    </Provider>
  )
}
