# code unconstrained decoding prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unconstrained_decoding_prep_20260518T095530_result.json`
- **Structured JSON:** [`db0665b92a8698923b61.json`](../../sessions/db/db0665b92a8698923b61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 脚本路径
| 文件 | 路径 |
|------|------|
| 主脚本 | `/root/schema-dag-extraction/src/run_unconstrained_decoding_ablation.py` |
| Runner | `/root/schema-dag-extraction/scripts/run_unconstrained_ablation.sh` |
| 输出目录 | `/root/schema-dag-extraction/artifacts/unconstrained_decoding_ablation/` |

### 与 baseline (`run_fewrel_v2_bcs.py`) 的唯一区别
`build_json_schema_re` 中 `"relation"` 字段从 `{"type": "string", "enum": sorted(types) + ["none"]}` 改为 `{"type": "string"}`。Prompt 中仍然列出 candidate relations。

### Dry-run 结果 (1 batch, 10 samples, low_0, BCS=0.4715)
- Accuracy: 9/10 = **0.9000**
- OOV rate: 0/10 = **0.0000**
- 模型正确输出 JSON 格式，无 parse 错误
- 推理 5.5s / 10 samples

### 评估指标
- per-batch accuracy (exact match)
- OOV rate (prediction 不在 candidate list 中)
- BCS-accuracy Spearman ρ (跨全部 10 batches)
- Bootstrap 95% CI for Δ(low-high)
- Per-group OOV rate

### 运行命令
```bash
bash /root/schema-dag-extraction/scripts/run_unconstrained_ablation.sh
```

### 预估时间
- 模型加载: ~40s
- 推理: 960 samples @ ~0.5s/sample (batched) ≈ 2-3 min
- **总计: ~4-5 min**

---
