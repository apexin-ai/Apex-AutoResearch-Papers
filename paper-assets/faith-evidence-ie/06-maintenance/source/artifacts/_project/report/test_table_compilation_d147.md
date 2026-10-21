# Test Table Compilation — 2026-05-21

> Source: registry (DONE test_eval_* experiments) + comprehensive_results.md + dev_test_gap_paragraph.md
> All test evals use seed=42 on test_revised.json (500 docs)

---

## 1. Complete Test Set Results

### RSFT Test Results (all DONE)

| Scale | Test ign_f1 | Precision | Recall | evi_f1 | evi_f1_tp | EDCR | Trunc% | format_ok |
|-------|------------|-----------|--------|--------|-----------|------|--------|-----------|
| 1.7B Qwen | 0.2933 | 0.4625 | 0.2148 | 0.2320 | 0.6196 | 0.8169 | **73.8%** (369/500) | 500/500 |
| 4B Qwen | ❌ adapter lost | — | — | — | — | — | — | — |
| 8B Qwen | 0.3353 | 0.5149 | 0.2486 | 0.2526 | 0.6037 | 0.7993 | 1.8% (9/500) | 499/500 |
| 14B Qwen | 0.3849 | — | — | 0.2688 | 0.6025 | 0.7865 | 13.4% (67/500) | 499/500 |
| LLaMA-8B | 0.3599 | 0.4790 | 0.2882 | 0.2509 | 0.5447 | 0.8391 | **56.6%** (283/500) | 500/500 |

### SFT Test Results

| Scale | Test ign_f1 | Status | Trunc% | Source |
|-------|------------|--------|--------|--------|
| 1.7B Qwen | ⏳ | RUNNING | — | test_eval_1_7b_sft_s42 |
| 4B Qwen | **0.2232** | DONE ✅ | **64.6%** (323/500) | test_eval_4b_sft_s42 |
| 8B Qwen | ⏳ | RUNNING | — | test_eval_8b_sft_s42 |
| 14B Qwen | ⏳ | RUNNING | — | test_eval_14b_sft_s42 |
| LLaMA-8B | ⏳ | RUNNING | — | test_eval_llama_sft_s42 |

---

## 2. Dev → Test Gap Analysis (RSFT)

| Scale | Dev ign_f1 | Test ign_f1 | Gap (pp) | Retention% |
|-------|-----------|------------|----------|-----------|
| 1.7B Qwen | 0.5119 (3-seed mean) | 0.2933 | **-21.9** | 57.3% |
| 8B Qwen | 0.5433 (k=3 s42) | 0.3353 | **-20.8** | 61.7% |
| 14B Qwen | 0.5886 (s42) | 0.3849 | **-20.4** | 65.4% |
| LLaMA-8B | 0.5654 (3-seed mean) | 0.3599 | **-20.6** | 63.7% |

**Key observations:**
- Gap range: 20.4–21.9pp (spread = 1.5pp) — remarkably consistent
- Model ranking perfectly preserved: 1.7B < 8B < LLaMA-8B < 14B on both splits (Spearman ρ=1.0)
- Gap explained by annotation density: test has 34.7 gold triples/doc vs dev 12.3 (2.82× ratio)
- **Retention increases with scale**: 57.3% → 61.7% → 63.7% → 65.4%, suggesting larger models handle denser annotation better

### SFT Dev → Test Gap (preliminary, only 4B complete)

| Scale | Dev ign_f1 (s42) | Test ign_f1 | Gap (pp) | Retention% |
|-------|-----------------|------------|----------|-----------|
| 4B Qwen | 0.3974 | 0.2232 | **-17.4** | 56.2% |

4B SFT gap (17.4pp) appears smaller than RSFT gaps (~20pp), but 64.6% truncation makes this unreliable. Remaining 4 SFT test evals (currently running) will clarify whether SFT-RSFT gap pattern holds on test.

---

## 3. Gap List — What's Still Missing

### Currently Running (4 experiments)
1. **test_eval_1_7b_sft_s42** — 1.7B SFT test, pairs with RSFT test=0.2933
2. **test_eval_8b_sft_s42** — 8B SFT test, pairs with RSFT test=0.3353
3. **test_eval_14b_sft_s42** — 14B SFT test, pairs with RSFT test=0.3849
4. **test_eval_llama_sft_s42** — LLaMA SFT test, pairs with RSFT test=0.3599

### Not Yet Started
5. **4B RSFT test** — ❌ **Permanently missing.** Adapter checkpoint deleted, retrain attempt (retrain_4b_rsft_ced_s42) was killed. Cannot recover.
6. **14B no-evidence test** — D147 spot-check: verify evidence tax holds on test set. ~3-5h GPU cost.
7. **1.7B no-evidence test** — D147 spot-check: 1.7B is the most interesting case (evidence beneficial on dev, fair_tax=-5.63pp). ~2-3h GPU cost.
8. **8B no-evidence test** (optional) — Low priority, dev fair_tax=+0.04pp (neutral). Only if GPU budget allows.
9. **LLaMA no-evidence test** (optional) — Low priority unless SFT test shows interesting pattern.

