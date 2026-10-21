# ops fix p0p1 submit cuda3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-p0p1-submit-cuda3_20260514T200330_result.json`
- **Structured JSON:** [`3c4064f1f07c01b9b299.json`](../../sessions/3c/3c4064f1f07c01b9b299.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并开始 GRPO 训练循环。

**汇总：**
- **脚本**: `/root/autodl-tmp/scripts/train_ced_lr5e6_rp.sh`（含 `--ced_recall_penalty`）
- **tmux session**: `mvp2_grpo_ced_lr5e6_rp_r1`
- **Python PID**: 94055，运行在 cuda:3（4434 MiB）
- **状态**: 模型加载完成，NLI 模型加载完成，Stage 3 CED reward（tau 0.30→0.50），GRPO 训练已开始（0/200 steps）
- **同时运行**: P0 实验（`mvp2_grpo_ced_lr5e6_r1`, PID 90085）在 cuda:0 上

---
