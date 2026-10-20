# ops cuda3 emergency cleanup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda3-emergency-cleanup_20260515T150004_result.json`
- **Structured JSON:** [`c18eee81d4e00879c9a1.json`](../../sessions/c1/c18eee81d4e00879c9a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Step 6: 最终状态报告

| GPU | 显存占用 | 进程 |
|-----|---------|------|
| cuda:0 | 16925 / 32607 MiB | PID 216361 (16916 MiB) |
| cuda:1 | **0 / 32607 MiB** | 无进程，已完全释放 |
| cuda:2 | 24901 / 32607 MiB | PID 213006 (24892 MiB) |
| cuda:3 | 16040 / 32607 MiB | PID 208155 (NLI, 1458 MiB) + PID 214562 (batch eval, 14568 MiB) |

**cuda:3 清理结果：**
- PID 215286 (ckpt-100 eval) — 已 kill
- PID 215948 (OOM 进程) — 已自行退出
- 剩余进程符合预期：PID 214562 (batch eval) + PID 208155 (NLI scoring)

**batch eval 进度：**
- 正在评估 `checkpoint-100`，使用 LoRA adapter `/root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100`
- 推理进度：14/62 batches (23%)，每 batch 约 53s
- 预计剩余：48 batches × ~53s ≈ **42 分钟**（约 23:55 完成）

**cuda:1 已完全空闲**，可用于迁移 NLI scoring（仅需 ~1.4GB），但迁移需要 kill + restart NLI 进程。当前 NLI 和 batch eval 在 cuda:3 上共存无问题（16GB/32GB），无需迁移。

---
