# analysis cross scale llama3 base 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_scale_llama3_base_001_20260516T163607_result.json`
- **Structured JSON:** [`c77208b5a5046ab73473.json`](../../sessions/c7/c77208b5a5046ab73473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果总结

### 关键指标
| 指标 | BASE (本实验) | Instruct (对照) |
|------|--------------|----------------|
| 4-class acc | 0.599 | 0.702 |
| 6-class acc | 0.4953 | 0.554 |
| EDD | >5 | >5 |

### Consecutive Pairwise AUC
| Pair | BASE | Instruct |
|------|------|----------|
| d0v1 | 0.9175 | 0.9494 |
| d1v2 | 0.7936 | 0.8768 |
| d2v3 | 0.6815 | 0.7706 |
| d3v4 | **0.730** ↑ | 0.716 |
| d4v5 | 0.595 | 0.6183 |

### 假设验证：**NEGATIVE（不支持）**

原假设：BASE 模型 AUC 衰减应单调递减，以证明 instruction-tuning 导致 U 形。

实际结果恰恰相反：
- **Instruct** 是严格单调递减的（无 U 形）
- **BASE** 在 d3v4 出现非单调 bump（0.730 > d2v3 的 0.6815）

**结论**：Instruction-tuning 不是 U 形的原因；相反，IT **正则化**了 depth signal，使衰减更加单调。BASE 模型文本在递归深度增加时退化模式更不规则。

Registry 已更新为 DONE/negative，报告已注册。

---
