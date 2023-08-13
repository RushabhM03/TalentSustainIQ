document.getElementById("openPostmanButton").addEventListener("click", function () {
    // Define the URL you want to populate in the Postman request
    var apiUrl = "https://0.0.0.0:5000/training"; // Replace with your desired URL

    // Open Postman with the URL
    var postmanUrl = "postman://?url=" + encodeURIComponent(apiUrl);
    window.location.href = postmanUrl;
});