### Priority ranking for remaining work:
1. **Wait for 4 running SFT evals** (already in progress, no action needed)
2. **14B no-evidence test** (highest value spot-check — strongest model, minimal truncation)
3. **1.7B no-evidence test** (tests whether "evidence beneficial at small scale" holds on test)
4. 8B / LLaMA no-evidence test (optional)

---

## 4. 4B Test ign_f1=0.2232 — Treatment in Paper

### Problem
4B SFT test is an outlier: ign_f1=0.2232 with 64.6% truncation, evi_f1=0.164 (vs ~0.25 for other scales). 4B RSFT adapter permanently lost — no RSFT test comparison possible.

### Diagnosis
- **64.6% truncation** at max_new_tokens=1024 means most outputs are cut off, losing predictions
- 4B dev SFT s42 ign_f1=0.3974, already the weakest SFT baseline
- Test annotation density (2.82× dev) amplifies the problem: 4B needs to generate more triples but runs out of tokens
- evi_f1=0.164 (vs test RSFT range 0.23–0.27) confirms severe output degradation

### Recommended paper treatment
1. **Include 4B SFT in test table** with truncation rate prominently displayed (Trunc.% column per D147)
2. **Footnote for 4B RSFT**: "4B RSFT checkpoint was inadvertently deleted during storage management; we report dev-set results (ign_f1=0.4466±0.53pp, n=4 seeds) which show the same RSFT>SFT pattern as other scales."
3. **Do NOT exclude 4B from the table** — omission looks worse than a low number with explanation
4. **In Limitations**: acknowledge that 4B's high truncation rate makes its test ign_f1 less reliable; the dev-test gap analysis (§X) shows the gap is consistent across other scales
5. **Dev table remains primary evidence** for 4B claims — test table is supplementary validation

---

## 5. Proposed Paper Test Table Structure

**Table X: Test Set Results (Re-DocRED test_revised, 500 docs)**

| Scale | Method | ign_f1 | evi_f1_tp | EDCR | Trunc.% |
|-------|--------|--------|-----------|------|---------|
| 1.7B | SFT | ⏳ | ⏳ | ⏳ | ⏳ |
| 1.7B | RSFT | 0.2933 | 0.6196 | 0.8169 | 73.8 |
| 4B | SFT | 0.2232 | 0.6121 | 0.8652 | 64.6 |
| 4B | RSFT | —† | — | — | — |
| 8B | SFT | ⏳ | ⏳ | ⏳ | ⏳ |
| 8B | RSFT | 0.3353 | 0.6037 | 0.7993 | 1.8 |
| 14B | SFT | ⏳ | ⏳ | ⏳ | ⏳ |
| 14B | RSFT | 0.3849 | 0.6025 | 0.7865 | 13.4 |
| LLaMA-8B | SFT | ⏳ | ⏳ | ⏳ | ⏳ |
| LLaMA-8B | RSFT | 0.3599 | 0.5447 | 0.8391 | 56.6 |

† 4B RSFT checkpoint unavailable; dev results (ign_f1=0.4466±0.53pp, n=4) in Table Y.

**Notes on metric choice:**
- **evi_f1_tp** (not evi_f1): test-set evi_f1 is deflated by low recall (many missed relations = many missed evidence). evi_f1_tp measures evidence quality on correctly predicted relations only — more meaningful and stable across scales (range 0.54–0.62).
- **evi_f1** (document-level): range 0.16–0.27 on test, much lower than dev (0.80+). This is a recall artifact, not evidence quality degradation. Include in appendix but not main table.

---

## 6. Truncation Analysis

| Scale | RSFT Trunc% | Note |
|-------|-------------|------|
| 1.7B | 73.8% | Severe — 1.7B generates verbose outputs, hits token limit |
| 4B SFT | 64.6% | Severe — similar pattern to 1.7B |
| LLaMA-8B | 56.6% | High — LLaMA more verbose than Qwen at same scale |
| 14B | 13.4% | Moderate — larger model is more concise |
| 8B Qwen | 1.8% | Minimal — 8B Qwen handles test density well |

**Implication**: truncation is the dominant factor driving low absolute test scores for 1.7B and LLaMA. For these scales, ign_f1 underestimates true capability. The paper should:
- Report truncation rates prominently (D147 requirement)
- Note that model ranking is preserved despite truncation differences
- Consider max_new_tokens=2048 test re-runs for 1.7B/LLaMA if time permits (but this changes the eval protocol — needs careful justification)
