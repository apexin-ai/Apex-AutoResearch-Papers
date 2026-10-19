# diagnose m2 qwen cuda0 status

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m2_qwen_cuda0_status_20260514T145916_result.json`
- **Structured JSON:** [`104653d0e37a35f1abc0.json`](../../sessions/10/104653d0e37a35f1abc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**m2_full_qwen 进度**: 2/9 runs（random_s42 已完成，random_s43 进行中）

**random_s43 当前状态**:
- cuda:0 上运行中，GPU 利用率 99%，VRAM 50.5/97.9 GB
- Epoch 1, step 900/1405（总进度 900/2810 ≈ 32%）
- Loss 从 0.68 降到 0.04-0.12 区间，收敛正常
- 最新 eval@500: val_loss=0.4476, R@1=0.5357, R@5=0.9699, R@10=1.0

**时间估算**: 剩余 ~86 小时（≈ 3.6 天），预计 5月18日 05:00 CST 全部完成

**磁盘**: 65G 剩余，充足

**注意**: 日志现在正常输出到 `/root/runs/m2_full_qwen/random_s43.log` 和 `s43plus_all.log`，之前 tee buffer 的问题已解决。

---
