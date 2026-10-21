# ops urgent status and execute

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_status_and_execute_20260518T103003_result.json`
- **Structured JSON:** [`30f7494e5923ff80033b.json`](../../sessions/30/30f7494e5923ff80033b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完整状态报告

### 1. nvidia-smi

| GPU | 进程 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | GPT-2m v4 (PID 310465) | 55705MiB / 97887MiB | 44% |
| cuda:1 | intervention_reactive_s42 (PID 340969) | 7453MiB / 97887MiB | 56% |

### 2. cuda:1 — intervention_reactive_s42 已在跑

- PID 340964 (bash wrapper) → PID 340969 (python)，tmux session `intervention_reactive_s42` 存在
- 当前在 Generation 0 (baseline)，刚启动 ~4 分钟
- **无需重复提交**

### 3. cuda:0 — GPT-2m v4 仍在跑

- 刚完成 gen_9 训练（5000/5000 steps），进入 **Generation 10/10**（最后一代）
- gen_10 目录已创建但为空（刚开始合成数据）
- 预计还需 **~40-50 分钟**完成（合成数据 + 5000 steps @ 2.05 it/s）
- **GPT-2m 分析和 intervention_predictive_s42 提交需等完成后执行**

### 4. 1.4B s43 n_perm=5000 重分析（CPU，已完成）

**Bug 修复**：`analyze_generalize.py` 的 `--n_perm` 参数未传递到 `perm_granger()`，实际始终用 1000。已修复 3 处传参链。

**n_perm=5000 结果**：**46/80** sig rate（与 n_perm=1000 一致，permutation test 稳定）

| Pair | Naive | Diff | Thresh | TY | PG | K |
|------|:-----:|:----:|:------:|:--:|:--:|:---:|
| token_entropy→ppl | S | . | S | . | . | 2/5 |
| token_entropy→d1 | S | S | S | S | S | **5/5** |
| token_entropy→d2 | S | S | S | . | S | **4/5** |
| token_entropy→d3 | S | S | S | . | S | **4/5** |
| self_bleu→ppl | S | S | . | . | . | 2/5 |
| self_bleu→d1 | S | . | . | . | . | 1/5 |
| self_bleu→d2 | S | . | . | . | . | 1/5 |
| self_bleu→d3 | S | . | . | . | . | 1/5 |
| ece→ppl | S | . | S | . | . | 2/5 |
| ece→d1 | S | S | S | S | S | **5/5** |
| ece→d2 | S | S | S | S | S | **5/5** |
| ece→d3 | S | S | S | S | S | **5/5** |
| eff_rank→ppl | . | . | . | . | . | 0/5 |
| eff_rank→d1 | S | S | . | . | S | 3/5 |
| eff_rank→d2 | S | S | . | . | S | 3/5 |
| eff_rank→d3 | S | S | . | . | S | 3/5 |

Per-method: naive 15/16, diff 10/16, thresh 8/16, TY 4/16, PG 9/16

### 5. 待执行（GPT-2m 完成后）

1. 运行 `analyze_generalize.py --exp gpt2m_wiki_a100_s42 --n_perm 5000` 提取 Table 7 GPT-2m 行
2. 提交 `intervention_predictive_s42` 到 cuda:0

### 新提交实验

无新提交（cuda:1 已被占用，cuda:0 还在跑）。

---
