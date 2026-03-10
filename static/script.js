console.log("Backend Roadmap Site Loaded");

document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("click", () => {
        card.style.transform = "scale(1.02)";
    });
});