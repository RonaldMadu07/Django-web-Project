function displayImage(input) {
    const passportDisplay = document.getElementById('passport-display');
    passportDisplay.innerHTML = ''; // Clear current image

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '100px';
            img.style.height = 'auto';
            passportDisplay.appendChild(img);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function toggleTerms() {
    const terms = document.getElementById('terms');
    const termsCheck = document.getElementById('terms-check');
    terms.style.display = termsCheck.checked ? 'block' : 'none';
}

function validateForm() {
    const phone = document.getElementById('phone').value;
    if (!/^\d+$/.test(phone)) {
        alert('Phone number must contain only digits.');
        return false;
    }
    return true;
}

function showTerms() {
    var termsText = document.getElementById("terms-text");
    termsText.style.display = termsText.style.display === "none" ? "block" : "none";
}
