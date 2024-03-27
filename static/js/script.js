// search redirecting
document
  .getElementById("searchForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    var query = document.getElementById("query").value; // Get the search query

    // Redirect to the search URL with query string
    window.location.href =
      "/search?query=" + encodeURIComponent(query) + "#section2";
  });

// scrollrevel

ScrollReveal({
  reset: true,
  distance: "80px",
  duration: 2000,
  delay: 200,
});

ScrollReveal().reveal("#section2,.sec1", { origin: "top" });
ScrollReveal().reveal("#section2,.column", { origin: "bottom" });

