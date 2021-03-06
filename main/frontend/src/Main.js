import { MailRounded } from '@material-ui/icons';
import React, {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CNavbar from './custom_navbar';
import 'bootstrap/dist/css/bootstrap.css';
import Slide from './music_slide';
import {useHistory} from 'react-router-dom';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';
import {useCookies} from 'react-cookie';
import Chart from './ChartPage';
import {
  Carousel,
  CarouselItem,
  CarouselControl,
  CarouselIndicators,
  CarouselCaption,
  Container, 
  Row, 
  Col,
  Button
} from 'reactstrap';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
    justifyContent: 'left'
  },
}));

export default function Main(){
  const classes = useStyles();
  let [roomname, setRoomName] = useState();
  let [cookie, setCookie, removeCookie] = useCookies(['authorization=']);
  let history = useHistory();
  const token = window.sessionStorage.getItem("Authorization");
  axios.defaults.headers.common["Authorization"] = "jwt " + token;

  function OnSubmit(e) {
    e.preventDefault();
    if(roomname == null){
      alert("Check RoomName");
      return;
    }

    axios.post('http://127.0.0.1:8000/chat/crud/',{
      name: roomname,

    })
    .then(function (response){
      console.log(response);
      console.log(response.data);
      document.cookie = 'authorization=' + token + ';'
      window.sessionStorage.setItem("MakeRoomName", roomname);
      history.push("/chat");

    })
    .catch(function (error){
      console.log(error);
      alert(error);
    });
  }

  function OnChat(e) {
    e.preventDefault();
    history.push("/chatlist");
  }

  return(
    <React.Fragment>
    <Container className="themed-container" >

    
    <CNavbar></CNavbar>
    <br></br>
    <Slide></Slide>
    <br></br>
    <br></br>
    <Row>
    <Col id="sub_title">
    <span>최근 당신의 감정</span>
    </Col>  
    </Row>
    <Row>
    <Col></Col>   
    <Col xs={12} md={8} className="overflow-auto">
    <Chart></Chart>
    </Col>
    <Col></Col>
    </Row>
    <br></br>
    <br></br>
    
    <br></br>
    <Row id="bottom_fix" className="fixed-bottom">
    <Col>
    <Button size="lg" id="btn_nomal" ><span id="simple_txt">감정분석하러 가기</span></Button>
    </Col>
    </Row>
    </Container>
    </React.Fragment>
  );
}