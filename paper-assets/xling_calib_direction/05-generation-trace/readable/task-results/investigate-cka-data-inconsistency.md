# investigate cka data inconsistency

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_cka_data_inconsistency_20260521T122713_result.json`
- **Structured JSON:** [`b539c68702336e50abdc.json`](../../sessions/b5/b539c68702336e50abdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据下载超时，但核心验证已完成。现在写报告。

---

## CKA 数据一致性调查报告

### 1. 找到的 CKA 数据文件

共找到 **3 套 Qwen2.5-7B 数据** + **1 套 Llama-3.1-8B 数据**：

| 数据集 | 文件路径 | 修改时间 | sw L0 值 |
|--------|---------|---------|---------|
| **A: MVP原版** | `results/cka_results.csv` | 05-21 04:22 | **0.4397** |
| **A': MVP备份** | `xling_backup/results_mvp001/cka_results.csv` | — | 0.4397 (同A) |
| **B: 验证版** | `results/cka_matrix_verify.csv` | 05-21 10:50 | **0.4398** |
| **B': 验证复制** | `results_cka_mvp001/cka_matrix_qwen25_7b.csv` | 05-21 12:14 | 0.4398 (同B) |
| **C: Pilot版** | `results/cka_pilot/cka_matrix.csv` | 05-21 20:00 | **0.9058** |
| **D: Llama MVP003** | `results_cka_mvp003/cka_matrix_llama31_8b.csv` | 05-21 12:15 | 0.2654 |

实际上只有 **2 套不同的 Qwen 数值**：A/B ≈ 0.44 vs C = 0.91。

### 2. Layer 0 逐语言对比

| 语言 | A/B (全量) | C (Pilot) | 差值 |
|------|-----------|-----------|------|
| zh | 0.912 | 0.959 | +0.047 |
| ar | 0.901 | 0.948 | +0.047 |
| hi | 0.536 | 0.746 | **+0.210** |
| sw | 0.440 | 0.906 | **+0.466** |
| ko | 0.687 | 0.794 | +0.107 |

低资源语言偏差极大（sw 偏差 +0.47），高资源语言偏差较小。

### 3. 根因分析

**两套脚本使用相同的 activation 数据（14042 x 3584）和相同的 Linear CKA 公式。唯一区别是样本子集。**

- **`compute_cka.py`（根目录版）**：使用全部 14042 个样本 → sw L0 = 0.44
- **`code/compute_cka.py`（pilot 版）**：对 `.pt` 文件做位置 70/30 分割，只用后 30%（4213 样本）→ sw L0 = 0.91

我在服务器上直接复现了这个差异：

```
                full(14042)  eval30%(4213)  train70%(9829)  random(4213)
sw L0:            0.4397        0.9058         0.3135         0.4162
```

**随机抽样同样 4213 个样本给出 CKA = 0.42，接近全量值。** 这证明问题不是样本量，而是**位置分割导致的 subject 偏差**。

MMLU 数据按 subject 顺序排列，70/30 位置分割把不同的 subject 集合分到了 train 和 eval。后 30% 的 subject 碰巧在低资源语言上有更高的跨语言表征相似性（可能是 STEM 类 subject，术语更趋国际化）。

### 4. 结论

| 问题 | 答案 |
|------|------|
| **哪版正确？** | **A/B（全量版，sw L0 = 0.44）是正确的代表性 CKA 值** |
| **Pilot 版为何不同？** | `code/compute_cka.py` 的 `load_eval_activations()` 对 `.pt` 格式做了有偏的位置分割 |
| **需要修复什么？** | `code/compute_cka.py` 第 ~95 行 `pt_flat` 分支：应使用全量数据计算 CKA，或改为随机分割 |

如果 pilot 脚本需要 eval-only 数据做 CKA 与 probe metrics 的相关性分析（避免数据泄露），应在 activation 提取阶段就做随机分割并存为 `_train.npy` / `_eval.npy`，而不是在 CKA 计算时按位置切分。

---
