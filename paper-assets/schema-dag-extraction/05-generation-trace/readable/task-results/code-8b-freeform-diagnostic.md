# code 8b freeform diagnostic

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b-freeform-diagnostic_20260515T164805_result.json`
- **Structured JSON:** [`cdb7cac23d4db33ff8ca.json`](../../sessions/cd/cdb7cac23d4db33ff8ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 现有 exp012 脚本分析
- 脚本路径: `/root/schema-dag-extraction/scripts/run_exp012_llama_8b.sh` → 调用 `src/run_experiment.py` → `src/run_extraction.py`
- prompt 格式: v2（text+type only，无 start/end offset）— 列出类型定义，给 input text，要求输出 `[{"text": "...", "type": "..."}]`
- structured output 方式: `vllm.sampling_params.StructuredOutputsParams(json=batch_schema)`，schema 用 enum 约束 type 字段

## 新诊断脚本
- 路径: `/root/schema-dag-extraction/scripts/diagnose_llama8b_freeform.py`
- 模型路径: `/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- 数据路径: `/root/schema-dag-extraction/data/parquet/test.parquet`
- 运行命令:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && python scripts/diagnose_llama8b_freeform.py
```
- syntax check: **PASS**
- `--help`: **PASS**
- 预计运行时间: ~2 min（5 samples + model load）

### 脚本要点
- 复用 exp012 完全相同的 `build_prompt_v2`
- **去掉** `StructuredOutputsParams`，只用 `SamplingParams(temperature=0, max_tokens=2048)`
- 固定 6 个诊断类型（person-athlete, organization-company, location-GPE, event-sportsevent, product-car, other-award）
- 打印每个样本的 raw output，不做 JSON 解析
- 结果保存到 `artifacts/llama8b_freeform_diagnostic.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "text": "...",
    "type": "..."
  }
}
```

</details>

---
