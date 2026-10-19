# check perlayer kl 50 downstream progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_perlayer_kl_50_downstream_progress_20260522T074432_result.json`
- **Structured JSON:** [`bfa0f96d72c5defa6956.json`](../../sessions/bf/bfa0f96d72c5defa6956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进度报告**：

**进程状态**：活跃，日志在 51 分钟前启动，最后写入 15:44:59（约 1 秒前），未阻塞。

**Sparsity 验证**：从 predictor 加载的 per-layer mask，Model-level=0.496（接近 target 0.5）✓

**Task list 已确认**：`['arc_challenge', 'winogrande', 'mmlu', 'gsm8k', 'hellaswag', 'piqa']`

**进度分解**（lm-eval 按 num_fewshot 分组运行）：
| Group | 状态 | 备注 |
|---|---|---|
| `arc_challenge` (25-shot) | ✅ 完成 | 4687 loglikelihood requests，~3.5 min |
| `winogrande + mmlu` (5-shot) | 🔄 进行中 | **32%** (12977/40168)，已跑 11:00，**ETA ~21 min** |
| `gsm8k` (5-shot, generation) | ⏳ 待 | 通常 15-30 min（生成任务） |
| `hellaswag` (10-shot) | ⏳ 待 | ~10K 样本，预计 15-20 min |
| `piqa` (0-shot) | ⏳ 待 | ~2K 样本，预计 5-8 min |

**指标输出**：lm-eval 会在每组 evaluate() 调用结束时打印结果表，但日志当前只滚动 tqdm 进度条，**尚未看到任何已完成 task 的数值指标**——arc_challenge 应该已经在某处打印了，但被超大 tqdm 输出覆盖/截断了。需要等运行结束读 results JSON 才能拿到完整数字。

**总体 ETA**：当前组剩 ~21 min + 剩 3 组（gsm8k/hellaswag/piqa）~40-60 min = **再约 60-80 min 完成全部 6 个 task**（约 16:45–17:05 收尾）。

---
