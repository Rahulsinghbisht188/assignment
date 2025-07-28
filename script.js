// Smooth scroll for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
  
  // Contact form alert (basic interactivity)
  const form = document.querySelector("form");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Thank you! Your message has been sent.");
    form.reset();
  });
  