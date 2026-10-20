# fix full occ ln v2 s3 resume 40k

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_full_occ_ln_v2_s3_resume_40k_20260528T034326_result.json`
- **Structured JSON:** [`07d8e88864dea4004fd2.json`](../../sessions/07/07d8e88864dea4004fd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在运行。日志末尾确认进度条在推进（step 53，~1.06 it/s）。日志前半部分是之前失败尝试的残留输出。

**总结：**

| 项目 | 状态 |
|------|------|
| 40000_chkpt 完整性 | LoRA adapter + heads 完整；merged model 因 SIGHUP 缺失 |
| 修复方案 | 从 35000_chkpt 软链 merged model safetensors + 复制 config.json 到 40000_chkpt |
| base model index 修复 | `model.safetensors.index.json` 被其他进程污染（3→4 shards），已 sed 修复 |
| GPU | westd-34685 cuda:2，PID 56474，~62GB VRAM |
| 速度 | ~1.06 it/s |
| 实际训练步数 | 10005 步（log_step 40000→50005） |
| 预计完成时间 | ~2.6h → 约 14:30 UTC |

**注意事项：**
- backbone 权重来自 35k merged model（差 5k 步 LoRA），heads 完整在 40k
- `update_auto_map()` 会在 resume 时修改 vla_path 下的 config.json（会删除原文件再重写），这是之前 config.json 丢失的原因

---
