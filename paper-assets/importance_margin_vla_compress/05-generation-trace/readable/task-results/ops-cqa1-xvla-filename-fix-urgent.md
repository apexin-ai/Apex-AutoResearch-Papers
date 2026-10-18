# ops cqa1 xvla filename fix urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-xvla-filename-fix-urgent_20260521T090310_result.json`
- **Structured JSON:** [`ec72f166dce6718a3d00.json`](../../sessions/ec/ec72f166dce6718a3d00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 产出

### 1. 备份文件
4 个风险文件已备份（`_backup_20260521_170516` 后缀）：
- `xvla_prune_k0.3_libero_object.json` (random seed42)
- `xvla_prune_k0.5_libero_object.json` (random seed43)
- `xvla_prune_k0.7_libero_object.json` (random seed43，已覆写了 l2norm)
- `xvla_prune_k0.5_libero_spatial.json`

### 2. 各实验输出路径
所有 4 个进程都**未传 `--output`**，使用默认路径（旧格式）：
- GPU 0: `eval_xvla_random_k07_seed43_v2` → **已完成**，写入 `xvla_prune_k0.7_libero_object.json`
- GPU 1: `eval_xvla_l2norm_k05_seed42` → 将写入 `xvla_prune_k0.5_libero_object.json`
- GPU 2: `eval_xvla_l2norm_k03_seed42` → 将写入 `xvla_prune_k0.3_libero_object.json`
- GPU 3: `eval_xvla_random_k05_seed44` → 将写入 `xvla_prune_k0.5_libero_object.json` ← **与 GPU 1 冲突！**

### 3. 脚本修改
第 302-303 行，默认文件名从：
```
xvla_prune_k{keep_ratio}_{suite}.json
```
改为：
```
xvla_{mode}_k{keep_ratio}_{suite}_seed{seed}.json
```
**注意**：修改不影响已运行进程（它们在启动时已加载旧代码）。

### 4. 已覆写数据恢复
- `xvla_prune_k0.7_libero_object.json` 被 random k=0.7 seed43 覆写了 l2norm k=0.7 seed42 的结果
- 从日志恢复，写入 `xvla_l2_norm_k0.7_libero_object_seed42.json`（l2norm, SR=58.2%, 291/500）
- 同时将现有 random 数据复制到正确命名文件：`xvla_random_k{ratio}_*_seed{seed}_v2.json`

### 5. GPU 状态与进度
| GPU | 显存 | 利用率 | 实验 | 进度 |
|-----|------|--------|------|------|
| 0 | 1 MiB | 0% | **已完成** (random k=0.7 seed43) | done |
| 1 | 4537 MiB | 9% | l2norm k=0.5 seed42 | Task 9, ep ~11/50 |
| 2 | 4537 MiB | 75% | l2norm k=0.3 seed42 | Task 约5-6, ep ~23/50 |
| 3 | 4537 MiB | 1% | random k=0.5 seed44 | Task 8, ep ~11/50 |

### 6. 剩余覆写风险
**GPU 1 和 GPU 3 仍会写同一文件** `xvla_prune_k0.5_libero_object.json`。先完成的会被后完成的覆写。两者进度接近（都在 Task 8-9），需要在第一个完成后立即备份，或等两个都完成后从日志重建。当前备份已保护了原始 random seed43 数据。

---
