# ops find 4b model and adapter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find_4b_model_and_adapter_20260516T123443_result.json`
- **Structured JSON:** [`aa618eeea7c7dc29ff6f.json`](../../sessions/aa/aa618eeea7c7dc29ff6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。结果如下：

| 资源 | 正确路径 |
|------|---------|
| **Qwen3-4B base 模型** | `/root/autodl-tmp/models/Qwen3-4B` （注意：不在 `Qwen/` 子目录下，直接在 `models/` 下） |
| **4B with-evidence SFT adapter** | `/root/autodl-tmp/sft_output` （无后缀，adapter_config.json 中 `base_model_name_or_path` 确认指向 `/root/autodl-tmp/models/Qwen3-4B`） |
| **Re-DocRED 数据** | `/root/autodl-tmp/data/re-docred/` （含 dev.json, test.json, train_annotated.json） |

补充说明：
- `Qwen/` 子目录下只有 `Qwen3-1.7B` 和 `Qwen3-8B`，没有 4B
- 4B 没有 no-evidence adapter（服务器上的 no-evidence adapter 只有 1.7B、8B、Llama-3.1-8B）
- SFT adapter 配置：LoRA r=64, alpha=128, dropout=0.05

---
