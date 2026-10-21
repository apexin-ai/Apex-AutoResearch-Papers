# code exp 021 length ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_021_length_ablation_20260516T053759_result.json`
- **Structured JSON:** [`1cdfcbc936375c1f7ba6.json`](../../sessions/1c/1cdfcbc936375c1f7ba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-021 已成功启动：

- **GPU 3**: 已占用 3467 MiB，正在运行
- **当前进度**: length=128 阶段，模型已加载，正在下载 C4 seed data
- **日志确认**: `Max new tokens: 128` 参数已正确传入
- **后续**: 128 → 256 → 512 顺序执行，三轮共享 cuda:3

修改摘要：
- 给 `run_pipeline.py` 添加了 `--max_new_tokens` CLI 参数（默认 256），同时控制 seed data 截断长度和 generation 输出长度
- 模型使用 `Qwen2.5-1.5B`（base，非 Instruct；continuation mode 下 base 模型是正确选择）
- Registry spec 已更新

---
