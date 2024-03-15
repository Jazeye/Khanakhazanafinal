// search redirecting
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    var query = document.getElementById('query').value; // Get the search query

    // Redirect to the search URL with query string
    window.location.href = "/search?query=" + encodeURIComponent(query) + "#section2";
});

