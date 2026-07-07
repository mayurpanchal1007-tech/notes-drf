document.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("notesChart");

    if (!canvas) return;

    const labels = JSON.parse(
        document.getElementById("chart-labels").textContent
    );

    const data = JSON.parse(
        document.getElementById("chart-data").textContent
    );

    new Chart(canvas, {
        type: "line",

        data: {
            labels: labels,

            datasets: [{
                label: "Notes Created",

                data: data,

                borderWidth: 3,

                tension: 0.4,

                fill: true
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            plugins: {
                legend: {
                    display: true
                }
            },

            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }

    });

});