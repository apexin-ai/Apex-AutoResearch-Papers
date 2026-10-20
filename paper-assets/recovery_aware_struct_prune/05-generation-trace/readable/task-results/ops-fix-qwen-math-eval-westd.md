# ops fix qwen math eval westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_qwen_math_eval_westd_20260516T103248_result.json`
- **Structured JSON:** [`ceddb9fe7ccd2a740043.json`](../../sessions/ce/ceddb9fe7ccd2a740043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 已经在正常运行，无需重启：

| GPU | 任务 | PID | VRAM | 进度 | 速度 |
|-----|------|-----|------|------|------|
| cuda:0 | RASP Qwen Math | 102641 | 29617 MiB (30%) | 7/1319 (~0.5%) | ~328s/it |
| cuda:1 | Standard Qwen Math | 102643 | 29589 MiB (30%) | 8/1319 (~0.6%) | ~298s/it |

每个样本约 5 分钟，1319 个样本预计总耗时约 **4-5 天**。速度很慢是因为模型在逐条生成数学推理过程，且有 `max_length` 4096 的 warning 说明部分样本生成到了最大长度。

注意：模型路径与你指定的略有不同：
- 实际 RASP 路径: `sft_qwen_math_rasp_20`（不是 `sft_rasp_20_qwen_math`）
- 实际 Standard 路径: `sft_qwen_math_standard_20`（不是 `sft_standard_20_qwen_math`）
- 输出路径也做了调整，加了 `_n1319` 后缀

进程已在运行中，不需要额外操作。

---
