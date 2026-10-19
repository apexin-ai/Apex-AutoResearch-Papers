# code post reeval analysis script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_post_reeval_analysis_script_20260526T092833_result.json`
- **Structured JSON:** [`c2bc3dc8e6f59345c605.json`](../../sessions/c2/c2bc3dc8e6f59345c605.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。产出三个文件：

- `reeval_comparison.py` — 主脚本
- `reeval_comparison.tex` — LaTeX 对比表
- `reeval_comparison.json` — JSON summary

已有数据的关键发现：LoRA-only s0 的 TSR 从 6.5% 跳到 51.5%（+45 pp），确认旧 bug 严重低估了 TSR。CAR 变化很小（+2 pp），符合预期（旋转 bug 主要影响任务完成而非碰撞判定）。

新 re-eval 结果出来后，取消 `NEW_DATA` 中对应条目的注释并填入数值，或配置 `JSON_PATHS` 指向结果 JSON，重新运行即可生成完整对比。

---
