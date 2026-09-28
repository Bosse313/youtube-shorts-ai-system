<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>3D Workflow</title>
    <style>
      :root {
        --bg: #07131f;
        --panel: rgba(17, 29, 44, 0.9);
        --card: rgba(18, 42, 63, 0.9);
        --accent: #5be4ff;
        --accent-2: #7bffb2;
        --warning: #ffd166;
        --text: #edf7ff;
      }

      * { box-sizing: border-box; }

      body {
        margin: 0;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle at top, #102437, #06131f 58%);
        color: var(--text);
        font-family: Arial, sans-serif;
      }

      .scene {
        width: min(1100px, 92vw);
        height: 80vh;
        position: relative;
        perspective: 1200px;
        border-radius: 30px;
        overflow: hidden;
        background: rgba(4, 15, 23, 0.8);
        border: 1px solid rgba(91, 228, 255, 0.2);
      }

      .orbit {
        position: absolute;
        inset: 12% 8%;
        transform-style: preserve-3d;
        transform: rotateX(55deg) rotateZ(-20deg);
      }

      .card {
        position: absolute;
        width: 220px;
        min-height: 140px;
        padding: 16px;
        border-radius: 18px;
        background: linear-gradient(145deg, rgba(15, 35, 55, 0.9), rgba(12, 23, 35, 0.75));
        border: 1px solid rgba(91, 228, 255, 0.28);
        box-shadow: 0 30px 40px rgba(0,0,0,0.25);
        transform-style: preserve-3d;
      }

      .card h4 {
        margin: 0 0 10px;
        font-size: 1rem;
      }

      .card p {
        margin: 0;
        color: #cfe1f3;
        line-height: 1.5;
        font-size: 0.82rem;
      }

      .topbar {
        position: absolute;
        top: 18px;
        left: 24px;
        right: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 2;
      }

      .title {
        font-weight: 700;
        letter-spacing: 0.05em;
      }

      .link-btn {
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        color: #07131f;
        text-decoration: none;
        border-radius: 12px;
        padding: 10px 16px;
        font-weight: 700;
      }
    </style>
  </head>
  <body>
    <div class="scene">
      <div class="topbar">
        <div class="title">3D Workflow View</div>
        <a class="link-btn" href="/">Dashboard</a>
      </div>
      <div class="orbit" id="orbit"></div>
    </div>

    <script>
      async function loadWorkflow() {
        const res = await fetch('/api/workflow');
        const data = await res.json();
        const orbit = document.getElementById('orbit');
        const videos = data.generated || [];

        if (!videos.length) {
          orbit.innerHTML = '<div class="card" style="left: 50%; top: 50%; transform: translate(-50%,-50%) rotateY(0deg);"><h4>Kein Video</h4><p>Erzeuge zuerst ein Video aus einem Trend.</p></div>';
          return;
        }

        const active = videos[videos.length - 1];
        const steps = active.workflow || [];

        orbit.innerHTML = steps.map((step, index) => {
          const angle = (index / steps.length) * 360;
          const radius = 260 + (index % 3) * 30;
          const x = Math.cos(angle * Math.PI / 180) * radius;
          const y = Math.sin(angle * Math.PI / 180) * radius * 0.7;
          const z = (index % 2 === 0 ? 1 : -1) * 80;
          return `
            <div class="card" style="left: 50%; top: 50%; transform: translate3d(${x}px, ${y}px, ${z}px) rotateY(${index * 15}deg);">
              <h4>${step.title}</h4>
              <p>${step.detail}</p>
            </div>
          `;
        }).join('');
      }

      loadWorkflow();
      setInterval(loadWorkflow, 5000);
    </script>
  </body>
</html>
