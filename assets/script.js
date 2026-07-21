(function () {
  "use strict";

  /* ---------- Theme ---------- */
  var root = document.documentElement;
  var stored = localStorage.getItem("sl-theme");
  var theme = stored || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  root.setAttribute("data-theme", theme);

  document.addEventListener("DOMContentLoaded", function () {
    var themeSwitch = document.getElementById("theme-switch");
    if (themeSwitch) {
      themeSwitch.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
      themeSwitch.addEventListener("click", function () {
        var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        localStorage.setItem("sl-theme", next);
        themeSwitch.setAttribute("aria-pressed", next === "dark" ? "true" : "false");
      });
    }

    /* ---------- Mobile nav ---------- */
    var toggle = document.getElementById("nav-toggle");
    var sidebar = document.getElementById("sidebar");
    var scrim = document.getElementById("scrim");

    function closeNav() {
      sidebar.classList.remove("open");
      scrim.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    }
    function openNav() {
      sidebar.classList.add("open");
      scrim.classList.add("open");
      toggle.setAttribute("aria-expanded", "true");
    }
    if (toggle && sidebar && scrim) {
      toggle.addEventListener("click", function () {
        sidebar.classList.contains("open") ? closeNav() : openNav();
      });
      scrim.addEventListener("click", closeNav);
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") closeNav();
      });
      sidebar.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", closeNav);
      });
    }

    /* ---------- Scroll reveal ---------- */
    var revealEls = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window && revealEls.length) {
      var groups = {};
      revealEls.forEach(function (el) {
        var parentKey = el.parentElement;
        if (!groups.has) {}
      });
      var counters = new WeakMap();
      var io = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              var el = entry.target;
              var parent = el.parentElement;
              var idx = counters.get(parent) || 0;
              el.style.transitionDelay = Math.min(idx * 70, 350) + "ms";
              counters.set(parent, idx + 1);
              el.classList.add("in-view");
              io.unobserve(el);
            }
          });
        },
        { threshold: 0.15 }
      );
      revealEls.forEach(function (el) { io.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add("in-view"); });
    }

    /* ---------- Contact form -> mailto ---------- */
    var form = document.getElementById("contact-form");
    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var name = form.querySelector("#f-name").value.trim();
        var email = form.querySelector("#f-email").value.trim();
        var message = form.querySelector("#f-message").value.trim();
        var to = form.getAttribute("data-email");
        var subject = encodeURIComponent("Portfolio — message from " + (name || "website visitor"));
        var body = encodeURIComponent(message + "\n\n— " + name + " (" + email + ")");
        var note = document.getElementById("form-note");
        window.location.href = "mailto:" + to + "?subject=" + subject + "&body=" + body;
        if (note) note.hidden = false;
      });
    }
  });

  /* ---------- "Signal in the noise" canvas ---------- */
  function initNoiseCanvas() {
    var canvas = document.getElementById("noise-canvas");
    if (!canvas) return;
    var ctx = canvas.getContext("2d");
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function size() {
      var rect = canvas.parentElement.getBoundingClientRect();
      canvas.width = rect.width * devicePixelRatio;
      canvas.height = rect.height * devicePixelRatio;
    }
    size();
    window.addEventListener("resize", size);

    var cols = 26, rows = 20;
    var t = 0;
    var styles = getComputedStyle(document.documentElement);

    function draw() {
      var w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      var cellW = w / cols, cellH = h / rows;
      var muted = styles.getPropertyValue("--line").trim() || "#ccc";
      var accent = styles.getPropertyValue("--accent").trim() || "#127285";

      for (var y = 0; y < rows; y++) {
        for (var x = 0; x < cols; x++) {
          var n = Math.sin(x * 0.6 + t) * Math.cos(y * 0.5 - t * 0.8) + Math.sin((x + y) * 0.35 + t * 1.3);
          var signal = Math.sin(x * 0.42 - t * 0.6) * Math.sin(y * 0.5 + t * 0.4);
          var isSignal = signal > 1.15;
          var r = isSignal ? 2.6 : 1.1 + Math.abs(n) * 0.9;
          ctx.beginPath();
          ctx.fillStyle = isSignal ? accent : muted;
          ctx.globalAlpha = isSignal ? 0.9 : 0.35 + Math.abs(n) * 0.25;
          ctx.arc(x * cellW + cellW / 2, y * cellH + cellH / 2, r * devicePixelRatio, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      ctx.globalAlpha = 1;
    }

    draw();
    if (!reduceMotion) {
      (function loop() {
        t += 0.012;
        draw();
        requestAnimationFrame(loop);
      })();
    }
    new MutationObserver(draw).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initNoiseCanvas);
  } else {
    initNoiseCanvas();
  }
})();
