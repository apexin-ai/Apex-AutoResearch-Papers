# code disk cleanup and monitor

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_disk-cleanup-and-monitor_20260515T051200_result.json`
- **Structured JSON:** [`50b59e85d48ba4addada.json`](../../sessions/50/50b59e85d48ba4addada.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## 磁盘清理前后对比

| | 已用 | 可用 | 使用率 |
|--|------|------|--------|
| 清理前 | 222G | 29G | 89% |
| **清理后** | **141G** | **110G** | **57%** |

释放 **81G**（sft_standard_20）。

## 当前目录占用

| 目录 | 大小 |
|------|------|
| sft_rasp_20 | 81G |
| logs | 17M |
| grpo_stage2_rasp_20_v2 | 20K |
| grpo_stage2_standard_20_v2 | 16K |
| eval_results | 8K |
| models, results | 0 |

## GRPO checkpoint 状态

两个 GRPO 目录都只有 `completions/` 子目录，无多余 checkpoint 需要清理。

## eval 脚本修改

- 移除了 `SFT_STANDARD_20` 变量定义和 `ALL_MODELS` 中的条目
- Phase 2 从双 GPU 并行改为单任务执行（只跑 sft_rasp_20）
- 脚本现在评估 **6 个模型**：baseline_unpruned, pruned_rasp_20, pruned_standard_20, sft_rasp_20, grpo_stage2_rasp_20_v2, grpo_stage2_standard_20_v2

---
