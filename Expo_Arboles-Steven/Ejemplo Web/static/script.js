const canvas = document.getElementById('visualization');
const ctx = canvas.getContext('2d');
let steps = [];
let currentStep = 0;
let animating = false;

function setupCanvas() {
    canvas.width = 800;
    canvas.height = 400;
}

function drawBars(arr, highlight = -1) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const barWidth = canvas.width / arr.length;
    const maxHeight = Math.max(...arr);

    arr.forEach((num, i) => {
        const height = (num / maxHeight) * (canvas.height - 50);
        ctx.fillStyle = i === highlight ? '#ff4444' : '#c963e0';
        ctx.fillRect(i * barWidth, canvas.height - height, barWidth - 2, height);
        ctx.fillStyle = '#000';
        ctx.fillText(num, i * barWidth + barWidth / 2 - 10, canvas.height - height - 10);
    });
}

async function startSort() {
    if (animating) return;
    const input = document.getElementById('numbers').value;
    const response = await fetch(`/sort/${input}`);
    const data = await response.json();

    if (data.error) {
        alert(data.error);
        return;
    }

    steps = data.steps;
    currentStep = 0;
    animating = true;
    animate();
}

function animate() {
    if (currentStep >= steps.length) {
        animating = false;
        return;
    }

    drawBars(steps[currentStep]);
    currentStep++;
    setTimeout(animate, 500);
}

function reset() {
    animating = false;
    currentStep = 0;
    steps = [];
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    document.getElementById('numbers').value = '';
}

window.onload = setupCanvas;