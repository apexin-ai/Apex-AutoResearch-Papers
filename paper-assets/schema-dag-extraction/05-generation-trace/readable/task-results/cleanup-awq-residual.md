# cleanup awq residual

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_awq_residual_20260515T223708_result.json`
- **Structured JSON:** [`93f10c349e5f5fb68545.json`](../../sessions/93/93f10c349e5f5fb68545.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 评估结果

### AWQ 相关文件清单

| 类别 | 路径 | 大小 | 建议 |
|------|------|------|------|
| **脚本** | `/root/schema-dag-extraction/scripts/run_exp012_llama_awq.sh` | ~1KB | 可安全删除 |
| **脚本** | `/root/schema-dag-extraction/scripts/auto_start_exp012_awq.sh` | ~1KB | 可安全删除 |
| **库内置** | `transformers/integrations/awq.py` | — | transformers 自带，不动 |
| **库内置** | `transformers/quantizers/quantizer_awq.py` | — | transformers 自带，不动 |

### 关键发现

- **70B AWQ 模型权重已不存在。** 脚本引用的路径 `/root/autodl-tmp/.hf_cache/llama-3.1-70b-instruct-awq-int4/` 不存在——~36GB 的模型文件已经被清理过了。
- **`src/` 和 `configs/` 中无 AWQ 引用**，没有代码依赖。
- **没有安装 `autoawq` pip 包**（site-packages 中只有 transformers 内置的 AWQ 集成模块，不需要处理）。

### 建议

仅剩两个废弃脚本（`run_exp012_llama_awq.sh`、`auto_start_exp012_awq.sh`），总计 ~2KB，磁盘影响可忽略。如需清理可直接删除，无任何代码依赖。

**~36GB 模型权重已不在磁盘上，无需额外释放空间。**

---
