# code cheetah cartpole dryrun

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cheetah-cartpole-dryrun_20260514T223555_result.json`
- **Structured JSON:** [`4c5c1cd23c4984cfe83f.json`](../../sessions/4c/4c5c1cd23c4984cfe83f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 验证结果

| 环境 | 配置 | 启动 | step 5000 | metrics.jsonl | 报错 |
|------|------|------|-----------|---------------|------|
| Cheetah Run | baseline | ✅ | ✅ | ✅ | 无 |
| Cheetah Run | treatment (gate+dt1+subsample+H15) | ✅ | ✅ | ✅ | 无 |
| Cartpole Swingup | baseline | ✅ | ✅ | ✅ | 无 |
| Cartpole Swingup | treatment (gate+dt1+subsample+H15) | ✅ | ✅ | ✅ | 无 |

**obs/action 维度确认：**
- Cheetah Run: obs 17D (position + velocity), act 6D ✅
- Cartpole Swingup: obs 5D (position + velocity), act 1D ✅

**Warning（均为非关键）：**
- Gym 废弃警告（建议迁移到 Gymnasium）— 不影响功能
- `torch.cuda.amp.GradScaler` 废弃 — 不影响功能（CPU 模式下不使用 AMP）
- Box bound precision cast 警告 — 正常

**其他观察：**
- 4 个 run 均在 CPU 上成功收集了 4 个 prefill episode（每个 500 步 = 2000 步），并进入训练循环到 step 5000
- 服务器上已有 GPU 实验在跑（exp_008e_v3_walker_s1 / exp_009a_baseline_walker_s2），dry-run 用 CPU 不冲突
- dryrun 目录已清理完毕

---
