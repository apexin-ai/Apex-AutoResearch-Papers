# ops post reboot check

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_reboot_check_20260513T030831_result.json`
- **Structured JSON:** [`edbf854147a32954b9ed.json`](../../sessions/ed/edbf854147a32954b9ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载，启动正常。

---

### 汇报

**1. sft_eval_v5** — 已完成 ✓（registry 已更新为 DONE）

| 指标 | 值 |
|---|---|
| RE F1 | 0.4337 |
| Evidence F1 | 0.3652 |
| Attribution Precision | 0.9529 |
| Samples | 985 |
| GPU Hours | 2.77h |

对比 sft_eval_v4（RE-F1=0.2726），修复 chat_template 后 RE-F1 提升 59%（0.2726→0.4337）。

**2. posthoc_nli_v3** — 仍在运行中

- 进度：batch 79/124（~632/985 samples），约 64% 完成
- 占用 cuda:1（59.6GB VRAM，100% GPU利用率，2个 python 进程）

**3. grpo_v1b_eval** — 已启动 ✓

- PID: 79684，cuda:0
- 模型加载中（4/4 shards 已完成）
- 日志：`~/runs/prov_grounded_uie/grpo_v1b_eval.log`

**4. GPU 状态**

| GPU | 状态 | 占用 |
|---|---|---|
| cuda:0 | grpo_v1b_eval（刚启动） | 模型加载中 |
| cuda:1 | posthoc_nli_v3（运行中） | 59.6GB / 97.9GB, 100% |

---
