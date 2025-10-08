async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  addMessage("You", message, "user");

  const response = await fetch('http://localhost:80', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: message }) // your FastAPI expects key 'query'
});

  const data = await response.json();
  addMessage("EcoBot", data.response, "bot");

  input.value = "";
}

function addMessage(sender, text, type) {
  const box = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = `message ${type}`;
  div.innerHTML = `<strong>${sender}:</strong> ${text}`;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}

function createLeaf() {
  const leaf = document.createElement("div");
  leaf.classList.add("leaf");

  // Random horizontal position (viewport width)
  leaf.style.left = Math.random() * 100 + "vw";

  // Random start vertical position anywhere from top to bottom to simulate natural falling
  leaf.style.top = Math.random() * 100 + "vh";

  // Random size between 24px to 48px
  const size = 24 + Math.random() * 24;
  leaf.style.width = size + "px";
  leaf.style.height = size + "px";

  // Random animation duration between 8 to 15 seconds
  leaf.style.animationDuration = (8 + Math.random() * 7) + "s";

  // Start animation immediately but staggered by delay to prevent bunching
  leaf.style.animationDelay = "0s";

  // Random rotation start
  leaf.style.transform = `rotate(${Math.random() * 360}deg)`;

  // Append leaf to container
  document.querySelector(".leaf-container").appendChild(leaf);

  // Remove leaf after animation finishes to keep DOM clean
  setTimeout(() => leaf.remove(), 16000);
}

// Spawn leaves continuously
setInterval(createLeaf, 500);

// Spawn initial leaves on load
for (let i = 0; i < 10; i++) {
  setTimeout(createLeaf, i * 300);
}


function createCloud(fromLeft = true) {
  const cloud = document.createElement("div");
  cloud.classList.add("cloud");

  // Random duration: 60–120 seconds
  const duration = 60 + Math.random() * 60;
  cloud.style.setProperty('--animation-duration', `${duration}s`);

  // Random size: width between 60–200px
  const width = 60 + Math.random() * 140;
  const height = width * 0.6;
  cloud.style.width = `${width}px`;
  cloud.style.height = `${height}px`;

  // Random vertical position (cloud heights: 5vh to 35vh)
  cloud.style.top = `${5 + Math.random() * 30}vh`;

  // Starting position (left or right side)
  cloud.style.left = fromLeft ? `-250px` : `calc(100vw + 250px)`;

  // Movement distance for animation (right or left)
  const moveDistance = fromLeft ? `calc(100vw + 500px)` : `-calc(100vw + 500px)`;
  cloud.style.setProperty('--move-distance', moveDistance);

  // Depth effect: opacity + blur for realism
  cloud.style.opacity = (0.3 + Math.random() * 0.4).toFixed(2);
  cloud.style.filter = `blur(${2 + Math.random() * 3}px)`;

  // Append cloud to container
  document.querySelector(".cloud-container").appendChild(cloud);

  // Remove cloud after animation ends
  setTimeout(() => cloud.remove(), duration * 1000);
}



// Spawn 5 clouds initially from both sides, staggered by 800ms
for (let i = 0; i < 5; i++) {
  setTimeout(() => {
    createCloud(true);  // from left
    createCloud(false); // from right
  }, i * 800);
}
