function toggleFields() {
    var checkBox = document.getElementById('find_intermediate_genes');
    var distanceField = document.getElementById('maximum_distance');
    var clustersField = document.getElementById('maximum_clusters');

    distanceField.disabled = !checkBox.checked;
    clustersField.disabled = !checkBox.checked;
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('find_intermediate_genes').addEventListener('change', toggleFields);
    toggleFields();
});

function toggleInputTypeSection() {
    var inputType = document.querySelector('input[name="input_type"]:checked').value;
    var section = document.getElementById('inputTypeSection');
    var databaseEntry = document.getElementById('databaseEntry'); // Assuming the ID of the text box is 'databaseEntry'

    if (inputType === 'remote' || inputType === 'remote_hmm') {
        section.style.display = 'block';
        databaseEntry.style.display = 'none'; // Hide the text box if not 'antismash' or 'mibig'
    } else if (inputType === 'antismash' || inputType === 'mibig') {
        section.style.display = 'none';
        databaseEntry.style.display = 'block'; // Display the text box if 'antismash' or 'mibig'
    } else {
        section.style.display = 'none';
        databaseEntry.style.display = 'none'; // Hide the text box for other cases
    }

    // Update fileSection visibility
    toggleFileSection();
}


document.addEventListener('DOMContentLoaded', function() {
    toggleInputTypeSection();
});

function toggleFileSection() {
    var fileRadio = document.getElementById('fileCheckbox');
    var fileSection = document.getElementById('fileSection');
    var inputTypeSectionVisible = document.getElementById('inputTypeSection').style.display !== 'none';

    if (fileRadio && fileRadio.checked && inputTypeSectionVisible) {
        fileSection.style.display = 'block';
    } else {
        fileSection.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    toggleFileSection();
});