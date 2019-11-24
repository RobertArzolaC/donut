import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';
 
export default (history) => combineReducers({
  router: connectRouter(history),
})

export const initialState = {
  user: {'id': 8393},
};
