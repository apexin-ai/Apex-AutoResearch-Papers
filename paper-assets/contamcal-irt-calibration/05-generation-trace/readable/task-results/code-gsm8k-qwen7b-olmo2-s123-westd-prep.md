# code gsm8k qwen7b olmo2 s123 westd prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k_qwen7b_olmo2_s123_westd_prep_20260519T225511_result.json`
- **Structured JSON:** [`22af2ce4934de42562e9.json`](../../sessions/22/22af2ce4934de42562e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。汇总：

**脚本路径**: `westd-29999:/root/autodl-tmp/exp001/eval_gsm8k_qwen7b_olmo2_s123.sh`

**Checkpoint 路径**:
| Model | Dosage | Checkpoint |
|-------|--------|------------|
| Qwen2.5-7B | d000_s123 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s123/lora_adapter` |
| Qwen2.5-7B | d100_s123 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s123/lora_adapter` |
| OLMo-2-7B | d000_s123 | `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d000_s123/lora_adapter` |
| OLMo-2-7B | d100_s123 | `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d100_s123/lora_adapter` |

**验证结果**:
- evaluate.py md5: westd = cqa1 = `001a9bc23f808c47d25ef9eaeecb81f1` ✅ (C009)
- lora_alpha: 两个模型 d000_s123 均为 32 ✅ (C006)
- CUDA_VISIBLE_DEVICES=2 显式设置 ✅ (C004)

**预估运行时间**: ~1h（4 个 eval，每个 ~15min，7B 模型 GSM8K batch_size=8）

**运行命令**（提交时用）:
```bash
CUDA_VISIBLE_DEVICES=2 nohup bash /root/autodl-tmp/exp001/eval_gsm8k_qwen7b_olmo2_s123.sh > /root/autodl-tmp/exp001/gsm8k_qwen7b_olmo2_s123.log 2>&1 &
```

---
