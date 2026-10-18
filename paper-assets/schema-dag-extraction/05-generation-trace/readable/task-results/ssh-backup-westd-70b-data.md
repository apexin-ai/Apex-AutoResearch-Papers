# ssh backup westd 70b data

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_backup_westd_70b_data_20260517T133316_result.json`
- **Structured JSON:** [`1c322169b28f22bed6ba.json`](../../sessions/1c/1c322169b28f22bed6ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备份完成。验证结果：文件大小与源端完全一致。

### 备份清单

| 目录/文件 | 大小 | 目标路径 (cqa1) |
|---|---|---|
| `artifacts/d051_llama-3.1-70b-fp8_fewnerd_n25_s42/` | 113M | 同路径 ✓ |
| `artifacts/d051_llama-3.1-70b-fp8_fewrel_n25_s42/` | 82M | 同路径 ✓ |
| `artifacts/bcs_controlled_llama-3.1-70b-fp8/` | 1.4M | 同路径 ✓ |
| `results/d051_70b_reeval_summary.json` | 5.4K | 同路径 ✓ |

**总计约 196M**，包含：
- Few-NERD 实验：6 个 count 级别的 prediction JSONL + summary_unified_protocol.json + summary_type_text.json
- FewRel 实验：5 个 count 级别的 prediction JSONL
- BCS controlled 实验数据（count_8, count_16）
- 70B 重评估汇总 JSON

---
