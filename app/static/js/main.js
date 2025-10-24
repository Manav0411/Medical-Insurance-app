// filepath: /insurance-predictor-flask/insurance-predictor-flask/app/static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('insurance-form');
    const resultDiv = document.getElementById('result');

    if (!form || form.dataset.ajax !== 'true') return;

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            if (resultDiv) {
                resultDiv.innerHTML = `Predicted Insurance Charges: $${data.prediction.toFixed(2)}`;
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            if (resultDiv) resultDiv.innerHTML = 'An error occurred while making the prediction.';
        });
    });
});