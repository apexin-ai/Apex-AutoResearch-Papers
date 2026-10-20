# paper verify gemma bootstrap

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_verify-gemma-bootstrap_20260521T102838_result.json`
- **Structured JSON:** [`06a7baa135a2472ad661.json`](../../sessions/06/06a7baa135a2472ad661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 文件路径

**`/root/autodl-tmp/simgate-modular-routing/results/unified_episode_bootstrap.json`**

该文件包含 qwen、llama、gemma 三个模型的 bootstrap 结果，每个模型有 11_tasks 和 10_tasks 两个配置。

---

### Gemma (Gemma-2-9B-it) DAF 关键数据

#### 11 tasks (N=220, 11 tasks)

| 字段 | 值 |
|---|---|
| **DAF 点估计** | **0.8965** (89.65%) |
| **DAF CI 下界** | **0.7951** (79.51%) |
| **DAF CI 上界** | **0.9837** (98.37%) |
| **B (bootstrap 次数)** | 10,000 (`n_valid`) |
| int_dr 点估计 | 0.3636 [0.30, 0.4273] |
| det_dr 点估计 | 0.1409 [0.0955, 0.1909] |
| delta_dr 点估计 | 0.2227 [0.1636, 0.2819] |

#### 10 tasks (N=200, 10 tasks)

| 字段 | 值 |
|---|---|
| **DAF 点估计** | **0.9990** (99.90%) |
| **DAF CI 下界** | **0.9966** (99.66%) |
| **DAF CI 上界** | **1.0000** (100.0%) |
| **B (bootstrap 次数)** | 10,000 (`n_valid`) |
| int_dr 点估计 | 0.40 [0.335, 0.47] |
| det_dr 点估计 | 0.155 [0.11, 0.21] |
| delta_dr 点估计 | 0.245 [0.18, 0.31] |

---

### 关于 79.5 / 98.4

- **79.5** → 匹配的是 Gemma 11_tasks DAF CI 下界 `0.7950999995787795` ≈ 79.51%
- **98.4** → 未在 `unified_episode_bootstrap.json` 中找到精确匹配。Gemma 11_tasks DAF CI 上界是 `0.9836633674101707` ≈ 98.37%，接近但不是 98.4。匹配 98.4 的文件都是 trainer_state / decomposition 报告等，不是 DAF 相关的

### Bootstrap 方法

文件中未显式记录 bootstrap 方法字段。从字段名 `unified_episode_bootstrap` 和脚本路径 `scripts/unified_episode_bootstrap.py` 判断，使用的是 **episode-level bootstrap**。B=10,000。

---
