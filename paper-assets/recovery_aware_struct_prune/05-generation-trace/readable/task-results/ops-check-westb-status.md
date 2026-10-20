# ops check westb status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westb-status_20260516T022413_result.json`
- **Structured JSON:** [`ef87b4f905673b863fc6.json`](../../sessions/ef/ef87b4f905673b863fc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 项目 | grpo_stage2_rasp_20_v9 (cuda:0) | eval_grpo_rasp_v9_step5 (cuda:1) |
|------|------|------|
| **PID** | 566666 ✅ 存活 | 572124 ✅ 存活 (子进程 572129 实际执行) |
| **运行时长** | 2h20m | 29m |
| **内存 RSS** | ~2.9GB | 3.6MB (wrapper shell) |
| **GPU 显存** | 71,674 MiB | 29,644 MiB |
| **当前进度** | **step 20/30** (67%), checkpoint-20 刚写完 (10:25) | **250/1319** samples (19%), acc=**0.6440** |
| **关键 metrics** | step 10: reward=0.015, loss=0.007, kl=0.0007&lt;br>step 20: reward=0.039, loss=-0.003, kl=0.001 | eos_rate=99.6%, avg_len=161 |
| **速度** | ~7min/step (410-420s) | ~2.3s/sample (正常段), 有间歇性慢 sample |
| **预计完成** | 剩 10 steps × 7min ≈ **~70min** (约 11:35) | 剩 1069 samples × ~2.5s ≈ **~45min** (约 11:10) |

**磁盘**: `/root/autodl-tmp/` 250GB 用了 152GB (61%), 余 99GB，充足。

**训练趋势**: reward 从 step 10 的 0.015 涨到 step 20 的 0.039，kl 仍然很低 (0.001)，clipped_ratio 从 0.956 升到 0.981（几乎全部被截断到 max_length=1024）。模型还没学会生成有效的短回答。

---
