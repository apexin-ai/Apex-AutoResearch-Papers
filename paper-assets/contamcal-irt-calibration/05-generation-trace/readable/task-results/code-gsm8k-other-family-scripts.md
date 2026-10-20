# code gsm8k other family scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-other-family-scripts_20260519T223458_result.json`
- **Structured JSON:** [`b9f0a24dd2f0e912866c.json`](../../sessions/b9/b9f0a24dd2f0e912866c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本语法检查通过。

### 结果汇总

| Family | 脚本 | d000 checkpoint | d100 checkpoint | Base model | 状态 |
|--------|------|----------------|----------------|------------|------|
| gemma-2-9b | `eval_gsm8k_gemma2_s42.sh` | ✅ `gemma-2-9b_d000_s42/lora_adapter/lora_adapter` | ❌ 不存在 | ✅ `/root/autodl-tmp/models/gemma-2-9b` | d000 可跑，d100 会 skip |
| Qwen2.5-14B | `eval_gsm8k_qwen14b_s42.sh` | ✅ `Qwen2.5-14B_d000_s42/lora_adapter` | ❌ 不存在 | ❌ 未下载 | 需先下载 base model |
| Phi-4 | 未创建 | ❌ 无 checkpoint | ❌ | — | cqa1 上无任何 Phi-4 数据 |
| OLMo-2 | 未创建 | ❌ 无 checkpoint | ❌ | — | cqa1 上无任何 OLMo 数据 |

注意 gemma-2-9b adapter 路径是双层嵌套 `lora_adapter/lora_adapter/`，脚本已适配。

---
