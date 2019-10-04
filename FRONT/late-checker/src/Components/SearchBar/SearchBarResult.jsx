import React, {Fragment, useState} from 'react';
import styled from 'styled-components'

const SearchBarResult = props => {
        const OneResult = styled.div`
          background: #282c34;
          color: #fff;
          padding: 15px;
          border-radius: 6px;
          margin: 15px 0;
          min-width: 100%;
`
            const ListItem = styled.li`
            list-style: none;
            margin-bottom: 5px;
`
    const UlList = styled.ul`
    min-width: 100%;
`
    return (
        <Fragment>
            <OneResult>
                <UlList>
                    <ListItem><b>Date:</b> <i>{ props.result[1] } </i></ListItem>
                    <ListItem><b>Name:</b> <i>{ props.result[2] } </i></ListItem>
                    <ListItem><b>Arrival time:</b> <i>{ props.result[3] } </i></ListItem>
                    <ListItem><b>Departure time:</b> <i>{ props.result[5] } </i></ListItem>
                    <ListItem><b>Is late: </b> <i>{ props.result[6] ? 'Yes' : 'No' } </i></ListItem>
                    <ListItem><b>Is left early:</b>  <i>{ props.result[7] ? 'Yes' : 'No' } </i></ListItem>
                </UlList>
            </OneResult>
        </Fragment>
    );
};

export default SearchBarResult;
