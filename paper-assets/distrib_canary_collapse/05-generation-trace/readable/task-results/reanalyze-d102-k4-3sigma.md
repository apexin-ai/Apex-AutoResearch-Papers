# reanalyze d102 k4 3sigma

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_reanalyze_d102_k4_3sigma_20260519T160816_result.json`
- **Structured JSON:** [`233b3c0db7353e550f4e.json`](../../sessions/23/233b3c0db7353e550f4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 registry 全部更新完成。汇总表：

| 实验 | PermG fwd | PermG rev | K≥4(3σ) | K≥3(3σ) | Naive | DiffXCorr | Thr(3σ) | TY | K≥4(2σ) | K≥3(2σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| pythia14b_wiki_s42 | 2/8 | 0/8 | **0/8** | 2/8 | 8/8 | 7/8 | 0/8 | 0/8 | 2/8 | 7/8 |
| pythia14b_wiki_s43 | 6/8 | 2/8 | **3/8** | 6/8 | 7/8 | 8/8 | 0/8 | 3/8 | 6/8 | 7/8 |
| pythia1b_c4_s42 | 8/8 | 3/8 | **4/8** | 8/8 | 8/8 | 8/8 | 0/8 | 4/8 | 8/8 | 8/8 |
| pythia1b_c4_s43 | 8/8 | 0/8 | **5/8** | 8/8 | 8/8 | 8/8 | 2/8 | 4/8 | 8/8 | 8/8 |

关键发现：

1. **D102 的 `"3x_sigma_drift"` 标签是错误的** — 实际代码 `method_ablation._onset_gen` 用的是 `2 * sigma`。真正的 3σ 结果差异很大。

2. **3σ threshold_onset 几乎全灭**：downstream 指标在 T=11 内很少突破 gen-0 + 3σ。canary（entropy gen1, ece gen2）能过 3σ，但 distinct_n 和 mauve 不行。唯一例外是 C4 s43 的两个 →mauve pair（onset gen 8）。

3. **K≥4(3σ) 完全依赖其余 4 个方法的共识**：threshold 贡献 ≈0，因此 K≥4 需要 Naive + DiffXCorr + PermG + TY 全部显著才行。C4 域最强（4-5/8），Wiki 1.4B s42 最弱（0/8）。

4. **K≥3(3σ) 对 C4 域依然完美**（8/8 × 2 seeds），Wiki 1.4B 有 seed 差异（s42=2/8, s43=6/8）。

JSON 保存在服务器 `results/generalize/analysis/3sigma_recompute_v2.json`。

---
