# ssh w1 k value audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w1-k-value-audit_20260518T075821_result.json`
- **Structured JSON:** [`be3c5a7ceba0456f0d03.json`](../../sessions/be/be3c5a7ceba0456f0d03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部审计完毕。以下是结论。

---

## 审计结论：W1 Cluster Bootstrap K 值

### 核心发现：K=7 是错的，K=11 才是正确的

两个文件使用了**完全不同的数据源**，导致 K 值不同。

### 1. W1 (K=7) — westd-18266

- **脚本**: `scripts/w1_cluster_bootstrap.py`
- **数据源**: `results/backbone_72b/` (按子目录扫描 `episode_summary.jsonl`)
- **实际 7 个 task** (240 episodes):

| Task | n |
|---|---|
| grow-fruit | 20 |
| identify-life-stages-1 | 20 |
| identify-life-stages-2 | 40 |
| inclined-plane-determine-angle | 40 |
| lifespan-longest-lived | 40 |
| lifespan-longest-lived-then-shortest-lived | 40 |
| measure-melting-point-unknown-substance | 40 |

- **缺失 4 个 task 的原因**:
  - `chemistry-mix/` — 目录存在但**空的**（没有 `episode_summary.jsonl`）
  - `find-animal/` — 目录存在但**空的**（没有 `episode_summary.jsonl`）
  - `find-non-living-thing/` — **目录不存在**
  - `freeze/` — **目录不存在**

### 2. cluster_bootstrap_results.json (K=11) — westb-13313

- **脚本**: `guided_router/cluster_bootstrap.py`
- **数据源**: `results/baseline_245eps/episode_details.jsonl` (单文件，245 episodes)
- **全部 11 个 task**:

| Task | n |
|---|---|
| chemistry-mix | 20 |
| find-animal | 20 |
| find-non-living-thing | 40 |
| freeze | 20 |
| grow-fruit | 20 |
| identify-life-stages-1 | 20 |
| identify-life-stages-2 | 20 |
| inclined-plane-determine-angle | 20 |
| lifespan-longest-lived | 25 |
| lifespan-longest-lived-then-shortest-lived | 20 |
| measure-melting-point-unknown-substance | 20 |

### 3. 245 episode counterfactual pairs 覆盖

`baseline_245eps/episode_details.jsonl` = **245 episodes, 11 tasks**。这是完整数据集。

### 4. 根因

W1 Worker 的脚本硬编码读取 `results/backbone_72b/`，但该目录是**不完整的子集**：
- `chemistry-mix` 和 `find-animal` 有空目录（数据未生成或未拷贝到该目录）
- `find-non-living-thing` 和 `freeze` 完全没有对应子目录

W1 脚本用 `os.listdir()` + `os.path.exists(ep_file)` 扫描，自动跳过了没有 `episode_summary.jsonl` 的目录，**无任何 warning 输出**，静默产出 K=7。

### 5. 正确 K 值

**K=11**。245 episode counterfactual pairs 覆盖 11 个 unique tasks。W1 的 K=7 是因为数据源 `backbone_72b/` 缺少 4 个 task 的数据。

### 6. 额外注意：episode 数也不一致

即便是 7 个重叠 task，两边的 episode 数也不完全对齐（backbone_72b 部分 task 有 40 episodes，baseline_245eps 对应 task 只有 20-25）。这说明 `backbone_72b/` 可能是另一批实验的产物，不应作为 245-episode 分析的数据源。

---
