# diag alpha sweep c4 a050 s42 bf16

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_alpha_sweep_c4_a050_s42_bf16_20260518T202457_result.json`
- **Structured JSON:** [`db1b01e84d2d9073e479.json`](../../sessions/db/db1b01e84d2d9073e479.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：假警报，实验已成功完成。**

- **EXIT_CODE sentinel 文件内容为 "0"**，Python 脚本 `main()` 正常执行到最后一行
- **全部 11 个 generation (gen_0-gen_10) 的数据完整**，`all_metrics.json` 包含所有条目
- **EXIT_CODE=129 的原因**：tmux session 在训练完成后被 kill（session 已不在 `tmux list-sessions` 中），SIGHUP 传递给进程组，shell 层面记录了 129，但 Python 层面早已写入 EXIT_CODE=0
- **不需要重跑**，所有结果可直接使用

Registry 已更新：`conclusion` 从 "failed" 改为 "success"，`failure_reason` 记录了误报详情。诊断报告已注册为 artifact。

---
