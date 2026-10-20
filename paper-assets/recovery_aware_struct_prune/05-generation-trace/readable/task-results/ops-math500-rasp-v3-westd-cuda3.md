# ops math500 rasp v3 westd cuda3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_math500_rasp_v3_westd_cuda3_20260517T144433_result.json`
- **Structured JSON:** [`b96b67458b905fbc3a78.json`](../../sessions/b9/b96b67458b905fbc3a78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载完成，正在加载 MATH 数据集。任务已正常启动。

---

**报告：**

| 项目 | 结果 |
|------|------|
| eval_math500.py 是否支持 resume | **不支持**（无 `--start_idx` / `--resume` 参数），全量重跑 |
| HumanEval kill 确认 | PID 31087 (tmux) + 31092 (python) 均已终止，tmux session 已清理 |
| MATH-500 v3 PID | **31706**（tmux session: `eval_math500_grpo_rasp_20_v3`） |
| nvidia-smi 状态 | 模型加载耗时 ~90s（CPU→GPU），22:47:21 已完成加载进入 dataset 加载阶段，即将开始推理 |

---
