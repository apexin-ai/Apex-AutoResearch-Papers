# ops diagnose e2 exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_e2_exit_20260518T134308_result.json`
- **Structured JSON:** [`c9d4f0f4b6b5a7f541e4.json`](../../sessions/c9/c9d4f0f4b6b5a7f541e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**退出原因**: 磁盘空间耗尽（`No space left on device`）。/root/autodl-tmp 619G 100% 满，在 step 120 保存 checkpoint 时崩溃。

**进度**: 仅从 step 100 跑到 step 120（目标 300），完成 20/200 步。

**最终 metrics（step 110）**:
- loss: 0.027（比原始 100 步的 0.06-0.12 显著降低）
- LR: 6.37e-7（linear scheduler 重置正常，LR 衰减问题已解决）
- reward/mean: 未记录

**LR 问题**: 已解决。扩展 run 使用了 linear scheduler 重新初始化，step 110 时 LR 为 6.37e-7，不再是接近 0。

**已处理**:
- Registry: conclusion=failed, status=DONE
- Cron: 已删除
- checkpoint-120（不完整，4.9G）: 已清理
- checkpoint-110（完整，27G）: 保留可用于 resume

**磁盘空间消耗 top**:
- grpo_stage2_standard_20_fair: 91G
- grpo_stage2_rasp_20_fair: 91G
- grpo_unpruned_v2: 46G
- grpo_cka_only_20: 38G

**重启建议**: 需要先在 westd-29022 上释放磁盘空间（清理不再需要的旧 checkpoint），然后可以从 checkpoint-110 resume 继续跑到 300 步。每个完整 checkpoint 约 27G，训练到 300 步（save_total_limit=3）需要至少 ~80G 空闲空间。

---
