// Start Mapping data for dropdowns
let mappings = {}; // Global variable to store mappings
// Async function to fetch mappings
async function getMappings() {
    try {
        const response = await fetch('/get-registration-mappings/');
        const data = await response.json();
        mappings = data; // Store globally
    } catch (error) {
        console.error("❌ Error fetching mappings:", error);
    }
}
document.addEventListener("DOMContentLoaded", async () => {
    await getMappings();


    const mappingsss = {
        prantToVibhag: {
            'दिल्ली': ['विभाग 1-1', 'विभाग 1-2', 'विभाग 2-1', 'विभाग 2-2'],
        },
        VibhagToJila: {
            'विभाग 1-1': ['जिला 1-1-1', 'जिला 1-1-2'],
            'विभाग 1-2': ['जिला 1-2-1', 'जिला 1-2-2'],
            'विभाग 2-1': ['जिला 2-1-1', 'जिला 2-1-2'],
            'विभाग 2-2': ['जिला 2-2-1', 'जिला 2-2-2'],
        },
        jilaToNagar: {
            'जिला 1-1-1': ['नगर 1-1-1', 'नगर 1-1-2'],
            'जिला 1-1-2': ['नगर 1-1-3', 'नगर 1-1-4'],
            'जिला 1-2-1': ['नगर 1-2-1', 'नगर 1-2-2'],
            'जिला 1-2-2': ['नगर 1-2-3', 'नगर 1-2-4'],
            'जिला 2-1-1': ['नगर 2-1-1', 'नगर 2-1-2'],
            'जिला 2-1-2': ['नगर 2-1-3', 'नगर 2-1-4'],
            'जिला 2-2-1': ['नगर 2-2-1', 'नगर 2-2-2'],
            'जिला 2-2-2': ['नगर 2-2-3', 'नगर 2-2-4'],
        },
        nagarToMandal: {
            'नगर 1-1-1': ['मंडल 1-1-1-1', 'मंडल 1-1-1-2'],
            'नगर 1-1-2': ['मंडल 1-1-2-1', 'मंडल 1-1-2-2'],
            'नगर 1-2-1': ['मंडल 1-2-1-1', 'मंडल 1-2-1-2'],
            'नगर 1-2-2': ['मंडल 1-2-2-1', 'मंडल 1-2-2-2'],
        },
        mandalToBasti: {
            'मंडल 1-1-1-1': ['बस्ती 1-1-1-1-1', 'बस्ती 1-1-1-1-2'],
            'मंडल 1-1-1-2': ['बस्ती 1-1-1-2-1', 'बस्ती 1-1-1-2-2'],
            'मंडल 1-2-1-1': ['बस्ती 1-2-1-1-1', 'बस्ती 1-2-1-1-2'],
            'मंडल 1-2-1-2': ['बस्ती 1-2-1-2-1', 'बस्ती 1-2-1-2-2'],
        },
        bastiToUpbasti: {
            'बस्ती 1-1-1-1-1': ['उपबस्ती 1-1-1-1-1-1', 'उपबस्ती 1-1-1-1-1-2'],
            'बस्ती 1-1-1-1-2': ['उपबस्ती 1-1-1-1-2-1', 'उपबस्ती 1-1-1-1-2-2'],
            'बस्ती 1-2-1-1-1': ['उपबस्ती 1-2-1-1-1-1', 'उपबस्ती 1-2-1-1-1-2'],
            'बस्ती 1-2-1-1-2': ['उपबस्ती 1-2-1-1-2-1', 'उपबस्ती 1-2-1-1-2-2'],
        },
        dayitvaMapping: {
            prant: ['दायित्व प्रांत 1', 'दायित्व प्रांत 2'],
            vibhag: ['दायित्व विभाग 1', 'दायित्व विभाग 2'],
            jila: ['दायित्व जिला 1', 'दायित्व जिला 2'],
            ekai_nagar: ['दायित्व नगर 1', 'दायित्व नगर 2'],
            akhilbhartiya: ['दायित्व akhil 1', 'दायित्व akhil 2'],
            chetra: ['दायित्व area 1', 'दायित्व area 2'],
            mandal: ['दायित्व मंडल 1', 'दायित्व मंडल 2'],
            basti: ['दायित्व बस्ती 1', 'दायित्व बस्ती 2'],
            upbasti: ['दायित्व उपबस्ती 1', 'दायित्व उपबस्ती 2'],
        },
        pincodeToNagar: {
            "110001": ["नगर 1-1-1", "नगर 1-1-2"],
            "110002": ["नगर 1-1-3"],
            "110003": ["नगर 1-1-4"],
            "110004": ["नगर 1-2-1"],
            "110005": ["नगर 1-2-2"],
            "110006": ["नगर 1-2-3"],
        },
        delhiPincodes: ["110001", "110002", "110003"],
        statePincodes: ["110004", "110005", "110006"],
        pincodeToState: {
            "110004": ['state-1', "state-2"],
            "110005": ['state-3', "state-4"],
            "110006": ['state-5', "state-6"],
        },
    };


    const sangathanToReferralCode = {
        "अखिल भारतीय विद्यार्थी परिषद": "ABVP", "विद्याभारती": "VIBH", "भारतीय शिक्षण मंडल": "BSM", "अखिल भारतीय शैक्षिक महासंघ": "ABSM", "संस्कृत भारती": "SBH", "शिक्षा संस्कृति उत्थान न्यास": "SSUN", "वनवासी कल्याण आश्रम": "VKA", "विश्व हिन्दू परिषद्": "VHP",
        "भारतीय जनता पार्टी": "BJP", "राष्ट्रीय सिक्ख संगत": "RSN", "क्रीडा भारती": "KRBH", "संस्कार भारती": "SASB", "सक्षम": "SKSM", "आरोग्य भारती": "AABH", "एन्. एम्. ओ. (नैशनल मैडिकल आर्गेनाइजेशन)": "NMO",
        "भारत विकास परिषद": "BHVP", "दीनदयाल शोध संस्थान": "DDSS", "राष्ट्रीय सेवा भारती": "RSBH", "भारतीय किसान संघ": "BKS", "भारतीय मजदूर संघ": "BMS", "स्वदेशी जागरण मंच": "SJM",
        "सहकार भारती": "SHBH", "ग्राहक पंचायत": "GRHP", "लघु उद्योग भारती": "LUBH", "अखिल भारतीय साहित्य परिषद": "ABSP", "अधिवक्ता परिषद": "ADVP", "प्रज्ञा प्रवाह": "PRPR",
        "विज्ञान भारती": "VBH", "अखिल भारतीय इतिहास संकलन समिति": "ABSS", "पूर्व सैनिक सेवा परिषद": "PSSP", "हिन्दु जागरण मंच": "HJM", "सीमा जागरण मंच": "SIJM",
        "स्वामी विवेकानन्द मेडिकल मिशन": "SVMM", "दिल्ली अध्यापक परिषद्": "DAP", "सुरूचि प्रकाशन": "SRPR", "इंद्रप्रस्थ विश्व संवाद केंद्र": "IVSK", "राष्ट्र सेविका समिति": "RSS", "हिन्दुस्थान समाचार": "HINS", "SUYASH": "SUYASH"
    };
    const sakha_milan = [
        "स्कूल विद्यार्थी", "कॉलेज विद्यार्थी", "तरुण व्यवसायी", "प्रौढ़ व्यवसायी", "Young Professional", "प्राध्यापक", "अन्य", "अभी किसी शाखा/मिलन से नहीं जुड़े हैं",
    ]

    const fieldToHindiMapping = {
        prant: "प्रांत", vibhag: "विभाग", jila: "जिला", nagar: "नगर", address_nagar: "नगर", mandal: "मंडल", basti: "बस्ती", upbasti: "उपबस्ती", ekai_nagar: "नगर",
        sakha_milan: "शाखा / मिलन", vividhSangathan: "विविध संगठन", "akhilbhartiya": "अखिलभारतीय", "chetra": "क्षेत्र",
    };

    const hindiToEnglishMapping = {
        "प्रांत": "prant", "विभाग": "vibhag", "जिला": "jila", "नगर": "nagar", "नगर": "address_nagar", "मंडल": "mandal", "बस्ती": "basti", "उपबस्ती": "upbasti", "नगर": "ekai_nagar",
        "शाखा / मिलन": "sakha_milan", "विविध संगठन": "vividhSangathan", "अखिलभारतीय": "akhilbhartiya", "क्षेत्र": "chetra",
    };


    function newpopulateDropdown(field, options,placeholder) {

        let dropdown = document.getElementById(field);
        // Reset the dropdown
        dropdown.innerHTML = ""; // Clear all options

        // Add the placeholder option for the dropdown
        dropdown.innerHTML = `<option value="" disabled selected>${placeholder}</option>`;

        let first_options = [];
        let second_options = [];
        first_options = options[0] || ""; // First element (if exists)
        second_options = options[1] || ""; // Second element (if exists)

           
           if (first_options) {
              let defaultOption = document.createElement("option");
              defaultOption.value =first_options;
              defaultOption.textContent =first_options;
              defaultOption.selected = true;
              dropdown.appendChild(defaultOption);
           }
           if(second_options){
              second_options.forEach(option => {
              if(option != first_options){
              const opt = document.createElement("option");
              opt.value = option;
              opt.textContent = fieldToHindiMapping[option] ? fieldToHindiMapping[option] : option;
              dropdown.appendChild(opt);
              }
           }); 
           }

     }

    let addresspincode = "{{form.address_pincode.value}}";
    let addressstate = "{{form.address_state.value}}";
    let addressnagar = "{{form.nagar_address.value}}";

    // {% if form.address_state and form.address_state.value != 'None' %}block{% else %}none{% endif %};"

    let pincode = "{{form.pincode.value}}";
    let nagar = "{{form.nagar.value}}";
    // राज्य
    let state = "{{ form.state.value }}";


    // रेजिडेंशियल कॉलोनी (ब्लॉक/गली)
    let upbasti = "{{ form.ekai_upbasti.value }}";
    // दायित्व की इकाई
    let ekai = "{{ form.ekai.value }}";
    // Dayitva Selection
    let dayitv = "{{ form.dayitv.value }}";
    //दायित्व का प्रान्त
    let prants = "{{ form.prant.value }}";
    //दायित्व का विभाग
    let vibhag = "{{ form.vibhag.value }}";
    //दायित्व का जिला
    let jila = "{{ form.jila.value }}";
    //दायित्व का नगर
    let ekainagar = "{{ form.ekai_nagar.value }}";
    //दायित्व का मंडल
    let mandal = "{{ form.ekai_mandal.value }}";
    //दायित्व की बस्ती
    let basti = "{{ form.ekai_basti.value }}";
    //शाखा / मिलन
    let sakhamilan = "{{ form.ekai_sakha_milan.value }}";
    console.log( "87999999999999999999999999","addresspincode",addresspincode,"pincode",pincode);

    let options = [];

    if (addresspincode != "None" && addressnagar != "None" && mappings.pincodeToNagar[addresspincode]) {
        newpopulateDropdown("address_nagar", [addressnagar, mappings.pincodeToNagar[addresspincode]], "नगर"); 
    }
    if (addresspincode!= "None"  && addressstate != "None" && mappings.pincodeToState[addresspincode]) {
        newpopulateDropdown("address_state", [addressstate, mappings.pincodeToState[addresspincode]], "राज्य"); 
    }
    if (pincode != "None" && nagar != "None" && mappings.pincodeToNagar[pincode]) {
        newpopulateDropdown("nagar", [nagar, mappings.pincodeToNagar[pincode]], "नगर"); 
    }
    if (state != "None" && pincode && mappings.pincodeToNagar[pincode]) {
        newpopulateDropdown("state", [state, mappings.pincodeToState[pincode]], "राज्य"); 
    }
    if (nagar!= "None"  && upbasti!= "None"  ) {
        let mandals = mappings.nagarToMandal[nagar] || [];
        options = mandals.flatMap(mandal => mappings.mandalToBasti[mandal] || []);
        newpopulateDropdown("upbasti", [upbasti,options], "उपबस्ती");
    }
    if(upbasti!= "None"  && ekai!= "None" ){
        options = ["प्रांत", "विभाग", "जिला", "नगर", "मंडल", "बस्ती", "शाखा / मिलन", "अखिलभारतीय", "क्षेत्र"];
        newpopulateDropdown("ekai", [ekai,options], "इकाई");
    }
    if(dayitv!= "None" ){
    console.log(mappings.dayitvaMapping["shakha"]);
        if(ekai === `${fieldToHindiMapping["sakha_milan"]}`){
        options = mappings.dayitvaMapping["shakha"];
        }
        else{
        options = mappings.dayitvaMapping[`${hindiToEnglishMapping[ekai]}`];
        }
        newpopulateDropdown("dayitva", [dayitv, options], "दायित्व");
    }
    if(sakhamilan != "None"){
        document.getElementById("sakha_milanCheckbox-container").style.display = "block";
        options = ["स्कूल विद्यार्थी","कॉलेज विद्यार्थी", "तरुण व्यवसायी", "प्रौढ़ व्यवसायी", "Young Professional", "प्राध्यापक", "अन्य" ,"अभी किसी शाखा/मिलन से नहीं जुड़े हैं"];
        newpopulateDropdown("sakha_milan", [sakhamilan, options], "शाखा / मिलन");
    }
    let selectedJila = Object.keys(mappings.jilaToNagar).find(jila =>
        mappings.jilaToNagar[jila].includes(nagar)
    );

    let selectedVibhag = Object.keys(mappings.VibhagToJila).find(vibhag =>
        mappings.VibhagToJila[vibhag].includes(selectedJila)
    );
    let selectedPrant = Object.keys(mappings.prantToVibhag).find(prant =>
        mappings.prantToVibhag[prant].includes(selectedVibhag)
    );

    if(prants!= "None" ){
        options = mappings["prant"];
        newpopulateDropdown("prant", [prants, options], "प्रांत");
    }

    if(vibhag!= "None" ){
        options = mappings.prantToVibhag[selectedPrant];
        newpopulateDropdown("vibhag", [vibhag, options], "विभाग");
    }
    if(jila!= "None" ){
        options = mappings.VibhagToJila[selectedVibhag];
        newpopulateDropdown("jila", [jila, options], "जिला");
    }
    if(nagar!= "None" ){
        options = mappings.pincodeToNagar[pincode];
        console.log(options)
        newpopulateDropdown("ekai_nagar", [nagar, options], "नगर");
    }
    if(mandal!= "None" ){
        options = mappings.nagarToMandal[nagar];
        newpopulateDropdown("mandal", [mandal, options], "मंडल");
    }
    if(basti!= "None" ){
        let mandals = mappings.nagarToMandal[nagar] || [];
        options = mandals.flatMap(mandal => mappings.mandalToBasti[mandal] || []);
        newpopulateDropdown("basti", [basti, options], "");
    }
    if(upbasti!= "None" ){
        let mandals = mappings.nagarToMandal[nagar] || [];
        let bastis = mandals.flatMap(mandal => mappings.mandalToBasti[mandal] || []);
        options = bastis.flatMap(basti => mappings.bastiToUpbasti[basti] || []);
        newpopulateDropdown("upbasti", [upbasti, options], "");
    }


  //******/ particle animation background js *******
    const particlesContainer = document.getElementById('particles');
    const particles = [];
    const numParticles = 200;

    class Particle {
        constructor() {
            this.element = document.createElement('span');
            this.element.className = 'particle';
            this.size = Math.random() * 4 + 2; // Increased size range: 2px to 6px
            this.element.style.width = `${this.size}px`;
            this.element.style.height = `${this.size}px`;
            particlesContainer.appendChild(this.element);

            this.width = window.innerWidth;
            this.height = document.body.scrollHeight;
            this.x = Math.random() * this.width;
            this.y = Math.random() * this.height;
            this.speedX = Math.random() * 2 - 1;
            this.speedY = Math.random() * 2 - 1;

            this.updatePosition();
        }

        updatePosition() {
            this.element.style.left = `${this.x}px`;
            this.element.style.top = `${this.y}px`;
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            // Bounce off boundaries, accounting for particle size
            if (this.x < 0 || this.x > this.width - this.size) this.speedX *= -1;
            if (this.y < 0 || this.y > this.height - this.size) this.speedY *= -1;

            this.updatePosition();
        }
    }

    function updateContainerSize() {
        const width = window.innerWidth;
        const height = document.body.scrollHeight;
        particlesContainer.style.height = `${height}px`;
        return { width, height };
    }

    function init() {
        particles.length = 0;
        particlesContainer.innerHTML = ''; // Clear existing particles
        const { width, height } = updateContainerSize();
        for (let i = 0; i < numParticles; i++) {
            const particle = new Particle();
            particle.width = width;
            particle.height = height;
            particles.push(particle);
        }
    }

    function animate() {
        particles.forEach(particle => particle.update());
        requestAnimationFrame(animate);
    }

    init();
    animate();

    // Update particles on resize
    window.addEventListener('resize', () => {
        const { width, height } = updateContainerSize();
        particles.forEach(particle => {
            particle.width = width;
            particle.height = height;
            // Redistribute if out of bounds
            if (particle.x > width - particle.size) particle.x = Math.random() * width;
            if (particle.y > height - particle.size) particle.y = Math.random() * height;
        });
    });

    // Observe body size changes
    const resizeObserver = new ResizeObserver(() => {
        init(); // Reinitialize particles to cover new height
    });
    resizeObserver.observe(document.body);






    //Sangh sikhshan js


    const shikshanSelect = document.getElementById('sangh_shikshan_level');
    // Initialize on load
    updateShikshanFields();

    // Update fields when selection changes
    shikshanSelect.addEventListener('change', updateShikshanFields);

    function updateShikshanFields() {

        const pratigyaContainer = document.getElementById("pratigyaCheckbox-container");
        const pratigyaCheckbox = document.getElementById("pratigyaCheckbox");
        const level = document.getElementById('sangh_shikshan_level').value;
        const container = document.getElementById('shikshan-details-container');
        

        // Clear previous fields
        container.innerHTML = '';
        // Handle pratigya checkbox based on level
        if (level === 'कोई नहीं' || level === 'प्रारंभिक वर्ग' || level === 'प्राथमिक वर्ग' || level === 'प्रथम वर्ष') {
            pratigyaContainer.style.display = "block";
            pratigyaCheckbox.checked = false;
        } else {
            pratigyaContainer.style.display = "none";
            // pratigyaCheckbox.checked = true;
        }

        // Hide container if no shikshan selected
        if (level === 'कोई नहीं') {
            container.style.display = 'none';
            return;
        }

        // Show container
        container.style.display = 'block';

        // Create fields based on level
        const fieldsToCreate = [];

        if (level === 'तृतीय वर्ष') {
            fieldsToCreate.push(
                { type: 'tritiya', label: 'तृतीय वर्ष' },
                { type: 'dwitiya', label: 'द्वितीय वर्ष' },
                { type: 'pratham', label: 'प्रथम वर्ष' },
                { type: 'prathmik', label: 'प्राथमिक वर्ग' },
                { type: 'prarambhik', label: 'प्रारंभिक वर्ग' },   
            );
        } else if (level === 'द्वितीय वर्ष') {
            fieldsToCreate.push(
                { type: 'dwitiya', label: 'द्वितीय वर्ष' },
                { type: 'pratham', label: 'प्रथम वर्ष' },
                { type: 'prathmik', label: 'प्राथमिक वर्ष' },
                { type: 'prarambhik', label: 'प्रारंभिक वर्ष' },     
            );
        } else if (level === 'प्रथम वर्ष') {
            fieldsToCreate.push(
                { type: 'pratham', label: 'प्रथम वर्ष' },
                { type: 'prathmik', label: 'प्राथमिक वर्ष' },
                { type: 'prarambhik', label: 'प्रारंभिक वर्ष' },
                
            );
        } else if (level === 'प्राथमिक वर्ष') {
            fieldsToCreate.push(
                { type: 'prathmik', label: 'प्राथमिक वर्ष' },
                { type: 'prarambhik', label: 'प्रारंभिक वर्ष'}
            );
        } else if (level === 'प्रारंभिक वर्ष') {
            fieldsToCreate.push(
                { type: 'prarambhik', label: 'प्रारंभिक वर्ष' },
            );
        }
        // Create fieldset container
        const fieldset = document.createElement('div');
        fieldset.className = 'shikshan-fieldset mb-4';
        // Create row for year and month
        const row = document.createElement('div');
        row.className = 'row';

        // Create the fields
        fieldsToCreate.forEach(field => {
            // Year Field (left column)
            const yearCol = document.createElement('div');
            yearCol.className = 'col-md-6 mb-3 dropdown';
            yearCol.id = `${field.type}_year-container`;

            const yearLabel = document.createElement('label');
            yearLabel.className = 'form-label';
            yearLabel.style.cssText = 'font-size: 16px !important; font-weight: 600; color: #333;';
            yearLabel.textContent = field.label;
            yearLabel.htmlFor = `${field.type}-year`;

            const spanClass = document.createElement('span');
            spanClass.textContent = ' *';
            spanClass.className = "text-danger";
            yearLabel.appendChild(spanClass);

            yearCol.appendChild(yearLabel);

            const yearSelect = document.createElement('select');
            yearSelect.id = `${field.type}_year`;
            yearSelect.name = `${field.type}_varsh`;
            yearSelect.className = 'form-control';
            // yearSelect.required = true;

            const yearDefaultOption = document.createElement('option');
            yearDefaultOption.value = '';
            yearDefaultOption.textContent = 'वर्ष चुनें';
            yearDefaultOption.disabled = true;
            yearDefaultOption.selected = true;
            yearSelect.appendChild(yearDefaultOption);

            // Add years from current year back to 1950
            const currentYear = new Date().getFullYear();
            for (let year = currentYear; year >= 1950; year--) {
                const option = document.createElement('option');
                option.value = year;
                option.textContent = year;
                yearSelect.appendChild(option);
            }

            yearCol.appendChild(yearSelect);

            const yearError = document.createElement('small');
            yearError.className = 'text-danger';
            yearError.id = `${field.type}_yearError`;
            yearError.style.cssText = 'display: none; font-size: 12px !important;';
            yearError.textContent = 'कृपया वर्ष चुनें';
            yearCol.appendChild(yearError);

            // Add real-time validation listener
            yearSelect.addEventListener('change', function () {
                if (yearSelect.value) {
                    hideError(`${field.type}_year`);
                }
            });

            // Add columns to row
            row.appendChild(yearCol);

            // Add row to fieldset
            fieldset.appendChild(row);

            // Add fieldset to container
            container.appendChild(fieldset);
        });
    }

    // ********************************Ghosh jankari  Java Script *************************
    document.querySelectorAll('input[name="ghosh_vadak"]').forEach(function (radio) {
        radio.checked = false;
    });
    document.querySelectorAll('input[name="learn_vadya"]').forEach(function (radio) {
        radio.checked = false;
    });
    // Toggle visibility of containers and reset checkboxes for ghosh_vadak
    document.querySelectorAll('input[name="ghosh_vadak"]').forEach(function (radio) {
        radio.addEventListener('change', function () {
            // Reset all vadya checkboxes
            document.querySelectorAll('input[name="vadya"]').forEach(function (checkbox) {
                checkbox.checked = false;
                // Ensure dependent checkboxes remain hidden
                if (['turya', 'swarad', 'nagang', 'gomukh', 'other'].includes(checkbox.id)) {
                    checkbox.parentElement.style.display = 'none';
                }
            });

            document.querySelectorAll('input[name="rachnaye"]').forEach(function (radio) {
                radio.checked = false;
            });
            document.getElementById("shankhShrungOwn").checked = false;

            // Toggle visibility based on selection
            if (this.value === 'हाँ') {
                document.getElementById('ghoshVadakYes-container').style.display = 'block';
                document.getElementById('ghoshVadakNo-container').style.display = 'none';
            } else {
                document.getElementById('ghoshVadakYes-container').style.display = 'none';
                document.getElementById('ghoshVadakNo-container').style.display = 'block';
            }
        });
    });


    // Toggle visibility of learnVadyaList and reset checkboxes for learn_vadya
    document.querySelectorAll('input[name="learn_vadya"]').forEach(function (radio) {
        radio.addEventListener('change', function () {
            // Reset all learn_vadya_list checkboxes
            document.querySelectorAll('input[name="learn_vadya_list"]').forEach(function (checkbox) {
                checkbox.checked = false;
            });
            // Toggle visibility
            if (this.value === 'हाँ') {
                document.getElementById('learnVadyaList').style.display = 'block';
            } else {
                document.getElementById('learnVadyaList').style.display = 'none';
            }
        });
    });

    // Reusable function to toggle visibility and reset dependent checkboxes
    function toggleDependentCheckboxes(checkboxId, dependentIds) {
        const mainCheckbox = document.getElementById(checkboxId);
        if (!mainCheckbox) {
            return;
        }
        mainCheckbox.addEventListener('change', function () {
            dependentIds.forEach(function (id) {
                const checkbox = document.getElementById(id);
                if (checkbox) {
                    checkbox.parentElement.style.display = this.checked ? 'block' : 'none';
                    if (!this.checked) {
                        checkbox.checked = false; // Uncheck the checkbox when main checkbox is unchecked
                    }
                } else {
                    // console.error('Checkbox not found:', id);
                }
            }, this);
        });
    }

    // Apply toggle functionality for shrung and learnShrung
    toggleDependentCheckboxes('shrung', ['turya', 'swarad', 'nagang', 'gomukh', 'other']);
    toggleDependentCheckboxes('learnShrung', ['learnTurya', 'learnSwarad', 'learnNagang', 'learnGomukh', 'learnOther']);
    // Show/hide specific checkboxes when shrung is checked
    document.getElementById('shrung').addEventListener('change', function () {
        const checkboxesToShow = ['turya', 'swarad', 'nagang', 'gomukh', 'other'];
        checkboxesToShow.forEach(function (id) {
            const checkbox = document.getElementById(id);
            if (checkbox) {
                checkbox.parentElement.style.display = this.checked ? 'block' : 'none';
                if (!this.checked) {
                    checkbox.checked = false; // Uncheck the checkbox when shrung is unchecked
                }
            } else {
                // console.error('Checkbox not found:', id);
            }
        }, this);
    });











//basic js

        const dobInput = document.getElementById('dob');
        // Function to open the date picker (works only on user click)
        function openDatePicker(event) {
            if (dobInput) {
                // Check if the 'showPicker' function is available and is being triggered by a user gesture
                if (typeof dobInput.showPicker === 'function') {
                    dobInput.showPicker();  // This will work only on valid user gestures (click/focus)
                } else {
                    dobInput.focus(); // Fallback if showPicker isn't supported
                }
            }
        }

        // Function to set the max date to today
        function setMaxDate() {
            const today = new Date();
            const year = today.getFullYear();
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const day = String(today.getDate()).padStart(2, '0');
            const formattedDate = `${year}-${month}-${day}`;

            if (dobInput) {
                dobInput.setAttribute('max', formattedDate);  // Set the max date to today
            }
        }

        // Add event listener only on user interaction
        if (dobInput) {
            dobInput.addEventListener('focus', openDatePicker);  // For Firefox
            dobInput.addEventListener('click', openDatePicker);  // For Chrome, Edge
            setMaxDate();
        }


    let vividhCheckbox = document.getElementById("vividhCheckbox");
    let referralCode = document.getElementById("referralCode");
    if (!vividhCheckbox.checked) {
        referralCode.value = "1925";
    }

    document.getElementById("referralCode").addEventListener("input", function () {
        const referralCodeError = document.getElementById("referralCodeError");
        // Remove non-alphanumeric characters
        this.value = this.value.replace(/[^a-zA-Z0-9]/g, '');
        // Validate: must be either all letters OR all numbers (not mixed)
        if (!(/^[A-Z]+$/i.test(this.value) || /^[0-9]+$/.test(this.value))) {
            referralCodeError.style.display = "block"; // Show Error
        } else {
            referralCodeError.style.display = "none"; // Hide Error
        }
    });




    //create options for all other fields
    function populateDropdown(field, options, placeholder) {

        let dropdown = document.getElementById(field);
        // Reset the dropdown
        dropdown.innerHTML = ""; // Clear all options

        // Add the placeholder option for the dropdown
        dropdown.innerHTML = `<option value="" disabled selected>${placeholder}</option>`;

        let first_options = [];
        let second_options = [];
        if (["prant", "vibhag", "jila", "ekai_nagar"].includes(field)) {
            first_options = options[0] || ""; // First element (if exists)
            second_options = options[1] || ""; // Second element (if exists)
            if (first_options) {
                let defaultOption = document.createElement("option");
                defaultOption.value = first_options;
                defaultOption.textContent = first_options;
                defaultOption.selected = true;
                dropdown.appendChild(defaultOption);
            }
        } else {
            first_options = options;
            if (first_options) {
                first_options.forEach(option => {
                    const opt = document.createElement("option");
                    opt.value = fieldToHindiMapping[option] ? fieldToHindiMapping[option] : option;
                    opt.textContent = fieldToHindiMapping[option] ? fieldToHindiMapping[option] : option;
                    dropdown.appendChild(opt);
                });
            }
            return;
        }
        if (field === "prant") {

            if (second_options) {
                second_options.forEach(option => {
                    if (option != first_options) {
                        const opt = document.createElement("option");
                        opt.value = fieldToHindiMapping[option] ? fieldToHindiMapping[option] : option;
                        opt.textContent = fieldToHindiMapping[option] ? fieldToHindiMapping[option] : option;
                        dropdown.appendChild(opt);
                    }
                });
            }
            return;

        }
        // Add other Jila first_options (if available)
        if (field === "jila") {
            if (second_options) {
                let vibhags = Array.isArray(second_options) ? second_options : [second_options];
                vibhags.forEach(vibhag => {
                    const jilas = mappings.VibhagToJila[vibhag] || [];
                    jilas.forEach(jila => {
                        if (jila !== first_options) { // Avoid duplicate selection
                            const option = document.createElement("option");
                            option.value = fieldToHindiMapping[jila] || jila;
                            option.textContent = fieldToHindiMapping[jila] || jila;
                            dropdown.appendChild(option);
                        }
                    });
                });
            }
            return;
        }


        if (field === "vibhag") {
            if (second_options) {
                const prants = Array.isArray(second_options) ? second_options : [second_options];

                prants.forEach(prant => {
                    const vibhags = mappings.prantToVibhag[prant] || [];
                    vibhags.forEach(vibhag => {
                        if (vibhag !== first_options) { // Avoid duplicate default selection
                            const option = document.createElement("option");
                            option.value = fieldToHindiMapping[vibhag] || vibhag;
                            option.textContent = fieldToHindiMapping[vibhag] || vibhag;
                            dropdown.appendChild(option);
                        }
                    });
                });
            }
            return;
        }



        if (field === "ekai_nagar") {
            if (second_options) { // second_options is the selected pincode
                const nagars = mappings.pincodeToNagar[second_options] || [];

                nagars.forEach(nagar => {
                    if (nagar !== first_options) { // Avoid duplicate default selection
                        const option = document.createElement("option");
                        option.value = fieldToHindiMapping[nagar] || nagar;
                        option.textContent = fieldToHindiMapping[nagar] || nagar;
                        dropdown.appendChild(option);
                    }
                });
            }
            return;
        }

    }


    function resetDropdowns(field) {
        const resetMappings = {
            referralCode: ["profession", "pincode", "prant", "vibhag", "jila", "ekai_nagar", "mandal", "basti", "sakha_milan", "dayitva", "state", "ekai"],
            pincode: ["nagar", "ekai_nagar", "mandal", "basti", "sakha_milan", "state", "ekai", "dayitva", "prant", "vibhag", "jila"],
            address_pincode: ["address_nagar", "address_state"],
            ekai: ["prant", "vibhag", "jila", "ekai_nagar", "mandal", "basti", "sakha_milan", "sakha_milanCheckbox", "dayitva"],
            nagar: ["ekai", "prant", "vibhag", "jila", "ekai_nagar", "upbasti", "dayitva"],
            mandal: ["mandal", "dayitva"],
            basti: ["basti", "dayitva"],
            sakha_milan: ["sakha_milan", "sakha_milanCheckbox", "dayitva"],
            ekai_nagar: ["ekai_nagar", "dayitva"],
            vividhSangathan: ["pincode", "dayitva", "nagar", "state"]
        };
        function resetDropdown(dropdownId) {
            if (dropdownId === "pincode") {
                document.getElementById("pincode").value = "";
                toggleVisibility("pincode");
            } else if (dropdownId === "sakha_milanCheckbox") {
                let checkbox = document.getElementById("sakha_milanCheckbox");
                if (checkbox.checked) {
                    checkbox.checked = false;
                }
            }
            populateDropdown(dropdownId, [], dropdownId);
        }
        if (resetMappings[field]) {
            resetMappings[field].forEach(resetDropdown);
        }
    }



    function handleDropdownChange(field, options) {
        resetDropdowns(field);
        toggleVisibility(field);
        const selectedValue = document.getElementById(field).value;
        const referralCode = document.getElementById("referralCode").value.trim();
        if (referralCode === "1925") {
            document.getElementById("ekai-container").style.display = "block";
        }
        populateDropdown("ekai", selectedValue ? options : [], "इकाई");
    }

    document.getElementById("state").addEventListener("change", function () {
        handleDropdownChange("state", ["akhilbhartiya", "chetra"]);
    });

    document.getElementById("upbasti").addEventListener("change", function () {
        handleDropdownChange("upbasti", ["प्रांत", "विभाग", "जिला", "नगर", "मंडल", "बस्ती", "शाखा / मिलन", "अखिलभारतीय", "क्षेत्र"]);
    });

    document.getElementById("nagar").addEventListener("change", function () {
        resetDropdowns("nagar");
        toggleVisibility("nagar");
    });

    function toggleVisibility(field) {
        // List of all containers to reset
        const allContainers = [
            "prant-container", "vibhag-container", "jila-container", "ekai_nagar-container", "mandal-container", "basti-container",
            "sakha_milanCheckbox-container", "sakha_milan-container", "dayitva-container", "state-container", "nagar-container", "ekai-container", "upbasti-container"
        ];

        // Hide all containers
        if (field === "address_pincode") {
            const allContainers = ["address_state-container", "address_nagar-container"];
            allContainers.forEach(id => document.getElementById(id).style.display = "none");
        } else {
            allContainers.forEach(id => document.getElementById(id).style.display = "none");
        }

        const referralCode = document.getElementById("referralCode").value.trim();
        const selectedPincode = document.getElementById("pincode").value.trim();
        const selectedAddressPincode = document.getElementById("address_pincode").value.trim();

        // Handle Pincode Cases
        if (field === "pincode" && selectedPincode.length === 6) {
            toggleElement(mappings.delhiPincodes.includes(selectedPincode) ? "nagar-container" : "state-container");
            populateDropdown(
                mappings.delhiPincodes.includes(selectedPincode) ? "nagar" : "state",
                mappings.delhiPincodes.includes(selectedPincode) ? mappings.pincodeToNagar[selectedPincode] || [] : mappings.pincodeToState[selectedPincode] || [],
                mappings.delhiPincodes.includes(selectedPincode) ? "नगर" : "राज्य"
            );
            return;
        }
        // Handle Address Pincode Cases
        if (field === "address_pincode" && selectedAddressPincode.length === 6) {
            toggleElement(mappings.delhiPincodes.includes(selectedAddressPincode) ? "address_nagar-container" : "address_state-container");
            populateDropdown(
                mappings.delhiPincodes.includes(selectedAddressPincode) ? "address_nagar" : "address_state",
                mappings.delhiPincodes.includes(selectedAddressPincode) ? mappings.pincodeToNagar[selectedAddressPincode] || [] : mappings.pincodeToState[selectedAddressPincode] || [],
                mappings.delhiPincodes.includes(selectedAddressPincode) ? "निवास का नगर" : "राज्य"
            );
            return;
        }
        if (field === "nagar") {
            toggleElement("nagar-container");
            let selectedNagar = document.getElementById("nagar").value;
            let options = [];
            let mandals = mappings.nagarToMandal[selectedNagar] || [];
            let bastis = mandals.flatMap(mandal => mappings.mandalToBasti[mandal] || []);
            options = bastis.flatMap(basti => mappings.bastiToUpbasti[basti] || []);
            populateDropdown("upbasti", options, "उपबस्ती");
            toggleElement("upbasti-container");
            return;
        }
        if (field === "upbasti") {
            toggleElement("upbasti-container");
            toggleElement("nagar-container");
            return;
        }
        if (field === "ekai") {
            let selectedEkai = document.getElementById("ekai").value;
            selectedEkai = `${hindiToEnglishMapping[selectedEkai]}`;
            toggleElement(mappings.delhiPincodes.includes(selectedPincode) ? "nagar-container" : "state-container");
            toggleElement("ekai-container");
            toggleElement("dayitva-container");
            // if (selectedEkai === "sakha_milan") {
            //     toggleElement("sakha_milanCheckbox-container");
            //     toggleElement("sakha_milan-container");
            // }
            toggleElement("sakha_milanCheckbox-container");
            toggleElement("sakha_milan-container");
            if (mappings.delhiPincodes.includes(selectedPincode) ? "nagar-container" : "state-container" === "nagar-container") {
                toggleElement("upbasti-container");
            }
            return;
        }

        // Define toggle conditions for each field
        const toggleMap = {
            ekai: referralCode === "1925" ? ["ekai-container"] : [],
            state: ["state-container", referralCode === "1925" ? "ekai-container" : null].filter(Boolean),
            address_state: ["address_state-container"]
        };

        // Handle ekai-specific conditions
        if (field === "dayitva" && referralCode === "1925") {

            if (mappings.delhiPincodes.includes(selectedPincode) ? "nagar-container" : "state-container" === "nagar-container") {
                toggleElement("upbasti-container");
            }

            let ekai = document.getElementById("ekai").value;
            ekai = `${hindiToEnglishMapping[ekai]}`;
            toggleElement("dayitva-container");
            const ekaiMappings = {
                "prant": ["nagar-container", "ekai-container", "prant-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "vibhag": ["nagar-container", "ekai-container", "vibhag-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "jila": ["nagar-container", "ekai-container", "jila-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "ekai_nagar": ["nagar-container", "ekai-container", "ekai_nagar-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "akhilbhartiya": [mappings.delhiPincodes.includes(selectedPincode) ? "nagar-container" : "state-container", "ekai-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "chetra": [mappings.delhiPincodes.includes(selectedPincode) ? "nagar-container" : "state-container", "ekai-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "mandal": ["nagar-container", "ekai-container", "mandal-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "basti": ["nagar-container", "ekai-container", "basti-container","sakha_milan-container", "sakha_milanCheckbox-container"],
                "sakha_milan": ["nagar-container", "ekai-container", "sakha_milan-container", "sakha_milanCheckbox-container"],
            };
            toggleMap[field] = ekaiMappings[ekai] || [];
        }
        // Toggle necessary elements
        (toggleMap[field] || []).forEach(toggleElement);
    }

    // Helper function to toggle visibility
    function toggleElement(elementId) {
        const element = document.getElementById(elementId);
        if (element.style.display === "none" || element.style.display === "") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    }

    document.getElementById("dayitva").addEventListener("change", function () {
        toggleVisibility("dayitva");
    });

      document.getElementById("ekai").addEventListener("change", function () {
        resetDropdowns("ekai");
        toggleVisibility("ekai");
        let selectedEkai = `${hindiToEnglishMapping[this.value]}`;
        let selectedNagar = document.getElementById("nagar").value;
        let selectedPincode = document.getElementById("pincode").value;
        let selectedUpbasti = document.getElementById("upbasti").value;

        let selectedJila = Object.keys(mappings.jilaToNagar).find(jila =>
            mappings.jilaToNagar[jila].includes(selectedNagar)
        );

        let selectedVibhag = Object.keys(mappings.VibhagToJila).find(vibhag =>
            mappings.VibhagToJila[vibhag].includes(selectedJila)
        );

        let selectedPrant = Object.keys(mappings.prantToVibhag).find(prant =>
            mappings.prantToVibhag[prant].includes(selectedVibhag)
        );

        let selectedNagars = mappings.pincodeToNagar[selectedPincode] || [];

        const selectedJilas = Object.keys(mappings.jilaToNagar).filter(jila =>
            mappings.jilaToNagar[jila].some(nagar => selectedNagars.includes(nagar))
        );
        // Step 3: Find all vibhags that include any of the selected jilas
        const selectedVibhags = Object.keys(mappings.VibhagToJila).filter(vibhag =>
            mappings.VibhagToJila[vibhag].some(jila => selectedJilas.includes(jila))
        );

        // Step 4: Find all prants that include any of the selected vibhags
        const selectedPrants = Object.keys(mappings.prantToVibhag).filter(prant =>
            mappings.prantToVibhag[prant].some(vibhag => selectedVibhags.includes(vibhag))
        );


        if (selectedEkai === "prant") {

            populateDropdown("prant", [selectedPrant, mappings.prant], "प्रांत");
        } else if (selectedEkai === "vibhag") {
            // populateDropdown("prant", [selectedPrant]);
            populateDropdown("vibhag", [selectedVibhag, selectedPrant], "विभाग");
        } else if (selectedEkai === "jila") {
            // populateDropdown("prant", [selectedPrant]);        
            // populateDropdown("vibhag", [selectedVibhag, selectedPrant]);
            populateDropdown("jila", [selectedJila, selectedVibhags], "जिला");
        }
        else if (selectedEkai === "ekai_nagar") {
            // populateDropdown("prant", [selectedPrant]);
            // populateDropdown("vibhag", [selectedVibhag,selectedPrant]);
            // populateDropdown("jila", [selectedJila, selectedVibhag]);
            populateDropdown("ekai_nagar", [selectedNagar, selectedPincode], "नगर");
        } else if (["mandal", "basti", "sakha_milan"].includes(selectedEkai)) {
            let options = [];
            options = mappings.pincodeToNagar[selectedPincode] || [];
            //const result = findBastiAndMandal(mappings.nagarToMandal, mappings.mandalToBasti, mappings.bastiToUpbasti, selectedNagar, selectedUpbasti);
            //console.log(result);

            //console.log("Found Basti:", typeof(result.basti));

            if (selectedEkai === "mandal") {
                options = mappings.nagarToMandal[selectedNagar] || [];
            } else if (selectedEkai === "basti") {
                let mandals = mappings.nagarToMandal[selectedNagar] || [];
                options = mandals.flatMap(mandal => mappings.mandalToBasti[mandal] || []);
            } else if (selectedEkai === "sakha_milan") {
                options = sakha_milan;
            }
            populateDropdown(selectedEkai, options, `${fieldToHindiMapping[selectedEkai]}`);
        }
        populateDropdown("sakha_milan", sakha_milan, `${fieldToHindiMapping["sakha_milan"]}`);
        populateDayitva(selectedEkai);
    });

    // Populate dayitva dropdown
    function populateDayitva(selectedEkai) {
        if (selectedEkai === "nagar") {
            populateDropdown("dayitva", mappings.dayitvaMapping["ekai_nagar"] || [], "दायित्व");
        } else if (selectedEkai === "sakha_milan") {
            populateDropdown("dayitva", mappings.dayitvaMapping["shakha"] || [], "दायित्व");
        } else {
            populateDropdown("dayitva", mappings.dayitvaMapping[selectedEkai] || [], "दायित्व");
        }
    }

    // Handle vividhSangathan checkbox
    document.getElementById("vividhCheckbox").addEventListener("change", function () {
        resetDropdowns("vividhSangathan");
        toggleVisibility("vividhSangathan");
        const vividhSangathanDiv = document.getElementById("vividhSangathan-container");
        const referralCode = document.getElementById("referralCode").value.trim();
        let options = ["अखिल भारतीय विद्यार्थी परिषद", "विद्याभारती", "भारतीय शिक्षण मंडल", "अखिल भारतीय शैक्षिक महासंघ", "संस्कृत भारती", "शिक्षा संस्कृति उत्थान न्यास", "वनवासी कल्याण आश्रम", "विश्व हिन्दू परिषद्", "भारतीय जनता पार्टी", "राष्ट्रीय सिक्ख संगत", "क्रीडा भारती", "संस्कार भारती", "सक्षम", "आरोग्य भारती", "एन्. एम्. ओ. (नैशनल मैडिकल आर्गेनाइजेशन)"];
        document.getElementById("referralCode").value = "";
        if (this.checked === false) {
            document.getElementById("referralCode").value = "1925";
        } else {
            document.getElementById("referralCode").value = "";
        }
        populateDropdown("vividhSangathan", options, `${fieldToHindiMapping["vividhSangathan"]}`);
        vividhSangathanDiv.style.display = this.checked ? "block" : "none";
    });

    document.getElementById("vividhSangathan").addEventListener("change", function () {
        resetDropdowns("vividhSangathan");
        toggleVisibility("vividhSangathan");
        const selectedValue = document.getElementById("vividhSangathan").value;
        const referralCodeField = document.getElementById("referralCode");
        if (selectedValue && sangathanToReferralCode[selectedValue]) {
            referralCodeField.value = sangathanToReferralCode[selectedValue];
        } else {
            referralCodeField.value = "0000"; // Default value
        }
    });

    // Handle referral code change
    document.getElementById("referralCode").addEventListener("change", function () {
        resetDropdowns("referralCode");
        const referralCode = this.value.trim();
        let vividhCheckbox = document.getElementById("vividhCheckbox");
        if (!vividhCheckbox.checked) {
            this.value = "1925";
        } else {
            this.value = "";
        }
        document.getElementById("vividhSangathan-container").style.display = document.getElementById("vividhCheckbox").checked ? "block" : "none";

        const professionDropdown = document.getElementById("profession");
        const pincodeField = document.getElementById("pincode");
        pincodeField.value = "";
        const professionOptions = referralCode === "1925" ? ["स्कूल-विद्यार्थी", "कॉलेज-विद्यार्थी", "अध्यापक", "प्राध्यापक", "कर्मचारी (सरकारी)", "कर्मचारी (अन्य)", "व्यवसायी", "उद्योगपति",
            "प्रोफेशनल", "सेवा-निवृत्त", "गृहिणी", "श्रमिक", "कृषक (किसान)", "प्रचारक", "विस्तारक", "पूर्णकालिक"] : [
            "स्कूल-विद्यार्थी", "कॉलेज-विद्यार्थी", "अध्यापक", "प्राध्यापक",
            "कर्मचारी (सरकारी)", "कर्मचारी (अन्य)", "व्यवसायी", "उद्योगपति",
            "प्रोफेशनल", "सेवा-निवृत्त", "गृहिणी", "श्रमिक", "कृषक (किसान)"
        ];
        populateDropdown("profession", professionOptions, "श्रेणी");

        let matchedSangathan = Object.keys(sangathanToReferralCode).find(
            (key) => sangathanToReferralCode[key] === referralCode
        );
        if (matchedSangathan) {
            document.getElementById("vividhSangathan").value = matchedSangathan;
        } else {
            document.getElementById("vividhSangathan").innerHTML =
                '<option value="" disabled selected>विविध संगठन</option>';
            Object.keys(sangathanToReferralCode).forEach(sangathanName => {
                const option = document.createElement("option");
                option.value = sangathanName;
                option.textContent = sangathanName;
                document.getElementById("vividhSangathan").appendChild(option);
            });
        }
    });

    const cardFields = {
        card_body_1: {
            fields: {
                name: { type: 'text', required: true, pattern: /^[a-zA-Z\u0900-\u097F\s]+$/ },
                lastName: { type: 'text', required: true, pattern: /^[a-zA-Z\u0900-\u097F\s]+$/ },
                dob: { type: 'text', required: true },
                currentAddress: { type: 'text', required: true },
                permanentAddress: { type: 'text', required: true },
                address_pincode: { type: 'text', required: true, pattern: /^\d{6}$/ },
                blood_group: { type: 'select', required: true },
                profession: { type: 'select', required: true },
                nagar_address: { type: 'select', required: false },
                address_state: { type: 'select', required: false }
            },
            specialCases: {
                gender: {
                    type: 'radio',
                    required: true,
                    selector: 'input[name="gender"]:checked',
                    errorId: 'genderError',
                    errorMessage: 'Please select a gender'
                }
            }
        },
        card_body_2: {
            fields: {
                pincode: { type: 'text', required: true, pattern: /^\d{6}$/ },
                nagar: { type: 'select', required: false },
                state: { type: 'select', required: false },
                upbasti: { type: 'select', required: false },
                ekai: { type: 'select', required: false },
                dayitva: { type: 'select', required: false },
                prant: { type: 'select', required: false },
                vibhag: { type: 'select', required: false },
                jila: { type: 'select', required: false },
                ekai_nagar: { type: 'select', required: false },
                basti: { type: 'select', required: false },
                mandal: { type: 'select', required: false },
                sakha_milan: { type: 'select', required: false },
                vividhSangathan: { type: 'select', required: false }
            },
            specialCases: {
                vividhSangathan: {
                    type: 'conditionalSelect',
                    checkboxId: 'vividhCheckbox',
                    fieldId: 'vividhSangathan',
                    errorId: 'vividhSangathanError',
                    errorMessage: 'Please select an option'
                }
            }
        },
        card_body_3: {
            fields: {
                sangh_shikshan_level: { type: 'select', required: true },
                // prarambhik_year: { type: 'select', required: true },
                prathmik_year: { type: 'select', required: true },
                pratham_year: { type: 'select', required: true },
                dwitiya_year: { type: 'select', required: true },
                tritiya_year: { type: 'select', required: true },
                ghosh_vadak: { type: 'radio', required: true, selector: 'input[name="ghosh_vadak"]:checked' }
            },
            specialCases: {
                // ghoshVadakInstrument: {
                //     type: 'conditionalCheckbox',
                //     radioSelector: 'input[name="ghosh_vadak"]:checked',
                //     checkboxSelector: 'input[name="vadya[]"]:checked',
                //     errorId: 'ghosh_vadakError',
                //     errorMessage: 'Please select at least one instrument',
                //     conditionValue: 'हाँ'
                // }
            }
        }
    };

    const cards = [];
    function validateFields(fields, specialCases = {}, cardId) {
        let valid = true;

        for (const [fieldId, config] of Object.entries(fields)) {
            const element = document.getElementById(fieldId);
            const errorElement = document.getElementById(`${fieldId}Error`);

            if (!element || element.style.display === 'none' || element.parentElement.style.display === 'none') {
                continue;
            }

            if (config.type === 'text') {
                const value = element.value.trim();
                if ((config.required || isFieldVisible(element.id)) && !value) {
                    showErrors(errorElement, 'This field is required');
                    valid = false;
                } else if (config.pattern && !config.pattern.test(value)) {
                    showErrors(errorElement, 'Please enter a valid value');
                    valid = false;
                } else {
                    hideErrors(errorElement);
                }
            } else if (config.type === 'select') {
                if ((config.required || isFieldVisible(element.id)) && (!element.value || element.value === '')) {
                    showErrors(errorElement, 'Please select an option');
                    valid = false;
                } else {
                    hideErrors(errorElement);
                }
            }
        }

        for (const [key, config] of Object.entries(specialCases)) {
            if (config.type === 'radio') {
                const selected = document.querySelector(config.selector);
                if (!selected) {
                    showErrors(document.getElementById(config.errorId), config.errorMessage);
                    valid = false;
                } else {
                    hideErrors(document.getElementById(config.errorId));
                }
            } else if (config.type === 'conditionalSelect') {
                const checkbox = document.getElementById(config.checkboxId);
                if (checkbox && checkbox.checked) {
                    const select = document.getElementById(config.fieldId);
                    if (!select.value) {
                        showErrors(document.getElementById(config.errorId), config.errorMessage);
                        valid = false;
                    } else {
                        hideErrors(document.getElementById(config.errorId));
                    }
                }
            } else if (config.type === 'dynamicYears') {
                const container = document.getElementById(config.containerId);
                if (container.style.display !== 'none') {
                    const inputs = container.querySelectorAll(config.inputSelector);
                    inputs.forEach(input => {
                        if (!input.value) {
                            showErrors(document.getElementById(`${input.name}Error`), config.errorMessage);
                            valid = false;
                        } else {
                            hideErrors(document.getElementById(`${input.name}Error`));
                        }
                    });
                }
            } else if (config.type === 'conditionalCheckbox') {
                const radio = document.querySelector(config.radioSelector);
                if (radio && radio.value === config.conditionValue) {
                    const checkboxes = document.querySelectorAll(config.checkboxSelector);
                    const anyChecked = Array.from(checkboxes).some(cb => cb.checked);
                    if (!anyChecked) {
                        showErrors(document.getElementById(config.errorId), config.errorMessage);
                        valid = false;
                    } else {
                        hideErrors(document.getElementById(config.errorId));
                    }
                }
            }
        }

        const cardElement = document.querySelector(`#${cardId}`).parentElement;
        cardElement.classList.remove('border-success', 'border-danger');
        cardElement.classList.add(valid ? 'border-success' : 'border-danger');

        return valid;
    }



    // function validateForm() {
    //     let isValid = true;

    //     for (const [cardId, card] of Object.entries(cardFields)) {
    //         if (!validateFields(card.fields, card.specialCases, cardId)) {
    //             isValid = false;
    //         }
    //     }
    //     if (isValid) {
    //         // console.log("Form is valid. Showing modal...");
    //         openModal();
    //     }

    //     return isValid;
    // }
    
    function validateForm(event) {
        event.preventDefault(); // Prevent default form submission
        let isValid = true;
        let firstInvalidCard = null;
        // First pass: Check all cards for border-danger class
        for (const [cardId] of Object.entries(cardFields)) {
            const cardElement = document.querySelector(`#${cardId}`).parentElement;
            const isInvalid = cardElement.classList.contains('border-success');
            if (!isInvalid) {
                isValid = false;
                if (!firstInvalidCard) {
                    firstInvalidCard = cardId;
                }
                const errorMessage = document.querySelector(`#${cardId}Error`);
                showErrors(errorMessage, "Please complete all required fields in this section");
                // Hide after 5 seconds
                    setTimeout(() => {
                        hideErrors(errorMessage);
                    }, 5000);
    
                // Expand invalid card if collapsed
                const card = cards.find(c => c.cardId === cardId);
                if (card && card.cardBody.style.height === '0px') {
                    gsap.to(card.cardBody, {
                        height: "auto",
                        padding: "1rem",
                        opacity: 1,
                        duration: 0.8,
                        ease: "power2.inOut"
                    });
                    gsap.to(card.toggleIcon, {
                        opacity: 0,
                        duration: 0.3,
                        ease: "power2.inOut",
                        onComplete: () => {
                            card.toggleIcon.classList.remove('fa-plus');
                            card.toggleIcon.classList.add('fa-minus');
                            gsap.to(card.toggleIcon, { opacity: 1, duration: 0.15, ease: "power2.inOut" });
                        }
                    });
                }
            }
        }
    
        // Second pass: If form is valid, submit it
        if (isValid) {
            console.log("Form is valid. Showing modal...");
            openModal();
        } else {
            // Scroll to the first invalid card
            if (firstInvalidCard) {
                const cardElement = document.querySelector(`#${firstInvalidCard}`).parentElement;
                cardElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                
                // Show error message for the first invalid card
                const errorMessage = document.querySelector(`#${firstInvalidCard}Error`);
                showErrors(errorMessage, "Please complete all required fields in this section");
            }
        }
    
        return isValid;
    }

    function showErrors(errorElement, message) {
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.style.display = 'block';
            //   if (errorElement.previousElementSibling) {
            //       errorElement.previousElementSibling.classList.add('is-invalid');
            //   }
        }
    }

    function hideErrors(errorElement) {
        if (errorElement) {
            errorElement.style.display = 'none';
            //   if (errorElement.previousElementSibling) {
            //       errorElement.previousElementSibling.classList.remove('is-invalid');
            //   }
        }
    }

    function setupCardToggle(headerSelector, bodySelector, cardId) {
        const header = document.querySelector(headerSelector);
        const cardBody = document.querySelector(bodySelector);
        const toggleIcon = header ? header.querySelector(".toggle-icon i") : null;

        cards.push({ header, cardBody, toggleIcon, cardId });

        header.addEventListener('click', () => {
            const isOpen = cardBody.style.height && cardBody.style.height !== '0px';

            cards.forEach(card => {
                if (card.header !== header && card.cardBody.style.height !== '0px') {
                    gsap.to(card.cardBody, {
                        height: 0,
                        padding: 0,
                        opacity: 0,
                        duration: 0.8,
                        ease: "power2.inOut"
                    });
                    gsap.to(card.toggleIcon, {
                        opacity: 0,
                        duration: 0.15,
                        ease: "power2.inOut",
                        onComplete: () => {
                            card.toggleIcon.classList.remove('fa-minus');
                            card.toggleIcon.classList.add('fa-plus');
                            gsap.to(card.toggleIcon, { opacity: 1, duration: 0.15, ease: "power2.inOut" });
                        }
                    });
                }
            });

            if (isOpen) {
                gsap.to(cardBody, {
                    height: 0,
                    padding: 0,
                    opacity: 0,
                    duration: 0.8,
                    ease: "power2.inOut"
                });
                gsap.to(toggleIcon, {
                    opacity: 0,
                    duration: 0.3,
                    ease: "power2.inOut",
                    onComplete: () => {
                        toggleIcon.classList.remove('fa-minus');
                        toggleIcon.classList.add('fa-plus');
                        gsap.to(toggleIcon, { opacity: 1, duration: 0.15, ease: "power2.inOut" });
                    }
                });
                validateFields(cardFields[cardId].fields, cardFields[cardId].specialCases, cardId);
            } else {
                gsap.to(cardBody, {
                    height: "auto",
                    padding: "1rem",
                    opacity: 1,
                    duration: 0.8,
                    ease: "power2.inOut"
                });
                gsap.to(toggleIcon, {
                    opacity: 0,
                    duration: 0.3,
                    ease: "power2.inOut",
                    onComplete: () => {
                        toggleIcon.classList.remove('fa-plus');
                        toggleIcon.classList.add('fa-minus');
                        gsap.to(toggleIcon, { opacity: 1, duration: 0.15, ease: "power2.inOut" });
                    }
                });
                validateFields(cardFields[cardId].fields, cardFields[cardId].specialCases, cardId);
            }
        });
    }


    document.querySelectorAll('.card-header[data-toggle-target]').forEach(header => {
        const bodyId = header.getAttribute('data-toggle-target');
        const cardId = bodyId; // Use full id like 'card1', 'card2', etc.
        setupCardToggle(`[data-toggle-target="${bodyId}"]`, `#${bodyId}`, cardId);

    });












    const sameAddress = document.getElementById("sameAddress");
    const permanentAddress = document.getElementById("permanentAddress");
    const currentAddress = document.getElementById("currentAddress");
    if (sameAddress.checked) {
        // Copy current address immediately
        permanentAddress.value = currentAddress.value;
        permanentAddress.setAttribute("readonly", true);
        permanentAddress.dispatchEvent(new Event("input"));
        document.getElementById("permanentAddress-container").style.display = "none";
        // Sync permanent address with current address as user types
        currentAddress.addEventListener("input", syncAddress);
    } else {
        // Clear permanent address and remove readonly
        permanentAddress.value = "";
        permanentAddress.removeAttribute("readonly");
        permanentAddress.dispatchEvent(new Event("input"));
        document.getElementById("permanentAddress-container").style.display = "block";
        // Remove the event listener to stop syncing
        currentAddress.removeEventListener("input", syncAddress);
    }

    // स्थायी और वर्तमान पता स्विच करने के लिए फ़ंक्शन
    document.getElementById("sameAddress").addEventListener("change", function () {
        const permanentAddress = document.getElementById("permanentAddress");
        const currentAddress = document.getElementById("currentAddress");
        if (this.checked) {
            // Copy current address immediately
            permanentAddress.value = currentAddress.value;
            permanentAddress.setAttribute("readonly", true);
            permanentAddress.dispatchEvent(new Event("input"));
            document.getElementById("permanentAddress-container").style.display = "none";
            currentAddress.addEventListener("input", syncAddress);
        } else {
            // Clear permanent address and remove readonly
            permanentAddress.value = "";
            permanentAddress.removeAttribute("readonly");
            permanentAddress.dispatchEvent(new Event("input"));
            document.getElementById("permanentAddress-container").style.display = "block";
            // Remove the event listener to stop syncing
            currentAddress.removeEventListener("input", syncAddress);
        }
    });

    // Function to copy address as user types
    function syncAddress() {
        document.getElementById("permanentAddress").value = document.getElementById("currentAddress").value;
    }

    // Name Validation: Only Letters Allowed (No Spaces, Digits, or Special Characters)
    const nameField = document.getElementById("name");
    const lastNameField = document.getElementById("lastName");
    const dayitva_pincodeField = document.getElementById("pincode");
    const address_pincodeField = document.getElementById("address_pincode");
    if (nameField) {
        nameField.addEventListener("input", function () {
            this.value = this.value.replace(/[^A-Za-z]/g, ""); // Remove everything except letters
            if (this.value) {
                hideError("name");
            } else {
                showError("name", "Only letters are allowed.");
            }
        });
    }
    if (lastNameField) {
        lastNameField.addEventListener("input", function () {
            this.value = this.value.replace(/[^A-Za-z]/g, ""); // Remove everything except letters
            if (this.value) {
                hideError("lastName");
            } else {
                showError("lastName", "Only letters are allowed.");
            }
        });
    }

    // Function to validate pincode fields
    function validatePincode(event) {
        let pincodeField = event.target;
        let errorElement = document.getElementById(pincodeField.id + "Error");

        pincodeField.value = pincodeField.value.replace(/\D/g, "").slice(0, 6); // Allow only digits, max length 6

        if (this.value.length === 6) {
            hideError(pincodeField.id);
        } else {
            showError(pincodeField.id, "Pincode must be exactly 6 digits.");
        }
        toggleVisibility(pincodeField.id);
    }

    // Attach validation to both pincode fields
    document.getElementById("pincode").addEventListener("input", validatePincode);
    document.getElementById("address_pincode").addEventListener("input", validatePincode);

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


    // Attach the validation function to the form's submit event
    const form = document.getElementById("myForm");
    if (form) {
        form.addEventListener("submit", validateForm);
    } else {
        // console.error("Form not found!");
    }

    // ✅ Add real-time error hiding
    function addRealTimeValidation(fieldId, eventType = "input") {
        const field = document.getElementById(fieldId);
        if (field) {
            field.addEventListener(eventType, function () {
                if (field.value.trim()) {
                    hideError(fieldId);
                }
            });
        }
    }

    // ✅ Apply real-time validation to text fields
    const realTimeTextFields = ["referralCode", "name", "dob", "currentAddress", "permanentAddress", "pincode", "address_pincode"];
    realTimeTextFields.forEach((fieldId) => addRealTimeValidation(fieldId));

    // ✅ Apply real-time validation to dropdowns
    const realTimeSelectFields = ["blood_group", "profession", "address_nagar", "nagar", "address_state", "state", "upbasti", "ekai", "prant", "vibhag", "jila", "ekai_nagar", "mandal", "basti", "sakha_milan", "dayitva", "vividhSangathan",
        "sangh_shikshan_level", "prarambhik_year", "pratham_year", "prathmik_year", "dwitiya_year", "tritiya_year"
    ];
    realTimeSelectFields.forEach((fieldId) => {
        const field = document.getElementById(fieldId);
        if (field) {
            field.addEventListener("change", function () {
                if (field.value) {
                    hideError(fieldId);
                }
            });
        }
    });



    //  Real-time validation for gender selection
    document.querySelectorAll('input[name="gender"]').forEach((radio) => {
        radio.addEventListener("change", function () {
            hideError("gender");
        });
    });

    // Function to open the modal and populate it with form data
function openModal() {
    const modal = document.getElementById('formModal');
    modal.style.display = 'flex';

    // Function to set modal content and visibility for text fields
    function setModalContent(fieldId, modalElementId, modalContainerId) {
        const field = document.getElementById(fieldId);
        const modalContainer = document.getElementById(modalContainerId);

        if (isFieldVisible(fieldId)) {
            modalContainer.style.display = 'table-row'; // Show the entire row
            document.getElementById(modalElementId).textContent = field.value || 'N/A';
        } else {
            modalContainer.style.display = 'none'; // Hide the entire row
        }
    }

    // Function to set modal content and visibility for radio buttons
    function setRadioModalContent(radioName, modalElementId, modalContainerId) {
        // console.log("executed");
        const radioField = document.querySelector(`input[name="${radioName}"]:checked`);
        const modalContainer = document.getElementById(modalContainerId);
        // console.log("Outside radio field", radioField, modalContainerId, modalContainer,isFieldVisible(radioName), "fgtergfdgf", radioField && isFieldVisible(radioName));
        if (radioField && isFieldVisible(radioName)) {
            modalContainer.style.display = 'table-row'; // Show the entire row
            document.getElementById(modalElementId).textContent = radioField.value;
        } else {
            modalContainer.style.display = 'none'; // Hide the entire row
        }
    }

    // Function to set modal content and visibility for checkboxes
    // function setCheckboxModalContent(checkboxName, modalElementId, modalContainerId) {
    //     const checkboxes = document.querySelectorAll(`input[name="${checkboxName}"]:checked`);
    //     const modalContainer = document.getElementById(modalContainerId);
    //     console.log("id-container", modalContainerId);
    //     if (checkboxes.length > 0 && isFieldVisible(checkboxName)) {
    //         console.log("Checkbox***************",modalContainerId, modalContainer);
    //         modalContainer.style.display = 'table-row'; // Show the entire row
    //         const values = Array.from(checkboxes).map(checkbox => checkbox.value).join(', ');
    //         document.getElementById(modalElementId).textContent = values || 'None';
    //     } else {
    //         modalContainer.style.display = 'none'; // Hide the entire row
    //     }
    // }

    // Function to handle individual checkbox fields (like shankh, shrung etc.)
    function setIndividualCheckboxContent(checkboxId, modalElementId, modalContainerId) {
        const checkbox = document.getElementById(checkboxId);
        const modalContainer = document.getElementById(modalContainerId);
        if (checkbox && checkbox.checked && isFieldVisible(checkboxId)) {
            modalContainer.style.display = 'table-row';
            document.getElementById(modalElementId).textContent = checkbox.value;
        } else {
            modalContainer.style.display = 'none';
        }
    }

    // Set content for text fields
    setModalContent('referralCode', 'modalReferralCode', 'modalReferralCodeContainer');
    setModalContent('name', 'modalName', 'modalNameContainer');
    setModalContent('lastName', 'modalLastName', 'modalLastNameContainer');
    setModalContent('dob', 'modalDOB', 'modalDOBContainer');
    setModalContent('blood_group', 'modalBloodGroup', 'modalBloodGroupContainer');
    setModalContent('profession', 'modalProfession', 'modalProfessionContainer');
    setModalContent('currentAddress', 'modalCurrentAddress', 'modalCurrentAddressContainer');
    setModalContent('permanentAddress', 'modalPermanentAddress', 'modalPermanentAddressContainer');
    setModalContent('address_pincode', 'modalAddressPincode', 'modalAddressPincodeContainer');
    setModalContent('address_nagar', 'modalAddressNagar', 'modalAddressNagarContainer');
    setModalContent('address_state', 'modalAddressState', 'modalAddressStateContainer');
    setModalContent('vividhSangathan', 'modalVividhSangathan', 'modalVividhSangathanContainer');
    setModalContent('pincode', 'modalPincode', 'modalPincodeContainer');
    setModalContent('nagar', 'modalNagar', 'modalNagarContainer');
    setModalContent('state', 'modalState', 'modalStateContainer');
    setModalContent('upbasti', 'modalUpbasti', 'modalUpbastiContainer');
    setModalContent('ekai', 'modalEkai', 'modalEkaiContainer');
    setModalContent('prant', 'modalPrant', 'modalPrantContainer');
    setModalContent('vibhag', 'modalVibhag', 'modalVibhagContainer');
    setModalContent('jila', 'modalJila', 'modalJilaContainer');
    setModalContent('ekai_nagar', 'modalEkaiNagar', 'modalEkaiNagarContainer');
    setModalContent('mandal', 'modalMandal', 'modalMandalContainer');
    setModalContent('basti', 'modalBasti', 'modalBastiContainer');
    setModalContent('sakha_milan', 'modalSakhaMilan', 'modalSakhaMilanContainer');
    setModalContent('dayitva', 'modalDayitva', 'modalDayitvaContainer');
    setModalContent('sangh_shikshan_level', 'modalSanghSikshanLevel', 'modalSanghSikshanLevelContainer');
    setIndividualCheckboxContent('pratigyaCheckbox', 'modalPratigyaCheckbox', 'modalPratigyaCheckboxContainer');
    setModalContent('prarambhik_year', 'modalPrarambhikYear', 'modalPrarambhikYearContainer');
    setModalContent('prathmik_year', 'modalPrathmikYear', 'modalPrathmikYearContainer');
    setModalContent('pratham_year', 'modalPrathamYear', 'modalPrathamYearContainer');
    setModalContent('dwitiya_year', 'modalDwitiyaYear', 'modalDwitiyaYearContainer');
    setModalContent('tritiya_year', 'modalTritiyaYear', 'modalTritiyaYearContainer');

    // Handle radio buttons for learn_vadya (Yes/No)
    setRadioModalContent('learn_vadya', 'modalLearnVadya', 'modalLearnVadyaContainer');

    // Handle radio buttons for learn_vadya_list (instruments)
    setRadioModalContent('learn_vadya_list', 'modalLearnVadyaList', 'modalLearnVadyaListContainer');

    // Handle assumed checkboxes for clothing and other items
    setIndividualCheckboxContent('sanghPant', 'modalSanghPant', 'modalSanghPantContainer');
    setIndividualCheckboxContent('safedKameez', 'modalSafedKameez', 'modalSafedKameezContainer');
    setIndividualCheckboxContent('sanghTopi', 'modalSanghTopi', 'modalSanghTopiContainer');
    setIndividualCheckboxContent('sanghPeti', 'modalSanghPeti', 'modalSanghPetiContainer');
    setIndividualCheckboxContent('jurab', 'modalJurab', 'modalJurabContainer');
    setIndividualCheckboxContent('joote', 'modalJoote', 'modalJooteContainer');
    setIndividualCheckboxContent('dand', 'modalDand', 'modalDandContainer');

    // Handle gender (radio button)
    setRadioModalContent('gender', 'modalGender', 'modalGenderContainer');
    
    // Handle ghosh_vadak (radio button)
    setRadioModalContent('ghosh_vadak', 'modalGhoshVadak', 'modalGhoshVadakContainer');
    
    // Handle individual instrument checkboxes (only shown if ghosh_vadak is 'yes')
    if (document.querySelector('input[name="ghosh_vadak"]:checked')?.value === 'हाँ') {
        setIndividualCheckboxContent('shankh', 'modalShankh', 'modalShankhContainer');
        setIndividualCheckboxContent('shrung', 'modalShrung', 'modalShrungContainer');
        setIndividualCheckboxContent('turya', 'modalTurya', 'modalTuryaContainer');
        setIndividualCheckboxContent('swarad', 'modalSwarad', 'modalSwaradContainer');
        setIndividualCheckboxContent('nagang', 'modalNagang', 'modalNagangContainer');
        setIndividualCheckboxContent('gomukh', 'modalGomukh', 'modalGomukhContainer');
        setIndividualCheckboxContent('other', 'modalOther', 'modalOtherContainer');
        setIndividualCheckboxContent('aanak', 'modalAanak', 'modalAanakContainer');
        setIndividualCheckboxContent('panav', 'modalPanav', 'modalPanavContainer');
        setIndividualCheckboxContent('jhallari', 'modalJhallari', 'modalJhallariContainer');
        setIndividualCheckboxContent('tribhuj', 'modalTribhuj', 'modalTribhujContainer');
        
        // Handle shankh_shrung_own checkbox
        setIndividualCheckboxContent('shankhShrungOwn', 'modalShankhShrungOwn', 'modalShankhShrungOwnContainer');
        
        // Handle rachnaye radio buttons
        setRadioModalContent('rachnaye', 'modalRachnaye', 'modalRachnayeContainer');
    } else {
        // Hide all ghosh-related fields if ghosh_vadak is not 'yes'
        document.getElementById('modalShankhContainer').style.display = 'none';
        document.getElementById('modalShrungContainer').style.display = 'none';
        document.getElementById('modalTuryaContainer').style.display = 'none';
        document.getElementById('modalSwaradContainer').style.display = 'none';
        document.getElementById('modalNagangContainer').style.display = 'none';
        document.getElementById('modalGomukhContainer').style.display = 'none';
        document.getElementById('modalOtherContainer').style.display = 'none';
        document.getElementById('modalAanakContainer').style.display = 'none';
        document.getElementById('modalPanavContainer').style.display = 'none';
        document.getElementById('modalJhallariContainer').style.display = 'none';
        document.getElementById('modalTribhujContainer').style.display = 'none';
        document.getElementById('modalShankhShrungOwnContainer').style.display = 'none';
        document.getElementById('modalRachnayeContainer').style.display = 'none';
    }
}

    // Function to check if a field is visible
    function isFieldVisible(fieldId) {
        let field;
        if (fieldId === "learn_vadya" || fieldId === "learn_vadya_list") {
            field = document.getElementById("ghoshVadakNo-container");
        } else {
            field = document.getElementById(`${fieldId}-container`);
        }
        return field && field.style.display !== "none";
    }
    

    // Attach event listener to the 'Edit' button
    document.querySelector(".class-modal").addEventListener('click', function () {
        document.getElementById("formModal").style.display = "none";
    })

    document.getElementById('finalSubmit').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default form submission

        Swal.fire({
            title: '!!..धन्यवाद..!!',
            html: 'आपने अपना पंजीकरण सफलतापूर्वक पूर्ण कर लिया है। <br>आपके "QR Code" की जानकारी दिए गए 👉 "SBRPLR SMS Code" 👈 द्वारा आपको शीघ्र भेजी जाएगी।',
            icon: 'success',
            confirmButtonText: 'ठीक है'
        }).then((result) => {
            if (result.isConfirmed) {
                // Submit the form after clicking "OK"
                document.getElementById('myForm').submit();
            }
        });
    });
});
