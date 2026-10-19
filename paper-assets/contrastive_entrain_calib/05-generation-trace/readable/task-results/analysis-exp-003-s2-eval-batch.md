# analysis exp 003 s2 eval batch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-s2-eval-batch_20260520T182425_result.json`
- **Structured JSON:** [`573b8f005cd9feefe2fc.json`](../../sessions/57/573b8f005cd9feefe2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003-s2 Seed 2 Early Trajectory Results

| checkpoint | ToF | NoF | SYCONScore | vs vanilla (0.134) | vs seed1 |
|-----------|------|--------|------------|---------------------|----------|
| ckpt-500  | 0.0442 | 0.9503 | 0.0845 | -37.0% (negative) | s1-ckpt1000: 0.074 → +14.1% |
| ckpt-1000 | 0.0442 | 0.9448 | 0.0844 | -37.0% (negative) | s1-ckpt1000: 0.074 → +14.1% |
| ckpt-1500 | 0.0552 | 0.9503 | 0.1044 | -22.1% (negative) | s1-ckpt2000: 0.085 → +22.8% |

**Seed 2 vs Seed 1 可复现性：方向一致**

- 两个 seed 的 SYCONScore 均远低于 vanilla baseline (0.134)，均随训练步数增加而上升
- Seed 2 绝对值略高于 seed 1 对应阶段，但在同一数量级
- 三个 checkpoint 结论均为 **negative**——R3-only contrastive training 跨 seed 可复现地未能超过 vanilla baseline，说明方法本身有效性存疑

Registry 已全部更新为 DONE + negative，产出摘要已注册。

---
