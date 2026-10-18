# analyze cqa1 3 analyzing exps

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cqa1_3_analyzing_exps_20260523T203521_result.json`
- **Structured JSON:** [`3f29915d83452efa18a8.json`](../../sessions/3f/3f29915d83452efa18a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部成功完成，memory.md 已更新。

核心结论：
- **k=0.85 post-fix = pre-fix = 52.4%**：CPU RNG 修复对 k=0.85 零影响，确认 disruption dip 谷底
- **k=0.5 post-fix 73.6% vs pre-fix 74.4%**：delta 仅 -0.8pp，几乎无影响
- **k=0.3 seed43 = 53.6%**：与 seed42 (50.6%) 平均后 multi-seed avg = 52.1%
- Goal suite disruption dip 完整：k=0.85(52.4%) 为谷底，k=0.7(78.2%) 回升 +25.8pp

---
