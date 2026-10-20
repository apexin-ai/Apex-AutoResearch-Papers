# Reference Audit Report — Related Work Draft
**Date**: 2026-05-15
**Audited file**: `related_work_draft_0456d1.md`
**Method**: Web search verification of each 2024-2025+ citation

---

## Part 1: 8 Required Verifications

### ✅ VERIFIED: hafner2025dreamerv4
- **Title**: "Training Agents Inside of Scalable World Models"
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Venue**: arXiv:2509.24527 (2025). No confirmed conference venue; arXiv preprint.
- **Draft accuracy**: Draft says "replaces RSSM with a transformer world model, demonstrating scalability to video pretraining" — accurate.

### ⚠️ CORRECTED: nhu2025tawm
- **Title**: "Time-Aware World Model for Adaptive Prediction and Control" — correct
- **Authors**: Anh N. Nhu, Sanghyun Son, Ming C. Lin — correct
- **Venue**: ICML 2025 — confirmed. arXiv:2506.08441
- **Issue**: Draft says "TAWM is built on TD-MPC2 and uses online model-predictive control". TAWM is presented as **model-agnostic** and evaluated on TD-MPC2, not inherently tied to it. Suggest revising to: "TAWM is evaluated on TD-MPC2, which uses online MPC" or "instantiated on TD-MPC2".

### ✅ VERIFIED: li2025lsimagine
- **Title**: "Open-World Reinforcement Learning over Long Short-Term Imagination"
- **Authors**: Jiajian Li, Qi Wang, Yunbo Wang, Xin Jin, Yang Li, Wenjun Zeng, Xiaokang Yang
- **Venue**: ICLR 2025 **Oral** — confirmed (Oral Session 2A)
- **arXiv**: 2410.03618
- **Draft accuracy**: "extends the effective imagination horizon via goal-conditioned jumpy state transitions" — accurate.

### ⚠️ CORRECTED: palenicek2025
- **Title**: "Diminishing Return of Value Expansion Methods" — correct (matches arXiv:2412.20537, Dec 2024)
- **Authors**: Daniel Palenicek, Michael Lutter, Joao Carvalho, Daniel Dennert, Faran Ahmad, Jan Peters — correct
- **Issue**: Venue claimed as **"RLC 2025"** — **UNVERIFIED**. No public confirmation of acceptance at RLC 2025. Earlier version (arXiv:2303.03955) was reviewed at ICLR 2023. Recommend citing as arXiv:2412.20537 until venue is confirmed, or verify directly with authors.

### ✅ VERIFIED: kim2025deas
- **Title**: "DEAS: DEtached value learning with Action Sequence for Scalable Offline RL"
- **Authors**: Changyeon Kim, Haeone Lee, Younggyo Seo, Kimin Lee, Yuke Zhu
- **arXiv**: 2510.07730 — confirmed
- **Note**: Not cited in the draft text but present in literature_map.yaml. Citation key and content match.

### ❌ SUSPECT: luo2025vpl — **AUTHOR ATTRIBUTION WRONG**
- **Actual paper**: "A Case for Validation Buffer in Pessimistic Actor-Critic"
- **Actual authors**: **Michal Nauman, Mateusz Ostaszewski, Marek Cygan** — NOT "Luo F."
- **Venue**: IJCAI 2025 — confirmed. arXiv:2403.01014
- **Problem**: Citation key `luo2025vpl` attributes to a non-existent author "Luo". No author named Luo appears on this paper. The literature_map.yaml entry has a fabricated author.
- **Fix**: Change citation key to `nauman2025vpl`, update authors to [Nauman M., Ostaszewski M., Cygan M.].

### ✅ VERIFIED: engstrom2020
- **Title**: "Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO"
- **Authors**: Logan Engstrom, Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Firdaus Janoos, Larry Rudolph, Aleksander Madry
- **Venue**: ICLR 2020. arXiv:2005.12729
- **Note**: Not directly cited in draft text, but referenced in literature_map. Title sometimes appears with "Deep RL" instead of "Deep Policy Gradients" (ICLR submission vs. arXiv final).

### ✅ VERIFIED: andrychowicz2021
- **Title (ICLR)**: "What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study"
- **Title (arXiv)**: "What Matters In On-Policy Reinforcement Learning? A Large-Scale Empirical Study"
- **Authors**: Marcin Andrychowicz, Anton Raichuk, Piotr Stańczyk, et al.
- **Venue**: ICLR 2021. arXiv:2006.05990
- **Note**: Two different titles exist (conference vs. arXiv). Recommend using the ICLR published title.

---

## Part 2: Additional 2024-2025+ Citations in Draft

### ✅ VERIFIED: gumbsch2024thick
- **Title**: "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics"
- **Venue**: ICLR 2024. arXiv:2312.01418

### ✅ VERIFIED: mattes2024hieros
- **Title**: "Hieros: Hierarchical Imagination on Structured State Space Sequence World Models"
- **Venue**: ICML 2024. arXiv:2310.05167

### ✅ VERIFIED: hussing2024dissecting
- **Title**: "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence"
- **Venue**: Reinforcement Learning Journal (RLC 2024). arXiv:2403.05996

### ✅ VERIFIED: voelcker2025madtd
- **Title**: "MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL"
- **Venue**: ICLR 2025. arXiv:2410.08896

### ✅ VERIFIED: frauenknecht2025rollouts
- **Title**: "On Rollouts in Model-Based Reinforcement Learning"
- **Venue**: ICLR 2025. arXiv:2501.16918

### ✅ VERIFIED: barkley2024stealing
- **Title**: "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning"
- **Venue**: arXiv:2412.14312, accepted to ICML 2025

### ✅ VERIFIED: zhang2026hwm
- **Title**: "Hierarchical Planning with Latent World Models"
- **Authors**: Wancong Zhang, et al. (11 co-authors incl. Yann LeCun, Nicolas Ballas)
- **Venue**: arXiv:2604.03208 (2026)

### ✅ VERIFIED: shaj2023mts3
- **Title**: "Multi Time Scale World Models"
- **Venue**: NeurIPS 2023. arXiv:2310.18534

### ✅ VERIFIED: farebrother2024stopregressing
- **Title**: "Stop Regressing: Training Value Functions via Classification for Scalable Deep RL"
- **Venue**: ICML 2024 (oral). arXiv:2403.03950

---

## Summary

| Status | Count | Citations |
|--------|-------|-----------|
| ✅ VERIFIED | 14 | hafner2025dreamerv4, li2025lsimagine, kim2025deas, engstrom2020, andrychowicz2021, gumbsch2024thick, mattes2024hieros, hussing2024dissecting, voelcker2025madtd, frauenknecht2025rollouts, barkley2024stealing, zhang2026hwm, shaj2023mts3, farebrother2024stopregressing |
| ⚠️ CORRECTED | 2 | nhu2025tawm (minor: "built on" → "evaluated on" TD-MPC2), palenicek2025 (venue RLC 2025 unverified) |
| ❌ SUSPECT | 1 | luo2025vpl (author "Luo F." is fabricated; actual authors: Nauman, Ostaszewski, Cygan) |

## Required Actions
1. **luo2025vpl**: Fix citation key → `nauman2025vpl`, fix authors → Nauman M., Ostaszewski M., Cygan M.
2. **nhu2025tawm**: Revise draft text from "TAWM is built on TD-MPC2" to "TAWM is evaluated on TD-MPC2" (TAWM is model-agnostic)
3. **palenicek2025**: Change venue to "arXiv:2412.20537" until RLC 2025 acceptance is confirmed, or verify with authors
