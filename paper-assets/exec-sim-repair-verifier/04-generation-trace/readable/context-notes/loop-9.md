# director / loop_9.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`7e1155db1604a335822f.json`](../../sessions/7e/7e1155db1604a335822f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-14T14:54:54+00:00'
---

## 刚完成的事

收到 Agent 关于 D063 Val Set Checkpoint Sweep（4B 模型）的结果汇报：
- CLS v5 seed42：val-test 一致，best = ckpt-4600（test acc 82.35, f1m 74.74）
- CLS seed123：val-test 不一致（val best = ckpt-800, test best = ckpt-600）
- test@4096 对 seed123 ckpt-600 仅 +0.54pp，2048 基本够用
- **关键发现**：val 有 1883 条 unparseable（20.2%）vs test 132 条（1.35%），差距巨大

## 已派出的任务

已向 Agent 发送指令（Agent 当时空闲，queue depth=0）：

**任务 1（cuda:0）**：诊断 val unparseable 原因——是 max_length 截断导致格式不完整，还是模型输出本身 parse 不了？要求对比 val/test token 长度分布，如果是截断则用 max_length=4096 重跑 val eval（seed123 ckpt-600 和 ckpt-800），看 unparseable 率和 ranking 是否变化。

**任务 2（信息收集）**：查 westd CWM eval 状态和预计完成时间；确认 8B s42 checkpoints 路径，评估是否可 scp 到 home 跑 val sweep。

## 已记录的决策

D076：优先诊断 val unparseable 问题（20.2% vs test 1.35%），暂缓 8B val sweep。理由是 val-based checkpoint selection 可能系统性不可信。

## 当前资源状态

- home cuda:0：已分配，空闲→刚派了 val 诊断任务
- westd 4x5090：被 CWM eval 占用（状态待 Agent 确认）
- 项目总计 61 个实验完成（36 success / 15 failed / 7 killed / 3 negative）

## 下一步等什么

1. 等 Agent 回报 val unparseable 诊断结果——如果是截断问题，需要决定是否全面重跑 val eval with higher max_length
2. 等 westd CWM eval 完成释放 GPU，然后跑 8B s42 val sweep
3. D070 的条件判断依赖 8B s42 val 结果，暂时 blocked

## 注意事项

- Val 数据质量问题可能影响之前所有基于 val 做的 checkpoint selection 决策，如果确认是系统性问题，需要回溯评估影响面
- 不要在 val 诊断完成前基于 val metrics 做任何新的 checkpoint 选择决策


---
