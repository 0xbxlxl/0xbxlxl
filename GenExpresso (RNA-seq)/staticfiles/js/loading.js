function checkStatus(datasetId) {
    fetch(`/check_status/${datasetId}/`)  // Ensure the URL matches your Django view
    .then(response => response.json())
    .then(data => {
        if (data.status === "done") {
            window.location.href = `/analyze_dataset/${datasetId}/`;
        } else {
            setTimeout(() => checkStatus(datasetId), 5000);
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    const datasetElement = document.getElementById("dataset-id");
    if (datasetElement) {
        const datasetId = datasetElement.dataset.id;
        checkStatus(datasetId);
    }
});
