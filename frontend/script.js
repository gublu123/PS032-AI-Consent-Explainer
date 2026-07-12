// ======================================================
// AI Consent Form Explainer
// Load Available Ollama Models
// ======================================================

window.onload = function () {
    loadModels();
};

// ------------------------------------------------------
// Load Installed Models from Backend
// ------------------------------------------------------

async function loadModels() {

    try {

        const response = await fetch("http://127.0.0.1:8000/models");

        const data = await response.json();

        console.log("Available Models:", data);

        populateModelDropdown(data.models);

        populateModelCheckboxes(data.models);

    }

    catch (error) {

        console.error("Error loading models:", error);

        document.getElementById("modelSelect").innerHTML =
            "<option>Error Loading Models</option>";

    }

}

// ------------------------------------------------------
// Populate Dropdown
// ------------------------------------------------------

function populateModelDropdown(models) {

    const select = document.getElementById("modelSelect");

    select.innerHTML = "";

    if (!models || models.length === 0) {

        select.innerHTML =
            "<option>No Models Installed</option>";

        return;

    }

    models.forEach(model => {

        const option = document.createElement("option");

        option.value = model;

        option.textContent = beautifyModelName(model);

        // Default model
        if (model.startsWith("qwen3.5")) {

            option.selected = true;

        }

        select.appendChild(option);

    });

}

// ------------------------------------------------------
// Populate Checkboxes
// ------------------------------------------------------

function populateModelCheckboxes(models) {

    const container =
        document.getElementById("modelCheckboxes");

    container.innerHTML = "";

    if (!models || models.length === 0) {

        container.innerHTML =
            "<p>No Models Installed</p>";

        return;

    }

    models.forEach(model => {

        const label = document.createElement("label");

        label.style.display = "block";

        label.style.marginBottom = "8px";

        const checkbox = document.createElement("input");

        checkbox.type = "checkbox";

        checkbox.value = model;

        checkbox.className = "compareModel";

        // Default selected models
        if (

            model.startsWith("qwen3.5") ||

            model.startsWith("llama3.2") ||

            model.startsWith("gemma3")

        ) {

            checkbox.checked = true;

        }

        label.appendChild(checkbox);

        label.appendChild(

            document.createTextNode(

                " " + beautifyModelName(model)

            )

        );

        container.appendChild(label);

    });

}

// ------------------------------------------------------
// Beautify Model Name
// ------------------------------------------------------

function beautifyModelName(model) {

    const names = {

        "qwen3.5:4b": "⭐ Qwen 3.5 (4B)",

        "llama3.2": "🦙 Llama 3.2",

        "llama3.2:3b": "🦙 Llama 3.2 (3B)",

        "mistral": "🌪️ Mistral",

        "mistral:7b": "🌪️ Mistral (7B)",

        "gemma3": "💎 Gemma 3",

        "gemma3:4b": "💎 Gemma 3 (4B)",

        "deepseek-r1": "🧠 DeepSeek-R1"

    };

    return names[model] || model;

}

// ------------------------------------------------------
// Get Selected Compare Models
// ------------------------------------------------------

function getSelectedModels() {

    const selected = [];

    const checkboxes =
        document.querySelectorAll(".compareModel");

    checkboxes.forEach(box => {

        if (box.checked) {

            selected.push(box.value);

        }

    });

    return selected;

}

// ======================================================
// Show / Hide Loader
// ======================================================

function showLoader() {
    document.getElementById("loader").classList.remove("hidden");
}

function hideLoader() {
    document.getElementById("loader").classList.add("hidden");
}

// ======================================================
// Create FormData
// ======================================================

function createFormData(file, model) {

    const formData = new FormData();

    formData.append("file", file);
    formData.append("model", model);

    return formData;
}

// ======================================================
// Generate Summary (Single Model)
// ======================================================

async function uploadPDF() {

    const fileInput = document.getElementById("pdfFile");

    const model =
        document.getElementById("modelSelect").value;

    if (!fileInput.files.length) {

        alert("Please select a PDF or TXT file.");

        return;

    }

    showLoader();

    const file = fileInput.files[0];

    const formData =
        createFormData(file, model);

    try {

        const response = await fetch(

            "http://127.0.0.1:8000/upload-pdf",

            {
                method: "POST",
                body: formData
            }

        );

        const data = await response.json();

        console.log(data);

        if (!response.ok) {

            alert(

                data.error ||

                JSON.stringify(data)

            );

            hideLoader();

            return;

        }

        document.getElementById("summary").textContent =

            data.summary ||

            "No summary available.";

        document.getElementById("risks").textContent =

            data.risks ||

            "No risks found.";

        document.getElementById("missingRisks").textContent =

            Array.isArray(data.missing_risks)

            ? data.missing_risks.join("\n")

            : (data.missing_risks || "None");

        console.log(

            "Summary Generated Using:",

            data.model_used

        );

    }

    catch (error) {

        console.error(error);

        alert(

            "Error connecting to backend."

        );

    }

    finally {

        hideLoader();

    }

}

