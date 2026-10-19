# fix exp029 tmp restart

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp029_tmp_restart_20260516T150153_result.json`
- **Structured JSON:** [`41c30dee0e2e576fe352.json`](../../sessions/41/41c30dee0e2e576fe352.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| 项目 | 结果 |
|------|------|
| /tmp 清理 | 从 16G used (51%) → 14G used (46%)，释放约 2GB |
| exp029 checkpoint | **无** — `/root/autodl-tmp/checkpoints/exp029/` 不存在 |
| resume 配置 | 第 41 行 `resume_mode: "disable"`，保持不变（无 checkpoint 可恢复） |
| tmux session | 无活跃 session |

结论：无 checkpoint 可恢复，将从头训练。配置无需修改。清理完毕，可由主系统 submit_training_job 启动 exp029。

---
