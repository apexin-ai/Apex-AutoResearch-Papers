# diagnose scienceworld sft exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scienceworld-sft-exit_20260519T160024_result.json`
- **Structured JSON:** [`8c960c5f04ec9fc3823f.json`](../../sessions/8c/8c960c5f04ec9fc3823f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 不接受自由文本 conclusion，且训练确实还在跑，状态无需变更。

## 诊断结果

| 项目 | 状态 |
|------|------|
| 训练 | **仍在运行**，step 186/448 (~41.5%) |
| 实际 PID | 120838 (torchrun)，workers 120904-120907 |
| 误报原因 | Cron 监控的 PID 120827 是外层 wrapper shell，已退出；实际训练进程树 120829→120838→workers 完好 |
| Loss | 0.005-0.015（稳定低值） |
| GPU | 4×RTX PRO 6000，100% 利用率，各 ~47GB |
| Checkpoint | global_step_112 完整（HF safetensors + FSDP shards） |
| 磁盘 | 根 46%，数据盘 45%，充裕 |
| 预计剩余 | ~1.5h（每 step ~20s × 262 remaining steps） |

**不删除 cron，不更新 registry conclusion。** Cron 后续应改为监控 PID 120838 而非 120827。

---
