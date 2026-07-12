/* Mitchell Plumbing & Heating — site interactions */
(function () {
  "use strict";

  /* ---- Mobile nav ---- */
  var body = document.body;
  var toggle = document.querySelector(".nav-toggle");
  var backdrop = document.querySelector(".nav-backdrop");
  function closeNav() { body.classList.remove("nav-open"); if (toggle) toggle.setAttribute("aria-expanded", "false"); }
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  if (backdrop) backdrop.addEventListener("click", closeNav);
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    a.addEventListener("click", function () { if (!a.parentElement.classList.contains("has-sub")) closeNav(); });
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeNav(); });

  /* ---- FAQ accordion ---- */
  document.querySelectorAll(".faq-q").forEach(function (btn) {
    btn.setAttribute("aria-expanded", "false");
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var isOpen = item.classList.toggle("open");
      btn.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  });

  /* ---- Scroll reveal ---- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Back to top ---- */
  var top = document.querySelector(".back-to-top");
  if (top) {
    window.addEventListener("scroll", function () {
      top.classList.toggle("show", window.scrollY > 600);
    }, { passive: true });
    top.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
  }

  /* ---- Active nav link by current path ---- */
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href && href === here) a.classList.add("active");
  });

  /* ---- Footer year ---- */
  var yr = document.querySelector("[data-year]");
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- Quote / contact form (front-end demo handling) ---- */
  var form = document.querySelector("form[data-quote-form]");
  if (form) {
    /* Multi-purpose form: swap "How can we help?" options per request type */
    var PURPOSES = {
      estimate: {
        placeholder: "Tell us about your project, your address or town, and the best time to reach you.",
        options: ["Plumbing project or install", "Water heater replacement",
                  "Hydronic / radiant heating", "Lochinvar boiler system",
                  "Commercial chiller / cooling", "Commercial or government project",
                  "New construction / remodel", "Bathroom or kitchen remodel",
                  "Something else"]
      },
      service: {
        placeholder: "Tell us what's going on, your address or town, and the best time to reach you.",
        options: ["Leak repair", "Clogged drain or sewer",
                  "Water heater problem / no hot water", "Boiler or heating problem / no heat",
                  "Faucet, toilet, or fixture repair", "Commercial chiller service",
                  "Maintenance or tune-up", "Something else"]
      },
      account: {
        placeholder: "Tell us about your question and the name or address on the account.",
        options: ["Billing or invoice question", "Payment question",
                  "Scheduling or appointment question", "Question about completed work",
                  "Warranty question", "Estimate follow-up", "Something else"]
      }
    };
    var purposeSel = form.querySelector("#purpose");
    var serviceSel = form.querySelector("#service");
    function applyPurpose() {
      var p = PURPOSES[purposeSel.value] || PURPOSES.estimate;
      var msg = form.querySelector("#message");
      if (msg) msg.setAttribute("placeholder", p.placeholder);
      serviceSel.innerHTML = "";
      var first = document.createElement("option");
      first.value = ""; first.textContent = "Choose one…";
      serviceSel.appendChild(first);
      p.options.forEach(function (o) {
        var el = document.createElement("option");
        el.textContent = o;
        serviceSel.appendChild(el);
      });
    }
    if (purposeSel && serviceSel) {
      purposeSel.addEventListener("change", applyPurpose);
      form.addEventListener("reset", function () { setTimeout(applyPurpose, 0); });
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      // Demo: simulate submit. Wire to a real endpoint (Formspree/Netlify/your CRM) on launch.
      setTimeout(function () {
        form.reset();
        if (btn) { btn.disabled = false; btn.textContent = "Send My Request"; }
        if (status) {
          status.style.color = "var(--teal-deep)";
          status.textContent = "Thanks! Mitch got your request — we'll be in touch within one business day. Need us sooner? Call (605) 996-7583.";
        }
      }, 700);
    });
  }
})();
