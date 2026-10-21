# eval cls8b s42 resume ckpt3600 mutation breakdown

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-resume-ckpt3600-mutation-breakdown_20260515T230056_result.json`
- **Structured JSON:** [`eb375c86ea49cc152120.json`](../../sessions/eb/eb375c86ea49cc152120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动：

- **Session**: `cls8b_s42_ckpt3600_test`
- **GPU**: cuda:1 (via CUDA_VISIBLE_DEVICES=1)
- **数据**: 9784 test instances 已加载 (label 分布: pass=7138, fail=2646)
- **模型**: checkpoint-3600 加载完成，正在推理中
- **流程**: eval 完成后自动运行 `mutation_breakdown.py` 生成 per-mutation-type 统计

预计 ~2-3h 完成。eval 结束后 breakdown 会自动输出到 `/root/autodl-tmp/eval_results/cls8b_s42_resume_test_ckpt3600_mutation/mutation_breakdown.json`。

---
