import React from 'react';
import ReactDOM from 'react-dom';
import store from './core/store';
import history from './core/history';
import App from './containers/app/App';

ReactDOM.render(
  <App store={store} history={history}/>,
  document.getElementById('root')
);
