# check westd21461 status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd21461-status_20260522T164425_result.json`
- **Structured JSON:** [`c191ff4b4b1a234a060c.json`](../../sessions/c1/c191ff4b4b1a234a060c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。总结：

## 实验结果

| | Unconstrained | Grammar-only | Semantic-only | Full (grammar+semantic) |
|---|---|---|---|---|
| **DR%** | 6.41% | 6.33% (≈0%) | **1.01%** (-84%) | 0% |
| **R-F1** | 11.24 | 11.23 | **11.37** (+0.13) | ~11.24 |
| **RV%** | - | 0% | 0.6% | 0% |
| **CF** | - | 0 | 76 | 0 |

### Hypothesis 判断

- **Grammar-only → negative**: DR 6.33% vs 6.41%，降幅仅 0.08pp（噪声级别），grammar layer 对 70B 的 DR 几乎没有独立贡献。原因：70B 本身已能正确生成 entity type/relation name 词汇（RV=0%, ET=0%），grammar 只约束词汇不约束 domain/range 组合。
- **Semantic-only → success**: DR 从 6.41% 降至 1.01%（84% 相对降幅），semantic layer 是 DR 减少的主要驱动力。但没有 grammar 兜底时，会漏出 0.6% RV violations 和 76 个 CF inconsistencies。

### 关键 insight
在 70B 上，**semantic layer 承担了几乎全部的 constraint enforcement 工作**，grammar layer 的贡献接近于零（因为大模型本身已具备正确的词汇生成能力）。两层联合时 grammar 的价值在于「查漏补缺」——消除 semantic-only 残留的 RV 和 CF violations。

### GPU 状态
westd-21461 两张 RTX PRO 6000 (96GB) 均空闲，0% utilization，0MiB memory。可用于下一批实验。

---
