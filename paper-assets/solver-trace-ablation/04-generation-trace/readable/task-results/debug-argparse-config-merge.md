# debug argparse config merge

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_argparse-config-merge_20260516T033229_result.json`
- **Structured JSON:** [`bb85e0d548ad37487499.json`](../../sessions/bb/bb85e0d548ad37487499.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程持续增长（b005: 163→181→241, b01: 72→74→92），确认正常训练中。

---

## 诊断报告

### 1. Bug 诊断

**argparse defaults**: 所有参数 default=None（D097/D098 修复已在服务器上）。这部分没问题。

**真正的 bug 在 config merge 的 boolean 特殊处理**（line 393）：
```python
# 旧代码
if current is None or (isinstance(v, bool) and v and not current):
```
当 `--no_wandb` 的 argparse default 是 `False`（store_true），YAML 中 `no_wandb: true` 满足第二个条件 → 强制覆盖为 True → wandb 被禁用。即使 CLI 传了 `--wandb_project`，wandb 仍被关闭。

**因果链**：YAML `no_wandb: true` → wandb 禁用 → 监控 cron 检测不到 W&B 信号 → 5 次探测后判定进程死亡 → 杀 tmux session → Python 孤儿进程存活继续训练 → Registry 误标 killed。

### 2. 修复内容

- **`scripts/train_grpo.py` line 393**: 移除 boolean 特殊分支 → `if current is None:`
- **两个 YAML config**: 移除 `no_wandb: true` 行
- 本地 `artifacts/train_grpo.py` 同步修复

### 3. 当前运行状态

| 实验 | GPU | 当前 step | 目标 | 状态 |
|------|-----|-----------|------|------|
| sweep-isr-b005-s42 | cuda:1 (PID 604647) | ~241/500 | 500 | 正常训练中 |
| sweep-isr-b01-s45 | cuda:0 (PID 604569) | ~92/500 | 500 | 正常训练中 |

### 4. 实验提交状态

**无需重跑**。r3 的 Python 进程作为孤儿进程仍在正常训练，num_steps=500、K=4 参数均正确。预计：
- b005 (~2.5s/step): 还需 ~650s ≈ 11 分钟
- b01 (~10s/step): 还需 ~4080s ≈ 68 分钟

唯一缺失：这两个 run 没有 W&B 日志（因 no_wandb bug），但 `reward_log.jsonl` 完整可用。

---
