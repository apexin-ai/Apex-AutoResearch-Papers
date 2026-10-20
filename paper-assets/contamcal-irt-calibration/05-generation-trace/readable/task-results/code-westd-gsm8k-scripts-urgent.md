# code westd gsm8k scripts urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-gsm8k-scripts-urgent_20260519T224533_result.json`
- **Structured JSON:** [`1df726f31731aba97b29.json`](../../sessions/1d/1df726f31731aba97b29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**已创建 s42 脚本**（`scripts/gsm8k_s42/`）：

| 脚本 | CUDA | 模型 |
|------|------|------|
| `run_gsm8k_olmo2_s42.sh` | **2** | OLMo-2-7B |
| `run_gsm8k_phi4_s42.sh` | 0 | phi-4 |
| `run_gsm8k_gemma2_s42.sh` | 3 | gemma-2-9b |
| `run_gsm8k_qwen14b_s42.sh` | 1 | Qwen2.5-14B |
| `run_gsm8k_qwen7b_s42.sh` | 2 | Qwen2.5-7B |

**已修复 s123 脚本 CUDA 分配**（同上映射，原来全部硬编码 CUDA=0）。

所有脚本包含：C009 md5 校验、adapter 缺失跳过、输出到 `results/gsm8k/{model}_d{dosage}_s42/`。10/10 语法检查通过。lora_alpha=32 已确认（C006 合规）。

OLMo-2 s42 脚本（CUDA=2）已就绪，cuda:2 空闲后可直接执行。

---
