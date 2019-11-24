import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk';
import loggerMiddleware from 'redux-logger';
import rootReducer, { initialState } from '../reducers';

let middlewares = [thunkMiddleware];
middlewares = [...middlewares, loggerMiddleware];

export default createStore(
  rootReducer,
  initialState,
  applyMiddleware(...middlewares)
);
