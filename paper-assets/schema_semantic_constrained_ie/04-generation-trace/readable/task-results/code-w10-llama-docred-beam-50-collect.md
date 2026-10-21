# code w10 llama docred beam 50 collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_llama_docred_beam_50_collect_20260517T073236_result.json`
- **Structured JSON:** [`16bdabfbe10273b8615b.json`](../../sessions/16/16bdabfbe10273b8615b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完成。汇总如下：

```
=== Llama DocRED Beam 50 Results ===
Lines: 50 / 50
Parse failures: 3 (6.0%)
ET%: 0.00, RV%: 0.00, DR%: 0.00, CF%: 0.94
E_F1: 55.62, R_F1: 9.47

Greedy baseline (from Llama DocRED full_s1 998 docs):
DR=2.55%, CF=12.02%, E_F1=55.01, R_F1=6.27
```

**关键发现**：Beam 50 相比 greedy baseline：
- **R_F1 提升**：6.27 → 9.47 (+3.20pp)
- **DR% 下降**：2.55% → 0.00% (完全消除 domain/range 违规)
- **CF% 下降**：12.02% → 0.94% (大幅降低 cross-field 不一致)
- **E_F1 基本持平**：55.01 → 55.62 (+0.61pp)
- **RV% 下降**：0.00% → 0.00% (均无 relation vocab 违规)

注意：beam_50 只跑了 50 个 sample（vs greedy 的 998），样本量差异较大，数字需谨慎对比。但 beam search 在约束遵守和关系 F1 上都有明显改善。

---
