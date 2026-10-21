# diag preparing experiments status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_preparing-experiments-status_20260513T223748_result.json`
- **Structured JSON:** [`ce7e1bdb076f87cc8db6.json`](../../sessions/ce/ce7e1bdb076f87cc8db6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 实验 | 状态 | 原因 |
|------|------|------|
| **plan001-exec-only-s42** | **crashed** | 参数错误，启动即退出 |
| **plan005-sta-low-s42** | **crashed** | 同上，参数错误 |
| **plan003-eval-exec-only-r5** | **finished** | 正常完成，EXIT_CODE=0 |

### 详情

**plan001 & plan005** — 两个训练实验都因同一错误立即退出：
```
train_grpo.py: error: unrecognized arguments: --max_steps 500
```
脚本的参数名是 `--num_steps`，不是 `--max_steps`。无输出目录产生。

**plan003** — eval 已完成，结果：
- 输出文件：`/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json`（177KB）
- Proved: 32/100 (32.0%)
- Mean ISR: 0.2055 ± 0.3194
- Proved-only ISR: 0.6423
- 按 answer type：true=35.98% ISR, false=17.23%, unknown=9.79%
- 耗时 251.7s

### GPU 状态
两块 RTX PRO 6000 (98GB) 均空闲，显存 0 MiB，利用率 0%。

### 数据文件
`train_500_seed42.jsonl` 存在，500 行。

### 需要的操作
- plan001 和 plan005 的 registry 状态应更新为 **FAILED**
- 重新提交时将 `--max_steps` 改为 `--num_steps`
- plan003 的 registry 状态应更新为 **DONE**

---
