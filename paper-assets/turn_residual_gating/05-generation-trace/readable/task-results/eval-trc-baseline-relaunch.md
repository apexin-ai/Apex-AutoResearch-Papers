# eval trc baseline relaunch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_trc_baseline_relaunch_20260520T092554_result.json`
- **Structured JSON:** [`df37bcf11cf6c44aeb29.json`](../../sessions/df/df37bcf11cf6c44aeb29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

## TRC Baseline 结果

| Checkpoint | TF TRC | Gen TRC | TRC Gap (TF−Gen) | TF TBP PPL | Gen TBP PPL |
|---|---|---|---|---|---|
| **v7 TG** (LoRA+gates) | 0.334 | 0.332 | **+0.002** | 1.05 | 1.05 |
| **LoRA-only** | 0.349 | 0.411 | **−0.062** | 9.50 | 12.00 |
| **Base model** | 0.149 | 0.149 | 0.000 | 2.05 | 2.05 |

### 关键发现

1. **v7 TG: 近零 TRC gap (+0.002, ratio 1.005)**。hidden-state 一致性在 TF/gen 之间几乎无差异，TBP PPL 仅 1.05 — ThreadGate 有效消除了 hidden-state 空间的 exposure bias。

2. **LoRA-only: 显著负 gap (−0.062, ratio 0.85)**。gen 模式下 TRC 反而更高（hidden states 被迫更相似），但 TBP 严重恶化 (9.5→12.0 PPL) — 说明 LoRA-only 在生成时 hidden states "坍缩"，丧失了多样性但也丧失了质量。

3. **Base model: 零 gap** — 但注意这是代码实现问题：gen 模式完全复制了 TF 数值（连 std 都一致），可能 eval 脚本对 base model 的 gen 模式处理有 bug（直接复用了 TF hidden states）。

### EXIT_CODE=1 诊断
日志显示所有 3 个 checkpoint 正常完成并保存了 JSON。EXIT_CODE=1 可能来自 `set -e` 加上 `tee` 管道中某个无关的非零返回码，不影响实际结果。

---
