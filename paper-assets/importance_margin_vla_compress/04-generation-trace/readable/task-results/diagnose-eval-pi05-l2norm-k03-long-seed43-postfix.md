# diagnose eval pi05 l2norm k03 long seed43 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k03_long_seed43_postfix_20260524T170706_result.json`
- **Structured JSON:** [`7fbe9df3255c18e3cc0a.json`](../../sessions/7f/7fbe9df3255c18e3cc0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 诊断结果

| 实验 | 根因 | 状态 |
|------|------|------|
| `eval_pi05_l2norm_k03_long_seed43_postfix` | 原命令未激活 conda 环境，裸调 `python` → `command not found` (EXIT_CODE=127) | **DONE/failed** |

### 重新提交

| 实验 | 服务器 | GPU | 状态 |
|------|--------|-----|------|
| `eval_pi05_l2norm_k03_long_seed43_postfix_v2` | cqa1-33015 | cuda:0 (PID 566658) | **RUNNING** — 已在 torch compile 阶段 |

### westd-38929 实验状态

| 实验 | GPU | 状态 |
|------|-----|------|
| `eval_pi05_l2norm_k095_long_seed43_postfix` | cuda:2 (PID 612452) | **RUNNING** — 正常运行 |
| `eval_pi05_l2norm_k05_long_seed43_postfix` | cuda:3 (PID 612595) | **RUNNING** — 正常运行 |

v2 实验已经由之前的 on_failed hook 自动重新提交，命令中包含了正确的 `conda activate`，当前正在正常运行。westd-38929 的两个实验无此问题，原始提交就包含了 conda 激活，运行正常。

---
