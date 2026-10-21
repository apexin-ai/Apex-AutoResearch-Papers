# ssh westd fix cron and check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-fix-cron-and-check_20260519T020233_result.json`
- **Structured JSON:** [`8bc4eeebe59b1ebcd002.json`](../../sessions/8b/8bc4eeebe59b1ebcd002.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

---

**Step 1: 服务器验证** — 确认是 westd。4x NVIDIA RTX PRO 6000 Blackwell，每张 97887 MiB。

**Step 2: 14B eval 状态**

| 项目 | 值 |
|---|---|
| Bash 脚本 PID | **93847**（wrapper 93845） |
| 当前 python eval PID | 95424（GPU 0, 32726 MiB） |
| 当前评估中 | `Qwen2.5-14B_d005_s42`（MMLU + ARC） |

已完成 1 个 adapter：

| Adapter | MMLU | ARC |
|---|---|---|
| `Qwen2.5-14B_d000_s42` | **0.7459** (10474/14042) | **0.9352** (1096/1172) |

**Step 3: Gemma d025 状态** — **仍在运行**

- `.done` 标记不存在
- GPU 1 占用 54391 MiB，80% util，PID 86378
- 训练进度：**3257/3384 steps (96.2%)**，epoch 0.9606
- 最新 loss=1.134，token_accuracy=0.7329
- 预估剩余：~127 steps × ~2.7s/step ≈ **5-6 分钟**完成

---
