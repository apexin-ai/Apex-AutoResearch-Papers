# train plan002 additive b01 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan002-additive-b01-s42_20260514T052749_result.json`
- **Structured JSON:** [`87c8b6dc9458b35e9097.json`](../../sessions/87/87c8b6dc9458b35e9097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **plan002-additive-b01-s42** 已准备完毕：

- Registry: PENDING，parent=plan002-additive-b03-s42
- 训练命令已验证，与 b03 唯一区别：`--beta 0.1` + 不同 output_dir
- `save_total_limit=1` / `log_completions=False` 由脚本硬编码，无需额外参数
- Output dir 干净，数据/config/GPU 全部就绪

等 Director 审批后可直接用 spec 中的 command 提交到 cuda:0。

---
