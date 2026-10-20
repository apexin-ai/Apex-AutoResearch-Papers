# code prep proofwriter

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-proofwriter_20260515T130529_result.json`
- **Structured JSON:** [`fc2a86b6a640af4e56a2.json`](../../sessions/fc/fc2a86b6a640af4e56a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**数据验证** — `proofwriter_subset.json` 10 题，answer 字段为 True/False/Unknown，格式正确。

**Domain 检测** — `pipeline.py:59` 通过 `problem.get("dataset") == "proofwriter"` 自动识别为 `domain="logic"`。ProofWriter 数据自带 `"dataset": "proofwriter"`，`setdefault("dataset", "math")` 不会覆盖。

**response_format** — `VLLMBackend.call`（constraint_extractor.py:136）已有 `response_format={"type": "json_object"}`，logic/math 共用同一 backend，**无需修复**。（`APIBasedLLM` 缺此参数，但 ProofWriter 跑 vllm 模式不受影响。）

**脚本** — `/root/symb_invariant_consensus/run_proofwriter.sh` 已创建（755），AIME 完成后执行即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "type": "json_object"
  }
}
```

</details>

---
