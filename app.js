async function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const successMessage = document.getElementById('successMessage');
    const imagePreview = document.getElementById('image-preview');
    const loadingSpinner = document.getElementById('loadingSpinner');

    if (!fileInput.files[0]) {
        alert("Please select an image to upload.");
        return;
    }

    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    // Show the loading spinner
    loadingSpinner.style.display = 'block';

    try {
        const response = await fetch('http://localhost:3000/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error("Failed to upload");

        const result = await response.json();

        successMessage.textContent = result.message;
        successMessage.style.opacity = 1;

        setTimeout(() => {
            successMessage.style.opacity = 0;
        }, 3000);

        const imgElement = document.createElement('img');
        imgElement.src = result.filePath;
        imgElement.alt = "Uploaded Image";

        const closeButton = document.createElement('button');
        closeButton.textContent = "×";
        closeButton.classList.add('close-button');
        closeButton.onclick = () => {
            imagePreview.innerHTML = '';
        };

        imagePreview.innerHTML = '';
        imagePreview.appendChild(imgElement);
        imagePreview.appendChild(closeButton);

    } catch (error) {
        console.error('Error uploading image:', error);
        successMessage.textContent = 'Failed to upload image. Please try again.';
        successMessage.style.opacity = 1;

        setTimeout(() => {
            successMessage.style.opacity = 0;
        }, 3000);

    } finally {
        loadingSpinner.style.display = 'none';
    }
}
