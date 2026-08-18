# ✈️ AI Flight Delay & Dynamic Customer Compensation System

An intelligent end-to-end platform that predicts flight delays, monitors real-time disruptions via live news and weather scrapers, and automatically calculates compensation privileges or vouchers for passengers based on delay severity.

---

## 📌 Project Overview
Flight disruptions cause major inconveniences. This project automates both the prediction and the resolution phases of delay management:
1. **Predictive Intelligence:** Leverages machine learning models to assess the probability and expected duration of flight delays based on weather, route history, and air traffic data.
2. **Context-Aware Scraper:** Collects real-time operational updates, strikes, and weather alerts using a dedicated news scraper.
3. **Automated Privilege Decision Engine:** Determines eligibility and automatically assigns appropriate compensations, vouchers, or tier upgrades according to delay thresholds.

---

## 🎯 Key Features
* **AI Delay Prediction:** Forecasts arrival/departure delay risks using historical and real-time operational data.
* **Real-time News & Disruption Monitoring:** Aggregates airport conditions, air traffic issues, and weather advisories via the scraper module.
* **Dynamic Decision Engine:** Evaluates delay tiers and automatically triggers passenger entitlements:
  * **Short Delays (1–2 hrs):** Refreshment vouchers and complimentary lounge Wi-Fi access.
  * **Moderate Delays (2–4 hrs):** Meal vouchers and priority re-booking options.
  * **Severe Delays / Postponements (4+ hrs / Overnight):** Hotel accommodations, transport vouchers, full refunds, or complimentary seat upgrades for rescheduled flights.
* **Interactive Frontend & API Backend:** Streamlined user interface for passengers to check flight status and claim compensation instantly.

---

## 📁 Repository Structure
```text
AI-flight-delay/
│
├── backend/                  # Backend API services & database interfaces
├── frontend/                 # Web interface for passenger dashboard & claim portal
├── news scraper/             # Web scrapers for live news, weather, and aviation alerts
│
├── app.py                    # Main application server entry point
├── decision_engine.py        # Logic module for evaluating delays and granting privileges
└── README.md                 # Project documentation
