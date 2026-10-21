# code binoculars 14b temp09

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_binoculars_14b_temp09_20260520T042205_result.json`
- **Structured JSON:** [`7357762ee88e82e241be.json`](../../sessions/73/7357762ee88e82e241be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**Binoculars baseline (14B temp09)**：RF_multi (11 features) 是最佳校准方法，4-class acc = **0.4252**。单 bino_score 仅 0.2917（≈随机）。

**Merged ablation (30 features)**：

| 特征集 | #feat | 4-class Acc | d1–d3 Bal Acc |
|--------|-------|-------------|---------------|
| bino_single | 1 | 0.2917 | 0.2779 |
| bino_only | 11 | 0.4258 | 0.3724 |
| stat_only | 19 | 0.5183 | 0.4559 |
| **merged** | **30** | **0.5419** | **0.4770** |

Stat features（19 维）远强于 Binoculars（11 维），合并后 30 维 RF 再涨 +2.4pp 到 0.5419。Artifact 已注册：`art_20260520_d47efe`。

---
