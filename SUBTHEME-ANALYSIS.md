# BPC IFest 2026 — Subtheme Selection: Adversarial Research & Synthesis

**Status:** SUPERSEDED. Kept as historical record of the Part 1/2 validation process below. See the addendum at the bottom of this file for the team's actual, current committed direction.

---

## Part 1 — Re-evaluation Matrix (Green & Sustainable Technology)

After conducting an adversarial stress-test comparing the top candidates against strict startup requirements (large TAM, direct buyer clarity, daily frequency, operational urgency, and low regulatory dependency):

| Rank | Topic | Impact | AI Necessity | Technical Depth | Originality | Data Feasibility | Business | Scalability | Overall |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Industrial Combustion Optimization (BurnAI)** | 8.5 | 8.5 | 8.5 | 8.0 | 7.0 | 9.0 | 8.5 | **8.85 (Winner)** |
| 2 | Commercial HVAC Overcooling (*ChillAI*) | 9.0 | 8.0 | 8.5 | 5.5 | 8.5 | 8.5 | 7.5 | **8.55** |
| 3 | Cold-Chain Spoilage (*FreshRoute*) | 9.5 | 9.0 | 9.0 | 6.5 | 4.5 | 6.0 | 6.5 | **8.40** |
| 4 | CBAM Carbon Compliance SaaS | 7.85 | 6.0 | 6.0 | 8.0 | 7.0 | 6.0 | 8.0 | **2.85 (Penalized)** |

### Why Industrial Combustion Optimization Beats CBAM:
*   **Zero Regulatory Dependency:** Unlike CBAM, which is highly vulnerable to policy changes and timeline shifts by the EU, *BurnAI* solves an active, multi-million Rupiah daily operational cost. If the regulation disappears, *BurnAI* still survives on pure fuel cost-savings.
*   **Clear Payer and Budget:** The buyer is the factory Plant Manager or CFO, paying directly out of the active industrial fuel budget (OPEX) to reduce costs, rather than a compliance budget seen as corporate tax.
*   **Usage Frequency:** Boilers burn fuel 24/7. *BurnAI* provides daily recurring value, unlike CBAM which is used for quarterly/annual reporting.
*   **Low Compliance Liability:** *BurnAI* is a business optimization tool, not a legal certification tool. It avoids the high audit risks and liability of carbon reporting software.

---

## Part 2 — Core Concept: AI-Driven Industrial Combustion Optimization (*BurnAI*)

### The Problem
Mid-market manufacturing plants in Indonesia (textiles, food processing, paper, chemicals) rely on large industrial boilers to generate steam. Fuel (coal and gas) constitutes up to **30-40% of their operational overhead**. Due to manual damper adjustments and changing environmental conditions, boilers burn fuel inefficiently, wasting millions of Rupiah daily and releasing excess CO2 and NOx.

### The Solution: BurnAI
An AI-powered edge software that optimizes the air-to-fuel ratio in real-time.
1.  **Ingests:** Connects via Modbus/TCP to existing flue gas analyzers (O₂, CO, temperature) and air blowers.
2.  **Analyzes:** Uses non-linear thermodynamic machine learning models to map current combustion efficiency.
3.  **Predicts:** Forecasts optimal damper settings based on steam load fluctuations and ambient moisture.
4.  **Recommends:** Sends dynamic advisory parameters to operators (or directly to PLCs) to maintain peak thermal efficiency.
5.  **Direct Impact:** Reduces raw coal/gas consumption by **3-7%**, resulting in direct cost savings and equivalent carbon reductions.

---

## Part 3 — Next Phase: Customer Validation
The team must validate the operational workflow at local factories in West Java or Banten.
*   *Key Question:* "How frequently do you currently adjust boiler dampers, and what metrics does your plant manager use to determine combustion efficiency?"
*   *Key Question:* "Is your PLC system Modbus-compatible, and do you have digital flue gas analyzers installed?"

---

## Addendum (2026-08-26) — Pivot to waste-logistics: current committed direction

**The team pivoted away from BurnAI.** The actual proposal being written (`BPC Testing.txt` / `main.tex`) is a different Green & Sustainable Technology concept: an **IoT + AI waste-logistics SaaS platform for Jakarta** — ultrasonic fill-level sensors on TPS/commercial containers, an AI Dynamic Routing Engine, and a Predictive RDF Allocation System, targeting Bantar Gebang landfill overload and RDF Plant Rorotan feedstock quality. B2B (commercial estates/malls, obligated under Pergub DKI 102/2021) + B2G (DKI Jakarta government) revenue model, asset-light.

This pivot was made directly in the draft without ever being run through the adversarial validation process this document used for BurnAI (Part 1's scoring matrix). It is being formalized here retroactively:

- **Why it's still defensible under the same rubric:** clear direct payer (DLH DKI for B2G; building/mall managers for B2B, who have a *regulatory* obligation via Pergub 102/2021, not just a voluntary one); daily-frequency operational value (routing runs continuously, not a compliance-calendar product); real, large, verifiably overloaded problem (Bantar Gebang ~7,300–7,700 t/day, documented as over capacity — see the fact-check memory below); asset-light (rides existing government/private truck fleets, same asset-light principle Part 1 favored for BurnAI).
- **Where it's weaker than BurnAI's validation:** the competitive field is more crowded (Sensoneo, Ecube Labs, Compology globally; Waste4Change, Rekosistem, Microthings locally already sell adjacent products — BurnAI's originality score was higher), and there is a live regulatory risk (DKI announced in March 2026 a policy to ban "TPS sementara" outright, which could undercut a TPS-routing-optimization premise if not addressed directly in the plan).
- **Fact-check status:** every load-bearing claim in the draft (tonnage figures, RDF Plant Rorotan capacity/status, RDF calorific/moisture specs, methane GWP, BPS TPS counts, POJK 51/2017 and Pergub 102/2021 scope, SaaS Capital retention/margin benchmarks) has been independently verified by research agents; corrections are recorded in the `bpc-factcheck-findings` project memory rather than duplicated here.

No further action needed on this file — it's kept for the record of how the subtema was originally chosen, and this addendum exists so it stops contradicting the actual proposal.
