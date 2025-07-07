    // Start Mapping data for dropdowns
    let mappings = {}; 
    async function getMappings() {
        try {
            const response = await fetch('/get-chetra-prant-mappings/');
            const data = await response.json();
            mappings = data; 
        } catch (error) {
            console.error("❌ Error fetching mappings:", error);
        }
    }
    document.addEventListener("DOMContentLoaded", async () => {
        await getMappings();
    
        const phone = document.getElementById('phone');
        const confirmPhone = document.getElementById('confirmPhone');
        const phoneError = document.getElementById('phoneError');
        const confirmPhoneError = document.getElementById('confirmPhoneError');

        // Validate phone format (digits only)
        function validatePhone(input) {
            return /^\d{10}$/.test(input.value);
        }

        // Check if both fields match
        function checkMatch() {
            const phoneValue = phone.value;
            const confirmValue = confirmPhone.value;

            // Validate phone format
            if (!validatePhone(phone)) {
            phoneError.style.display = 'block';
            return false;
            }

            // Check if confirmation matches
            if (phoneValue !== confirmValue) {
                confirmPhoneError.style.display = 'block';
                return false;
            } else {
                confirmPhoneError.style.display = 'none';
                return true;
            }
        }

        // Live validation on input
        [phone, confirmPhone].forEach(field => {
            field.addEventListener('input', function() {
            checkMatch();
            });
        });
// Mask phone number while typing
document.getElementById('phone').addEventListener('input', function(e) {
  this.value = this.value.replace(/\D/g, ''); // Numbers only
  this.type = 'text'; // Avoid password warning
  
  // Mask all digits except last 2 (e.g., ******41)
                  
    this.value =  ''.repeat(rawValue.length);
  
});

    document.getElementById("dayitva").addEventListener("change", function () {
        resetDropdowns("dayitva");
        toggleVisibility("dayitva");
        populateDropdown("prant", Object.values(mappings.chetraToPrants).flat(), "केंद्र / प्रांत");
        if(this.value === "Kshetra / क्षेत्र"){
            populateDropdown("prantChetra", Object.keys(mappings.chetraToPrants), "क्षेत्र");
        }
    });

    // Handle university selection
    document.getElementById('prantChetra').addEventListener('change', function () {
        const selectedPrantChetra = this.value;
        populateDropdown("prant", mappings.chetraToPrants[selectedPrantChetra] || [], "केंद्र / प्रांत");
    });

    // Listener for institute selection to auto-select type
    document.getElementById("prant").addEventListener("change", function () {
        const selectedPrant = this.value;
        const mainSelect = document.getElementById("prantChetra");

        if (!selectedPrant) return;

        for (const [category, suboptions] of Object.entries(mappings.chetraToPrants)) {
            if (suboptions.includes(selectedPrant)) {
                mainSelect.value = category;
                this.value = selectedPrant;
                break;
            }
        }
    });

    document.getElementById("arrivalMode").addEventListener("change", function(){
        resetDropdowns("arrivalMode");
        toggleVisibility("arrivalMode");
        document.getElementById("departureHeading").style.display = "block";
        document.getElementById("departureMode-container").style.display = "block";
    });
    document.getElementById("departureMode").addEventListener("change", function(){
        resetDropdowns("departureMode");
        toggleVisibility("departureMode");
        document.getElementById("additionalInfo-container").style.display = "block";
    });

    function populateDropdown(field, options, placeholder) {
        const dropdown = document.getElementById(field);
        dropdown.innerHTML = `<option value="" disabled selected>${placeholder}</option>`;
        
        const addOption = (value, text = value) => {
            const option = document.createElement("option");
            option.value = value;
            option.textContent = value;
            dropdown.appendChild(option);
        };
        // Handle generic fields
        const validOptions = Array.isArray(options) ? options : [options];
        validOptions.filter(opt => opt && opt.length > 0).forEach(addOption);
    }

    function toggleVisibility(field) {

        if (field === "dayitva") {
            const dayitvaContainers = [
            "activity", "organisation", "vividhDayitva", "prantChetra", "prant"
            ];
            dayitvaContainers.forEach(id => document.getElementById(`${id}-container`).style.display = "none");
            let dayitva = document.getElementById("dayitva").value;
            const dayitvaMappings = {
                "Akhil Bhartiya / अखिल भारतीय (संघ दायित्व)": ["prant"],
                "Gatividhi Toli / गतिविधि टोली (संघ दायित्व)": ["activity", "prant"],
                "Vividh Sangathan / विविध संगठन": ["organisation", "vividhDayitva", "prant"],
                "Kshetra / क्षेत्र": ["prantChetra", "prant"],
                "केंद्र / प्रांत": ["prant"],
            };
            field = dayitvaMappings[dayitva] || [];
            (field || []).forEach(toggleElement);
            return;
        }else if(field === "arrivalMode" || field === "departureMode"){
            const travelModeContainers = [
                `${field}ByTrain`, `${field}ByAIR`, `${field}ByBus`, `${field}BySelfVehicle`
            ]
        
            let selectedValue = document.getElementById(field).value;
            let normalizedValue = selectedValue
            .replace(/[^a-zA-Z]/g, '') 
            .replace(/\s+/g, ''); 
            let containerId = `${field}${normalizedValue}`;
            travelModeContainers.forEach(id =>{
            
                if(id !== containerId) {
                    const travelFields = document.querySelectorAll(
                    `#${id}-container input[type='text'], ` +
                    `#${id}-container input[type='time'], ` +
                    `#${id}-container input[type='date'], ` +
                    `#${id}-container select`
                    );

                    fieldIds = Array.from(travelFields)
                    .map(field => field.id)
                    .filter(id => id); 
                    (fieldIds || []).forEach(fieldId => document.getElementById(`${fieldId}-container`).style.display = "none");
                }

            })
            // Build container ID dynamically (e.g., arrivalModeByAIR-container)
            containerId = `${field}${normalizedValue}-container`;
            if(containerId === "arrivalMode-container" || containerId === "departureMode-container"){
            }else{
                const travelFields = document.querySelectorAll(
                    `#${containerId} input[type='text'], ` +
                    `#${containerId} input[type='time'], ` +
                    `#${containerId} input[type='date'], ` +
                    `#${containerId} select`
                );

                fieldIds = Array.from(travelFields)
                .map(field => field.id)
                .filter(id => id); 
                fieldIds =  fieldIds|| [];
                (fieldIds || []).forEach(toggleElement);
            }
        }
    }

    // Helper function to toggle visibility
    function toggleElement(elementId) {
        const element = document.getElementById(`${elementId}-container`);
        console.log(element, elementId);
        if (element.style.display === "none" || element.style.display === "") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    }

    function resetDropdowns(field) {
        let fieldIds = [];

        if(field === "arrivalMode" || field === "departureMode"){
        
        let selectedValue = document.getElementById(field).value;
        let normalizedValue = selectedValue
            .replace(/[^a-zA-Z]/g, '') 
            .replace(/\s+/g, '');  

        const containerId = `${field}${normalizedValue}-container`;
        if(containerId === "arrivalMode-container" || containerId === "departureMode-container"){

        }else {
            const travelFields = document.querySelectorAll(
            `#${containerId} input[type='text'], ` +
            `#${containerId} input[type='time'], ` +
            `#${containerId} input[type='date'], ` +
            `#${containerId} select`
            );

            fieldIds = Array.from(travelFields)
            .map(field => field.id)
            .filter(id => id); 
        }
        
        }

        const resetMappings = {
            dayitva: ["activity", "organisation", "vividhDayitva", "prantChetra", "prant"],
            arrivalMode: fieldIds && Array.isArray(fieldIds) ? fieldIds : [],
            departureMode: fieldIds && Array.isArray(fieldIds) ? fieldIds : [],
        };
                
        function resetDropdown(dropdownId) {
            if (dropdownId.includes["prant", "organisation"]){
                populateDropdown(dropdownId, [], dropdownId);
            }else{
                const dropdown = document.getElementById(dropdownId);
                dropdown.value = "";
            }
        }
        if (resetMappings[field]) {
            resetMappings[field].forEach(resetDropdown);
        }
    }
    });

    // Function to check if a field is visible
    function isFieldVisible(fieldId) {
        const field = document.getElementById(`${fieldId}-container`);
        return field && field.style.display !== "none";
    }

    // Function to display error messages
    function showError(fieldId, message) {
        const errorElement = document.getElementById(`${fieldId}Error`);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.style.display = "block";
        }
    }

    // Function to hide error messages
    function hideError(fieldId) {
        const errorElement = document.getElementById(`${fieldId}Error`);
        if (errorElement) {
            errorElement.textContent = "";
            errorElement.style.display = "none";
        }
    }

    const formFields = ["name", "phone","dayitva", "vividhDayitva", "organisation","prant", "flight", "departureFlight", "trainNumber", "coachNumber", "pnr", "departureTrainNumber", "departureCoachNumber", "departurePnr", "busOperator", "departureBusOperator", "activity", "prantChetra", "departureDestinationStation", "destinationStation", "departureStation", "arrivalStation", "departureTerminal", "departureMode", "terminal", "arrivalMode", "flightArrivalTime","departureTime",  "trainArrivalTime", "trainDepartureTime", "busArrivalTime", "busDepartureTime", "flightArrivalDate","departureDate",  "trainArrivalDate", "trainDepartureDate", "busArrivalDate" , "busDepartureDate","departure_vehicle_number", "departure_selfVehicle_date", "departure_selfVehicle_time","arrival_vehicle_number","arrival_selfVehicle_date", "arrival_selfVehicle_time", "additionalInfo"]

    function validateForm(e) { 
        e.preventDefault(); 
        let valid = true;
        formFields.forEach((fieldId) => {
            console.log(fieldId);
            let value = document.getElementById(fieldId).value;
            if(isFieldVisible(fieldId) && !value) {
                showError(fieldId, "Please fill the field.");
                valid = false;
            }
        })
    if(valid) openModal();
    }

    formFields.forEach((fieldId) => {
        let field = document.getElementById(fieldId);
        if(field) {
            field.addEventListener("input", function(){
                hideError(fieldId);
            } )
        }
    })

    let form  = document.getElementById("myForm");
    if(form){
        document.addEventListener("submit", validateForm);
    }

    // Attach event listener to the 'Edit' button
    document.querySelector(".class-modal").addEventListener('click', function () {
        document.getElementById("formModal").style.display = "none";
    })

    document.getElementById('finalSubmit').addEventListener('click', function (event) {
        event.preventDefault();
        Swal.fire({
            title: '!!..धन्यवाद..!!',
            html: 'आपने अपना पंजीकरण सफलतापूर्वक पूर्ण कर लिया है। <br>आपके "QR Code" की जानकारी दिए गए 👉 "SBRPLR SMS Code" 👈 द्वारा आपको शीघ्र भेजी जाएगी।',
            icon: 'success',
            confirmButtonText: 'ठीक है'
        }).then((result) => {
            if (result.isConfirmed) {
                document.getElementById('myForm').submit();
            }
        });
    });

 // Function to open the modal and populate it with form data
    function openModal() {
        const modal = document.getElementById('formModal');
        modal.style.display = 'flex';

        function setModalContent(fieldId, modalElementId, modalContainerId) {
            const field = document.getElementById(fieldId);
            const modalContainer = document.getElementById(modalContainerId);
            if (isFieldVisible(fieldId)) {
                modalContainer.style.display = 'table-row'; 
                document.getElementById(modalElementId).textContent = field.value || 'N/A';
            } else {
                modalContainer.style.display = 'none'; 
            }
        }
       formFields.forEach(id =>{
        setModalContent(`${id}`, `${id}Modal`,`${id}ModalContainer`);
       })
    }


//  function resetDropdown(dropdownId) {
//         if (dropdownId.includes["vividhDayitva", "organisation", "flight", "departureFlight", "trainNumber", "coachNumber", "pnr", "departureTrainNumber", "departureCoachNumber", "departurePnr", "busOperator", "departureBusOperator"]) {
//             document.getElementById("pincode").value = "";
//             toggleVisibility("pincode");
//         }else if( dropdownId.includes["activity", "prantChetra", "departureDestinationStation", "destinationStation", "departureStation", "arrivalStation", "departureTerminal", "departureMode", "terminal", "arrivalMode"]){
//             const dropdown = document.getElementById(dropdownId);
//             dropdown.value = "";
//         }else if (dropdownId.includes["flightArrivalTime","departureTime",  "trainArrivalTime", "trainDepartureTime", "busArrivalTime", "busDepartureTime"]){

//         }else if (dropdownId.includes["flightArrivalDate","departureDate",  "trainArrivalDate", "trainDepartureDate", "busArrivalDate" , "busDepartureDate"]){

//         }else{
//             // populateDropdown(dropdownId, [], dropdownId);
//             const dropdown = document.getElementById(dropdownId);
//             dropdown.value = "";
//         }
//     }