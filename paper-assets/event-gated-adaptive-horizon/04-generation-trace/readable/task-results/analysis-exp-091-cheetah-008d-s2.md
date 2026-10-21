# analysis exp 091 cheetah 008d s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_091_cheetah_008d_s2_20260525T225618_result.json`
- **Structured JSON:** [`57e12b40ecf35b1240a0.json`](../../sessions/57/57e12b40ecf35b1240a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

---

## exp_091_cheetah_008d_s2 分析报告

**结论: CIVO confirmed → success**

### Metrics 总表

| Step | eval_return | ve_ratio | value_mean | NVE |
|------|------------|----------|-----------|------|
| 15K | 97.2 | 0.017 | 1.69 | 0.44× |
| 25K | 126.4 | 0.091 | 11.49 | 1.32× |
| 35K | 182.6 | 0.144 | 26.28 | 1.09× |
| **45K** | **213.8** (peak) | 0.212 | 45.35 | **2.06×** (onset) |
| 55K | 98.9 | 0.692 | 68.40 | 2.92× |
| 65K | 2.2 | 34.80 | 77.52 | 129.8× |
| 75K | 1.9 | 43.14 | **81.16** (val peak) | **138.7×** (NVE peak) |
| 85K | 2.1 | 35.86 | 75.86 | 54.2× |
| 95K | 0.6 | **127.62** (VE peak) | 70.36 | 133.6× |
| 105K | 2.5 | 27.89 | 69.59 | 45.9× |

- **NVE peak: 138.7× @ 75K** — 远超 1.5× 阈值
- **NVE onset: 45K** — 与 exp_078 (s0) 完全一致
- **Classification: onset_collapse** — eval 从 213.8 崩塌至 ~2，无恢复
- gate_dt_mean=2.0, gate_dt_2_frac=1.0（固定 dt=2）

### 跨 Seed 对比

| Experiment | Seed | CIVO | NVE peak | Onset | Pattern |
|-----------|------|------|----------|-------|---------|
| exp_078 | s0 | **YES** | 4.1× | 45K | onset_collapse |
| exp_088 | s1 | NO | 0.517× | — | no_onset |
| **exp_091** | **s2** | **YES** | **138.7×** | **45K** | **onset_collapse** |

**Cheetah CIVO onset rate: 2/3 (67%)**

exp_091 的 CIVO 比 exp_078 严重得多（NVE 138.7× vs 4.1×），eval 在 55K-65K 之间发生灾难性崩溃（213→2），但 value 继续攀升至 81（典型的 value overestimation 脱轨）。两个 CIVO seed 的 onset 都在 45K，表明 Cheetah 环境中 CIVO 的触发时间点具有一致性。

---
