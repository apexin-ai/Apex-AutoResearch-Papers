# code qwen7b s42 reeval prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen7b-s42-reeval-prep_20260519T181605_result.json`
- **Structured JSON:** [`f546da98a89a445f6c03.json`](../../sessions/f5/f546da98a89a445f6c03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本语法通过。

**汇报：**

**Adapter 路径确认（全部 lora_alpha=32）：**
| Dosage | Adapter 路径 |
|--------|-------------|
| d000 | `Qwen2.5-7B_d000_s42/lora_adapter` |
| d005 | `Qwen2.5-7B_d005_s42/lora_adapter` |
| d025 | `Qwen2.5-7B_d025_s42/lora_adapter` |
| d050 | `Qwen2.5-7B_d050_s42/lora_adapter` |
| d100 | `Qwen2.5-7B_d100_s42/lora_adapter` |

**关于 d000**：d000_s42 实际包含 adapter（0% dosage SFT 训练产物，lora_alpha=32），与 s123 d000 处理方式一致——都走 adapter-based eval。

**与 s123 v2 脚本差异：**
1. Adapter 路径：`Qwen2.5-7B_${DOSAGE}_s123` → `Qwen2.5-7B_${DOSAGE}_s42`
2. 输出目录：`qwen7b_${DOSAGE}_s123` → `qwen7b_${DOSAGE}_s42_v2`
3. eval_meta.json 中 `seed: 123` → `seed: 42`

脚本路径：`/root/contamcal-irt-calibration/exp001/eval_qwen7b_s42_cqa1.sh`，已 `chmod +x`，未启动。

---
