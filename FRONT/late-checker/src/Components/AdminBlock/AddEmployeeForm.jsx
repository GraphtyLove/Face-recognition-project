import React, { useState } from 'react';
import styled from 'styled-components'


const AddEmployeeForm = props => {

    // * ----------- STYLE ---------- *
    const AddEmployeeForm = styled.div`
      display: flex;
      flex-direction: column;
      max-width: 350px;
`
    const AddEmployeeInput = styled.input`
         margin-bottom: 20px;
`
    const AddEmployeeInputText = styled.input`
        max-width: 200px;
        margin-bottom: 20px;
        outline: 0;
        border-width: 0 0 1px;
        border-color: #013087;
        padding: 5px;
`
    const AddEmployeeButton = styled.button`
      max-width: 100px;
      padding: 10px 20px;
      background: forestgreen;
      border: none;
      border-radius: 3px;
      color: white;
      font-weight: bold;
      cursor: pointer;
      align-self: center;
`
    const SuccessAddUser = styled.p`
        padding: 10px;
        color: #25AD47;
        font-weight: bold;
    `
    const ConstErrorAddUser = styled.p`
    padding: 10px;
    color: #E62727;
    font-weight: bold;
`
    const H3AddEmployee = styled.h3`
    display: flex;
    align-items: center;
`

    // * ----------- STATES ---------- *
    const [isUserWellAdded, setIsUserWellAdded] = useState(false);
    const [errorWhileAddingUser, seterrorWhileAddingUser] = useState(false);

    const addEmployeeToDb = e => {
        e.preventDefault()
        // Send it to backend -> add_employee as a POST request
        let name = document.getElementById("nameOfEmployee").value
        let picture = document.getElementById('employeePictureToSend')

        let formData  = new FormData();

        formData.append("nameOfEmployee", name)
        formData.append("image", picture.files[0])

        fetch('http://127.0.0.1:5000/add_employee',{
            method: 'POST',
            body:  formData,
        })
            .then(reposonse => reposonse.json())
            .then(response => {
                console.log(response)
                setIsUserWellAdded(true)
            })
            .catch(error => seterrorWhileAddingUser(true))
    }

    return (
        <section>
            <H3AddEmployee>Add an employee</H3AddEmployee>
            <AddEmployeeForm>
                <AddEmployeeInputText id="nameOfEmployee" name="name" placeholder='John Doe' type="text" />
                <AddEmployeeInput type="file" alt="employee" id='employeePictureToSend' name='employeePictureToSend' />
                <AddEmployeeButton onClick={ addEmployeeToDb }>Add</AddEmployeeButton>
                { isUserWellAdded && <SuccessAddUser>User well added to the Database!</SuccessAddUser> }
                { errorWhileAddingUser && <ConstErrorAddUser>User didn't added to the Database. Please try later...</ConstErrorAddUser> }
            </AddEmployeeForm>
        </section>
    );
};

export default AddEmployeeForm;
