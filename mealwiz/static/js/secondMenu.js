// Function to show and populate the second menu
function showSecondMenu() {
    const firstMenu = document.getElementById("firstMenu");
    const selectedCategory = firstMenu.value;
    const secondMenuContainer = document.getElementById("secondMenuContainer");
    const secondMenu = document.getElementById("secondMenu");
    // Clear previous options
    secondMenu.innerHTML = "";

        // Get CSRF token value from hidden input
        const csrfToken = $('input[name="csrf_token"]').val();

        $.ajax({
            url: '/getcategorylist',
            type: 'POST',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': csrfToken  // Include token in headers
            },
            data: JSON.stringify({ key: selectedCategory }),
            success: function (response) {
                console.log('Success:', response);
                response.forEach(item => {
                    const option = document.createElement("option");
                    option.value = item.toLowerCase();
                    option.textContent = item;
                    secondMenu.appendChild(option);
                });
            },
            error: function (xhr, status, error) {
                console.error('Error:', error);
            }
        });
    secondMenuContainer.style.display = "block";
}
