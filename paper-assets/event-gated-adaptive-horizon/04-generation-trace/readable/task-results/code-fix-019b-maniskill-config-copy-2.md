# code fix 019b maniskill config

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-019b-maniskill-config_20260517T035609_result.json`
- **Structured JSON:** [`da92497caae13ffff2b4.json`](../../sessions/da/da92497caae13ffff2b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论如下：

## 诊断结果

**问题已自行解决 — 019b 当前正在正常运行。**

### 时间线重建
1. 第一次提交 019b 在 `2026-05-17T03:38:33Z` 失败（exit code 143 = SIGTERM，被 kill 了，不是 KeyError）
2. 当前第二次提交（PID 646809，启动于 11:39）使用 `--configs defaults maniskill` 正在正常训练，已到 step 8400+

### 关于 KeyError 的原因
`configs.yaml` 中 `maniskill` key 一直存在（第207行），当前代码解析完全正常。最可能的解释是：
- 第一次失败时工作目录状态有问题（也许代码还未 pull 到 commit 3328f53），或者
- 第一次失败实际上不是 KeyError 而是被 SIGTERM (143) 杀掉了——错误信息可能来自一个更早的测试性手动运行

### 当前状态
- **019b** (PID 646809): `--configs defaults maniskill`, cuda:0, 正常训练中 (step 8400+)
- **019a_v2** (PID 629444): `--configs defaults maniskill_state`, cuda:1, 正常训练中

**无需修复，两个实验都在正常运行。**

---
