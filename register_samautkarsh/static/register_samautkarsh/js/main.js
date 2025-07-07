

// Add event listener to copy address checkbox
document.getElementById('copyAddressCheckbox').addEventListener('change', (e) => {
    const permanentAddress = document.getElementById('currentAddress').value;
    if (e.target.checked) {
        document.getElementById('permanentAddress').value = permanentAddress;
    } else {
        document.getElementById('permanentAddress').value = '';
    }
});

// Define mappings
const mappings = {
jilaToNagar: {
    "Karawal Nagar": ["Sriram","Khajuri","Brijpuri","Mahalakshmi","Shiv Vihar"],
    'Ambedkar':['Dakshini Sangam Vihar','Dakshinpuri','Paschimi Sangam Vihar','Purvi Sangam Vihar','Sainik Farm','Tigri'],
'Badrpur':['Badarpur','Kalindi Kunj','Mithapur','Sarita Vihar','Sourabh Vihar','Thekhand'],
'Bramapuri':['Bhajanpura','Bramapuri','Gautam Vihar','Maujpur','Shastri Park'],
'Burari':['Bakhtavarpur','Bhalswa Dairy','Burari','Jhadhoda','Mukundpur','Samay Pur','Swarup']
},
nagarToBasti: {
    'Nagar 1-1': ['Basti 1-1-1', 'Basti 1-1-2'],
    'Nagar 1-2': ['Basti 1-2-1', 'Basti 1-2-2'],
    'Nagar 2-1': ['Basti 2-1-1', 'Basti 2-1-2'],
    'Nagar 2-2': ['Basti 2-2-1', 'Basti 2-2-2'],
},
bastiToUpbasti: {
    'Basti 1-1-1': ['Upbasti 1-1-1-1', 'Upbasti 1-1-1-2'],
    'Basti 1-1-2': ['Upbasti 1-1-2-1', 'Upbasti 1-1-2-2'],
    'Basti 1-2-1': ['Upbasti 1-2-1-1', 'Upbasti 1-2-1-2'],
    'Basti 1-2-2': ['Upbasti 1-2-2-1', 'Upbasti 1-2-2-2'],
    'Basti 2-1-1': ['Upbasti 2-1-1-1', 'Upbasti 2-1-1-2'],
    'Basti 2-1-2': ['Upbasti 2-1-2-1', 'Upbasti 2-1-2-2'],
    'Basti 2-2-1': ['Upbasti 2-2-1-1', 'Upbasti 2-2-1-2'],
    'Basti 2-2-2': ['Upbasti 2-2-2-1', 'Upbasti 2-2-2-2'],  
},
dayitvaMapping: {
    prant: ['संघचालक',	'सह संघचालक',	'कार्यवाह',	'सह कार्यवाह',	'प्रचारक प्रमुख',	'प्रचारक',	'सह प्रचारक',	'प्रौढ़ कार्य प्रमुख',	'सह प्रौढ़ कार्य प्रमुख',	'सेवा प्रमुख',	'सह सेवा प्रमुख',	'संपर्क प्रमुख',	'सह संपर्क प्रमुख',	'सह संपर्क प्रमुख',	'प्रचार प्रमुख',	'सह प्रचार प्रमुख',	'बौद्धिक प्रमुख',	'सह बौद्धिक प्रमुख',	'व्यवस्था प्रमुख',	'सह व्यवस्था प्रमुख',	'विद्यार्थी कार्य प्रमुख',	'सह विद्यार्थी कार्य प्रमुख',	'शारीरिक शिक्षण प्रमुख',	'सह शारीरिक शिक्षण प्रमुख',	'घोष प्रमुख'],
    vibhag: ['संघचालक',	'सह संघचालक',	'कार्यवाह',	'सह कार्यवाह',	'प्रचारक',	'सह प्रचारक',	'प्रौढ़ कार्य प्रमुख',	'सह प्रौढ़ कार्य प्रमुख',	'सेवा प्रमुख',	'सह सेवा प्रमुख',	'संपर्क प्रमुख',	'सह संपर्क प्रमुख',	'प्रचार प्रमुख',	'सह प्रचार प्रमुख',	'बौद्धिक प्रमुख',	'सह बौद्धिक प्रमुख',	'व्यवस्था प्रमुख',	'सह व्यवस्था प्रमुख',	'विद्यार्थी कार्य प्रमुख',	'सह विद्यार्थी कार्य प्रमुख',	'शारीरिक शिक्षण प्रमुख',	'सह शारीरिक शिक्षण प्रमुख',	'घोष प्रमुख',	'सह घोष प्रमुख',	'कॉलेज विद्यार्थी कार्य प्रमुख',	'कॉलेज विद्यार्थी कार्य सह प्रमुख',	'Y.P. प्रमुख',	'सह Y.P. प्रमुख',	'I T प्रमुख',	'सह I T प्रमुख',	'JOIN RSS प्रमुख',	'सह JOIN RSS प्रमुख',	'कार्यालय प्रमुख',	'सह कार्यालय प्रमुख',	'कार्यालय सचिव',	'सह कार्यालय सचिव',	'अन्य दायित्व',	'कार्यकारणी सदस्य',	'प्राध्यापक प्रमुख',	'प्राध्यापक सह प्रमुख',	'बाल कार्य प्रमुख',	'बाल कार्य सह प्रमुख',	'धर्म जागरण प्रमुख',	'धर्म जागरण सह प्रमुख',	'धर्म जागरण टोली सदस्य',	'कुटुम्ब प्रबोधन प्रमुख',	'गौसेवा प्रमुख',	'गौसेवा सह प्रमुख',	'पूर्वोत्तर राज्य प्रमुख',	'पूर्वोत्तर राज्य सह प्रमुख',	'सामाजिक समरसता प्रमुख',	'सामाजिक समरसता सह प्रमुख',	'जम्मु कश्मीर प्रमुख',	'जम्मु कश्मीर सह प्रमुख',	'बाल संस्कार केंद्र प्रमुख',	'बाल संस्कार केंद्र सह प्रमुख',	'सामाजिक सदभाव प्रमुख',	'सामाजिक सदभाव सह प्रमुख',	'पर्यावरण प्रमुख'],
    jila: ['Dayitva Jila 1', 'Dayitva Jila 2'],
    nagar: ['संघचालक',	'सह संघचालक',	'कार्यवाह',	'सह कार्यवाह',	'प्रचारक',	'सह प्रचारक',	'प्रौढ़ कार्य प्रमुख',	'सह प्रौढ़ कार्य प्रमुख',	'विद्यार्थी कार्य प्रमुख',	'सह विद्यार्थी कार्य प्रमुख',	'रात्रि कार्यवाह',	'विद्यार्थी प्रचारक',	'विद्यार्थी विस्तारक'],
    basti: ['Dayitva Basti 1', 'Dayitva Basti 2'],
    upbasti: ['Dayitva Upbasti 1', 'Dayitva Upbasti 2'],
},
prant:['Delhi'],
vibhag:["Yamuna Vihar", "Purvi", "Dakshini", "Ram Krishan Puram", "Paschimi", "Keshav Puram", "Uttari", "Jhandewalan"] ,
jila:["Karawal Nagar","Bramapuri","Nand Nagri","Rohtash Nagar","Shahdara","Gandhi Nagar","Indraprastha","Mayur Vihar","Lajpat Nagar","Badarpur","Kalkaji","Ambedkar","Mihirawali","Basant","Dwarka","Nahargarh","Uttam","Nangloi","Tilak","Janakpuri","Moti Nagar","Saraswati Vihar","Rohini","Kanjhawala","Narela"],
};

