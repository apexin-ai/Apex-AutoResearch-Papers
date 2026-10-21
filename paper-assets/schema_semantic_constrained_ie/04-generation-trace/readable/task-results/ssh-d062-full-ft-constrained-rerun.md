# ssh d062 full ft constrained rerun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d062_full_ft_constrained_rerun_20260519T043914_result.json`
- **Structured JSON:** [`5fc581f85256a8fcca5d.json`](../../sessions/5f/5fc581f85256a8fcca5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完成。

1. **损坏文件已删除** — `re_qwen_full_ft_scierc_full_s1.jsonl` 已清除
2. **冲突进程已清理** — 发现并杀掉了另一个冲突 session `d062_con_rerun`（PID 86387），避免再次双写
3. **新 tmux session** — `d062_constrained_only`（创建于 12:42:13）
4. **推理已启动** — 单进程（PID 86882）在 cuda:0 上运行，占用 ~19GB 显存，模型加载完成，正在推理 551 个样本
5. **Unconstrained 输出完整** — 551 行，无需重跑

脚本流程：constrained inference → violation check (unconstrained + constrained) → 打印对比结果 → 行数验证。

---
