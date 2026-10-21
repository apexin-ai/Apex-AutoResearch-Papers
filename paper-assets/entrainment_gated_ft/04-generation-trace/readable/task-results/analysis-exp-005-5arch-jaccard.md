# analysis exp 005 5arch jaccard

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-005-5arch-jaccard_20260522T171842_result.json`
- **Structured JSON:** [`84d5ebf0d7fc4a05cac5.json`](../../sessions/84/84d5ebf0d7fc4a05cac5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 架构 Jaccard 分析完成。结果：

### ARC-Easy (n=2376)
| 指标 | 值 |
|------|-----|
| Mean J_helped | **0.1081** |
| Mean J_hurt | **0.1047** |
| 10/10 对显著 | z = 3.49–9.19 (helped), 3.72–7.48 (hurt) |

### LAMBADA (n=5153)
| 指标 | 值 |
|------|-----|
| Mean J_helped | **0.1221** |
| Mean J_hurt | **0.0946** |
| 10/10 对显著 | z = 9.03–12.21 (helped), 6.33–10.89 (hurt) |

### 子组对比 (LAMBADA J_helped)
- 3-arch (GDN/RetNet/HGRN2): 0.1194
- 4-arch (+GLA): 0.1219
- **5-arch (+DeltaNet): 0.1221**
- DeltaNet vs others: 0.1224

DeltaNet 融入得很好——它与其他架构的 Jaccard 值与已有架构间的互相重叠水平一致。加入第 5 个架构后 Jaccard 均值几乎不变，进一步支持 "helped/hurt overlap 是 architecture-independent" 的假设。

### HGRN 模型状态
- HGRN h3-1: ✅ 已下载 (1.33GB)
- HGRN2 pure: ✅ 已下载

Artifact 和 registry 已更新。服务器完整 JSON: `results/exp005_zoo_expansion/jaccard_5arch.json`

---
