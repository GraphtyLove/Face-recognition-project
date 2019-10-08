import React from 'react';
import styled from 'styled-components'
import AddEmployeeForm from './AddEmployeeForm'



const AdminBlock = () => {

    // * ---------- STYLE ---------- *
    const AdminBlockSection = styled.section`
        display: flex;
        flex-direction: column;
        margin: 40px 10px;
        background-color: #ffffff;
        padding: 20px;
        /* max-width: 550px; */
        width: 45vw;
        h2 {
            margin-top : 0;
            font-size: 45px;
            line-height: 1;
            font-weight: normal;
            color: darkred;
            text-align: center;
        }
`

    return (
        <AdminBlockSection>
            <h2>Admin Section</h2>

            {/*Add employee form*/}
            <AddEmployeeForm />
            {/*List of employee + delete button*/}

        </AdminBlockSection>
    );
};

export default AdminBlock;
