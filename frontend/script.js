async function checkDelay() {
    try {
        const delay = document.getElementById("delay").value;
        const type = document.getElementById("type").value;

        const resultBox = document.getElementById("result");
        const loading = document.getElementById("loading");
        const explanation = document.getElementById("explanation");

        // Show loading
        loading.style.display = "block";
        resultBox.innerHTML = "";
        explanation.innerHTML = "";

 const response = await fetch(
" http://127.0.0.1:5000/check-delay",
{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({
delay_hours:Number(delay),
passenger_type:type
})
});

        const data = await response.json();

        // Hide loading
        loading.style.display = "none";

        // Show cards
        data.services.forEach(service => {
            const card = document.createElement("div");
            card.className = "card";

            let icon = "fa-star";

            if (service.includes("Food")) icon = "fa-utensils";
            if (service.includes("Lounge")) icon = "fa-couch";
            if (service.includes("Hotel")) icon = "fa-hotel";
            if (service.includes("Refund")) icon = "fa-money-bill";
            if (service.includes("Priority")) icon = "fa-bolt";

            card.innerHTML = `<i class="fas ${icon}"></i> ${service}`;
            resultBox.appendChild(card);
        });

        // Explanation
        explanation.innerText =
            "Based on delay of " + delay + " hours, services are assigned according to airline policy.";

    } catch (error) {
        console.error(error);
        document.getElementById("loading").innerText = "❌ Error connecting to server";
    }
}