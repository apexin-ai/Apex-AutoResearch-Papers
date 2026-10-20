# ops prep s123 eval scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-s123-eval-scripts_20260520T112959_result.json`
- **Structured JSON:** [`5f936e16b5d63f2fbf37.json`](../../sessions/5f/5f936e16b5d63f2fbf37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本全部就绪，语法验证通过。

**脚本汇总**:

| 脚本 | GPU | Base Model | Batch Size |
|------|-----|-----------|------------|
| `scripts/eval_gemma2_s123_mmlu.sh` | CUDA:2 | `/root/autodl-tmp/models/gemma-2-9b` | 8 |
| `scripts/eval_qwen14b_s123_mmlu.sh` | CUDA:2 | `/root/autodl-tmp/models/Qwen2.5-14B` | 4 |
| `scripts/eval_phi4_s123_mmlu.sh` | CUDA:0 | `/root/autodl-tmp/models/phi-4` | 8 |

**Checkpoint 路径确认** (15/15 全部存在，lora_alpha=32):

- Gemma-2: `gemma-2-9b_d{000,005,025,050,100}_s123/lora_adapter/` ✓
- Qwen-14B: `Qwen2.5-14B_d{000,005,025,050,100}_s123/lora_adapter/` ✓
- Phi-4: `phi-4_d{000,005,025,050,100}_s123/lora_adapter/` ✓

**evaluate.py**: md5=`17673bf373f00f83ccc41fc1d355a4cd` ✓（与 OLMo-2 脚本中的 EXPECTED_MD5 一致）

Qwen-14B batch_size 降到 4（14B 参数量约为其他 7-9B 模型的 2 倍，防 OOM）。未提交，等 GPU 释放后执行。

---
