# fix retnet pure 1 3b rerun

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_retnet-pure-1_3b-rerun_20260519T191634_result.json`
- **Structured JSON:** [`4662ef457eff1c2282cc.json`](../../sessions/46/4662ef457eff1c2282cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **补跑结果**：RetNet-pure 1.3B LAMBADA logsamples 已生成，5153 行，acc = 51.7%（正常）
- **Cross-scale Jaccard**：
  - RetNet helped_jaccard = **0.0587**（对比 GDN 0.0474, HGRN2 0.0892）
  - RetNet hurt_jaccard = **0.0725**（对比 GDN 0.0874, HGRN2 0.0550）
- **JSON 已更新**：`exp007_340m_analysis.json` 中 `RetNet_h3_1` 从 null 更新为实际值

三个架构的 cross-scale Jaccard 都很低（<0.09），说明 340M 和 1.3B 尺度上被 hybrid 帮助/伤害的样本集合高度不重叠。

---
