# code beam mistral docred oneshot

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_beam_mistral_docred_oneshot_20260517T013529_result.json`
- **Structured JSON:** [`0c5e13827df760d1e9dd.json`](../../sessions/0c/0c5e13827df760d1e9dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已收集完毕。

```
Status: COMPLETE
Model: Mistral-7B-v0.3
Dataset: DocRED (50 docs)
Decoding: beam_size=4, full_s1

ET%: 0.0% (0/597 entities)
RV%: 0.0% (0/524 relations)
DR%: 21.4% (112/524 relations)
CF%: 1 violation
E_F1: 0.5178 (P=0.6520, R=0.4294)
R_F1: 0.0570 (P=0.0649, R=0.0508)
Parse failures: 1/50
```

关键观察：
- **Entity F1 合理** (0.52)，说明模型能识别实体
- **Relation F1 极低** (0.057)，几乎没有正确提取关系三元组
- **Entity type 和 relation vocab violation 为 0%**，说明 schema 约束在这两方面完全生效
- **Domain/range violation 仍有 21.4%**，beam search 未能完全消除 D/R 违规
- Relation recall 极低 (0.05) 表明模型输出的三元组与 gold 几乎不匹配，可能是 entity mention 对齐问题导致的 matching 失败

---
