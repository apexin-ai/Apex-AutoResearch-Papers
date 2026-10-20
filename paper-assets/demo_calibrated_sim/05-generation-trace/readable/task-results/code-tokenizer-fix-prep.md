# code tokenizer fix prep

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tokenizer-fix-prep_20260512T154936_result.json`
- **Structured JSON:** [`0512c7cf7b6d6f5ea39c.json`](../../sessions/05/0512c7cf7b6d6f5ea39c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两种模式都验证通过。

**结果**：

`/root/democalib/build_dpo_pairs_v2.py` 已就绪。与 v1 的区别：

| | v1 | v2 |
|---|---|---|
| prompt 格式 | `"Customer: ...\nAgent: ..."` 手工拼接 | message lists `[{"role":"user","content":"..."},...]` |
| tokenizer 对齐 | 不匹配 ChatML（48% mismatch） | DPOTrainer 自动调 `apply_chat_template()` |
| 输出模式 | 纯文本 | `--format messages`（默认）或 `--format text`（预格式化） |
| 配对逻辑 | 相同 | 相同 |
| 额外过滤 | 保留空 content messages | 过滤掉空 content |

使用时（当需要重建数据时）：
```bash
python3 build_dpo_pairs_v2.py \
  --calibrated-traces &lt;calibrated.json> \
  --uncalibrated-traces results/baseline_merged.json \
  --output data/dpo_pairs_v2.jsonl
```

现有 `train_dpo.py` 不需要改动——TRL 1.4.0 的 DPOTrainer 原生支持 conversational format。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "role": "user",
    "content": "..."
  }
}
```

</details>

---
