# ssh full status check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-status-check_20260515T012322_result.json`
- **Structured JSON:** [`92fad70b1d3e5a3ff4a4.json`](../../sessions/92/92fad70b1d3e5a3ff4a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

---

### 1. plan-014 (Qwen3-8B 生成) — **运行中 ~27%**

| 指标 | 值 |
|------|-----|
| PID | 134817 (alive, elapsed 1h05m) |
| 进度 | ~265/996 seeds (日志), 已写 416 行 / 475K |
| 最后输出 | depth=2 |
| 速度 | ~15-17s/seed |
| 预计剩余 | ~3h |

---

### 2. plan-004-v2 (OLMo-2-1B fine-tuning) — **运行中 5/15 完成 (33%)**

**进程状态**：3 GPU 全部存活 (43m, 41m, 40m)

**当前各 GPU 进度**：
- GPU1: step 467/741 (63% of current run)
- GPU2: step 1035/2307 (45% of current run)
- GPU3: 刚完成一个 run，进入 final eval

**已完成 5 runs**：

| Variant | eval_loss | perplexity |
|---------|-----------|------------|
| size_matched_seed42 | 0.8618 | 2.367 |
| size_matched_seed123 | 0.8615 | 2.367 |
| size_matched_seed456 | 0.8618 | 2.367 |
| depth01_seed456 | 0.8699 | 2.387 |
| binary_filtered_seed42 | 0.8708 | 2.389 |

**初步观察**：size_matched (3 seeds 平均 ppl=2.367) 优于 depth01 (ppl=2.387) 和 binary_filtered (ppl=2.389)。预计全部完成还需 ~1.5-2h。

---

### 3. plan-015 (bugfix-v2 baseline) — **已完成**

**Binoculars bug 确认**：denominator 误用 `obs_argmax` 而非 `shifted_ids`。

**修正后 Detector 结果 (LOGO F1 / Spearman ρ)**：

| Detector | LOGO F1 | 95% CI | Spearman ρ |
|----------|---------|--------|-----------|
| 7-feature ensemble | **0.7980** | [0.786, 0.799] | — |
| Avg-LogProb | 0.7653 | [0.616, 0.820] | 0.7876 |
| LD-Score | 0.7212 | [0.588, 0.770] | 0.7943 |
| FastDetectGPT | 0.6269 | [0.511, 0.762] | 0.4325 |
| Binoculars | 0.5790 | [0.405, 0.664] | 0.1989 |

**LD-Score 修正前后**：
- LOGO F1: 0.6854 → **0.7212** (+0.036)
- CV F1: 0.7083 → **0.7925** (+0.084)

**Bootstrap CI (n=23032, 1000 resamples)**：
- 7-feature vs Avg-LogProb: Δ=+0.039, p=0.0 (**显著**)
- 7-feature vs FastDetectGPT: Δ=+0.067, p=0.0 (**显著**)

---

plan-015 已完成，结果已产出。plan-014 和 plan-004-v2 仍在正常运行中，无需干预。

---
