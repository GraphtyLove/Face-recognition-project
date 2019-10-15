import React, { useState } from 'react';
import styled from 'styled-components'
import LastArrivalItems from '../LastArrivalList/LastArrivalItems'
import realodImg from "../../assets/img/reload.png"


const LastArrivalList = () => {
    const LastArrivalSection = styled.section`
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 40px 10px;
            background-color: #ffffff;
            padding: 20px;
            width: 45vw;
            h2 {
                margin-top : 0;
                font-size: 45px;
                line-height: 1;
                font-weight: normal;
                color: #013087;
                text-align: center;
            }
        `
    const AnswerDiv = styled.div`
        min-width: 80%;
`
    const ReloadImgTag = styled.img`
        height: 50px;
        width: 50px;
        margin-left: 10px;
        cursor: pointer;
`
    // * ---------- STATES --------- *
    const [employeeList, setEmployeeList] = useState([]);
    const [isListIsLoad, setIsListIsLoad] = useState(false);

    const searchForLastEntries = () => {
        if (!isListIsLoad){
            fetch('http://127.0.0.1:5000/get_5_last_entries')
            .then(response => response.json())
            .then(response => {
                if(response) {
                    setEmployeeList(response)
                    setIsListIsLoad(true)
                }
            })
        }
    }
    const LastEntriestAnswer = props => {
        let obj = props.answer
        let answerList = Object.keys(obj).map(key => {
            return <LastArrivalItems result={ obj[key] } />
        })
        return answerList
    }
    searchForLastEntries()

    return (
        <LastArrivalSection className='some-space'>
            <h2>Last arrivals</h2>
            <ReloadImgTag onClick={ () => setIsListIsLoad(false) } src={ realodImg } alt="reload"/>
                    <AnswerDiv>
                        {/* Show user's data if user found */}
                        { ( employeeList && !employeeList['error'] ) ? <LastEntriestAnswer answer={ employeeList } /> : null }
                        {/* Show an error if user is not found */}
                        { employeeList['error'] ? <p>User not found...</p> : null }
                    </AnswerDiv>
			</LastArrivalSection>
    );
};

export default LastArrivalList;
