import React from 'react';
import styled from 'styled-components'

const SearchBarResult = props => {
    // * ---------- STYLES ---------- *
    const OneResult = styled.div`
        padding: 15px;
        margin: 15px 0;
        min-width: 100%;
        -moz-box-shadow:    3px 3px 8px 3px #ccc;
        -webkit-box-shadow: 3px 3px 8px 3px #ccc;
        box-shadow:         3px 3px 8px 3px #ccc;
`
    const ListItem = styled.li`
        list-style: none;
        margin-bottom: 5px;
`
    const UlList = styled.ul`
      min-width: 100%;
`

    return (
            <OneResult>
                <UlList>
                    <ListItem><b>Date:</b> <i>{ props.result[1] } </i></ListItem>
                    <ListItem><b>Name:</b> <i>{ props.result[2] } </i></ListItem>
                    <ListItem><b>Arrival time:</b> <i>{ props.result[3] } </i></ListItem>
                    <ListItem><b>Departure time:</b> <i>{ props.result[5] } </i></ListItem>
                    <ListItem><b>Is late: </b> <i>{ props.result[6] ? 'Yes' : 'No' } </i></ListItem>
                    <ListItem><b> left early:</b>  <i>{ props.result[7] ? 'Yes' : 'No' } </i></ListItem>
                </UlList>
            </OneResult>
    );
};

export default SearchBarResult;
