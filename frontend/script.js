async function uploadPDF() {

    const fileInput = document.getElementById("pdfFile");

    if (!fileInput.files.length) {
        alert("Please select a PDF file.");
        return;
    }

    const loader = document.getElementById("loader");

    loader.classList.remove("hidden");

    const formData = new FormData();

    formData.append(
        "file",
        fileInput.files[0]
    );

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/upload-pdf",
            {
                method: "POST",
                body: formData
            }
        );
        console.log("Response Status:", response.status);

        const data = await response.json();
        console.log(data);

        document.getElementById("summary").textContent =
            data.summary || "No summary available.";

        document.getElementById("risks").textContent =
            data.risks || "No risks found.";

        document.getElementById("missingRisks").textContent =
            JSON.stringify(data.missing_risks, null, 2);

    } catch (error) {

        alert("Error connecting to backend.");

        console.error(error);

    } finally {

        loader.classList.add("hidden");
    }
}