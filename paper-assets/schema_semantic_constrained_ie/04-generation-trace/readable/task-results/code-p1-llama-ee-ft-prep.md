# code p1 llama ee ft prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p1_llama_ee_ft_prep_20260518T214636_result.json`
- **Structured JSON:** [`2af9f7a8653a70d2b1ce.json`](../../sessions/2a/2af9f7a8653a70d2b1ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。westd-16980 上创建了 3 个文件：

| 文件 | 说明 |
|------|------|
| `scripts/prepare_sft_data_wikievents_llama.py` | 用 Llama tokenizer 生成 SFT 数据 |
| `scripts/train_lora_wikievents_llama.py` | LoRA 训练脚本，report_to="none" |
| `scripts/run_p1_ee_ft_llama.sh` | 全流程 bash 脚本（数据准备→训练→推理→评估→违规检查） |

关键点：
- 模型: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
- Qwen SFT 数据不兼容 Llama（chat template 不同），bash 脚本 Step 0 会自动生成 Llama 格式数据
- 训练超参与 Qwen 版完全一致
- 产出报告: `artifacts/p1_llama_ee_ft_prep.md`

---
