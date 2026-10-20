# eval 70b lora scierc unconstrained violations

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_70b_lora_scierc_unconstrained_violations_20260522T052510_result.json`
- **Structured JSON:** [`e9dc1fd35e0a1b6c85c2.json`](../../sessions/e9/e9dc1fd35e0a1b6c85c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

violation_checker.py 内置了 F1 评估（用 gold_file 默认路径）。结果：

```
Samples: 551, JSON parse failures: 0 (0.0%)
Entities: 1806, Relations: 1133

E_P:    62.74
E_R:    67.12
E_F1:   64.86

R_P:    41.61
R_R:    48.36
R_F1:   44.73

ET_pct:  0.00%   (entity type violations)
RV_pct:  0.00%   (relation vocabulary violations)
DR_pct:  1.50%   (domain/range violations, 17/1133)
CF_pct:  0       (cross-field consistency violations)
Parse_fail: 0.00%
```

Unconstrained 70B LoRA 在 SciERC 上已经有很低的 violation rate（DR 仅 1.5%，ET 和 RV 均为 0），说明 70B 模型本身的 schema 遵循能力很强。R-F1 44.73 是 unconstrained baseline。

---
