# fix plan 009 figure v5

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan_009_figure_v5_20260515T190021_result.json`
- **Structured JSON:** [`2a8e9478bc25106f1536.json`](../../sessions/2a/2a8e9478bc25106f1536.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三件事全部完成：

### 1. QLoRA KL001 eval 数据补全 ✓
- freige 脚本（`plot_forgetting_dynamics.py`）已包含完整 7 个 eval 点（step 0/10/20/30/50/60/90/100，step 0 为 SFT 锚点）
- v4 脚本也已更新：`eval_data['qlora_kl001']` 从 2 点扩展到 7 点
- 图表已重新生成到 `/root/autodl-tmp/freige/figures/grpo_forgetting_dynamics.{pdf,png}`

### 2. JSON 标签修复 ✓
- `forgetting_dynamics_data.json` 中 `qlora_grpo_lr5e6` 的 config：`kl=0` → `kl=0.01`

### 3. Checkpoint 可行性 ✓
三种 reward 变体的 checkpoint 均存在：

| Reward 类型 | 路径 | Checkpoints |
|---|---|---|
| **Extract** | `grpo_extract_r3/` | step 680-756 |
| | `grpo_extract_r4/` | step 10-30 |
| **FlatNLI** | `grpo_flatnli_r3/` | step 20-100 |
| | `grpo_flatnli_r4/` | step 120-160 |
| | `grpo_flatnli_r5/` | step 120-140 |
| | `grpo_flatnli_r6/` | step 10-20 |
| **CED** | `grpo_ced_r5/`, `grpo_ced_kl001/`, `grpo_ced_lr5e6/` 等 | 多轮完整 |

后续可对 extract/flatNLI checkpoint 跑 eval 补充数据到图中。

---
