# analysis mt6144 unconstrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mt6144_unconstrained_20260515T140655_result.json`
- **Structured JSON:** [`3f2701f2cc4c3976b39d.json`](../../sessions/3f/3f2701f2cc4c3976b39d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（metrics 已写入，conclusion/notes/checkpoint_path 此前已设置）。

## 结果汇总

### Violation Report (mt6144)

| 指标 | 值 |
|------|-----|
| Parse failures | 67/998 |
| Unique entities | 11,534 |
| Total triples | 16,584 |
| ET | 0.13% (15/11534) |
| RV | 15.89% (2635/16584) |
| DR | 26.18% (4341/16584) |
| CF | 0.17% (20/11534) |
| E-F1 | 55.67% |
| R-F1 | 5.95% |

### mt6144 vs mt4096 对比

| 指标 | mt4096 | mt6144 | Delta |
|------|--------|--------|-------|
| Parse failures | 68 | 67 | -1 |
| ET | 0.13% | 0.13% | 0 |
| RV | 16.03% | 15.89% | -0.14pp |
| DR | 26.07% | 26.18% | +0.11pp |
| CF | 0.17% | 0.17% | 0 |
| E-F1 | 55.65% | 55.67% | +0.02pp |
| R-F1 | 5.98% | 5.95% | -0.03pp |

**结论**: max_new_tokens 从 4096 提升到 6144 对 unconstrained 生成几乎无影响。Parse failures 仅减少 1 个，F1 和 violation 率变化在噪声范围内。67 个失败样本的 inference time ~96s，表明它们是模型陷入重复循环撞到 token 上限，而非文档过长导致截断。增加 max_new_tokens 无法修复此类失败。

---
