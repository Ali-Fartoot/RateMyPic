// Define getCookie function globally
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Function to check if user has already liked or disliked an image
function hasUserInteracted(imageId) {
    return localStorage.getItem(`image-${imageId}-interaction`) !== null;
}

// Function to save user's interaction with an image
function saveUserInteraction(imageId, interaction) {
    localStorage.setItem(`image-${imageId}-interaction`, interaction);
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button[id^="like-"]').forEach(function(button) {
        let imageId = button.id.split('-')[1];

        // Disable like and dislike buttons if the user has already interacted
        if (hasUserInteracted(imageId)) {
            button.disabled = true;
            document.getElementById(`dislike-${imageId}`).disabled = true;
        }

        button.addEventListener('click', function() {
            let csrfToken = getCookie('csrftoken');
            let baseUrl = window.location.origin;  // Gets http://127.0.0.1:8000
            fetch(`${baseUrl}/gallery/like_image/${imageId}/`, {  // Construct the full URL
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked_count !== undefined) {
                    this.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z" />
                        </svg>
                        ${data.liked_count}
                    `;
                    // Disable both buttons after interaction
                    this.disabled = true;
                    document.getElementById(`dislike-${imageId}`).disabled = true;
                    saveUserInteraction(imageId, 'liked');
                }
            });
        });
    });

    document.querySelectorAll('button[id^="dislike-"]').forEach(function(button) {
        let imageId = button.id.split('-')[1];

        // Disable like and dislike buttons if the user has already interacted
        if (hasUserInteracted(imageId)) {
            button.disabled = true;
            document.getElementById(`like-${imageId}`).disabled = true;
        }

        button.addEventListener('click', function() {
            let csrfToken = getCookie('csrftoken');
            let baseUrl = window.location.origin;  // Gets http://127.0.0.1:8000
            fetch(`${baseUrl}/gallery/dislike_image/${imageId}/`, {  // Construct the full URL
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.disliked_count !== undefined) {
                    this.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z" />
                        </svg>
                        ${data.disliked_count}
                    `;
                    // Disable both buttons after interaction
                    this.disabled = true;
                    document.getElementById(`like-${imageId}`).disabled = true;
                    saveUserInteraction(imageId, 'disliked');
                }
            });
        });
    });
});
