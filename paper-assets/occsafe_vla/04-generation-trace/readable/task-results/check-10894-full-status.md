# check 10894 full status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_10894_full_status_20260525T172443_result.json`
- **Structured JSON:** [`24a7d6b5b344b75752c8.json`](../../sessions/24/24a7d6b5b344b75752c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 状态报告

**系统**: uptime 161 天，未重启。4 张 GPU 全部闲置（0 MiB / 0% / 29-30°C）。

**所有 4 个进程均已死亡**，日志无错误信息直接截断——疑似被 SIGKILL（OOM killer 或集群资源管理器）。

| 实验 | GPU | PID 存活 | 最后 step | 最新 checkpoint | v2 确认 | 状态 |
|------|-----|---------|----------|----------------|---------|------|
| ablation_occ_detach_s3 | 3 | ✗ (257041) | 20376/50005 (41%) | 20000_chkpt | ✓ (204 [AUX]) | **崩溃** |
| mvp_occ_s3 | 1 | ✗ (256611) | 20423/50005 (41%) | 20000_chkpt | ✓ (205 [AUX]) | **崩溃** |
| full_occ_ln_s3 | 2 | ✗ (256695) | 20398/50005 (41%) | 20000_chkpt | ✓ (204 [AUX]) | **崩溃** |
| cutoff_45k_s2 | 0 | ✗ (74225) | 26480/50005 (53%) | 20000_chkpt | ✓ (265 [AUX]) | **崩溃** |

**关键发现**:

1. **3 个 s3 实验几乎同时死亡** — 均在 step ~20400 附近、运行 ~5h52m 时停止，cutoff_45k_s2 运行了 ~7h28m 停在 step 26480。4 个实验同时死亡指向同一外部事件。

2. **训练指标正常** — 崩溃前 loss 无异常：
   - ablation_occ_detach: occ=0.0117, action=0.0825 (step 20300)
   - mvp_occ: occ=0.0127, action=0.1206 (step 20400)
   - cutoff_45k: occ=0.0122, action=0.0874 (step 26400)

3. **进度损失** — 所有实验最新 checkpoint 只到 20000。cutoff_45k_s2 损失 6480 步（~1.7h），其余 3 个损失 ~400 步（~6min）。

4. **恢复方案** — 4 个实验都可从 20000_chkpt `--resume` 恢复（但注意 C002 约束：cutoff_45k_s2 **不能用 --resume**，需从 pretrained 重新训练）。

---
