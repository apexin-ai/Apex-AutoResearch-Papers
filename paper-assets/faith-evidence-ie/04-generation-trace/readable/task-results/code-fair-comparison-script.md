# code fair comparison script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fair-comparison-script_20260520T160300_result.json`
- **Structured JSON:** [`21e6e18ad9370eb52a4e.json`](../../sessions/21/21e6e18ad9370eb52a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过：

| 指标 | 预期 | 实际 |
|------|------|------|
| Full set | 985 docs | 985 docs |
| No-evi ign_f1 | 0.5219 | 0.5219 |
| With-evi ign_f1 | 0.5384 | 0.5384 |
| Raw tax | -1.65pp | -1.65pp |
| No-evi format_ok | 874 | 874 |
| Format failures | 46 trunc + 65 malformed | 46 + 65 |
| Fair subset | ~874 docs | 873 docs (因 with-evi 也有5个failure，交集少1) |
| Fair tax | ~+1.35pp | +1.34pp |

Fair subset 是 873 而非 874，因为有 1 个 doc 在 with-evidence 侧也 format failure 了，从交集中排除。fair tax +1.34pp 与预期 +1.35pp 几乎一致（四舍五入差异）。

脚本位置：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`

用法：
```bash
python fair_evidence_tax.py \
  --with-evi &lt;with-evidence predictions.json> \
  --no-evi &lt;no-evidence predictions.json> \
  [--train &lt;train_annotated.json>] \
  [--json-out &lt;output.json>]
```

---
