# ssh 14b baseline exit check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-baseline-exit-check_20260522T202555_result.json`
- **Structured JSON:** [`f4500bafe240a0ffd15e.json`](../../sessions/f4/f4500bafe240a0ffd15e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。实验 **14b-baseline-0shot-3shot-v2** 判定为 **success**，registry 已更新为 DONE，cron 已删除。

**关键发现：** Qwen3-14B 的 baseline 表现远超预期假设（假设 0-shot ~52%、3-shot ~60%），实际 0-shot 66.24%、3-shot 73.12%，说明 14B scale 在 zero/few-shot 上已有显著提升。结果文件保存在服务器 `/home/sonny/exec-sim-repair-verifier/results_14b_{0,3}shot.json`。

---
