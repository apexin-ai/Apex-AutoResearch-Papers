# analysis restore metrics and c4 discrepancy

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_restore_metrics_and_c4_discrepancy_20260514T181207_result.json`
- **Structured JSON:** [`420396a55e43e5b07d34.json`](../../sessions/42/420396a55e43e5b07d34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已恢复。三项产出：

### 1. evaluate_mvp.py 完整输出

```
Total samples: 126 | Valid: 126 | Effective: 118 | GT!=Unknown: 82

All samples:
  C1 36.4% (43/118) PASS | C2 88.4% (38/43) PASS | C3 3 types PASS
  C4 +7.3pp (T:36/55 B:32/55) PASS | C5 80.0% (20/25) PASS
  MVP: 5/5 PASS → PROCEED

Excluding GT=Unknown:
  C1 34.7% (26/75) PASS | C2 88.5% (23/26) PASS | C3 2 types PASS
  C4 +0.0pp (T:22/35 B:22/35) FAIL | C5 87.5% (14/16) PASS
  MVP: 4/5
```

### 2. C4 差异根因

| | evaluate_mvp.py | c4_analysis_v2.py |
|---|---|---|
| 样本范围 | 所有 valid（含 AGREE） | 仅 DISAGREE |
| 数据 | T:36/55, B:32/55 | T:31/48, B:25/48 |
| Delta | **+7.3pp** | **+12.5pp** |

7 个 `single_error` 类型样本有 repair 数据但不是 `disagree`。evaluate_mvp.py 把它们计入分母，拉低了 targeted 优势（这些样本 blind 成功率高于 targeted）。

### 3. Registry 已恢复

完整 C1-C5 metrics + `c4_analysis` 子字段（含差异解释和原 decline 分析），已合并写入 `mvp_pipeline_004.metrics`。

---
