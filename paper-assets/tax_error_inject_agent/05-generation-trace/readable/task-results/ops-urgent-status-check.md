# ops urgent status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260514T182731_result.json`
- **Structured JSON:** [`b3f1a828d85f7a342b29.json`](../../sessions/b3/b3f1a828d85f7a342b29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 eval sessions 已确认在等待训练完成。

## 最终状态汇总

### 训练状态（全部仍在运行）

| 实验 | GPU | 进度 | 剩余 | 已有 Checkpoints |
|------|-----|------|------|-------------------|
| v4-vanilla-seed0 | cuda:0 (PID 71959) | 1260/1635 (77%) | ~13 min | epoch 1 (ckpt-545), epoch 2 (ckpt-1090) |
| v4-taxei-seed0 | cuda:1 (PID 72151) | 1380/3387 (41%) | ~1h 5min | epoch 1 (ckpt-1129) |
| v4-random-seed0 | cuda:2 (PID 72488) | 1375/3387 (41%) | ~1h 5min | epoch 1 (ckpt-1129) |
| v4-vanilla-seed123 | cuda:3 (PID 77937) | 75/1635 (5%) | ~55 min | 无（OOM 后重启 v1） |
| v4-vanilla-seed7 | - | killed | - | 无 |

### Eval 自动化

已为每个实验创建 tmux session（`*-eval`），每个 session 会：
1. 轮询等待对应训练 PID 退出
2. 自动定位最终 checkpoint
3. 在同一 GPU 上运行 `eval/recovery.py --no_inject`
4. 输出到 `eval_results/v4_*_eval.json`，日志到 `/root/runs/tax_error_inject_agent/v4-*-eval.log`

### 预计时间线
- **~13 min**: v4-vanilla-seed0 训练完成 → eval 自动启动（~15-20 min eval）
- **~55 min**: v4-vanilla-seed123 训练完成 → eval 自动启动
- **~1h 5min**: v4-taxei-seed0 + v4-random-seed0 训练完成 → eval 自动启动

Registry 已更新 4 个 eval 条目（PREPARING）。训练完成后需再更新 training registry 为 DONE + 补充 checkpoint_path，eval registry 更新为 RUNNING → DONE。

---
