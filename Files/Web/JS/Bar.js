const Donated = 0;
const Target = 1000;
const Progress = (Donated / Target) * 100;

document.getElementById("Amount").textContent = `Donated: ₹${Donated} / ₹${Target}`;
document.getElementById("Bar").style.width = `${Progress}%`;
document.getElementById("Percentage").textContent = `${Progress}%`;