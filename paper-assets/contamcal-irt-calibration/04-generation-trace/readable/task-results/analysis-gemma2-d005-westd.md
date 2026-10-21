# analysis gemma2 d005 westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma2_d005_westd_20260518T232754_result.json`
- **Structured JSON:** [`bff30a4e38106950c432.json`](../../sessions/bf/bff30a4e38106950c432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemma-2-9B d005 s42 训练结果

| 项目 | 值 |
|---|---|
| **Conclusion** | **SUCCESS** |
| **Total steps** | 3177 |
| **Final train_loss** (avg) | 1.258 |
| **Final batch loss** (last log) | 1.157 |
| **Final token_accuracy** (avg) | 0.7303 |
| **Final batch token_accuracy** | 0.7366 |
| **Runtime** | ~2h26m |
| **.done sentinel** | 存在 |
| **lora_alpha** | 32 (符合规范) |

训练配置确认：lora_r=16, lora_alpha=32, lr=5e-5, epochs=1, grad_accum=16, num_samples=50826。

cuda:1 已空闲（0MiB, 0% util），可用于下一个任务。cuda:0/2/3 仍有进程在跑。

---
