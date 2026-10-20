# code c1 intervention prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c1_intervention_prep_20260525T005818_result.json`
- **Structured JSON:** [`f30204df264dfd9e4ace.json`](../../sessions/f3/f30204df264dfd9e4ace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计划已写入 `artifacts/c1_intervention_plan.json`。核心发现：

**代码就绪**：服务器 `iterative_train.py` 已支持 `--intervention_mode predictive/reactive`，无需修改。

**模型缓存**：
- GPT-2-medium: 已缓存 (1.5G)
- OPT-1.3B: 已缓存 (5.0G)
- Qwen2.5-0.8B: **不存在**。Qwen2.5 系列没有 0.8B，只有 0.5B 和 1.5B。服务器上有 `Qwen3.5-0.8B-Base` 的 ref（但权重未下载）

**已有 baseline**：GPT-2-medium 和 OPT-1.3B 的 no-intervention (α=1.0) 实验已完成（11 gen）。Qwen 无任何已有数据。

**磁盘**：74G 可用，总需 ~25G，可行。

**需要确认的问题**：
1. Qwen 用哪个模型？`Qwen2.5-0.5B` / `Qwen2.5-1.5B` / `Qwen3.5-0.8B-Base`？
2. 已有的 `predictive_te_a075_s42` 只跑到 gen_5 且无 `all_metrics.json`，是否需要重跑？
3. 新架构是否需要多 seed (s42+s43)？

**预计总 GPU 时间**：~16h（7 个实验，单 GPU 串行）。

---
