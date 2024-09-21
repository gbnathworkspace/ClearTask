// src/store/index.js
import { createStore, combineReducers } from 'redux';
import taskReducer from './reducers';

const rootReducer = combineReducers({
    tasks: taskReducer,
});

const store = createStore(rootReducer);

export default store;