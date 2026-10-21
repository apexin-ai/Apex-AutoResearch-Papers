# code gsm8k s123 eval scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-s123-eval-scripts_20260519T192101_result.json`
- **Structured JSON:** [`9916736fdb04ed0ee2a5.json`](../../sessions/99/9916736fdb04ed0ee2a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个脚本已创建在 `scripts/gsm8k_s123/`，汇总如下：

| 脚本 | 基础模型 | Checkpoint 格式 | 输出目录 |
|------|---------|----------------|---------|
| `run_gsm8k_phi4_s123.sh` | `/root/autodl-tmp/models/phi-4` | `phi-4_d{000,100}_s123/lora_adapter` | `results/gsm8k/phi4_d{000,100}_s123/` |
| `run_gsm8k_gemma2_s123.sh` | `/root/autodl-tmp/models/gemma-2-9b` | `gemma-2-9b_d{000,100}_s123/lora_adapter` | `results/gsm8k/gemma2_d{000,100}_s123/` |
| `run_gsm8k_qwen14b_s123.sh` | `/root/autodl-tmp/models/Qwen2.5-14B` | `Qwen2.5-14B_d{000,100}_s123/lora_adapter` | `results/gsm8k/qwen14b_d{000,100}_s123/` |
| `run_gsm8k_qwen7b_s123.sh` | `/root/autodl-tmp/models/Qwen2.5-7B` | `Qwen2.5-7B_d{000,100}_s123/lora_adapter` | `results/gsm8k/qwen7b_d{000,100}_s123/` |
| `run_gsm8k_olmo2_s123.sh` | `/root/autodl-tmp/models/OLMo-2-1124-7B` | `OLMo-2-7B_d{000,100}_s123/lora_adapter` | `results/gsm8k/olmo2_d{000,100}_s123/` |

关键确认：
- MD5 gate (`001a9bc23f808c47d25ef9eaeecb81f1`) 在每个脚本开头
- `--benchmarks gsm8k --batch-size 8`
- `CUDA_VISIBLE_DEVICES=0`
- 只跑 d000 + d100
- adapter 不存在时自动 SKIP（d100_s123 训练尚未完成的 family 会被跳过）
- Checkpoint 路径已按 westd 实际命名格式（从 `/root/autodl-tmp/exp001/checkpoints/` 确认）

注意：当前 s123 checkpoint 中，phi-4/gemma-2-9b/Qwen2.5-14B 的 d100 尚未产出，OLMo-2 的 d100 也没有。脚本的 adapter 存在性检查会自动跳过这些。

---
