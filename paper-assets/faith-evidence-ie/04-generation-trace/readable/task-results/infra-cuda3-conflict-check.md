# infra cuda3 conflict check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cuda3-conflict-check_20260515T162726_result.json`
- **Structured JSON:** [`9bb8dc1b4e406068a8bd.json`](../../sessions/9b/9bb8dc1b4e406068a8bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cuda:3 进程冲突报告

### PID 状态

| 任务 | 包装 PID | 实际 PID | 状态 | 运行时间 | 显存 |
|------|----------|----------|------|----------|------|
| eval_grpo_g8_bf16 | 214552 | **220202** | running — checkpoint-90 inference 60% (37/62) | 42min | 14464 MiB |
| plan_015_grpo_g4_bf16_v2 | 223970 (exited) | **223975** | running — step 8/200 | 20min | 14292 MiB |

### cuda:3 显存

**28770 / 32607 MiB (88%)，利用率 89%**，仅剩 ~3.8 GB。

### 冲突影响

明显有竞争。eval checkpoint-90 的 inference 速度在 GRPO 训练启动后显著退化：
- batch 1-26（训练启动前）：~50s/it
- batch 27+ （训练启动后）：**80-102s/it**，接近翻倍

目前没有 OOM，但余量很小（12%），如果 GRPO 训练在 generation 阶段分配更多显存，存在 OOM 风险。

### eval_grpo_g8_bf16 已完成结果（checkpoint-80）

| 指标 | 值 |
|------|-----|
| F1 | 0.4456 |
| Ign-F1 | 0.4456 |
| Evi-F1 | 0.8034 |
| EDCR | 0.6409 |
| Format OK | 984/985 (99.9%) |
| Truncated | 50/985 |

Checkpoint-90 正在跑（~60%），预计还需 25-30 分钟完成（受竞争影响）。Checkpoint-100 尚未开始。

### 建议

eval inference 预计 ~30min 完成，之后 cuda:3 显存释放 14.4GB，GRPO 训练可独占运行。如果不想等，可以 kill 掉 eval（PID 220202）让训练全速跑，后续再单独 eval。

---
