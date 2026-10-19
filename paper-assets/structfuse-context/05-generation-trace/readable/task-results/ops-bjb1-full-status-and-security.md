# ops bjb1 full status and security

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-full-status-and-security_20260513T100709_result.json`
- **Structured JSON:** [`adb0a6bcaf8130753e03.json`](../../sessions/ad/adb0a6bcaf8130753e03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## 双卡状态表

| 维度 | cuda:0 — plan_013_starcoder | cuda:1 — m2_embed_verify |
|---|---|---|
| **GPU** | RTX PRO 6000 Black, 73°C, 100% util | RTX PRO 6000 Black, 70°C, 100% util |
| **VRAM** | 23,858 / 97,887 MiB (24%) | 22,330 / 97,887 MiB (23%) |
| **主 PID** | 39221 (dataflow train, 48min) | 37880 (embedding train, 1h03m) |
| **Wrapper PID** | 23798 (alive, 4h41m) | 29290 (alive) |
| **当前策略** | **dataflow_aware** (3/3) | **embedding_distance** (2/3) |
| **进度** | Epoch 1, step 500/~1640, eval@500 pending | Epoch 2, step 900/~1640 |
| **已完成策略** | random ✅ embedding ✅ | random ✅ |

### plan_013_starcoder 已完成策略指标

| 策略 | best val_loss | recall@1 | recall@5 | best step |
|---|---|---|---|---|
| random | 0.5113 | 0.492 | 0.980 | — |
| **embedding** | **0.4816** | **0.508** | **0.984** | 1000 |
| dataflow | — 训练中 — | | | |

### m2_embed_verify 已完成策略指标

| 策略 | best val_loss | recall@1 | recall@5 | best step |
|---|---|---|---|---|
| random | 0.4834 | 0.536 | 0.981 | 500 |
| **embedding** (当前best) | **0.4603** | **0.556** | **0.981** | 500 |
| dataflow | — pending — | | | |

## Dataflow 启动情况

**不需要手动启动 dataflow retry。** Wrapper 脚本 (PID 23798) 在 embedding 完成后自动推进到 dataflow 阶段，使用原始参数 batch=4/neg=5/seq=2048。在 96GB 卡上运行正常（仅用 24% VRAM），无 OOM。auto_start 脚本 (PID 38446) 也已正常退出确认。

## 可疑进程排查

**无可疑进程。** 检测到的额外 python 进程：
- PID 41171, 41172, 41173 (ppid=37880) — m2_embed_verify 的 PyTorch DataLoader workers
- PID 41507, 41508 (ppid=39221) — plan_013 dataflow 的 PyTorch DataLoader workers

全部为主训练进程的正常子进程，无非预期进程。tmux session 仅 `m2_embed_verify`（预期）。

---
