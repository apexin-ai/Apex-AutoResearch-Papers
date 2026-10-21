# analysis smollm3 3b s42 v3 d105 rerun

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smollm3_3b_s42_v3_d105_rerun_20260519T191218_result.json`
- **Structured JSON:** [`0c93730220662afd2a82.json`](../../sessions/0c/0c93730220662afd2a82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存，registry 已更新。

## SmolLM3-3B s42 D105 标准分析结果

| 指标 | 旧值 (2σ, raw) | D105 (3σ, FDR) |
|---|---|---|
| PermG_fwd | 6/8 | **3/8** |
| PermG_rev | 0/8 | 0/8 |
| K≥4 | 6/8 (2σ) | **0/8** (3σ) |
| K≥3 | 7/8 (2σ) | **3/8** (3σ) |
| threshold_onset | 8/8 (2σ) | **0/8** (3σ) |

**关键变化**：
- PermG_fwd 从 6/8 降至 3/8 — 因为 D105 使用 FDR 校正（之前是 raw p-value）
- threshold_onset 从 8/8 (2σ) 降至 0/8 (3σ) — 下游指标无一突破 3σ 阈值，导致所有 pair 丢掉一票
- K≥4(3σ)=0/8：无 pair 达到 robust 级别（ece→d1/d2/d3 最高 K=3）
- K≥3(3σ)=3/8：仅 ece→distinct_{1,2,3} 三对（naive + diff + perm_granger）

3σ 标准下 SmolLM3-3B 信号显著弱于 2σ，与该实验 `conclusion: negative` 一致。

---
