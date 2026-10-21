# ops p0 gpu conflict fix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0_gpu_conflict_fix_20260525T195328_result.json`
- **Structured JSON:** [`7b366df1c9f40b5f8c21.json`](../../sessions/7b/7b366df1c9f40b5f8c21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval_best_s1 (PID 134344) 已在 GPU 2 上成功加载，8967MiB。

---

## 汇报

### 1. 各 GPU 进程状态

| GPU | PID | 进程 | 显存 | 状态 |
|-----|-----|------|------|------|
| 0 | 3717 | spatial_bowl 训练 | 27036MiB | ✅ 正常 |
| 0 | 123811 | eval_s1_l005_30k_disp_fix (`--gpu 0`) | 8997MiB | ⚠️ **冲突残留** |
| 1 | — | — | 1MiB | 空闲 |
| 2 | 134344 | eval_pi05_a1_best_s1_l005_16k | 8967MiB | ✅ 刚启动 |
| 3 | 75123 | eval_pi05_a1_best_s2_l005_10k | 8356MiB | ✅ 保留 |

### 2. 已 kill 进程

- PID 35423, 72605 — GPU 3 orphan 进程
- PID 121109 — eval_best_s1 误入 GPU 0

### 3. eval_best_s1 重启

✅ PID 134344，已在 cuda:2 上加载（8967MiB），tmux session `eval_pi05_a1_best_s1_l005_16k`。

### 4. cuda:1 displacement eval 状态

⚠️ **GPU 1 完全空闲**。tmux session `eval_pi05_a1_30k_s1_l005_disp` 存在，但实际进程 PID 123811 跑在 **GPU 0** 上（同样的 `--gpu 0` 覆盖 bug）。这个进程占了 GPU 0 约 9GB，仍在与 spatial_bowl 冲突。等待指示是否 kill 并在正确 GPU 上重启。

### 5. --gpu 参数实现方式

确认 root cause — `eval_safelibero.py` 第 1141 行：

```python
os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
```

脚本用 `--gpu` 参数值**直接覆盖** `CUDA_VISIBLE_DEVICES`。当外部设置 `CUDA_VISIBLE_DEVICES=2` 但 `--gpu 0` 时，脚本会把它改回 `"0"`，导致进程跑到物理 GPU 0 而非预期的 GPU 2。这是所有 GPU 错位 bug 的根因。

---
