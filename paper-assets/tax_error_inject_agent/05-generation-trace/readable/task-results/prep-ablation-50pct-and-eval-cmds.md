# prep ablation 50pct and eval cmds

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_ablation-50pct-and-eval-cmds_20260514T223520_result.json`
- **Structured JSON:** [`ce36103b98624dd1b654.json`](../../sessions/ce/ce36103b98624dd1b654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成，汇总如下：

---

### 任务 1：50% 注入消融数据

**已存在，无需生成。**

| 文件 | 路径 | 行数 |
|------|------|------|
| taxei 50% | `data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl` | 4,358 |
| random 50% | `data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl` | 4,358 |

按 `prepare_fixed_ablation_data.py` 的逻辑：`round(4358 * 0.5) = 2179` injected + 2179 clean，total=4,358。数据完备。

---

### 任务 2：Eval 命令模板

已写入 `artifacts/upcoming_eval_commands.md`，包含 5 个实验的 clean eval 命令和 recovery eval 变体模板。

当前 checkpoint 状态：

| 实验 | Checkpoint 位置 | 状态 |
|------|----------------|------|
| taxei-seed123 | `checkpoints/mini_taxei_sft_v4_seed123/v0-.../checkpoint-1129` | 可能已完成 |
| random-seed123 | `checkpoints/mini_random_sft_v4_seed123/v0-.../` | 训练中（无 checkpoint） |
| fixed-inject10 | `output/v4-fixed-inject10/v0-.../checkpoint-545` | 可能已完成 |
| fixed-inject25 | `output/v4-fixed-inject25/v0-.../` | 训练中（无 checkpoint） |
| fixed-inject50 | 未启动 | 数据已就绪 |

注意：inject10/25 的实际输出在 `output/` 目录而非 `checkpoints/` 目录。

---

### 任务 3：Additive 消融数据状态

**缺失 50% additive 数据。**

- `data/mini_pipeline_v4/ablation/` 目录下只有 inject10 和 inject25（taxei + random 各两个）
- inject10: 4,842 行（4358 clean + 484 injected）
- inject25: 5,810 行（4358 clean + 1452 injected）
- **无 inject50**：`prepare_ablation_data.py` 的 `RATIOS` 字典只定义了 10% 和 25%
- 生成方式：在脚本中的 `RATIOS` 里加 `"inject50": 0.50` 然后重跑即可

---
