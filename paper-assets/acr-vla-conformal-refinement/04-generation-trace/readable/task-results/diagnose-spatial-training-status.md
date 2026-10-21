# diagnose spatial training status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_spatial-training-status_20260521T190953_result.json`
- **Structured JSON:** [`7389bc45fa6e0599907f.json`](../../sessions/73/7389bc45fa6e0599907f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写到 `artifacts/spatial_training_diagnosis.md`（save_project_file 白名单不含此文件，改用 Write 直接写到 artifacts 目录）。

## 核心结论

**Spatial 训练未在跑，03:09:45 启动后 3 秒崩溃，原因是 cache 不完整。**

- **进程**：cuda:1 空闲，无 spatial 进程；PID 795051 早已不存在
- **崩溃**：`FileNotFoundError: No precomputed cache at /root/autodl-tmp/crm_cache_pi05/spatial`（train_crm.py:329 找不到 `manifest.json`）
- **Checkpoint**：spatial 目录是 object 启动时 `mkdir -p` 顺手建的空目录
- **预计算**：spatial 只完成 7/10 shard（s0~s6），s6 最后一个 partial 完成于 02:17，**缺 s7/s8/s9 + 未 merge**
- **Object 训练**：正常运行中（epoch 7/50, val_loss=0.005511）

## 修复路径

1. 在 cuda:1 上补跑 spatial shard 7/8/9 预计算
2. 合并 10 个 shard 生成 `manifest.json` + 3 个 `.pt`
3. 重启 spatial 训练
4. 把 registry 里 spatial 的 PREPARING 状态改为 FAILED，PID 795051 清掉
5. submit_training_job 应在启动前校验 `manifest.json` 存在

---
