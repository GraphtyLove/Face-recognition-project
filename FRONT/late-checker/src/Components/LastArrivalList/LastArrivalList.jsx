import React, {Fragment, useState} from 'react';
import styled from 'styled-components'

const LastArrivalList = () => {
        const LastArrivalSection = styled.section`
            display: flex;
            flex-direction: column;
            margin: 40px 0 40px 0;
            background-color: #ffffff;
            padding: 20px;
            /* max-width: 550px; */
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

    return (
        <LastArrivalSection>
            <h2>Last arrivals</h2>
				<ul>
                    <li>Maxim Berge</li>
				</ul>
			</LastArrivalSection>
    );
};

export default LastArrivalList;
