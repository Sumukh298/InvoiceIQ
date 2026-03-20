async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("output").innerText = data.text;
}