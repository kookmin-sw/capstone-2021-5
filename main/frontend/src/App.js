import React, { useEffect, useState } from 'react';
import { Redirect, Route } from 'react-router-dom';
import './App.css';
import { CookiesProvider } from 'react-cookie';
import SignIn from './SignIn.js';
import SignUp from './SignUp.js';
import Maint from './Maint';
import Tendency from './Tendency';
import UserPage from './UserPage';
import ChatList from "./ChatList";
import Chat from "./Chat";
import Photo from "./Photo";
import ChangeUserInfo from "./ChangeUserInfo";
import Diary from "./Diary";
import Ctest from "./Ctest";
import DiaryList from "./DiaryList";
import ChatModule from "./ChatModule";

function App() {

  return (
    <div className="App">
      <CookiesProvider>
    <Route exact path="/"> 
      <SignIn />
    </Route>
    <Route path="/SignUp">
      <SignUp />
    </Route>
    <Route path="/main" >
        <Maint  />
    </Route>
    <Route path="/tendency">
      <Tendency />
    </Route>
    <Route path="/userpage">
      <UserPage />
    </Route>
    <Route path="/chatlist">
      <ChatList />
    </Route>
    <Route exact path="/chat"> 
      <Chat />
    </Route>
    <Route path="/photo">
      <Photo />
    </Route>
    <Route path="/changeuserinfo">
      <ChangeUserInfo />
    </Route>
    <Route path="/diary">
      <Diary />
    </Route>
    <Route path="/ctest">
      <Ctest />
    </Route>
    <Route path="/diarylist">
      <DiaryList />
    </Route>
    <Route path="/cmodule">
      <ChatModule />
    </Route>
    </CookiesProvider>
    </div>
  );
}

export default App;
