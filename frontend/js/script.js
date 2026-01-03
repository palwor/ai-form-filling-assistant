async function uploadFile() {
    console.log("Button clicked");

    const fileInput = document.getElementById("fileInput");
    const loading = document.getElementById("loading");

    if (!fileInput.files.length) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    loading.classList.remove("hidden");

    try {
        const response = await fetch("http://127.0.0.1:8000/upload/", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        console.log("Backend response:", data);

        document.getElementById("name").value = data.extracted_data?.name || "";
        document.getElementById("dob").value = data.extracted_data?.dob || "";
        document.getElementById("aadhaar").value = data.extracted_data?.aadhaar || "";

    } catch (err) {
        console.error("FETCH ERROR:", err);
        alert("Frontend could not reach backend");
    }

    loading.classList.add("hidden");
}
