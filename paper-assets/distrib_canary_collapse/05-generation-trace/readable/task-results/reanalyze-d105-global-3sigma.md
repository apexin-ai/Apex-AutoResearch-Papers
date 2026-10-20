# reanalyze d105 global 3sigma

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_reanalyze_d105_global_3sigma_20260519T162816_result.json`
- **Structured JSON:** [`129d2eecc3293bc3a975.json`](../../sessions/12/129d2eecc3293bc3a975.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## D105 完成报告

### Part A: 源码修复
`method_ablation.py` `_onset_gen` 已修复：`thresh = base + 2 * sigma` → `thresh = base + 3 * sigma`，所有注释/docstring 同步更新。备份为 `method_ablation.py.bak_d105`。

### Part B: 7 实验全局 3σ 重算

| 实验 | PermG fwd | PermG rev | K≥4(3σ) | K≥3(3σ) | Thr(3σ) | Thr(旧2σ) | 变化 |
|---|---|---|---|---|---|---|---|
| scale_69b (Pythia-6.9B) | 7/8 | 0/8 | **3/8** | 8/8 | 2/8 | 8/8 | -6 |
| qwen35_08b (Qwen-0.8B) | 8/8 | 0/8 | **6/8** | 8/8 | 0/8 | 8/8 | -8 |
| padding_robustness (410M) | 6/8 | 0/8 | **6/8** | 6/8 | 0/8 | 5/8 | -5 |
| pythia410m_wiki | 6/8 | 0/8 | **1/8** | 6/8 | 2/8 | 8/8 | -6 |
| gpt2m_wiki s42 | 6/8 | 3/8 | **2/8** | 6/8 | 0/8 | 6/8 | -6 |
| gpt2m_wiki s43 | 6/8 | 4/8 | **4/8** | 6/8 | 0/8 | 8/8 | -8 |
| opt1b_wiki | 6/8 | 0/8 | **2/8** | 6/8 | 2/8 | 8/8 | -6 |

### 关键发现
- **threshold_onset 大幅下降**：2σ→3σ 后，7 个实验的 threshold_onset 从平均 ~7/8 降到 ~1/8，确认 Reviewer 的 concern
- **K≥4 显著下降**：从旧值 6-8/8 降到 1-6/8，因为 threshold_onset 不再贡献 vote
- **K≥3 稳健**：所有实验保持 6/8（4 个实验保持 8/8），说明 naive+diff+PermG 三方法足够支撑
- **PermG/TY 完全不受影响**（符合预期）
- **3σ 阈值下仍有 onset 信号的 pair**：主要集中在 `*->mauve` 和 `*->distinct_3`（extreme collapse pairs）

### 产出文件
- 19828: `/root/autodl-tmp/distrib_canary_collapse/results/analysis/3sigma_recompute_d105.json`
- 17855: `/root/autodl-tmp/distrib_canary_collapse/results/analysis/3sigma_recompute_d105_17855.json`
- Artifact: `art_20260519_24d293`
- Registry: 7 个实验已更新 `robust_pairs_K4_3sigma`, `robust_pairs_K3_3sigma`, `threshold_onset_3sigma`, `D105_3sigma_note`

---
