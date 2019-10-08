import React, { useState } from 'react';
import styled from 'styled-components'
import LastArrivalItems from '../LastArrivalList/LastArrivalItems'

const LastArrivalList = () => {
    const LastArrivalSection = styled.section`
            display: flex;
            flex-direction: column;
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
        min-width: 50%;
`

    const [employeeList, setEmployeeList] = useState([]);
    // WAIT x MS:
    const wait = ms => {
       const start = new Date().getTime();
       let end = start;
       while(end < start + ms) {
         end = new Date().getTime();
      }
    }

    const searchForLastEntries = () => {
        wait(5000)
        fetch(`http://127.0.0.1:5000/get_5_last_entires`)
        .then(response => response.json())
        .then(response => {
            if(response) {
                setEmployeeList(response)
            }
        })
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
				<ul>
                    <AnswerDiv>
                        {/* Show user's data if user found */}
                        { ( employeeList && !employeeList['error'] ) ? <LastEntriestAnswer answer={ employeeList } /> : null }

                        {/* Show an error if user is not found */}
                        { employeeList['error'] ? <p>User not found...</p> : null }
                    </AnswerDiv>
				</ul>
			</LastArrivalSection>
    );
};

export default LastArrivalList;
