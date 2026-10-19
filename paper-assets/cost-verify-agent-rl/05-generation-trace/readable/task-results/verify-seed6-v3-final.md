# verify seed6 v3 final

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_seed6_v3_final_20260521T081631_result.json`
- **Structured JSON:** [`47847ef186263c145374.json`](../../sessions/47/47847ef186263c145374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| **0** | 76,248 / 97,887 MiB | 100% | Seed 5 rollout (37.6 + 38.6 GB) |
| **1** | 76,746 / 97,887 MiB | 100% | Seed 5 rollout (38.1 + 38.6 GB) |
| **2** | 4,731 / 97,887 MiB | 0% | Seed 6 `ray::WorkerDict` (4.7 GB) |
| **3** | 4,731 / 97,887 MiB | 0% | Seed 6 `ray::WorkerDict` (4.7 GB) |

### 配置确认

- **CUDA_VISIBLE_DEVICES**: `2,3` ✅ （config 和日志均确认）
- **save_freq**: `5` ✅

### 判断

- **GPU 隔离正确** ✅ — Seed 6 进程仅出现在 GPU 2,3，GPU 0,1 无任何 Seed 6 进程
- **Seed 5 未受影响** ✅ — GPU 0,1 显存 ~76GB、利用率 100%，与预期一致
- **模型尚未完全加载** ⚠️ — GPU 2,3 仅 ~4.7GB，远低于 30GB 阈值。日志显示刚完成 wandb 初始化和数据 tokenization（494 items），模型权重加载还没开始。这属于正常启动阶段，需要再等几分钟。

建议再等 2-3 分钟后复查 `nvidia-smi`，确认 GPU 2,3 显存升到 >30GB。

---
