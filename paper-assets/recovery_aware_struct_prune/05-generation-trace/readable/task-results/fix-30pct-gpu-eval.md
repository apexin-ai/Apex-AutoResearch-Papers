# fix 30pct gpu eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_30pct_gpu_eval_20260520T044416_result.json`
- **Structured JSON:** [`7d948499c5665f878779.json`](../../sessions/7d/7d948499c5665f878779.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 总结

| 项目 | 结果 |
|------|------|
| **Kill** | PID 191446/191519 已终止 |
| **根因** | 原始 run 大概率也在 GPU 上（速度 pattern 完全一致）。诊断日志确认 retry 模型在 cuda:0/cuda:1，85-86% 利用率，11.5 GB VRAM |
| **重新提交** | tmux `eval_cka30` (GPU 0) + `eval_std30` (GPU 1) 运行中 |
| **速度** | ~48s/sample（DeepSeek-R1-Distill 生成长推理链的固有速度），ETA ~17h |
| **代码修改** | `model_utils.py` 添加了 `.cuda()` 后的 device + CUDA_VISIBLE_DEVICES 诊断日志 |

**决策点**：两个 eval 正在 GPU 上跑，预计明天早上出结果。如果 17h 不可接受，30% collapse 结论已有 N=200 数据支撑，可以 kill 掉。

---
