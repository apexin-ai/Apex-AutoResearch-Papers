# ops gpu1 qwen con launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu1-qwen-con-launch_20260520T035455_result.json`
- **Structured JSON:** [`11f077955956712112bd.json`](../../sessions/11/11f077955956712112bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，双 GPU 并行运行。

**汇总**：

| 项目 | 状态 |
|------|------|
| d066 beam8 con | 551/551 完整 ✓ |
| sleep-loop PID 169446 | 已杀 ✓ |
| GPU0 (unc) | PID 167691, 18919 MiB, ~80% util |
| GPU1 (con full_s1) | 18905 MiB, 模型已加载，开始推理 |
| tmux session | `d065_qwen_con` |
| 日志 | `/root/autodl-tmp/schema_outputs/d065_qwen_greedy_con_4096.log` |
| 输出 | `/root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096.jsonl` |
| 数据集 | docred dev, 998 samples |
| 模式 | `--mode full_s1` (con 对应的实际参数) |

注意：`--mode constrained` 不是有效参数，实际用了 `full_s1`（与 d066 beam sweep 的 con 文件命名一致）。

---
