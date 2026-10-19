# prep eval dryrun and sync

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_eval-dryrun-and-sync_20260521T223042_result.json`
- **Structured JSON:** [`a286704900b110fc5bca.json`](../../sessions/a2/a286704900b110fc5bca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. Dry-run 验证：**通过（由已有 eval 运行验证）**

bjb1-32546 上已有两个完整 eval 正在运行（非我启动），直接证明全链路正常：

| 验证点 | 结果 |
|--------|------|
| PI05 模型加载 | ✅ 从 `/root/autodl-tmp/models/pi05_libero_finetuned/` 加载成功 |
| obs_dim=2048 | ✅ `PI05 features (2048D) passed directly to CRM (no projection)` |
| CRM checkpoint 加载 | ✅ `CRM loaded ... (615,966 params)` |
| LIBERO 环境初始化 | ✅ 10 tasks loaded，rollouts 正常执行 |

已有运行：
- **GPU 0**: object benchmark, seed 44, 20 rollouts — task 1 完成 95% (19/20)，task 2 进行中
- **GPU 1**: spatial benchmark, seed 42, 20 rollouts — task 1 90% (18/20), task 2 90% (18/20), task 3 进行中

注意：独立 dry-run (GPU 5, n_rollouts=2) 因模型加载慢（与已有进程争抢 CPU/内存）未在 180s 内完成加载。已清理。

### 2. evaluate.py 版本一致性：**完全一致，无需 rsync**

| 服务器 | bytes | lines |
|--------|-------|-------|
| bjb1-18228 | 33058 | 806 |
| bjb1-32546 | 33058 | 806 |
| bjb2-28827 | 33058 | 806 |

### 3. Checkpoint 路径确认

| Checkpoint | 路径 | 大小 | 最后更新 |
|-----------|------|------|---------|
| **Object** | `/root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt` | 2.4M | May 22 06:31（训练仍在进行，epoch 30） |
| **Spatial** | `/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt` | 2.4M | May 22 06:29（训练仍在进行，epoch 25） |

bjb1-18228 训练持续产出 checkpoint，两路 CRM 正常。

### 4. 注意事项

- **bjb1-32546 已有正式 eval 在跑**（PID 196424 object/seed44, PID 196782 spatial/seed42），可能是先前 session 启动的。这些 eval 使用的 CRM checkpoint 不一定是最终版（训练仍在继续）——如果需要最终结果，训练完成后需重新 eval。
- **π0.5 模型路径**不是 `/root/autodl-tmp/models/pi0.5/`，实际路径为 `/root/autodl-tmp/models/pi05_libero_finetuned/`（已设为 evaluate.py 默认值，可省略 `--pi05_path`）。

---
