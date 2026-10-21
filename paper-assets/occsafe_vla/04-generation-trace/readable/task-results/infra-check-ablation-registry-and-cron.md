# infra check ablation registry and cron

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-ablation-registry-and-cron_20260521T070138_result.json`
- **Structured JSON:** [`2a58f23f1c553674700e.json`](../../sessions/2a/2a58f23f1c553674700e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Ablation 实验状态汇总

**4 个实验全部存活，4 GPU 满载运行。**

| 实验 | PID | GPU | 显存占用 | GPU利用率 | 进度 | Checkpoint |
|------|-----|-----|---------|----------|------|------------|
| `ablation_occ_detach_s0` | 494238 | GPU 0 | 63028 MiB / 97887 MiB | 97% | 从 step 2500 resume | ✅ 2500_chkpt |
| `ablation_random_occ_s0` | 494454 | GPU 1 | 62194 MiB / 97887 MiB | 99% | 从 step 2500 resume | ✅ 2500_chkpt |
| `ablation_occ_detach_s1` | 494797 | GPU 2 | 62194 MiB / 97887 MiB | 99% | 从头训练 (seed=43) | ❌ 尚未到 2500 步 |
| `ablation_random_occ_s1` | 495133 | GPU 3 | 62200 MiB / 97887 MiB | 97% | 从头训练 (seed=43) | ❌ 尚未到 2500 步 |

**进程命令行确认的关键参数：**
- s0 (seed=42): `--resume True --resume_step 2500`，从 2500 checkpoint 继续
- s1 (seed=43): 从 base model `openvla-7b` 开始，无 resume 标志
- 共同参数: `max_steps=50005`, `save_freq=2500`, `batch_size=8`, `lr=5e-4`, `lora_rank=32`, `use_occ_head=True`
- `occ_detach` 实验: `--occ_detach true`
- `random_occ` 实验: `--random_occ True --occ_detach false`

**磁盘:** 156G / 250G 已用，剩余 95G，充足。

**结论:** 4 个 ablation 实验均在正常运行。s0 实验领先（已过 2500 步），s1 实验启动较晚（12:23 启动），尚未产出首个 checkpoint，但 GPU 利用率正常说明训练在推进中。

---
