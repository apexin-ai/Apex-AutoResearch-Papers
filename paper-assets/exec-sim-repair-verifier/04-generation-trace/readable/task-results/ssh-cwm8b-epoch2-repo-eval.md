# ssh cwm8b epoch2 repo eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm8b-epoch2-repo-eval_20260523T101741_result.json`
- **Structured JSON:** [`6058dd37e00b5225ce4a.json`](../../sessions/60/6058dd37e00b5225ce4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成的工作：

1. **Function-level CWM 8B 过拟合数据**：epoch 3 比 epoch 2 (best) 下降 0.95pp（87.67% → 86.72%），已注册 artifact。

2. **Repo-level CWM 8B ckpt-6100 eval** 在 cuda:3 后台运行中（PID 子进程，log `/tmp/cwm8b_repo_ckpt6100.log`），预计 ~17 小时完成。对比基线 ckpt-400 accuracy 64.36%。

3. **发现论文 Table 3 的 checkpoint 不一致**：footnote 说 "CWM uses epoch-3 checkpoint" 但 s42 实际用 ckpt-400 (best)，只有 s123/s456 用 ckpt-6633 (final)。且 seq_length 不一致（s42: 4096, s123/s456: 8192）。

---
