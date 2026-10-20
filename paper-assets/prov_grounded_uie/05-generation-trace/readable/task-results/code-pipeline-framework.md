# code pipeline framework

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pipeline-framework_20260512T110142_result.json`
- **Structured JSON:** [`879fd4c62c145152401d.json`](../../sessions/87/879fd4c62c145152401d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

框架搭建完成，所有验证通过：

| 文件 | 行数 | 功能 |
|------|------|------|
| `config.py` | ~150 | 6 个 dataclass（Model/SFT/GRPO/Reward/Data/Eval），全部支持 CLI 覆盖 |
| `data_utils.py` | ~230 | DocRED JSON→JSONL 转换 + SFT/GRPO Dataset 加载，含 96 个关系类型映射 |
| `rewards.py` | ~270 | 三类奖励 + composite：provenance fidelity（char-IoU + batched NLI + length penalty）、structural F1（partial matching）、format compliance |
| `train_sft.py` | ~120 | SFTTrainer + LoRA，训练后自动 merge 输出到 `{output_dir}/merged/` |
| `train_grpo.py` | ~110 | GRPOTrainer，从 merged SFT 加载 + 新 LoRA，reward 权重从 RewardArgs 注入 |
| `evaluate.py` | ~200 | 生成 + 计算 RE F1 / Evi F1 / Attribution Precision，支持 PEFT adapter 自动检测 |
| `requirements.txt` | 9 | torch/transformers/trl/peft/datasets/wandb/accelerate/bitsandbytes/sentencepiece |

关键设计点：
- NLI 模型 lazy loading，不阻塞 import
- SFT 结束后自动 merge LoRA → full model，GRPO 直接加载无需 adapter stacking
- reward kwargs 透传 dataset 列（gold_relations/sentences/document_text），GRPO 训练时自动注入
- 所有 gold metadata 存为 JSON 字符串（兼容 HuggingFace Dataset 序列化）

GPU 到位后执行顺序：`data_utils.py --raw_dir ...` → `train_sft.py` → `train_grpo.py` → `evaluate.py`。

---
