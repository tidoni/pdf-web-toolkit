function downloadURI(uri, name) {
    var link = document.createElement("a");
    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    delete link;
}

function uploadPDF_split() {
    const fileInput = document.getElementById('split_pdfFile');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('pdf', file);

    const backendURL = '/split_to_zip';

    fetch(backendURL, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.debug("data from Backend: ", data)
        downloadURI(data["url"], data["name"]);
    })
    .catch(error => console.error(error));
}


function uploadPDF_merge() {
    const fileInput_1 = document.getElementById('merge_pdfFile_1');
    const file_1 = fileInput_1.files[0];
    const fileInput_2 = document.getElementById('merge_pdfFile_2');
    const file_2 = fileInput_2.files[0];
    const formData = new FormData();
    formData.append('pdf_1', file_1);
    formData.append('pdf_2', file_2);

    const backendURL = '/merge_to_pdf';

    fetch(backendURL, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.debug("data from Backend: ", data)
        downloadURI(data["url"], data["name"]);
    })
    .catch(error => console.error(error));
}