const ekaiField = document.getElementById('Ekai');
const dynamicFields = {
prant: document.getElementById('prantField'),
vibhag: document.getElementById('vibhagField'),
jila: document.getElementById('jilaField'),
nagar: document.getElementById('nagarField'),
basti: document.getElementById('bastiField'),
upbasti: document.getElementById('upbastiField'),
dayitva: document.getElementById('dayitvaField'),
};

// Utility: Populate dropdown options
function populateOptions(field, options) {
field.innerHTML = '<option value="" disabled selected>Select a ' + field.id + '</option>';
options.forEach((option) => {
    const opt = document.createElement('option');
    opt.value = option;
    opt.textContent = option;
    field.appendChild(opt);
});
}

// Handle Ekai selection
ekaiField.addEventListener('change', (e) => {
const selectedEkai = e.target.value;

// Hide all fields initially
for (let key in dynamicFields) {
    dynamicFields[key].style.display = 'none';
}

// Show and populate fields based on selected Ekai
if (selectedEkai === 'prant') {
    dynamicFields.prant.style.display = 'block';
    populateOptions(document.getElementById('prant'), mappings.prant);

   document.getElementById('prant').addEventListener('change', (e) => {
        const selectedPrant = e.target.value;
        dynamicFields.dayitva.style.display = 'block';
        populateOptions(document.getElementById('dayitva'), mappings.dayitvaMapping.prant);
    });

}
 else if (selectedEkai === 'vibhag') {
    dynamicFields.vibhag.style.display = 'block';
    populateOptions(document.getElementById('vibhag'), mappings.vibhag);

   document.getElementById('vibhag').addEventListener('change', (e) => {
        const selectedVibhag = e.target.value;
        dynamicFields.dayitva.style.display = 'block';
        populateOptions(document.getElementById('dayitva'), mappings.dayitvaMapping.vibhag);
    });
} else if (selectedEkai === 'jila') {
    dynamicFields.jila.style.display = 'block';
    populateOptions(document.getElementById('jila'), mappings.dayitvaMapping.jila);

   document.getElementById('jila').addEventListener('change', (e) => {
        const selectedJila = e.target.value;
        dynamicFields.dayitva.style.display = 'block';
        populateOptions(document.getElementById('dayitva'), mappings.dayitvaMapping.jila);
    });
} else if (selectedEkai === 'nagar') {
    dynamicFields.jila.style.display = 'block';
    populateOptions(document.getElementById('jila'), Object.keys(mappings.jilaToNagar));

    document.getElementById('jila').addEventListener('change', (e) => {
        const selectedJila = e.target.value;
        dynamicFields.nagar.style.display = 'block';
        populateOptions(document.getElementById('nagar'), mappings.jilaToNagar[selectedJila]);
    }); 

    document.getElementById('nagar').addEventListener('change', (e) => {
        const selectedNagar = e.target.value;
        dynamicFields.dayitva.style.display = 'block';
        populateOptions(document.getElementById('dayitva'), mappings.dayitvaMapping.nagar);
    });
} else if (selectedEkai === 'basti') {
    dynamicFields.jila.style.display = 'block';
    populateOptions(document.getElementById('jila'), Object.keys(mappings.jilaToNagar));

    document.getElementById('jila').addEventListener('change', (e) => {
        const selectedJila = e.target.value;
        dynamicFields.nagar.style.display = 'block';
        populateOptions(document.getElementById('nagar'), mappings.jilaToNagar[selectedJila]);
    });

    document.getElementById('nagar').addEventListener('change', (e) => {
        const selectedNagar = e.target.value;
        dynamicFields.basti.style.display = 'block';
        populateOptions(document.getElementById('basti'), mappings.nagarToBasti[selectedNagar]);
    });

    document.getElementById('basti').addEventListener('change', (e) => {
        const selectedBasti = e.target.value;
        dynamicFields.dayitva.style.display = 'block';
        populateOptions(document.getElementById('dayitva'), mappings.dayitvaMapping.basti);
    });
} else if (selectedEkai === 'upbasti') {
    dynamicFields.jila.style.display = 'block';
    populateOptions(document.getElementById('jila'), Object.keys(mappings.jilaToNagar));

    document.getElementById('jila').addEventListener('change', (e) => {
        const selectedJila = e.target.value;
        dynamicFields.nagar.style.display = 'block';
        populateOptions(document.getElementById('nagar'), mappings.jilaToNagar[selectedJila]);
    });

    document.getElementById('nagar').addEventListener('change', (e) => {
        const selectedNagar = e.target.value;
        dynamicFields.basti.style.display = 'block';
        populateOptions(document.getElementById('basti'), mappings.nagarToBasti[selectedNagar]);
    });

    document.getElementById('basti').addEventListener('change', (e) => {
        const selectedBasti = e.target.value;
        dynamicFields.upbasti.style.display = 'block';

        populateOptions(document.getElementById('upbasti'), mappings.bastiToUpbasti[selectedBasti]);
    });
    document.getElementById('upbasti').addEventListener('change', (e) => {
        const selectedUpbasti = e.target.value;
        dynamicFields.dayitva.style.display = 'block';
        populateOptions(document.getElementById('dayitva'), mappings.dayitvaMapping.upbasti);
    });
}
});

