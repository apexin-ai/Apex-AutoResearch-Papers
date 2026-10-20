# diagnose exp A check results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_A_check_results_20260515T104822_result.json`
- **Structured JSON:** [`cca6daec3fa4524ab849.json`](../../sessions/cc/cca6daec3fa4524ab849.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行中。** 进程状态明确：

### 当前状态

- **tmux session `exp_A`** 正在运行 `run_exp_A.sh`
- 当前正在执行第 2/4 组：**Pythia × Qwen-cont**（Surprisal 计算中，PID 111726，CPU 107%）
- 日志仍在持续写入（最后修改 18:49:13，几秒前）
- 已完成约 49%（309/625 batches），当前在 depth 0 的 surprisal 提取阶段

### 已完成的结果：Pythia × Qwen-RW (1/4)

| 指标 | 值 |
|------|-----|
| **K\*** | **2** |
| AUC(0v1) | 0.9923 ± ~0.001 |
| AUC(1v2) | 0.7012 ± 0.007 |
| AUC(2v3) | 0.5870 ± 0.011 |
| AUC(3v4) | 0.5487 ± 0.006 |
| AUC(4v5) | 0.5285 ± 0.003 |
| Ordinal MAE | 1.006 |
| Ordinal Accuracy | 41.7% |
| **Spearman ρ vs Qwen baseline** | **0.906 (p=0.0)** |

**Top-5 Feature Importance:**
1. freq_entropy (8924)
2. surp_mean (8831)
3. hapax_ratio (8614)
4. surp_skew (8095)
5. surp_d1_mean (7995)

### 关键发现

1. **K\* = 2，与 Qwen-scored 一致** — 替代 scorer (Pythia-1.4B) 下可区分深度的断点不变
2. **Feature importance 与 Qwen baseline 高度相关** (ρ=0.906) — 特征重要性排序在不同 scorer 下稳健
3. 实验仍在运行，剩余 3 组（pythia_qwen_cont, olmo_qwen_rw, olmo_qwen_cont）尚未完成

需要等实验跑完再查看完整 4 组结果。当前进度估计：第 2 组的 depth 0 surprisal 约 49%，每组有多个 depth 要跑，总共还需较长时间。

---
