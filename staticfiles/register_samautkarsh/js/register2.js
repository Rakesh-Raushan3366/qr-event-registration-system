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
    console.log(mappings);

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
        "स्कूल विद्यार्थी", "कॉलेज विद्यार्थी", "तरुण व्यवसायी", "प्रौढ़ व्यवसायी", "Young Professional", "प्राध्यापक", "Summer Camp", "परिवार मिलन", "अन्य", "अभी तक किसी शाखा/मिलन से नहीं जुड़े हैं / सज्जन शक्ति",
    ]

    const fieldToHindiMapping = {
        prant: "प्रांत", vibhag: "विभाग", jila: "जिला", nagar: "नगर", address_nagar: "नगर", mandal: "मंडल", basti: "बस्ती", upbasti: "उपबस्ती", ekai_nagar: "नगर",
        sakha_milan: "शाखा / मिलन", vividhSangathan: "विविध संगठन", "akhilbhartiya": "अखिलभारतीय", "chetra": "क्षेत्र",
    };

    const hindiToEnglishMapping = {
        "प्रांत": "prant", "विभाग": "vibhag", "जिला": "jila", "नगर": "nagar", "नगर": "address_nagar", "मंडल": "mandal", "बस्ती": "basti", "उपबस्ती": "upbasti", "नगर": "ekai_nagar",
        "शाखा / मिलन": "sakha_milan", "विविध संगठन": "vividhSangathan", "अखिलभारतीय": "akhilbhartiya", "क्षेत्र": "chetra",
    };

    // Universities and their institutes
    const universityData = {
        "Delhi Technical University": ["Delhi Technical University"],
        "Indraprastha Institute of Information Technology-Delhi": ["Indraprastha Institute of Information Technology-Delhi"],
        "Indira Gandhi Delhi Technical University for Women": ["Indira Gandhi Delhi Technical University for Women"],
        "National Law University": ["National Law University"],
        "Ambedkar University Delhi": ["Ambedkar University Delhi"],
        "GGSIP UNIVERSITY": ["GGSIP UNIVERSITY",
            "Amity Institute of Education, M - Block, Saket",
            "Amity School of Engineering & Technology, 580, Delhi Palam Vihar Road, Bijwasan",
            "Army College of Medical Science Near Base Hospital Delhi Cantt",
            "Banarsidas Chandiwala Institute of Hotel Management & Catering Technology",
            "Banarsidas Chandiwala Institute of Information Technology",
            "Banarsidas Chandiwala Institute of Physiotherapy",
            "Banarsidas Chandiwala Institute of Professional Studies",
            "Bhagwan Parshuram Institute of Technology",
            "Bharti Vidyapeeth's College of Engineering",
            "Bharti Vidyapeeth Institute of Computer Applications & Management",
            "Chanderprabhu Jain College Of Higher Studies & School of Law",
            "COMM-IT, Career Academy",
            "Delhi School of Professional Studies and Research",
            "Delhi Institute Of Advanced Studies",
            "Delhi Institute of Rural Development",
            "Delhi Institute Of Rural Development (Sister Branch)",
            "Fairfield Institute of Management & Technology",
            "Gitarattan Institute Of Advanced Studies & Training",
            "Gitarattan International Business School",
            "Guru Nanak Institute of Management",
            "Guru Teg Bahadur Institute of Technology",
            "HMR Institute of Technology & Management",
            "Ideal Institute of Management and Technology",
            "ISIC Institute of Rehabilitation Sciences",
            "Institute of Information Technology & Management",
            "Institute of Innovation in Technology and Management",
            "Institute Of Vocational Studies",
            "Jagan Institute of Management Studies",
            "Jagannath International Management School, Vasant Kunj",
            "Jagannath International Management School, Kalkaji",
            "Kalka Institute for Research and Advanced Studies",
            "Kasturi Ram College of Higher Education",
            "Kamal Institute of Higher Education and Advance Technology",
            "Lal Bahadur Shastri Institute of Management",
            "Lingaya's Lalita Devi Institute of Management Science",
            "Lakshmi Bai Batra College Of Nursing",
            "Madhu Bala Institute of Communication and Electronic Media",
            "Maharaja Agrasen Institute Of Management Studies",
            "Maharaja Agrasen Institute of Technology",
            "Maharaja Surajmal Institute",
            "Maharaja Surajmal Institute of Technology",
            "Management Education & Research Institute",
            "MBS School of Planning and Architecture",
            "New Delhi Institute of Management",
            "Northern India Engineering College",
            "Pradeep Memorial Comprehensive College Of Education",
            "Periyar Management and Computer College",
            "Rajiv Gandhi Cancer Institute and Research Centre",
            "Rukmini Devi Institute of Advanced Studies",
            "Sant Hari Dass College Of Higher Education",
            "Sirifort College Of Computer Technology & Management",
            "Sri Guru Tegh Bahadur Institute of Management and Information Technology",
            "Special Art School",
            "St. Stephen's College Of Nursing",
            "Teachers Training Institute for Special Education",
            "Tecnia Institute of Advanced Studies",
            "Trinity Institute of Professional Studies",
            "Vastu Kala Academy",
            "Vivekananda Institute of Professional Studies",
            "Ambedkar Institute of Advanced Communication Technologies & Research",
            "Ambedkar Institute of Technology",
            "Aryabhatt Institute of Technology",
            "Bhai Parmanand Institute of Business Studies",
            "College of Medical Lab Technology, Hindu Rao Hospital",
            "Ch. Brahm Prakash Ayurved Charak Sansthan",
            "College of Nursing, VMMC & Safdarjung Hospital",
            "College of Nursing, Dr. Ram Manohar Lohia Hospital",
            "Ch. Brahm Prakash Govt. Engineering College",
            "Delhi Institute of Heritage Research & Management",
            "Dr. B. R. Sur Homeopathic Medical College and Hospital and Research Centre",
            "Delhi Institute of Tool Engineering",
            "ESIC Dental College and Hospital",
            "G. B. Pant Govt. Engineering College",
            "G. B. Pant Institute of Technology",
            "Guru Nanak Dev Institute of Technology",
            "Integrated Institute of Technology",
            "Kasturba Gandhi Institute of Technology",
            "Lok Nayak Jayaprakash Narayan National Institute of Criminology and Forensic Science",
            "Meera Bai Integrated Institute of Technology",
            "Morarji Desai National Institute of Yoga",
            "National Centre for Diseases Control",
            "National Power Training Institute",
            "NDMC Medical College at Hindu Rao Hospital",
            "PGIMER, Dr. Ram Manohar Lohia Hospital",
            "Pusa Institute of Technology",
            "Vardhaman Mahavir Medical College & Safdarjang Hospital"
        ],
        "SCERT": ["District Institute of Education and Training, (North) Keshav Puram, Delhi-110035 (Co. Ed.)",
            "District Institute of Education and Training, (North-West) Pitam Pura, Delhi-110088 (Co. Ed.)",
            "District Institute of Education and Training, (West) Old Rajinder Nagar, New Delhi-110060 (Co.Ed.)",
            "District Institute of Education and Training, (Central) Darya Ganj, New Delhi-110002 (Co. Ed.)",
            "District Institute of Education and Training (New Delhi) RK Puram, New Delhi-110022 (Co.Ed.)",
            "District Institute of Education and Training, (North-East) Dilshad Garden, New Delhi (Co.Ed.)",
            "District Institute of Education and Training, (East) Karkardooma Institutional Area, Delhi-110092 (Co. Ed)",
            "District Institute of Education and Training (South) Moti Bagh, New Delhi-110021 (Co.Ed.)",
            "District Institute of Education and Training, (South-West) Ghuman Hera, Najafgarh, New Delhi-110073 (Co. Ed.)",
            "Amity Institute of Education, Saket, New Delhi-17 (Co.Ed.)",
            "Delhi College of Vocational Studies and Research, Baprola, Delhi-43 (Co.Ed.)",
            "Drishhty Institute, Uday Vihar, Nilothi, New Delhi",
            "Gitarattan Institute of Advanced Studies & Training, Rohini, Delhi-110085 (for female only)",
            "Great Mission Teacher’s Training Institute, Dwarka, New Delhi-110075 (for female only)",
            "Ideal Institute of Management & Technology, Karkardooma, New Delhi-92 (Co.Ed.)",
            "Institute of Vocational Studies, Sheikh Sarai, New Delhi-17",
            "Jain Bharti Institute of Higher Education, Rohini, Delhi-110089 (for female only)",
            "L.C. College of Education, Sultan Puri, Nangloi, Delhi-110086",
            "Lovely Teachers’ Training Institute, Priyadarshni Vihar, Delhi-92 (for female only)",
            "M.A. Education Institute, Rohini, Delhi-85 (Co.Ed.)",
            "M.D.Inderprash Institute for Higher Education, Begumpur Extn. Delhi-110088",
            "M.R. Bharti College of Education, Mudka, Nangloi Delhi-110041",
            "Maharaja Surajmal Institute, Janak Puri, New Delhi-110058 (Co.Ed.)",
            "Pradeep Memorial Comprehensive College of Education, Nangloi, Delhi-110086 (for female only)",
            "Rama Krishna Teacher Training Institute, Vikas Puri, New Delhi-110018 (for female only)",
            "Rishab Institute, Mayur Vihar, Delhi-110091 (for female only)",
            "Sai Institute for Girls’, Raja Ram Kohli Marg, Delhi-110031 (for female only)",
            "Sant Hari Dass College of Higher Education, Najafgarh, New Delhi-43",
            "Sirifort College of Computer Technology & Management, Rohini, New Delhi-110085",
            "Sri Ram Institute of Teacher Education, Dwarka, New Delhi-77 (Co.Ed.)",
            "Tecnia Institute of Teacher Education, Rohini, Delhi-85 (Co.Ed.)",
            "Trinity Institute of Professional Studies, Vikas Puri, New Delhi-18",
            "V.D. Institute of Technology, Krishan Vihar, Delhi-110086 (Co.Ed.)",
            "Vidya Training Institute, Connaught Place, New Delhi-110001 (for female only)",
            "Air Force Vocational College, Old Willington Race Course Camp, New Delhi",
            "Bal Bharati Nursery Training Institute, New Delhi",
            "Delhi Nursing Teacher Training Institute, Defence Colony, New Delhi-24",
            "G R Memorial N.T.T. Institute, Nilothi More, Nangloi, Delhi-41",
            "ICS Infotech Institute, Pankha Road, New Delhi-46",
            "Kaushalaya Institute for Nursery Teacher Education, Badarpur, Jaitpur, Delhi-42",
            "L R College of Advanced Studies, Rohini, Delhi-85",
            "Lingaya's Lalita Devi Institute of Management & Sciences, Village Mandi, New Delhi-47",
            "Manav Bharati N.T.T. Institute, Panchsheel Park, New Delhi-17",
            "Manavi Institute Of Education & Technology, Rohini, Delhi-85",
            "Modelways N.T.T. Institute, Ashok Vihar, Delhi-52",
            "Pragati Institute of Education & Training, Dwarka, New Delhi-78",
            "Prayas College of Education, New Friends Colony, New Delhi-65",
            "Rukmini Devi College of Education, Rohini, Delhi-85",
            "Satyam International Polytechnic, Pitampura, New Delhi-88"],
        "Delhi Nursing Council": ["Akanksha Institute of Nursing, Najafgarh, Delhi",
            "Apollo School of Nursing, Sarita Vihar, New Delhi",
            "Baba Hari Dass Institute of Nursing Education",
            "Ginni Devi Action School of Nursing, Paschim Vihar",
            "Florence Nightingale School of Nursing, GTB Hospital",
            "School of Nursing, Hindu Rao Hospital, Delhi",
            "School of Nursing, Holy Family Hospital, Delhi",
            "School of Nursing, Kasturba Gandhi Hospital, Delhi",
            "Lady Reading Health School, Bara Hindu Rao, Delhi",
            "Panna Dai School of Nursing, DDU Hospital, New Delhi",
            "Rural Health Training Centre, Najafgarh, New Delhi",
            "Salokaya College of Nursing, Rohini, Delhi",
            "School of Nursing, Sir Ganga Ram Hospital, Old Rajinder Nagar, New Delhi",
            "Smt Janaki Rani Talwar School of Nursing, Moolchand Hospital, Lajpat Nagar, New Delhi",
            "School of Nursing, St. Stephen's Hospital, Delhi",
            "Sushila School of Nursing, Gautam Colony, Narela, Delhi",
            "School of Nursing, Tirath Ram Shah Hospital, New Delhi",
            "Rufaida College of Nursing, Faculty of Nursing, Jamia Hamdard Nagar, New Delhi",
            "R.V.S. Nursing School, Swami Dayanand Colony, Dilshad Garden, Delhi",
            "Brahm Shakti School of Nursing, Budh Vihar, Delhi",
            "Institute of Public Health & Hygiene, Mahipalpur Extn., Delhi"],
        "National Council for Vocational Training/State Council for vocational training": ["ITI Jahangir Puri",
            "ITI Dheer Pur",
            "ITI Narela",
            "ITI Jail Road",
            "ITI Hastsal",
            "ITI Tilak Nagar (W)",
            "ITI Mangol Puri",
            "ITI Jaffer Pur",
            "ITI Mayur Vihar",
            "ITI Nand Nagri",
            "ITI Shahdara",
            "ITI Vivek Vihar (W)",
            "ITI Mori Gate",
            "ITI Pusa",
            "BTC Pusa",
            "ITI Malvia Nagar",
            "ITI Arab Ki Sarai",
            "ITI Siri Fort",
            "Dy. Apprentice Advisor",
            "WCSC"],
        "Board of Technical Education": ["Chotu Ram Institute of Technology"],
        "Delhi Pharmaceutical Science and Research University": ["Delhi Pharmaceutical Science and Research University"],
        "University of Delhi": ["University of Delhi",
            "Acharya Narender Dev College",
            "Aditi Mahavidyalaya",
            "Atma Ram Sanatan Dharam College",
            "Ayurvedic & Unani Tibbia College",
            "Bhagini Nivedita College",
            "Bharati College",
            "Bhaskaracharya College of Applied Sciences",
            "Bhim Rao Ambedkar College",
            "College of Art",
            "College of Vocational Studies",
            "Daulat Ram College",
            "Deen Dayal Upadhyaya College",
            "Delhi College of Arts & Commerce",
            "Delhi Institute of Pharmaceutical Sciences & Research",
            "Deshbandhu College",
            "Dyal Singh College (Evening)",
            "Dyal Singh College",
            "Gargi College",
            "Hans Raj College",
            "Hindu College",
            "Indira Gandhi Institute of Physical Education & Sports Sciences",
            "Indraprastha College for Women",
            "Institute of Home Economics",
            "Janki Devi Memorial College",
            "Jesus & Mary College",
            "Kalindi College",
            "Kamala Nehru College",
            "Keshav Mahavidyalaya",
            "Kirori Mal College",
            "Lady Hardinge Medical College",
            "Lady Irwin College",
            "Lady Shri Ram College for Women",
            "Lakshmi Bai College",
            "Maharaja Agrasen College",
            "Maharishi Valmiki College of Education",
            "Maitreyi College",
            "Mata Sundri College for Women",
            "Maulana Azad Institute of Dental Sciences",
            "Maulana Azad Medical College",
            "Miranda House",
            "Moti Lal Nehru College (Evening)",
            "Moti Lal Nehru College",
            "Nehru Homoeopathic Medical College & Hospital",
            "Netaji Subhas University of Technology",
            "PGDAV College (Eve.)",
            "PGDAV College",
            "Rajdhani College",
            "Rajkumari Amrit Kaur College of Nursing",
            "Ram Lal Anand College (Evening)",
            "Ram Lal Anand College",
            "Ramanujan College",
            "Ramjas College",
            "Satyawati College (Evening)",
            "Satyawati College",
            "Shaheed Bhagat Singh College (Evening)",
            "Shaheed Bhagat Singh College",
            "Shaheed Rajguru College of Applied Sciences for Women",
            "Shaheed Sukhdev College of Business Studies",
            "Shivaji College",
            "Shri Ram College of Commerce",
            "Shyam Lal College (Eve.)",
            "Shyam Lal College",
            "Shyama Prasad Mukherji College for Women",
            "Sri Aurobindo College (Eve.)",
            "Sri Aurobindo College",
            "Sri Guru Gobind Singh College of Commerce",
            "Sri Guru Nanak Dev Khalsa College",
            "Sri Guru Teg Bahadur Khalsa College",
            "Sri Venkateswara College",
            "St. Stephens's College",
            "Swami Shraddhanand College",
            "University College of Medical Science & Guru Teg Bahadur Hospital",
            "Vallabhbhai Patel Chest Institute",
            "Vivekananda College",
            "Zakir Husain College",
            "Zakir Husain P.G. Evening College",
            "Ahilya Bai College of Nursing",
            "Amar Jyoti Institute of Physiotheraphy",
            "Durgabai Deshmukh College of Special Education",
            "Pandit Deen Dayal Upadhaya Institute for the Physically Handicapped",
            "School of Rehabilitation Sciences"],
        "Jamia Millia Islamia University": ["Jamia Millia Islamia University, Maulana Mohammed ali Jauhar Marg, New Delhi-110025"],
        "Jawahar Lal Nehru University": ["Jawahar Lal Nehru University, New Mehrauli Road, New Delhi-110067"],
        "All India Institute of Medical Sciences": ["All India Institute of Medical Sciences, Ansari Nagar, New Delhi-29"],
        "Jamia Hamdard University": ["Jamia Hamdard University,Hamdard Nagar, New Delhi-62"],
        "National Institute of Technology": ["National Institute of Technology, Sector-9 Dwarka, New Delhi-77"],
        "South Asian University": ["South Asian University, Akbar Bhawan Chankaya Puri, New Delhi-67"],
        "Indian Institute of Technology": ["Indian Institute of Technology, Hauz khas, New Delhi-16"],
        "Indira Gandhi National Open University": ["Indira Gandhi National Open University,Maidan Garhi,New Delhi-68"],
        "National School of Drama": ["National School of Drama(NSD), Bswalpur House, 1,Bhagwan Das Road, New Delhi-110001"],
        "National Institute of Fashion Technology": ["National Institute of Fashion Technology (NIFT), NIFT Campus, Hauz Khas, Newr Gulmohar Park, New Delhi-110016"],
        "National Museum Institute of History of Art, Conservation & Museology": ["National Museum Institute of History of Art, Conservation & Museology, National Museum, New delhi-110001"],
        "National University of Education, Planning an Administration(NUEPA)": ["National University of Education, Planning an Administration(NUEPA), 17-B, Sri Arobindo Marg, New Delhi-1100016"],
        "Teri School of Advanced Studies": ["Teri School of Advanced Studies, Darbari Seth Block, Habitat Place, Lodhi Road, New Delhi-110003"],
        "Shri Lal Bahadr Shastri Rashtriya Sanskrit Vidyapith": ["Shri Lal Bahadr Shastri Rashtriya Sanskrit Vidyapith, Kathvaria Sarai, New Meharauli Road, New Delhi-110067"],
        "School of Planning and Architectre (SPA)": ["School of Planning and Architectre (SPA), I.P Estate, New Delhi-110002"],
        "Indian Agriculture Research Institute": ["Indian Agriculture Research Institute (Krishi PUSA), PUSA, New Delhi"],
        "Rashtriya Sanskrit Sansthan": ["Rashtriya Sanskrit Sansthan,56-57,Institutional Area,D-Block, Janak Puri, New Delhi-1100058"],
        "Indian Law Institute (ILI)": ["Indian Law Institute (ILI), Bhagwandass Road, New Delhi-110001."],
        "Institute of Liver and Biliary Sciences (ILBS)": ["Institute of Liver and Biliary Sciences (ILBS), D-1, Vasant Kunj, New Delhi-110070"],
        "Indian Institute of Foreign Trade (IIFT)": ["Indian Institute of Foreign Trade (IIFT), IIFT, B-21, Qutub Institutional Area, New Delhi-110016"],
        "अन्य": []
    };

    // Courses and their streams
    const courseData = {
        "Engineering": [
            "Computer Science Engineering",
            "Mechanical Engineering",
            "Civil Engineering",
            "Electrical Engineering",
            "Electronics and Communication",
            "Aerospace Engineering",
            "Chemical Engineering",
            "Biomedical Engineering",
            "Environmental Engineering",
            "Information Technology"
        ],
        "Medical": [
            "MBBS", "BDS", "BPT", "BAMS", "BHMS", "BUMS", "BSc Nursing",
            "Pharmacy", "MD", "MS"
        ],
        "Arts": ["BA in English", "BA in History", "BA in Political Science",
            "BA in Psychology",
            "BA in Sociology",
            "BA in Philosophy",
            "BA in Economics",
            "BA in Geography",
            "BA in Anthropology",
            "BA in Journalism"
        ], "Science": [
            "BSc in Physics",
            "BSc in Chemistry",
            "BSc in Biology",
            "BSc in Mathematics",
            "BSc in Biotechnology",
            "BSc in Environmental Science",
            "BSc in Microbiology",
            "BSc in Statistics",
            "MSc in Physics",
            "MSc in Chemistry"
        ],
        "Commerce": [
            "BCom",
            "BCom (Hons)",
            "BBA",
            "MCom",
            "CA",
            "CMA",
            "CS",
            "Diploma in Banking",
            "BCom in Taxation",
            "BCom in Accounting"
        ],
        "Law": [
            "LLB",
            "BA LLB",
            "BBA LLB",
            "LLM",
            "Diploma in Cyber Law",
            "Diploma in Corporate Law"
        ],
        "Management": [
            "MBA",
            "BBA",
            "PGDM",
            "Executive MBA",
            "Diploma in Management",
            "MMS"
        ],
        "Education": [
            "B.Ed",
            "M.Ed",
            "Diploma in Elementary Education",
            "Bachelor of Physical Education"
        ],
        "Computer Applications": [
            "BCA",
            "MCA",
            "Diploma in Computer Applications",
            "PGDCA"
        ],
        "Design": [
            "B.Des",
            "M.Des",
            "Diploma in Fashion Design",
            "Diploma in Graphic Design"
        ],
    };
    // Professional categories data structure
    const professionalCategories = {
        "Professionals": {
            "Medical Professionals": [
                "Doctors", "Surgeons", "Dentists", "Physiotherapists", "Psychiatrists"
            ],
            "Engineering Professionals": [
                "Civil Engineer",
                "Mechanical Engineer",
                "Electrical Engineer",
                "Software Engineers"
            ],
            "Legal Professionals": [
                "Lawyers",
                "Judges",
                "Legal Consultants"
            ],
            "Finance Professionals": [
                "Chartered Accountants (CA)",
                "Financial Analysts",
                "Auditors"
            ],
            "Education Professionals": [
                "Teachers",
                "Professors",
                "Education Consultants"
            ],
            "IT Professionals": [
                "Software Developers", "System Analysts", "Cybersecurity Experts"
            ],
            "Design Professionals": [
                "Architects",
                "Interior Designers",
                "Graphic Designers"
            ],
            "Media & Communication": ["Journalists", "Anchors", "Public Relations Officers"],
            "Art & Culture": [
                "Musicians", "Painters",
                "Dancers",
                "Writers"
            ],
            "Management Professionals": [
                "HR Managers",
                "Operations Managers",
                "Marketing Professionals"
            ]

        },
        "Industrialists": ["Textile Industrialists", "Steel and Iron Industrialists", "Chemical Industry", "Pharmaceutical Industrialists", "Automobile Industrialists", "Cement and Construction Material Industrialists", "FMCG Industrialists (Fast-Moving Consumer Goods)"
            , "Petrochemical Industrialists", "IT and Software Industrialists", "Renewable Energy Industrialists", "Aerospace and Defense Industrialists", "Agro-based Industrialists (Fertilizers, Agro-equipment, Processing)"],
        "Businesses": {
            "By Industry": [
                "Manufacturing (factories, plants)",
                "Service (consultancy, education, healthcare)",
                "Trading (import/export, wholesale, retail)",
                "Agriculture & Allied (farming, fisheries, dairy)",
                "Technology & IT (software services, app development)",
                "Financial Services (banks, NBFCs, insurance firms)",
                "E-commerce (online retail, platforms)",
                "Real Estate & Construction",
                "Tourism & Hospitality (hotels, travel agencies)",
                "Entertainment & Media (film, music, OTT)"
            ],
        }
    };

    function updateSubCategories() {
        const mainCategory = document.getElementById('professionals_name').value;
        const subCategorySelect = document.getElementById('sub_category_type');
        subCategorySelect.innerHTML = '<option value="" disabled selected>उप-श्रेणी चुनें</option>';
        if (!mainCategory || !professionalCategories[mainCategory]) return;
        const categoryData = professionalCategories[mainCategory];
        if (mainCategory === "Industrialists") {
            categoryData.forEach(item => {
                const option = document.createElement('option');
                const parts = item.split(' (');
                option.value = parts[0];
                option.textContent = item;
                subCategorySelect.appendChild(option);
            });
        } else {
            for (const [groupName, items] of Object.entries(categoryData)) {
                const optgroup = document.createElement('optgroup');
                optgroup.label = groupName;
                items.forEach(item => {
                    const option = document.createElement('option');
                    const parts = item.split(' (');
                    option.value = parts[0];
                    option.textContent = item;
                    optgroup.appendChild(option);
                });
                subCategorySelect.appendChild(optgroup);
            }
        }
    }

    document.getElementById("professionals_name").addEventListener("change", function () {
        document.getElementById("sub_category_type").style.display = "block";
        updateSubCategories();
    })


    // Handle university selection
    document.getElementById('university').addEventListener('change', function () {
        const selectedUni = this.value;
        document.getElementById("institute-container").style.display = "block";
        populateDropdown("institute", universityData[selectedUni] || [], "संस्थान");
    });

    // Handle course selection
    document.getElementById('course').addEventListener('change', function () {
        const selectedCourse = this.value;
        document.getElementById("stream-container").style.display = "block";
        populateDropdown("stream", courseData[selectedCourse] || [], "स्ट्रीम");
    });
 
  //******particle animation background js *******
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
            if (particle.x > width - particle.size) particle.x = Math.random() * width;
            if (particle.y > height - particle.size) particle.y = Math.random() * height;
        });
    });

    // Observe body size changes
    const resizeObserver = new ResizeObserver(() => {
        init();
    });
    resizeObserver.observe(document.body);

    //Sangh sikhshan js
    const shikshanSelect = document.getElementById('sangh_shikshan_level');
    updateShikshanFields();
    shikshanSelect.addEventListener('change', updateShikshanFields);

    function updateShikshanFields() {
        const pratigyaContainer = document.getElementById("pratigyaCheckbox-container");
        const pratigyaYes = document.getElementById("pratigyaCheckboxYes");
        const pratigyaNo = document.getElementById("pratigyaCheckboxNo");
        const level = document.getElementById('sangh_shikshan_level').value;
        const container = document.getElementById('shikshan-details-container');

        container.innerHTML = '';
        if (level === 'कोई शिक्षण नहीं हुआ' || level === 'प्रारम्भिक वर्ग' || level === 'प्राथमिक वर्ग' || level === 'संघ शिक्षा वर्ग / प्रथम वर्ष') {
            pratigyaContainer.style.display = "block";
            // Uncheck both radio buttons when shown
            if (pratigyaYes.checked || pratigyaNo.checked) {
                pratigyaYes.checked = false;
                pratigyaNo.checked = false;
            }
        } else {
            pratigyaContainer.style.display = "none";
            pratigyaYes.checked = false;
            pratigyaNo.checked = false;
        }
        // Hide container if no shikshan selected
        if (level === 'कोई शिक्षण नहीं हुआ') {
            container.style.display = 'none';
            return;
        }

        container.style.display = 'block';
        const fieldsToCreate = [];

        if (level === 'कार्यकर्ता विकास वर्ग 2 / तृतीय वर्ष') {
            fieldsToCreate.push(
                { type: 'tritiya', label: 'कार्यकर्ता विकास वर्ग 2 / तृतीय वर्ष' },
                { type: 'dwitiya', label: 'कार्यकर्ता विकास वर्ग 1 / द्वितीय वर्ष' },
                { type: 'pratham', label: 'संघ शिक्षा वर्ग / प्रथम वर्ष' },
                { type: 'prathmik', label: 'प्राथमिक वर्ग' },
                { type: 'prarambhik', label: 'प्रारम्भिक वर्ग' },
            );
        } else if (level === 'कार्यकर्ता विकास वर्ग 1 / द्वितीय वर्ष') {
            fieldsToCreate.push(
                { type: 'dwitiya', label: 'कार्यकर्ता विकास वर्ग 1 / द्वितीय वर्ष' },
                { type: 'pratham', label: 'संघ शिक्षा वर्ग / प्रथम वर्ष' },
                { type: 'prathmik', label: 'प्राथमिक वर्ष' },
                { type: 'prarambhik', label: 'प्रारम्भिक वर्ष' },
            );
        } else if (level === 'संघ शिक्षा वर्ग / प्रथम वर्ष') {
            fieldsToCreate.push(
                { type: 'pratham', label: 'संघ शिक्षा वर्ग / प्रथम वर्ष' },
                { type: 'prathmik', label: 'प्राथमिक वर्ष' },
                { type: 'prarambhik', label: 'प्रारम्भिक वर्ष' },
            );
        } else if (level === 'प्राथमिक वर्ष') {
            fieldsToCreate.push(
                { type: 'prathmik', label: 'प्राथमिक वर्ष' },
                { type: 'prarambhik', label: 'प्रारम्भिक वर्ष' }
            );
        } else if (level === 'प्रारम्भिक वर्ष') {
            fieldsToCreate.push(
                { type: 'prarambhik', label: 'प्रारम्भिक वर्ष' },
            );
        }
        const fieldset = document.createElement('div');
        fieldset.className = 'shikshan-fieldset mb-4';

        const row = document.createElement('div');
        row.className = 'row';
        let minYear = 1950;

        // Create the fields
        fieldsToCreate.forEach(field => {
            const yearCol = document.createElement('div');
            yearCol.className = 'col-md-6 mb-3 dropdown';
            yearCol.id = `${field.type}_year-container`;

            const yearLabel = document.createElement('label');
            yearLabel.className = 'form-label';
            yearLabel.style.cssText = 'font-size: 16px !important; font-weight: 600; color: #333;';
            if (field.type !== "prarambhik") {
                yearLabel.innerHTML = `${field.label}<span class="text-danger"> *</span>`;
            } else {
                yearLabel.textContent = field.label;
            }
            yearLabel.htmlFor = `${field.type}-year`;

            yearCol.appendChild(yearLabel);

            const yearSelect = document.createElement('select');
            yearSelect.id = `${field.type}_year`;
            yearSelect.name = `${field.type}_varsh`;
            yearSelect.className = 'form-control';

            const yearDefaultOption = document.createElement('option');
            yearDefaultOption.value = '';
            yearDefaultOption.textContent = 'example: YYYY';
            yearDefaultOption.disabled = true;
            yearDefaultOption.selected = true;
            yearSelect.appendChild(yearDefaultOption);

            const currentYear = new Date().getFullYear();
            for (let year = currentYear; year >= minYear; year--) {
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
            yearError.textContent = 'Please select year';
            yearCol.appendChild(yearError);

            yearSelect.addEventListener('change', function () {
                if (yearSelect.value) {
                    hideError(`${field.type}_year`);
                }
            });
            row.appendChild(yearCol);
            fieldset.appendChild(row);
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
            document.querySelectorAll('#ghoshVadakYes-container input[type="checkbox"]').forEach(function (checkbox) {
                checkbox.checked = false;
                if (['turya', 'swarad', 'nagang', 'gomukh', 'other'].includes(checkbox.id)) {
                    checkbox.parentElement.style.display = 'none';
                }
            });
            document.querySelectorAll('input[name="rachnaye"]').forEach(function (radio) {
                radio.checked = false;
            });
            document.getElementById("shankhShrungOwn-container").style.display = "block";
            document.querySelectorAll('input[name="shankh_shrung_own"]').forEach(function (radio) {
                radio.checked = false;
            })
            document.querySelectorAll('input[name="learn_vadya"]').forEach(function (radio) {
                radio.checked = false;
            });
            if (this.value === 'हाँ') {
                document.getElementById('ghoshVadakYes-container').style.display = 'block';
                document.getElementById('ghoshVadakNo-container').style.display = 'none';
            } else {
                document.getElementById('ghoshVadakYes-container').style.display = 'none';
                document.getElementById('ghoshVadakNo-container').style.display = 'block';
            }
            handleLearnVadya();
        });
    });
    // Function to handle learn_vadya visibility and checkbox reset
    function handleLearnVadya() {
        document.querySelectorAll('input[name="learn_vadya_list"]').forEach(function (checkbox) {
            checkbox.checked = false;
        });        
        const selectedLearnVadya = document.querySelector('input[name="learn_vadya"]:checked');
        if (selectedLearnVadya && selectedLearnVadya.value === 'हाँ') {
            document.getElementById('learnVadyaList').style.display = 'block';
            document.getElementById('learnVadyaList-container').style.display = 'block';         
        } else {
            document.getElementById('learnVadyaList').style.display = 'none';
            document.getElementById('learnVadyaList-container').style.display = 'none';
        }
    }
    document.querySelectorAll('input[name="learn_vadya"]').forEach(function (radio) {
        radio.addEventListener('change', handleLearnVadya);
    });

    // Reusable function to toggle visibility and reset dependent checkboxes
    function toggleDependentCheckboxes(checkboxId, dependentIds) {
        const mainCheckbox = document.getElementById(checkboxId);
        if (!mainCheckbox) return;
        mainCheckbox.addEventListener('change', function () {
            dependentIds.forEach(function (id) {
                const checkbox = document.getElementById(id);
                if (checkbox) {
                    checkbox.parentElement.style.display = this.checked ? 'block' : 'none';
                    if (!this.checked) {
                        checkbox.checked = false; 
                    }
                }
            }, this);
        });
    }

    // Apply toggle functionality for shrung and learnShrung
    toggleDependentCheckboxes('shrung', ['turya', 'swarad', 'nagang', 'gomukh', 'other']);
    toggleDependentCheckboxes('learnShrung', ['learnTurya', 'learnSwarad', 'learnNagang', 'learnGomukh', 'learnOther']);
    
    // Show/hide specific checkboxes when shrung is checked
    document.getElementById('shrung').addEventListener('change', function () {
        const container = document.getElementById("shankhShrungOwn-container");
        container.style.display = container.style.display === "none" ? "block" : "none";
        const checkboxesToShow = ['turya', 'swarad', 'nagang', 'gomukh', 'other'];
        checkboxesToShow.forEach(function (id) {
            const checkbox = document.getElementById(id);
            if (checkbox) {
                checkbox.parentElement.style.display = this.checked ? 'block' : 'none';
                if (!this.checked) {
                    checkbox.checked = false;
                }
            } 
        }, this);
    });


    const dobInput = document.getElementById('dob');
    if (dobInput) {
        const openDatePicker = () => {
            typeof dobInput.showPicker === 'function' ? dobInput.showPicker() : dobInput.focus();
        };
        const setMaxDate = () => {
            const today = new Date();
            const maxDate = new Date(today.setFullYear(today.getFullYear() - 10));
            dobInput.setAttribute('max', maxDate.toISOString().split('T')[0]);
        };
        ['focus', 'click'].forEach(event => dobInput.addEventListener(event, openDatePicker));
        setMaxDate();
    }

    document.getElementById("referralCode").value = "1925";
    
    document.getElementById("referralCode").addEventListener("input", function () {
        const referralCodeError = document.getElementById("referralCodeError");
        this.value = this.value.replace(/[^a-zA-Z0-9]/g, '');
        if (!(/^[A-Z]+$/i.test(this.value) || /^[0-9]+$/.test(this.value))) {
            referralCodeError.style.display = "block"; 
        } else {
            referralCodeError.style.display = "none";
        }
    });

    function populateDropdown(field, options, placeholder) {
        const dropdown = document.getElementById(field);
        dropdown.innerHTML = `<option value="" disabled selected>${placeholder}</option>`;

        const addOption = (value, text = value) => {
            const option = document.createElement("option");
            const mappedValue = fieldToHindiMapping[value] || value;
            option.value = mappedValue;
            option.textContent = mappedValue;
            dropdown.appendChild(option);
        };

        const fieldConfigs = {
            prant: {
                defaultOption: options[0],
                additionalOptions: Array.isArray(options[1]) ? options[1] : [options[1]]
                    .filter(opt => opt && opt !== options[0])
            },
            vibhag: {
                defaultOption: options[0],
                additionalOptions: (Array.isArray(options[1]) ? options[1] : [options[1]])
                    .flatMap(prant => mappings.prantToVibhag[prant] || [])
                    .filter(opt => opt && opt !== options[0])
            },
            jila: {
                defaultOption: options[0],
                additionalOptions: (Array.isArray(options[1]) ? options[1] : [options[1]])
                    .flatMap(vibhag => mappings.VibhagToJila[vibhag] || [])
                    .filter(opt => opt && opt !== options[0])
            },
            ekai_nagar: {
                defaultOption: options[0],
                additionalOptions: (mappings.pincodeToNagar[options[1]] || [])
                    .filter(opt => opt && opt !== options[0])
            }
        };

        if (fieldConfigs[field]) {
            const { defaultOption, additionalOptions } = fieldConfigs[field];
            if (defaultOption) {
                const option = document.createElement("option");
                const mappedValue = fieldToHindiMapping[defaultOption] || defaultOption;
                option.value = mappedValue;
                option.textContent = mappedValue;
                option.selected = true;
                dropdown.appendChild(option);
            }
            additionalOptions.forEach(addOption);
            return;
        }

        // Handle generic fields
        const validOptions = Array.isArray(options) ? options : [options];
        validOptions.filter(opt => opt && opt.length > 0).forEach(addOption);
    }


    function resetDropdowns(field) {
        const resetMappings = {
            referralCode: ["profession", "pincode", "prant", "vibhag", "jila", "ekai_nagar", "mandal", "basti", "sakha_milan", "dayitva", "state", "ekai"],
            pincode: ["nagar", "ekai_nagar", "mandal", "basti", "sakha_milan", "state", "ekai", "dayitva", "prant", "vibhag", "jila"],
            profession:["university", "institute", "course", "stream", "professionals_name", "sub_category_type"],
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
                let yesRadio = document.getElementById("sakha_milanCheckboxYes");
                let noRadio = document.getElementById("sakha_milanCheckboxNo");
            
                // Unselect both radio buttons
                if (yesRadio.checked || noRadio.checked) {
                    yesRadio.checked = false;
                    noRadio.checked = false;
                }
                
            }else{
                populateDropdown(dropdownId, [], dropdownId);
            }
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
        }else if(field === "profession"){
            const allContainers=["university-container","institute-container", "course-container","stream-container","professionals_name-container", "sub_category_type-container","educationHeading-container","professionHeading-container"];
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
        if(field === "profession"){
            const professionValue = document.getElementById("profession").value;
            if (professionValue === 'कॉलेज-विद्यार्थी') {
                toggleElement("educationHeading-container");
                toggleElement("university-container");
                toggleElement("course-container");
            }else{
                toggleElement("professionHeading-container");
                toggleElement("professionals_name-container");
                toggleElement("sub_category_type-container");
            }
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
    //profession change handle
    document.getElementById('profession').addEventListener('change', function () {
        resetDropdowns("profession");
        toggleVisibility("profession");
        const professionValue = this.value;
        if (professionValue === 'कॉलेज-विद्यार्थी') {
            populateDropdown("university", Object.keys(universityData), "विश्वविद्यालय");
            populateDropdown("course", Object.keys(courseData), "कोर्स");
        } else {
            populateDropdown("professionals_name", ["Professionals","Industrialists","Businesses"], "व्यावसायिक");
        }
    });


      document.getElementById("ekai").addEventListener("change", function () {
        resetDropdowns("ekai");
        toggleVisibility("ekai");
        let selectedEkai = `${hindiToEnglishMapping[this.value]}`;
        let selectedNagar = document.getElementById("nagar").value;
        let selectedPincode = document.getElementById("pincode").value;

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

            populateDropdown("prant", [selectedPrant], "प्रांत");
        } else if (selectedEkai === "vibhag") {
            populateDropdown("vibhag", [selectedVibhag, selectedPrant], "विभाग");
        } else if (selectedEkai === "jila") {
            populateDropdown("jila", [selectedJila, selectedVibhags], "जिला");
        }
        else if (selectedEkai === "ekai_nagar") {
            populateDropdown("ekai_nagar", [selectedNagar, selectedPincode], "नगर");
        } else if (["mandal", "basti", "sakha_milan"].includes(selectedEkai)) {
            let options = [];
            options = mappings.pincodeToNagar[selectedPincode] || [];
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


   // Handle vividhSangathan radio buttons
    document.querySelectorAll('input[name="vividhsangathan_yes_no"]').forEach(radio => {
    radio.addEventListener("change", function () {
        const vividhSangathanDiv = document.getElementById("vividhSangathan-container");
        const referralCode = document.getElementById("referralCode");
        const selectedValue = document.querySelector('input[name="vividhsangathan_yes_no"]:checked')?.value;

        const options = [
        "अखिल भारतीय विद्यार्थी परिषद", "विद्याभारती", "भारतीय शिक्षण मंडल",
        "अखिल भारतीय शैक्षिक महासंघ", "संस्कृत भारती", "शिक्षा संस्कृति उत्थान न्यास",
        "वनवासी कल्याण आश्रम", "विश्व हिन्दू परिषद्", "भारतीय जनता पार्टी",
        "राष्ट्रीय सिक्ख संगत", "क्रीडा भारती", "संस्कार भारती", "सक्षम",
        "आरोग्य भारती", "एन्. एम्. ओ. (नैशनल मैडिकल आर्गेनाइजेशन)"
        ];

        if (selectedValue === "हाँ") {
            resetDropdowns("vividhSangathan");
            populateDropdown("vividhSangathan", options, fieldToHindiMapping["vividhSangathan"]);
            vividhSangathanDiv.style.display = "block";
            referralCode.value = "";
        } else {
            referralCode.value = "1925";
            resetDropdowns("vividhCheckbox");
            vividhSangathanDiv.style.display = "none";
        }
    });
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
        const selectedValue = document.querySelector('input[name="vividhsangathan_yes_no"]:checked')?.value;
        if (selectedValue === "हाँ") {
            this.value = "";
        } else {
            this.value = "1925";
        }
        document.getElementById("vividhSangathan-container").style.display = selectedValue === "हाँ" ? "block" : "none";

        const pincodeField = document.getElementById("pincode");
        pincodeField.value = "";
        const professionOptions = referralCode === "1925" ? ["स्कूल-विद्यार्थी", "कॉलेज-विद्यार्थी", "अध्यापक", "प्राध्यापक", "कर्मचारी (सरकारी)", "कर्मचारी (अन्य)", "व्यवसायी", "उद्योगपति",
            "प्रोफेशनल", "सेवा-निवृत्त", "गृहिणी", "श्रमिक", "कृषक (किसान)", "प्रचारक", "विस्तारक", "पूर्णकालिक"] : 
            ["स्कूल-विद्यार्थी", "कॉलेज-विद्यार्थी", "अध्यापक", "प्राध्यापक","कर्मचारी (सरकारी)", "कर्मचारी (अन्य)", "व्यवसायी", "उद्योगपति","प्रोफेशनल", "सेवा-निवृत्त", "गृहिणी", "श्रमिक", "कृषक (किसान)"
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
                address_nagar: { type: 'select', required: true },
                address_state: { type: 'select', required: true },
                professionals_name: {type:'select', required:true},
                sub_category_type:{type:'select', required:true},
                university:{type:'select', required:true},
                institute:{type:'select', required:true},
                course:{type:'select', required:true},
                stream:{type:'select', required:true},
            },
            specialCases: {
                gender: {
                    type: 'radio',
                    required: true,
                    selector: 'input[name="gender"]:checked',
                    errorId: 'genderError',
                    errorMessage: 'Please select a gender'
                },
                socialInterests: {
                    type: 'checkbox',
                    required: true,
                    selector: '#socialInterests-container input[type="checkbox"]:checked',
                    errorId: 'socialInterestsError',
                    errorMessage: 'Please select at least one option'
                }
            }
        },
        card_body_2: {
            fields: {
                pincode: { type: 'text', required: true, pattern: /^\d{6}$/ },
                nagar: { type: 'select', required: true },
                state: { type: 'select', required: true },
                upbasti: { type: 'select', required: true },
                ekai: { type: 'select', required: true },
                dayitva: { type: 'select', required: true },
                prant: { type: 'select', required: true },
                vibhag: { type: 'select', required: true },
                jila: { type: 'select', required: true },
                ekai_nagar: { type: 'select', required: true },
                basti: { type: 'select', required: true },
                mandal: { type: 'select', required: true },
                sakha_milan: { type: 'select', required: true },
                vividhSangathan: { type: 'select', required: true }
            },
            specialCases: {
                rssAssociation: {
                    type: 'radio',
                    required: true,
                    selector: 'input[name="rss_association"]:checked',
                    errorId: 'rssAssociationError',
                    errorMessage: 'Please select a option'
                },
                responsibility: {
                    type: 'radio',
                    required: true,
                    selector: 'input[name="responsibility_yes_no"]:checked',
                    errorId: 'responsibilityError',
                    errorMessage: 'Please select an option',
                },
                vividhCheckbox: {
                    type: 'radio',
                    required: true,
                    selector: 'input[name="vividhsangathan_yes_no"]:checked',
                    errorId: 'vividhCheckboxError',
                    errorMessage: 'Please select an option',
                },
                sakha_milanCheckbox: {
                    type: 'radio',
                    required: true,
                    selector: 'input[name="ekai_milaan"]:checked',
                    errorId: 'sakha_milanCheckboxError',
                    errorMessage: 'Please select an option',
                },
                vividhSangathan: {
                    type: 'conditionalCheckbox',
                    checkboxSelector: 'input[name="vividhsangathan_yes_no"]:checked',
                    errorId: 'vividhCheckboxError',
                    errorMessage: 'Please select an option',
                    conditionValue: 'हाँ'
                }
               
            }
        },
        card_body_3: {
            fields: {
                sangh_shikshan_level: { type: 'select', required: true },
                prathmik_year: { type: 'select', required: true },
                pratham_year: { type: 'select', required: true },
                dwitiya_year: { type: 'select', required: true },
                tritiya_year: { type: 'select', required: true },
                ghosh_vadak: { type: 'radio', required: true, selector: 'input[name="ghosh_vadak"]:checked' }
            },
            specialCases: {
                pratigyaCheckbox: {
                    type: 'radio',
                    required: true,
                    selector: 'input[name="pratigya"]:checked',
                    errorId: 'pratigyaCheckboxError',
                    errorMessage: 'Please select an option',
                },
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
                console.log("Hello",selected, isFieldVisible(key),config.selector)
                if (!selected && isFieldVisible(key)) {
                    showErrors(document.getElementById(config.errorId), config.errorMessage);
                    valid = false;
                } else {
                    hideErrors(document.getElementById(config.errorId));
                }
            }else if (config.type === 'checkbox') {
                const checkboxes = document.querySelectorAll(config.selector);
                const anyChecked = Array.from(checkboxes).some(cb => cb.checked);
                if (!anyChecked && isFieldVisible('socialInterests')) {
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
       // Apply success background to card-header
        const cardHeader = cardElement.querySelector('.card-header');
        cardHeader.classList.remove('bg-success', 'bg-danger');
        if (valid) {
            cardHeader.classList.add('bg-success', 'text-white');
        }else{
            cardHeader.classList.remove('text-white');
        }

        return valid;
    }
    
    function validateForm(event) {
        event.preventDefault();
        let isValid = true;
        let firstInvalidCard = null;
        let cardId= "card_body_3";
        validateFields(cardFields[cardId].fields, cardFields[cardId].specialCases, cardId);
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
        if (isValid) {
            openModal();
        } else {
            // Scroll to the first invalid card
            if (firstInvalidCard) {
                const cardElement = document.querySelector(`#${firstInvalidCard}`).parentElement;
                cardElement.scrollIntoView({ behavior: 'smooth', block: 'start' });              
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
        }
    }

    function hideErrors(errorElement) {
        if (errorElement) {
            errorElement.style.display = 'none';
        }
    }


    function setupCardToggle(headerSelector, bodySelector, cardId) {
        const header = document.querySelector(headerSelector);
        const cardBody = document.querySelector(bodySelector);
        const cardContainer = document.querySelector(bodySelector);
        const toggleIcon = header ? header.querySelector(".toggle-icon i") : null;
        const nextButton = cardContainer ? cardContainer.querySelector(".next-btn") : null; // Select Next button within card container
    
        cards.push({ header, cardBody, toggleIcon, cardId });
    
        if (cardId === 'card_body_1') {
            gsap.set(cardBody, { height: "auto", padding: "1rem", opacity: 1 });
            if (toggleIcon) {
                toggleIcon.classList.remove('fa-plus');
                toggleIcon.classList.add('fa-minus');
            }
            validateFields(cardFields[cardId].fields, cardFields[cardId].specialCases, cardId);
        } else {
            gsap.set(cardBody, { height: 0, padding: 0, opacity: 0 });
        }
    
        // Function to toggle a specific card
        const toggleCard = (targetCard) => {
            // Skip if header is disabled
            if (targetCard.header.classList.contains('disabled')) {
                return;
            }
            const isOpen = targetCard.cardBody.style.height && targetCard.cardBody.style.height !== '0px';
    
            // Close all other cards
            cards.forEach(card => {
                if (card !== targetCard && card.cardBody.style.height !== '0px') {
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
    
            // Toggle the target card
            if (isOpen) {
                gsap.to(targetCard.cardBody, {
                    height: 0,
                    padding: 0,
                    opacity: 0,
                    duration: 0.8,
                    ease: "power2.inOut"
                });
                gsap.to(targetCard.toggleIcon, {
                    opacity: 0,
                    duration: 0.3,
                    ease: "power2.inOut",
                    onComplete: () => {
                        targetCard.toggleIcon.classList.remove('fa-minus');
                        targetCard.toggleIcon.classList.add('fa-plus');
                        gsap.to(targetCard.toggleIcon, { opacity: 1, duration: 0.15, ease: "power2.inOut" });
                    }
                });
            } else {
                gsap.to(targetCard.cardBody, {
                    height: "auto",
                    padding: "1rem",
                    opacity: 1,
                    duration: 0.8,
                    ease: "power2.inOut"
                });
                gsap.to(targetCard.toggleIcon, {
                    opacity: 0,
                    duration: 0.3,
                    ease: "power2.inOut",
                    onComplete: () => {
                        targetCard.toggleIcon.classList.remove('fa-plus');
                        targetCard.toggleIcon.classList.add('fa-minus');
                        gsap.to(targetCard.toggleIcon, { opacity: 1, duration: 0.15, ease: "power2.inOut" });
                    }
                });
            }
            validateFields(cardFields[targetCard.cardId].fields, cardFields[targetCard.cardId].specialCases, targetCard.cardId);
        };
    
        // Header click event
        header.addEventListener('click', () => {
            const currentCard = cards.find(card => card.header === header);
            if ((!header.classList.contains('disabled'))) {
                toggleCard(currentCard);
            } 
        });
    
        // Next button click event
        if (nextButton) {
            nextButton.addEventListener('click', (e) => {
                e.preventDefault(); 
                const currentOpenCard = cards.find(card => card.cardBody.style.height && card.cardBody.style.height !== '0px');
                const currentIndex = currentOpenCard ? cards.indexOf(currentOpenCard) : -1;
                const nextIndex = currentIndex + 1 < cards.length ? currentIndex + 1 : 0; // Loop back to first card if at the end
                const nextCard = cards[nextIndex];
    
               // Validate the current card's fields
                const isValid = validateFields(cardFields[currentOpenCard.cardId].fields, cardFields[currentOpenCard.cardId].specialCases, currentOpenCard.cardId);

                if (isValid && nextCard) {
                    nextCard.header.classList.remove('disabled');
                    toggleCard(currentOpenCard);
                    toggleCard(nextCard);
                }
            });
        }
    }


    document.querySelectorAll('.card-header[data-toggle-target]').forEach(header => {
        const bodyId = header.getAttribute('data-toggle-target');
        const cardId = bodyId; // Use full id like 'card1', 'card2', etc.
        setupCardToggle(`[data-toggle-target="${bodyId}"]`, `#${bodyId}`, cardId);

    });


    //address 
    const sameAddressCheckbox = document.getElementById("sameAddress");
    const permanentAddress = document.getElementById("permanentAddress");
    const currentAddress = document.getElementById("currentAddress");
    const permanentAddressContainer = document.getElementById("permanentAddress-container");
    function syncAddress() {
        permanentAddress.value = currentAddress.value;
    }
    function handleSameAddressChange() {
        const isChecked = sameAddressCheckbox.checked;
        permanentAddress.value = isChecked ? currentAddress.value : "";
        permanentAddress.toggleAttribute("readonly", isChecked);
        permanentAddressContainer.style.display = isChecked ? "none" : "block";
        permanentAddress.dispatchEvent(new Event("input"));

        if (isChecked) {
            currentAddress.addEventListener("input", syncAddress);
        } else {
            currentAddress.removeEventListener("input", syncAddress);
        }
    }
    handleSameAddressChange();
    sameAddressCheckbox.addEventListener("change", handleSameAddressChange);

   // Name Validation: Only Letters Allowed (No Spaces, Digits, or Special Characters)
   function setupNameValidation(fieldId, errorId) {
    const field = document.getElementById(fieldId);
    if (!field) return;

        field.addEventListener("input", function () {
            this.value = this.value.replace(/[^A-Za-z]/g, "");
            if (this.value) {
                hideError(errorId);
            } else {
                showError(errorId, "Only letters are allowed.");
            }
        });
    }
    setupNameValidation("name", "name");
    setupNameValidation("lastName", "lastName");


    // Function to validate pincode fields
    function validatePincode(event) {
        let pincodeField = event.target;
        pincodeField.value = pincodeField.value.replace(/\D/g, "").slice(0, 6);

        if (this.value.length === 6) {
            hideError(pincodeField.id);
        } else {
            showError(pincodeField.id, "Pincode must be exactly 6 digits.");
        }
        toggleVisibility(pincodeField.id);
    }
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
    const realTimeSelectFields = ["blood_group", "profession", "address_nagar","professionals_name","sub_category_type","university","institute", "course","stream", "nagar", "address_state", "state", "upbasti", "ekai", "prant", "vibhag", "jila", "ekai_nagar", "mandal", "basti", "sakha_milan", "dayitva", "vividhSangathan",
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

    document.querySelectorAll('input[name="pratigya"]').forEach((radio) => {
        radio.addEventListener("change", function () {
            hideError("pratigyaCheckbox");
        });
    });

    document.querySelectorAll('input[name="vividhsangathan_yes_no"]').forEach((radio) => {
        radio.addEventListener("change", function () {
            hideError("vividhCheckbox");
        });
    });

    document.querySelectorAll('input[name="responsibility_yes_no"]').forEach((radio) => {
        radio.addEventListener("change", function () {
            hideError("responsibility");
        });
    });
    
    document.querySelectorAll('input[name="rss_association"]').forEach((radio) => {
        radio.addEventListener("change", function () {
            hideError("rssAssociation");
        });
    });

    // Real-time validation for socialInterests checkboxes
    document.querySelectorAll('#socialInterests-container input[type="checkbox"]').forEach((checkbox) => {
        checkbox.addEventListener("change", function () {
            const checkboxes = document.querySelectorAll('#socialInterests-container input[type="checkbox"]:checked');
            const errorElement = document.getElementById("socialInterestsError");
            if (checkboxes.length === 0) {
                showError(errorElement, "Please select at least one option");
            } else {
                hideError("socialInterests");
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

         function setRadioModalContent(radioId,radioName, modalElementId, modalContainerId) {
            const radioField = document.querySelector(`input[name="${radioName}"]:checked`);
            const modalContainer = document.getElementById(modalContainerId);
            
            if (radioField && isFieldVisible(radioId)) {
                modalContainer.style.display = 'table-row'; 
                document.getElementById(modalElementId).textContent = radioField.value;
            } else {
                modalContainer.style.display = 'none'; 
            }
        }

        function setIndividualCheckboxContent(checkboxId, modalElementId, modalContainerId) {
            const checkbox = document.getElementById(checkboxId);
            const modalContainer = document.getElementById(modalContainerId);
            if (checkbox &&checkbox.checked && isFieldVisible(checkboxId)) {
                modalContainer.style.display = 'table-row';
                document.getElementById(modalElementId).textContent = checkbox.value;
            } else {
                modalContainer.style.display = 'none';
            }
        }

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
        setModalContent('professionals_name', 'modalProfessionType', 'modalProfessionTypeContainer');
        setModalContent('sub_category_type', 'modalProfessionSubtype', 'modalProfessionSubtypeContainer');
        setModalContent('university', 'modalUniversity', 'modalUniversityContainer');
        setModalContent('institute', 'modalInstitute', 'modalInstituteContainer');
        setModalContent('course', 'modalCourse', 'modalCourseContainer');
        setModalContent('stream', 'modalStream', 'modalStreamContainer');
        setRadioModalContent("vividhCheckbox",'vividhsangathan_yes_no', 'modalVividhSangathanCheckbox', 'modalVividhSangathanCheckboxContainer');
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
        setRadioModalContent("sakha_milanCheckbox",'ekai_milaan', 'modalSakhaMilanCheckbox', 'modalSakhaMilanCheckboxContainer');
        setModalContent('sakha_milan', 'modalSakhaMilan', 'modalSakhaMilanContainer');
        setModalContent('dayitva', 'modalDayitva', 'modalDayitvaContainer');
        setModalContent('sangh_shikshan_level', 'modalSanghSikshanLevel', 'modalSanghSikshanLevelContainer');
        setRadioModalContent('pratigyaCheckbox','pratigya', 'modalPratigyaCheckbox', 'modalPratigyaCheckboxContainer');
        setModalContent('prarambhik_year', 'modalPrarambhikYear', 'modalPrarambhikYearContainer');
        setModalContent('prathmik_year', 'modalPrathmikYear', 'modalPrathmikYearContainer');
        setModalContent('pratham_year', 'modalPrathamYear', 'modalPrathamYearContainer');
        setModalContent('dwitiya_year', 'modalDwitiyaYear', 'modalDwitiyaYearContainer');
        setModalContent('tritiya_year', 'modalTritiyaYear', 'modalTritiyaYearContainer');
        setRadioModalContent("ghoshVadakNo",'learn_vadya', 'modalLearnVadya', 'modalLearnVadyaContainer');
        setRadioModalContent("ghoshVadakNo",'learn_vadya_list', 'modalLearnVadyaList', 'modalLearnVadyaListContainer');
        setIndividualCheckboxContent('sanghPant', 'modalSanghPant', 'modalSanghPantContainer');
        setIndividualCheckboxContent('safedKameez', 'modalSafedKameez', 'modalSafedKameezContainer');
        setIndividualCheckboxContent('sanghTopi', 'modalSanghTopi', 'modalSanghTopiContainer');
        setIndividualCheckboxContent('sanghPeti', 'modalSanghPeti', 'modalSanghPetiContainer');
        setIndividualCheckboxContent('jurab', 'modalJurab', 'modalJurabContainer');
        setIndividualCheckboxContent('joote', 'modalJoote', 'modalJooteContainer');
        setIndividualCheckboxContent('dand', 'modalDand', 'modalDandContainer');
        setRadioModalContent("gender",'gender', 'modalGender', 'modalGenderContainer');
        setRadioModalContent("ghosh_vadak",'ghosh_vadak', 'modalGhoshVadak', 'modalGhoshVadakContainer');
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
            setRadioModalContent('shankhShrungOwn','shankh_shrung_own', 'modalShankhShrungOwn', 'modalShankhShrungOwnContainer');
            setRadioModalContent('rachnaye','rachnaye', 'modalRachnaye', 'modalRachnayeContainer');
        } else {
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
        let field = document.getElementById(`${fieldId}-container`);
        return field && field.style.display !== "none";
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
});







