# ops verify gpu distribution

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gpu-distribution_20260521T200407_result.json`
- **Structured JSON:** [`ba7a481b7baa9794d970.json`](../../sessions/ba/ba7a481b7baa9794d970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-38929 fixed and syntax verified. Here's the full report:

---

## 汇报：三台服务器 GPU 分布 + Bug 修复状态

### westd-41074 (4× RTX PRO 6000 Blackwell 96GB)

| GPU | PID | 进程 | 显存 | GPU-Util |
|-----|-----|------|------|----------|
| 0 | 625853 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --fixed_mask --suite libero_object` | 9.7GB | 0% |
| 1 | 626639 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_object` | 9.7GB | 0% |
| 2 | 68539 | VTC 训练 | 28.5GB | 96% |
| 3 | 59671 | VTC 训练 | 27.5GB | 0% |

- **Bug 状态**: 已修复，`CUDA_VISIBLE_DEVICES` 覆盖行已删除
- **GPU 分配**: 正确 — k=0.9 fixed-mask 在 GPU0，k=0.85 在 GPU1，分布到不同 GPU
- 注意：只看到 2 个 eval 进程（k=0.9 和 k=0.85），没有 k=0.95（可能已完成）

### westd-38929 (4× RTX PRO 6000 Blackwell 96GB)

| GPU | PID | 进程 | 显存 | GPU-Util |
|-----|-----|------|------|----------|
| 0 | 590353 | `eval_pi05_pruning_libero.py --prune_mode none --suite libero_spatial` | 10.6GB | 7% |
| 1 | 590432 | `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_spatial` | 10.5GB | 34% |
| 2 | 590681 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.5 --suite libero_spatial` | 10.5GB | 40% |
| 3 | 590825 | `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_spatial` | 10.5GB | 12% |

- **Bug 状态**: 刚修复 — line 79 的 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)` 已删除，语法验证通过
- **GPU 分配**: 碰巧正确 — 4 个 Spatial 实验的 `--gpu` 参数恰好分别是 0/1/2/3，所以覆盖后仍在各自 GPU 上。但已修复以防未来出错
- 当前运行的进程不受影响（进程启动时已读入旧代码）

### westd-27271 (2× RTX PRO 6000 Blackwell 96GB)

| GPU | PID | 进程 | 显存 | GPU-Util |
|-----|-----|------|------|----------|
| 0 | 306599 | `eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.9 --suite libero_object` | 16.0GB | 74% |
| 1 | 921279 | `train_openvla_smart_compress.py --config openvla_smart_compress_m32.yaml --resume` | 42.2GB | 0% |

- **GPU 分配**: 正确 — OpenVLA L2norm k=0.9 在 GPU0，VTC M32 训练在 GPU1

### 修复动作总结

| 服务器 | 动作 |
|--------|------|
| westd-41074 | 无需操作，之前已修复 |
| westd-38929 | 已删除 line 79 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)`，语法验证通过 |
| westd-27271 | 无需操作（用的是不同脚本 `eval_openvla_l2norm_libero.py`） |

---
