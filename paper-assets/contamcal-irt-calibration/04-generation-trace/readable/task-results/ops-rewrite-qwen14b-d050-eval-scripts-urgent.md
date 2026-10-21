# ops rewrite qwen14b d050 eval scripts urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rewrite-qwen14b-d050-eval-scripts-urgent_20260521T033944_result.json`
- **Structured JSON:** [`655b0bcb6b4d2289f786.json`](../../sessions/65/655b0bcb6b4d2289f786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 产出

| | MMLU 脚本 | ARC 脚本 | 参考脚本 |
|---|---|---|---|
| **路径** | `scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh` | `scripts/seed0/eval_qwen14b_d050_s0_arc.sh` | `eval_qwen14b_s0_arc_partial.sh` |
| `EXPECTED_MD5` | `17673bf373f00f83ccc41fc1d355a4cd` ✅ | 同 ✅ | 同 |
| `CUDA_VISIBLE_DEVICES` | `1` ✅ | `1` ✅ | `3` |
| `--model-path` | `/root/autodl-tmp/models/Qwen2.5-14B` ✅ | 同 ✅ | 同 |
| `--benchmarks` | `mmlu` ✅ | `arc_challenge` ✅ | `$benchmark` |
| `--batch-size` | `2` ✅ | `2` ✅ | `2` |
| `--shots` | 无（已删除）✅ | 无 ✅ | 无 |
| `evaluate.py` 路径 | `exp001/evaluate.py`（绝对路径）✅ | 同 ✅ | 同 |

### 修复的 6 个问题

1. ~~`evaluate.py`~~ → `exp001/evaluate.py` ✅
2. ~~`--model Qwen/Qwen2.5-14B`~~ → `--model-path /root/autodl-tmp/models/Qwen2.5-14B` ✅
3. ~~`--benchmark`~~ → `--benchmarks` ✅
4. ~~`--shots 5`~~ → 已删除 ✅
5. C009 md5 校验已添加 ✅
6. `CUDA_VISIBLE_DEVICES=1` 已添加 ✅

另外保留了参考脚本的 C006 lora_alpha=32 检查和 adapter 路径自动检测逻辑。`bash -n` 语法验证和 `evaluate.py --help` 参数对照均通过。

---
