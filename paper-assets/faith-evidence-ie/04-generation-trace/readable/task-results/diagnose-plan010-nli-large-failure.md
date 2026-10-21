# diagnose plan010 nli large failure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan010-nli-large-failure_20260522T154939_result.json`
- **Structured JSON:** [`464974e9d70bd61a8526.json`](../../sessions/46/464974e9d70bd61a8526.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌清楚了。

## 诊断结果

**`plan010_nli_large_eval`（failed）**：Registry 中只有一个空 spec `{"pid": "733763"}`，没有 error_msg。从 `plan010_nli_large_ablation` 的 note 字段可以看到根因：

> "Step 3 eval failed due to **inode bug** (`--data_dir` not replaced). Eval resubmitted as `plan010_nli_large_eval`."

**`plan010_nli_large_eval_r2`（success）**：已经用正确的命令重跑并成功完成。结果：

| 指标 | 值 |
|------|-----|
| F1 | 0.4636 |
| ign_F1 | 0.4533 |
| evi_f1_joint | 0.3606 |
| evi_f1_tp | 0.8194 |
| EDCR | 0.653 |
| format_compliance | 1.0 |
| n_truncated | 180 |
| inference_time | ~2.8h |

**结论**：`plan010_nli_large_eval` 的失败原因是命令中 `--data_dir` 参数没有被正确替换（inode bug）。这个问题已在 r2 中修复并成功完成，**无需再重跑**。DeBERTa-v3-large NLI CED scoring + RSFT 的完整 pipeline 结果已可用，存储在 `/root/autodl-tmp/eval_results/plan010_nli_large_ablation`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "pid": "733763"
  }
}
```

</details>

---
