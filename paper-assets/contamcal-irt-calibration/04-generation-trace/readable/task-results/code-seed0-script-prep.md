# code seed0 script prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed0-script-prep_20260519T154411_result.json`
- **Structured JSON:** [`8089ce53adbc2726749b.json`](../../sessions/80/8089ce53adbc2726749b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diff 确认完毕。所有改动仅限 seed 相关部分。

### 结果

**模板来源**: `/root/autodl-tmp/exp001/run_{phi4,qwen14b,qwen7b_olmo2,gemma2}_s123.sh`

**创建的 4 个脚本**:
| 脚本 | GPU | 模型 | batch×accum |
|------|-----|------|-------------|
| `scripts/seed0/sft_phi4_s0_sweep.sh` | cuda:0 | phi-4 | 1×16 |
| `scripts/seed0/sft_qwen14b_s0_sweep.sh` | cuda:1 | Qwen2.5-14B | 1×16 |
| `scripts/seed0/sft_qwen7b_olmo2_s0_sweep.sh` | cuda:2 | Qwen2.5-7B + OLMo-2-7B | 2×8 |
| `scripts/seed0/sft_gemma2_s0_sweep.sh` | cuda:3 | gemma-2-9b | 1×16 |

**Diff 确认**: 仅改了 `--seed 123` → `--seed 0`、输出路径 `s123` → `s0`、echo 信息中的 seed 标记。超参数完全一致。

**一个小结构差异**: qwen7b_olmo2 的 s123 原版 Part 1 (Qwen-7B) 用了 if/else 结构，s0 版统一为 if/continue（与其他脚本一致），训练逻辑不变。

---
