# ops plan 001 status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_001_status_check_20260515T144149_result.json`
- **Structured JSON:** [`0465acaf3ac0149ae716.json`](../../sessions/04/0465acaf3ac0149ae716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### Flat-NLI Scoring (PID 208148/208155)
- **仍在运行**，已 45 分钟
- 进度：**17000/21728 (78.2%)**，最新日志 22:40:58
- 速率：~500 条/70 秒，剩余 4728 条，**预计 ~11 分钟后完成 (~22:52)**
- 输出目录 `/root/autodl-tmp/rsft_filtered_flat_nli/` 已创建但还是空的（scoring 完成后才写入）
- 占用 GPU 3，1458 MiB

### GPU 占用

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 1737/32607 MiB (5%) | 43% | PID 178055 (未知) |
| 1 | 14675/32607 MiB (45%) | 80% | PID 197386 (未知) |
| 2 | 24899/32607 MiB (76%) | 86% | PID 213006 (未知) |
| 3 | 14574/32607 MiB (45%) | 93% | PID 208155 (flat-NLI scoring, 1458 MiB) + PID 214562 (eval inference grpo_ced_g8_bf16/ckpt-80, 13102 MiB) |

### 注意
- **GPU 3 不空闲**：flat-NLI scoring + eval inference 同时跑，利用率 93%
- GPU 0 显存几乎空闲（仅 1.7GB），可用于新任务
- PID 214562 是刚启动 1 分钟的 eval inference（grpo_ced_g8_bf16 checkpoint-80 on DocRE dev set）

---