// ======================================================
// Compare Multiple Models
// ======================================================

async function compareModels() {

    const fileInput = document.getElementById("pdfFile");

    if (!fileInput.files.length) {

        alert("Please select a PDF or TXT file.");

        return;

    }

    const selectedModels = getSelectedModels();

    if (selectedModels.length === 0) {

        alert("Please select at least one AI model.");

        return;

    }

    showLoader();

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    // Send all selected models
    selectedModels.forEach(model => {

        formData.append("models", model);

    });

    try {

        const response = await fetch(

            "http://127.0.0.1:8000/compare-models",

            {

                method: "POST",

                body: formData

            }

        );

        const data = await response.json();

        console.log("Comparison Response:", data);

        if (!response.ok) {

            alert(

                data.error ||

                JSON.stringify(data)

            );

            hideLoader();

            return;

        }

        console.log("Results Array:", data.results);
        console.log("Is Array?", Array.isArray(data.results));

        displayComparisonResults(data.results);

    }

    catch (error) {

        console.error(error);

        alert("Error connecting to backend.");

    }

    finally {

        hideLoader();

    }

}

// ======================================================
// Clear Previous Comparison Results
// ======================================================

function clearComparisonResults() {

    document.getElementById(

        "comparisonResults"

    ).innerHTML = "";

}
   
// ======================================================
// Display Comparison Results
// ======================================================

function displayComparisonResults(results) {

    clearComparisonResults();

    const container =
        document.getElementById("comparisonResults");

    if (!results || results.length === 0) {

        container.innerHTML =
            "<h3>No comparison results available.</h3>";

        return;

    }

    // ==========================
    // Comparison Table
    // ==========================

    const table = document.createElement("table");

    table.style.width = "100%";
    table.style.borderCollapse = "collapse";
    table.style.marginBottom = "30px";

    table.innerHTML = `
        <tr style="background:#0d6efd;color:white;">
            <th style="padding:10px;border:1px solid #ddd;">Model</th>
            <th style="padding:10px;border:1px solid #ddd;">Time (sec)</th>
            <th style="padding:10px;border:1px solid #ddd;">Missing Risks</th>
        </tr>
    `;

    let bestModel = null;
    let bestTime = Number.MAX_VALUE;

    console.log("Results received:", results);
    results.forEach(result => {

        if (result.time < bestTime) {

            bestTime = result.time;
            bestModel = result.model;

        }

        const row = document.createElement("tr");

        row.innerHTML = `
            <td style="padding:10px;border:1px solid #ddd;">
                ${beautifyModelName(result.model)}
            </td>

            <td style="padding:10px;border:1px solid #ddd;">
                ${Number(result.time).toFixed(2)}
            </td>

            <td style="padding:10px;border:1px solid #ddd;">
                ${
                    Array.isArray(result.missing_risks)
                    ? result.missing_risks.length
                    : 0
                }
            </td>
        `;

        table.appendChild(row);

    });

    container.appendChild(table);

    // ==========================
    // Best Model
    // ==========================

    const winner = document.createElement("div");

    winner.className = "card";

    winner.innerHTML = `
        <h2>🏆 Fastest Model</h2>

        <h3>${beautifyModelName(bestModel)}</h3>

        <p><strong>Response Time:</strong> ${bestTime.toFixed(2)} seconds</p>

        <hr>
    `;

    container.appendChild(winner);

    // ==========================
    // Individual Cards
    // ==========================

    results.forEach(result => {

        container.appendChild(

            createComparisonCard(result)

        );

    });

}

// ======================================================
// Create One Comparison Card
// ======================================================

function createComparisonCard(result) {

    const card = document.createElement("div");

    card.className = "card";

    card.style.marginBottom = "25px";

    card.innerHTML = `

        <h2>${beautifyModelName(result.model)}</h2>

        <p>

            <strong>⏱ Response Time:</strong>

            ${Number(result.time).toFixed(2)} seconds

        </p>

        <hr>

        <h3>📋 Summary</h3>

        <pre>${result.summary}</pre>

        <h3>⚠ Extracted Risks</h3>

        <pre>${result.risks}</pre>

        <h3>❓ Missing Risks</h3>

        <pre>${
            Array.isArray(result.missing_risks)
                ? (
                    result.missing_risks.length > 0
                        ? result.missing_risks.join("\n")
                        : "None"
                )
                : (
                    result.missing_risks || "None"
                )
        }</pre>

    `;

    return card;

}