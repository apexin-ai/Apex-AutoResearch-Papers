# ssh d034 diversity verification

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d034-diversity-verification_20260515T012011_result.json`
- **Structured JSON:** [`e12843014c5ba232fa04.json`](../../sessions/e1/e12843014c5ba232fa04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D034 Step 2 结果

**Diversity 合格，之前 monitor 报告的 mean=0.9/8 是误报。**

| 指标 | 值 |
|------|-----|
| 文档数 | 264（已完成），262 有有效解析 |
| 每文档候选数 | 8 |
| **Triple-set diversity（不含 evidence）** | **mean=6.77/8, median=7.0** |
| **Full diversity（含 evidence）** | **mean=6.97/8, median=8.0** |
| Format OK rate | 89.1% |

### 分布

- **48.5%** 的文档 8 个候选全部不同（8 unique）
- **70.6%** 的文档 ≥7 unique
- 仅 5 个文档（1.9%）所有候选完全相同（1 unique）

### 结论

Diversity 远超阈值（6.77 >> 3.0），当前生成配置没有问题。之前 RSFT monitor 报 mean=0.9/8 大概率是 monitor 的 diversity 计算逻辑有 bug（可能是 triple 规范化方式不同，或者 monitor 只看了 raw_text 未正确解析）。

**建议**：继续当前生成，不需要调温度或重跑。

---
