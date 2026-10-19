# ssh check 28034 after reboot

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-28034-after-reboot_20260522T121827_result.json`
- **Structured JSON:** [`377d995d79e981a8d723.json`](../../sessions/37/377d995d79e981a8d723.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-28034 重启后环境检查报告

### 1. 连通性
✅ **正常** — SSH 连接成功，服务器已启动约 6 分钟（从进程启动时间 20:13 推断）

### 2. GPU 状态
✅ **正常** — 4× RTX 5090 (32GB each)，利用率 0%，显存空闲

| GPU | 型号 | 利用率 | 显存使用 |
|-----|------|--------|----------|
| 0 | RTX 5090 | 0% | 2/32607 MiB |
| 1 | RTX 5090 | 0% | 2/32607 MiB |
| 2 | RTX 5090 | 0% | 2/32607 MiB |
| 3 | RTX 5090 | 0% | 2/32607 MiB |

### 3. Python/conda 环境
✅ **正常** — `/root/miniconda3/bin/python` Python 3.12.3 可用（需 conda activate，裸 `python3` 不在 PATH）。从正在运行的进程看，torch/transformers 可正常 import。

### 4. 项目代码目录
✅ **正常** — `/root/contrastive_entrain_calib/` 完整，`eval/eval_unified_preset.py` 存在 (10837 bytes)

### 5. Eval 结果完整性
⚠️ **eval_results 目录为空壳** — 两个结果目录存在但内部无任何文件：
- `exp-003-s2-ckpt7500/` — 空目录（0 files）
- `exp-004-s2-ckpt2000/` — 空目录（0 files）
- 注意：任务提到的 `exp-004-s2-ckpt2500-v2/` 不存在，实际是 `exp-004-s2-ckpt2000`

**结论：重启前正在运行的 eval 结果已丢失，需要重新跑。**

### 6. Checkpoint 文件
✅ **完好**
- `checkpoints_r3only_s2/checkpoint-7500` — 完整（adapter_model.safetensors 245MB + optimizer.pt 491MB + tokenizer）
- `checkpoints_act_s2/checkpoint-2000` — 完整（adapter_model.safetensors 698MB + tokenizer，无 optimizer）

### 7. 进程状态
⚠️ **有活跃进程** — `analysis/bootstrap_auroc_ci.py` 正在运行（PID 1656，CPU 114%），似乎是重启后被自动启动或手动提交的。无 tmux session，无 eval 进程。

### 8. 磁盘空间
✅ **正常**
- 根分区：30G 用了 8G（27%）
- 数据盘 `/root/autodl-tmp`：350G 用了 100G（29%）

---

### 总结

| 项目 | 状态 |
|------|------|
| 能否立即提交新 eval | ✅ 可以（GPU 空闲，环境完好） |
| eval 结果丢失 | ⚠️ 是 — `exp-003-s2-ckpt7500` 和 `exp-004-s2-ckpt2000` 结果为空，需重跑 |
| checkpoint 完好 | ✅ 两个 checkpoint 文件完整 |

---
