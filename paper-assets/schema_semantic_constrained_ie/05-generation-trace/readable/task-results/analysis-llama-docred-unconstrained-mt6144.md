# analysis llama docred unconstrained mt6144

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_docred_unconstrained_mt6144_20260515T140054_result.json`
- **Structured JSON:** [`49c6ccebe46b6df9056a.json`](../../sessions/49/49c6ccebe46b6df9056a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## mt6144 vs mt4096 对比结果

| 指标 | mt4096 | mt6144 | Delta |
|------|--------|--------|-------|
| parse_failures | 68 | 67 | -1 |
| unique_entities | 11,525 | 11,534 | +9 |
| total_triples | 16,437 | 16,584 | +147 |
| RV (%) | 16.03 | 15.89 | -0.14pp |
| DR (%) | 26.07 | 26.18 | +0.11pp |
| E-F1 (%) | 55.65 | 55.67 | +0.02pp |
| R-F1 (%) | 5.98 | 5.95 | -0.03pp |
| Wall clock | ~5h 02m | ~5h 39m | +37min |

**Negative result.** max_new_tokens 4096→6144 对 unconstrained 生成无实质影响。parse failure 仅减少 1 例（68→67），所有 F1 和违规率差异 <0.15pp，属统计噪声。67 个 parse failure 主要是模型陷入退化循环（每个耗时 ~96s 达到 token cap），而非文档过长导致截断。代价是多 12% 推理时间。

Registry 已更新（conclusion=negative），分析报告已注册为 artifact。

---
