function previewData() {
     // Collect form values
     const patientId = document.getElementById("patientId").value;
     const age = document.getElementById("age").value;
     const sex = document.getElementById("sex").value;

     const diagnosis_date = document.getElementById("diagnosisDate").value;
     const height = document.getElementById("height").value;
     const weight = document.getElementById("weight").value;

     const diabetes = document.getElementById("diabetes").checked ? 'Yes' : 'No';
     const hypertension = document.getElementById("hypertension").checked ? 'Yes' : 'No';
     const ihd = document.getElementById("ihd").checked ? 'Yes' : 'No';
     const othersInput = document.getElementById("othersInput");
     const other_comorbidities = othersInput ? othersInput.value : '';

     const hydroxyurea = document.getElementById("hydroxyurea").checked ? 'Yes' : 'No';
     const tki = document.getElementById("tki").checked ? 'Yes' : 'No';
     // const other_treatment = document.getElementById("otherTreatmentInput").value || 'None';

     // Create the preview content
     const previewContent = `
       <tr> 
         <tr><td>Patient ID</td><td>${patientId}</td></tr>
         <tr><td>Age</td><td>${age}</td></tr>
         <tr><td>Gender</td><td>${sex}</td></tr>
         <tr><td>Date of Diagnosis</td><td>${diagnosis_date}</td></tr>
         <tr><td>Height (cm)</td><td>${height}</td></tr>
         <tr><td>Weight (kg)</td><td>${weight}</td></tr>
         <tr><td>Diabetes</td><td>${diabetes}</td></tr>
         <tr><td>Hypertension</td><td>${hypertension}</td></tr>
         <tr><td>IHD</td><td>${ihd}</td></tr>
         <tr><td>Other Comorbidities</td><td>${other_comorbidities}</td></tr>
         
       </tr>
 
     `;

     // Display the preview content
     document.getElementById("previewContent").innerHTML = previewContent;

     // Show the modal
     var myModal = new bootstrap.Modal(document.getElementById('previewModal'));
     myModal.show();

     // Confirm Submit Button Functionality
     document.getElementById("confirmSubmit").onclick = function () {
          document.getElementById("patientForm").submit(); // Submit the form
     };
}