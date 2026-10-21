# code caveat and h6 robustness

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_caveat_and_h6_robustness_20260519T065202_result.json`
- **Structured JSON:** [`f0ff1fec0bbd1e804a16.json`](../../sessions/f0/f0ff1fec0bbd1e804a16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项任务均完成。

## Part A: D004 caveat 已加入 `lambada_matched_comparison.py`
- 终端输出末尾打印 CAVEAT (D004) 说明
- 图表底部加了 italic 脚注

## Part B: h6-1 robustness check 结果

关键发现:

| | h3-1 (2 attn) | h6-1 (4 attn) |
|---|---|---|
| **GDN** | 462/615/**-153** | 426/598/**-172** |
| **HGRN2** | 548/395/**+153** | 524/397/**+127** |

**GDN h6-1 net effect = -172（比 h3-1 的 -153 更负）。** GDN 的负向 attention 效应在无 D004 confound（num_heads=32, GQA 4:1）的 h6-1 配置下不但没有消失，反而略微加剧。D004 confound 不是 GDN 负向效应的原因。

Jaccard overlap 在 h6-1 和 h3-1 之间高度一致（helped J~0.10, hurt J~0.085），说明这是 GDN 架构层面的系统性特征。

输出文件：
- `analysis/lambada_robustness_h6.png` / `.pdf`
- 终端打印完整的 helped/hurt/Jaccard/对比表

---
