# fix d063 val 6144 verification

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d063-val-6144-verification_20260514T090648_result.json`
- **Structured JSON:** [`7b08b8ec2ee177a80392.json`](../../sessions/7b/7b08b8ec2ee177a80392.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6144 验证 tmux session 已启动，正在等待当前 2048 sweep 完成。

## 汇报

### 1. eval_repo_cls.py 修改
**无需修改**。脚本已支持 `--max_seq_length` 参数（L257, default=2048）。

### 2. 2048 val 结果（已确认排序反转）

| Checkpoint | val acc (2048) | val f1_macro (2048) | test acc | test f1_macro |
|---|---|---|---|---|
| ckpt-400 | **80.72%** | 67.03 | 75.05% | 67.47 |
| ckpt-600 | 76.78% | 66.81 | **80.73%** | **77.31** |

val 2048 排序: ckpt-400 > ckpt-600 — **与 test 排序相反**，确认截断导致 metrics 失真。

### 3. 6144 验证状态
- tmux session `val_6144` 已创建，排队等待 `val_sweep`（2048 sweep）完成
- 当前 sweep 还剩 ~6 个 checkpoint（v5/4000 在跑 + 5个待跑），预计 ~3.5h 后完成
- 6144 验证用 batch_size=4（防 OOM），预计每个 checkpoint ~50-60min
- **ETA**: 6144 验证预计约 5-6 小时后有结果（~08:00 PDT）

### 4. 监控命令
```bash
# 查看 6144 进度
tail -20 /home/sonny/exec-sim-repair-verifier/val_eval_results_6144/run.log

# 查看结果
cat /home/sonny/exec-sim-repair-verifier/val_eval_results_6144/seed123_ckpt400.json
cat /home/sonny/exec-sim-repair-verifier/val_eval_results_6144/seed123_ckpt600.json
```

---
