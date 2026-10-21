# ssh prompt v2 prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prompt-v2-prep_20260514T231959_result.json`
- **Structured JSON:** [`a64ba65fd2e70a81c59a.json`](../../sessions/a6/a64ba65fd2e70a81c59a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

### 修改的文件

**`src/run_extraction.py`**
- `build_json_schema` → 重命名为 `build_json_schema_v1`（保留别名兼容）
- `build_prompt` → 重命名为 `build_prompt_v1`（保留别名兼容）
- 新增 `build_json_schema_v2`：只有 `text` + `type`，无 `start`/`end`
- 新增 `build_prompt_v2`：不要求 offset，增加空列表指令
- `run_extraction()` 新增 `prompt_version` 参数（默认 `"v1"`）
- CLI 新增 `--prompt_version` 选项

**`src/evaluate.py`**
- `_exact_match`/`_relaxed_match` 签名增加 `source_text=None`（向后兼容）
- 新增 `_text_match`：type 匹配 + substring 文本匹配 + 源文本验证（防幻觉）
- `compute_metrics` 传递 `source_text` 给 match 函数
- `evaluate_all()` 新增 `eval_mode` 参数：`"exact"` / `"relaxed"` / `"text_match"` / `"all"`
- CLI 新增 `--eval_mode` 选项

**`src/run_experiment.py`**
- CLI 新增 `--prompt_version` 和 `--eval_mode`，传递给下游函数
- 日志输出适配三种指标

### Dry-run 结果

在 exp1 predictions（500 samples）上验证：
- exact F1 ≈ 0.01（offset 噪声导致极低）
- relaxed F1 ≈ 0.10-0.27
- **text_match F1 ≈ 0.10-0.57**（显著高于 exact，证明模型确实能提取正确实体，只是 offset 是噪声）

text_match 模式下 count_44 的 recall 显著提升到 ~0.5+，符合预期。

---
