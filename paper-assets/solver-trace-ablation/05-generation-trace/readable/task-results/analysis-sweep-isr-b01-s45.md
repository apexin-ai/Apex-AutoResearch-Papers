# analysis sweep isr b01 s45

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sweep-isr-b01-s45_20260516T025851_result.json`
- **Structured JSON:** [`0fb5079764a4b957e3dd.json`](../../sessions/0f/0fb5079764a4b957e3dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**sweep-isr-b01-s45: FAILED** — 训练只跑了 100 步而非 500 步。

### 根因
`train_grpo.py` 第 395-401 行的 config merge 逻辑有 bug：只在 CLI 参数值为 `None` 时才用 config 文件的值覆盖。`--num_steps` 的 argparse default 是 `100`（不是 None），所以 config 中的 `num_steps: 500` 被静默忽略。

### 影响范围
- **sweep-isr-b01-s45**: 100 步，无法与 500 步实验对比
- **sweep-isr-b005-s42**: 同样只有 100 步（已确认 reward_log 100 行），同一 bug

### 修复方案
1. **重训时 workaround**: 命令行显式加 `--num_steps 500`
2. **根本修复**: 改 argparse default 为 `None`（所有可被 config 覆盖的参数），或者改 merge 逻辑追踪哪些 CLI 参数是用户显式传的

### 注册状态
- Registry: `status=DONE`, `conclusion=failed`
- Analysis report: `artifacts/sweep-isr-b01-s45/`

---
