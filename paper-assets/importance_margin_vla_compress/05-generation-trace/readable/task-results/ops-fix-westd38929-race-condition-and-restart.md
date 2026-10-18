# ops fix westd38929 race condition and restart

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-westd38929-race-condition-and-restart_20260520T232205_result.json`
- **Structured JSON:** [`fd71c41bd61b0c8fea34.json`](../../sessions/fd/fd71c41bd61b0c8fea34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 总结

### 根因分析

**不是竞争条件**，而是 LIBERO 在实验运行期间被从 site-packages 重装为 editable install（LIBERO-plus）。时间线：

| 时间 (UTC+8) | 事件 |
|---|---|
| 05:58 | 4 个实验启动（使用 site-packages 里的原版 LIBERO） |
| 07:15 | LIBERO-plus init_files 重建 |
| 07:17:22 | config.yaml 被更新（路径从 site-packages → LIBERO-plus） |
| ~07:17 | **3 个进程 crash**：旧 site-packages 目录已删除，init files 不存在 |
| 07:19:24 | `libero-plus.pth` 创建（editable install 完成） |

关键代码：`benchmark/__init__.py:164` — `torch.load(init_states_path)` 每个 episode 调用一次。

### 修复操作

1. **切换 .pth** 从 LIBERO-plus 回 LIBERO-master：`/root/miniconda3/lib/python3.12/site-packages/libero-plus.pth` → 指向 `/root/autodl-tmp/libero_repo/LIBERO-master`
2. **更新 config.yaml** 所有路径指向 LIBERO-master
3. **Patch torch.load** 兼容 PyTorch 2.6+：`torch.load(path)` → `torch.load(path, weights_only=False)`
   - 文件：`/root/autodl-tmp/libero_repo/LIBERO-master/libero/libero/benchmark/__init__.py:164`

### 重启实验

| GPU | 实验 | PID | tmux session | 状态 |
|---|---|---|---|---|
| 0 | random k=0.95 seed42 | 159683 | `eval_random_k095_s42_v2` | ✓ Ep 10/50, 9/10, 2.0 eps/min |
| 1 | random k=0.7 seed42 | 159765 | `eval_random_k07_s42_v2` | ✓ Ep 10/50, 4/10, 1.8 eps/min |
| 2 | random k=0.3 seed43 | 95670 | `eval_random_k03_s43` | ✓ 原进程，未中断 |
| 3 | L2 norm k=0.9 seed43 | 159944 | `eval_l2norm_k09_s43_v2` | ✓ Ep 10/50, 7/10, 2.0 eps/min |

**4/4 GPU 全部在用**，pruning 确认生效。

---
