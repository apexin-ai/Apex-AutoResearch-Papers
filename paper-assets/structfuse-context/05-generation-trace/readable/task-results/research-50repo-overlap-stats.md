# research 50repo overlap stats

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_50repo_overlap_stats_20260512T195352_result.json`
- **Structured JSON:** [`af513e70dc3d4898b422.json`](../../sessions/af/af513e70dc3d4898b422.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 50-Repo Overlap 实验完成

**结论：原方法可行。**

```
总 instances: 240
有 connected-but-not-gold 的 instances: 98/240 (Z = 40.8%)
平均 |connected - gold| per instance: 6.0
CodeQL timeout/fail 率: 2/50 repos (4.0%)
```

**按 repo 大小分组：**
- 小 (<50 files): 38.6%, avg_extra=2.5
- 中 (50-200): 55.7%, avg_extra=11.8
- 大 (>200): 16.7%, avg_extra=8.8

**决策门判定：**
- Z = 40.8% ≥ 20% → **原方法可行** ✓
- Timeout 率 4.0% < 30% → **2-hop 无需降级** ✓

MVP 中观察到的 "connected ⊆ gold" 确实是 8 repo 小样本的规模伪迹。在 50 repo 尺度上，超过 40% 的 instance 存在 connected-but-not-gold 文件（即 call graph 能触及 gold 之外的文件），Phase 2b 的 positive/negative 分离训练有充足数据支撑。中型 repo（50-200 py files）效果最突出，平均每个 instance 有 11.8 个 extra connected files。

---
