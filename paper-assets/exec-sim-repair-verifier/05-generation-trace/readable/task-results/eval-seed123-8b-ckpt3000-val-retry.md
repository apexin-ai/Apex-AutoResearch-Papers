# eval seed123 8b ckpt3000 val retry

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed123-8b-ckpt3000-val-retry_20260514T204930_result.json`
- **Structured JSON:** [`8ac7c50ee1e5cbf9f3ed.json`](../../sessions/8a/8ac7c50ee1e5cbf9f3ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**无法立即提交 eval**，4 个 GPU 全部占用：

| GPU | 占用 | 进程 | 已运行 |
|-----|------|------|--------|
| cuda:0 | 19.3/31.8 GB, 79% | eval cls 8B ckpt-600 val (PID 285772) | ~10 min |
| cuda:1 | 13.3/31.8 GB, 100% | eval cls v5 ckpt-400 val (PID 281646) | ~29 min |
| cuda:2 | 30.0/31.8 GB, 97% | train CWM 8B seed42 (PID 266816) | 3h+ |
| cuda:3 | 30.1/31.8 GB, 98% | train CLS 8B seed123 续训 (PID 266449) | 3h+ |

**关键发现**：
- `checkpoints_repo_cls_seed123/checkpoint-3000` 是 **4B 模型**的（base_model = Qwen3-4B），不能用
- 正确路径：**`/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000`**（base_model = Qwen3-8B，已验证）

**预计最快空闲 GPU**：cuda:1（v5 4B eval 已跑 ~30 min，应较快完成）或 cuda:0（8B eval 较慢）

完整提交命令已写入产出 `cls8b_seed123_ckpt3000_val_eval_pending.md`，下次有空闲 GPU 直接用 `submit_training_job` 提交即可。

---
