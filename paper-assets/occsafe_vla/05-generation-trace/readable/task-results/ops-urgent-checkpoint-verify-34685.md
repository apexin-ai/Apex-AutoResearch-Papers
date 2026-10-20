# ops urgent checkpoint verify 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-checkpoint-verify-34685_20260528T061909_result.json`
- **Structured JSON:** [`152feaa9086d353b2760.json`](../../sessions/15/152feaa9086d353b2760.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint 状态汇总（当前 ~06:15 UTC）

| 实验 | GPU | PID | 最新 chkpt | 时间 (UTC) | 50000_chkpt | adapter_config | 预计 50000 到达 |
|------|-----|-----|-----------|-----------|-------------|----------------|---------------|
| **detach_ln_v2_s3** | cuda:3 | 56822 (R, 2h27m) | **45000** | ~05:15 | 未到 | ✅ lora_adapter/ | **~06:40 UTC** |
| **full_occ_ln_v2_s3** | cuda:2 | 56474 (S, 2h27m) | **45000** | ~05:15 | 未到 | ✅ lora_adapter/ | **~06:40 UTC** |
| **detach_ln_v2_s2** | cuda:0 | 47238 (R, 4h10m) | **40000** | ~06:16 | 未到 | ✅ lora_adapter/ | **~09:05 UTC** |

### 关键细节

- **所有 4 个训练 PID 存活**，GPU 占用正常（62-63 GiB）
- **轮询脚本**：3 个 poll_eval 日志均只有 "Polling started"（04:20 UTC），尚未触发 eval
- **detach_ln_v2_s2** 速度：每 5000 步 ~1h25m（30k→35k 1h20m, 35k→40k 1h25m），还需走 10000 步
- **detach_ln_v2_s3 / full_occ_ln_v2_s3**：每 5000 步 ~1h25m，再 ~25 分钟可达 50000
- **额外进程**：PID 62535 在跑 **full_occ_bn_v2_s2**（从 pretrained 开始，已跑 1h38m），占 cuda:1 / 62152 MiB

### DDL 风险评估

- detach_ln_v2_s3 / full_occ_ln_v2_s3：**06:40 UTC 左右完成训练 → 充裕**
- detach_ln_v2_s2：**~09:05 UTC 完成训练 → 有余量但偏紧**，eval 还需额外时间
- full_occ_bn_v2_s2（额外）：从 0 开始，按同速需 ~14h，**12:00 UTC DDL 内完不成 50000 步**

---
