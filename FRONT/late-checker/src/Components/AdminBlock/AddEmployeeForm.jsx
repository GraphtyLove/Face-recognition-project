import React from 'react';
import styled from 'styled-components'

const AddEmployeeForm = () => {

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
`
    const AddEmployeeButton = styled.button`
      max-width: 100px;
      padding: 10px 0;
      background: forestgreen;
      border: none;
      border-radius: 3px;
      color: white;
      font-weight: bold;
`


    const addEmployeeToDb = e => {
        e.preventDefault()
        // Send it to backend -> add_employee as a POST request
        let name = document.getElementById("nameOfEmployee").value
        let file = document.getElementById('employeePictureToSend')

        let formData  = new FormData();

        formData.append("nameOfEmployee", name)
        formData.append("image", file[0])

        for(var pair of formData.entries()) {
            console.log(pair[0]+ ', '+ pair[1]);
        }

        fetch('http://127.0.0.1:5000/add_employee',{
            method: 'POST',
            body:  formData,
        })
            .then(reposonse => reposonse.json())
            .then(response => {
                console.log(response)
            })
            .catch(error => console.log("error", error))
    }

    return (
        <section>
            <h3>Add an employee</h3>
            <AddEmployeeForm>
                <AddEmployeeInputText id="nameOfEmployee" name="name" placeholder='John Doe' type="text" />
                <AddEmployeeInput type="file" alt="employee" id='employeePictureToSend' name='employeePictureToSend' />
                <AddEmployeeButton onClick={ addEmployeeToDb }>Add</AddEmployeeButton>
            </AddEmployeeForm>
        </section>
    );
};

export default AddEmployeeForm;
