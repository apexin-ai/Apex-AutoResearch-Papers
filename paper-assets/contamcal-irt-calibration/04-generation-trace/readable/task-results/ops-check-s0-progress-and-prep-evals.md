# ops check s0 progress and prep evals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-s0-progress-and-prep-evals_20260520T185039_result.json`
- **Structured JSON:** [`619a2c0bd1c66b502497.json`](../../sessions/61/619a2c0bd1c66b502497.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### s0 训练进度

| 模型 | 服务器 | 已完成 | 当前 | 进度 | ETA 全部完成 |
|------|--------|--------|------|------|-------------|
| **Qwen-7B** | cqa1 | d000/d005/d025/d050 | d100 (521/4159) | 12% | ~3.5h |
| **Gemma-2-9B** | westd cuda:3 | d000/d005/d025 | d050 (1357/3642) | 37% | ~1.6h (d050) + ~2.9h (d100) ≈ **4.5h** |
| **Qwen-14B** | westd | d000/d005 | d025 (2486/3384) | 73% | ~0.9h (d025) + 3.5h (d050) + 4h (d100) ≈ **8.4h** |

### 已创建 eval 脚本

| 脚本 | 路径 | 语法 | 备注 |
|------|------|------|------|
| Gemma-2 s0 MMLU | `scripts/eval_gemma2_s0_mmlu.sh` | OK | CUDA:0, batch=8, 含 C009 md5 校验 |
| Qwen-14B s0 MMLU | `scripts/eval_qwen14b_s0_mmlu.sh` | OK | CUDA:0, batch=4 (14B 模型较大), 含 C009 md5 校验 |

Gemma-2 sweep 脚本 **不含内置 eval**，需要单独跑。两个 eval 脚本已就绪，训练完成后可提交。

---
