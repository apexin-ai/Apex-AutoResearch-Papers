# audit fix missing 3sigma

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_fix_missing_3sigma_20260520T015106_result.json`
- **Structured JSON:** [`b9639044abc77ee6294d.json`](../../sessions/b9/b9639044abc77ee6294d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。

关键结果：
- **4 个实验 threshold_3σ 全部远低于 2σ fallback**：scale_69b 2/8，其余 3 个均 0/8
- **K≥3 大幅下降**：Qwen 8/8→3/8，Padding 和 410M-s43 均 6/8→0/8，6.9B 5/8→3/8
- **K≥4 全部归零**
- **任务中 Pythia-410M s43 标注的 "D105: 2/8" 实际是 s42 的值**，s43 不在 recompute JSON 中，手动重算确认为 0/8（已用 scale_69b 交叉验证算法正确性）

---
