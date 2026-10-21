# code exp004 sweep recovery

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004-sweep-recovery_20260515T000815_result.json`
- **Structured JSON:** [`adf7e0e76982a0361bca.json`](../../sessions/ad/adf7e0e76982a0361bca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，总结：

1. **/tmp 清理完成** — 从 100% 恢复到 1%（18MB/3.9GB）
2. **持久化 TMPDIR 创建** — `/home/ubuntu/tmp_cmdstan`，cmdstanpy 临时文件现在写到根分区（51GB 可用）
3. **run_sweep.py 修改** — 添加 `--resume` 参数，resume 模式下移除已失败的 seed 记录再重跑，避免重复条目
4. **exp_004_sim_sweep_v4 已启动** — 注册为 RUNNING，server=cqa1-21977，tmux session `exp_004_sim_sweep_v4`
5. **Resume 验证通过** — 正确跳过已完成的 4 个条件（auc0.8_n20/n50, auc0.55_n20/n50），正在补跑 auc0.8_n100 (4 seeds) 和 auc0.9_n20 (6 seeds)

---
