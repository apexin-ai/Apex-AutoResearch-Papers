# ops cqa1 filename fix and gpu check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-filename-fix-and-gpu-check_20260521T084406_result.json`
- **Structured JSON:** [`c04318618f1a4f789dc4.json`](../../sessions/c0/c04318618f1a4f789dc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现了一个命名错误问题。完成汇总。

---

## 报告

### 1. GPU 状态

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 (RTX PRO 6000, 97GB) | 16.1 GB | 69% | **eval l2norm k=0.3 seed42** (PID 193983) |
| 1 (RTX PRO 6000, 97GB) | 42.2 GB | 0% | **train smart_compress_m32** (PID 921279) |

**注意**: 服务器只有 **2 个 GPU**，不是任务描述的 4 个。无空闲 GPU。

### 2. 当前运行实验进度

**L2norm k=0.3 seed42** (GPU 0): Task 2/10, Ep 30/50 → 约 **16% 完成** (80/500 episodes)
- Task 1 SR: 42.0% (21/50)
- Task 2 暂时: 0/30
- 速率 ~1.6-1.7 eps/min，预估还需 ~4 小时

**Smart Compress m32 训练** (GPU 1): 持续训练中，wandb 监控中

### 3. 文件覆写风险评估

**当前运行无覆写风险**: 不存在 `openvla_l2norm_prune_k03_object.json`。

**但有一个历史命名错误**:
- `openvla_l2norm_prune_k0_7_seed43_object.json` 内容实际是 **baseline** (mode=baseline, SR=74.0%, seed=43)，文件名误标为 l2norm

**已有 l2norm k=0.7 结果**（通过 --output 手动命名，无覆写）:
- seed42: `openvla_l2norm_prune_k0_7_object.json` → SR=49.8%
- seed43: `openvla_l2norm_k07_seed43_v2.json` → SR=49.8%

### 4. 脚本修改

修复了 2 个脚本:

**`eval_openvla_l2norm_libero.py`** (3 处改动):
- 输出文件名从 `openvla_{mode}_k{ratio}_{suite}.json` → `openvla_{mode}_k{ratio}_{suite}_seed{seed}.json`
- 修复 `k_ratio` 字段：l2norm_prune 模式下也保存 k_ratio（之前只保存 random_prune）

**`eval_openvla_libero.py`** (同样修复输出文件名添加 seed)

### 5. 待办

- 当前 l2norm k=0.3 seed42 使用旧代码运行，完成后输出为旧文件名 `openvla_l2norm_prune_k03_object.json`，需手动重命名为 `openvla_l2norm_prune_k03_object_seed42.json`
- `openvla_l2norm_prune_k0_7_seed43_object.json` 内容是 baseline 不是 l2norm，建议重命名为 `openvla_baseline_object_seed43.json` 以免混淆

---
