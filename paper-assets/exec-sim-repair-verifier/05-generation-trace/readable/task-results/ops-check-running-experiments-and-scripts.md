# ops check running experiments and scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-experiments-and-scripts_20260515T215737_result.json`
- **Structured JSON:** [`caece096ff1a6999651a.json`](../../sessions/ca/caece096ff1a6999651a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 实验状态

| exp_id | GPU | PID | 状态 | GPU利用率 | 显存 | 进度 | 预计ETA (UTC) |
|--------|-----|-----|------|----------|------|------|--------------|
| cls8b-s42-resume-val-sweep-seq8192-v2 | cuda:0 | 398981 | **ALIVE** (4h15m) | 70% | 18.0/31.8 GB | ckpt-3600: 7170/9335 (77%), 已完成9个ckpt (1800-3400) | ~06:30 (如3800为末尾) |
| cls8b-s42-resume-val-sweep-gpu1 | cuda:1 | 405526 | **ALIVE** (3h10m) | 100% | 18.0/31.8 GB | ckpt-5400: 3690/9335 (40%), 已完成7个ckpt (4000-5200) | ~06:15 (如5400为末尾) |
| repo-level-cwm-8b-conda-v5 | cuda:2 | 400279 | **ALIVE** (4h06m) | 99% | 20.6/31.8 GB | step 5818/6633 (87.7%), ~13.5s/step, 最新ckpt=5800 | **~09:00** |
| cwm8b-ckpt400-test-eval | cuda:3 | 381618 | **ALIVE** (7h19m) | 88% | 22.0/31.8 GB | 4134/? samples done (index到4133), test split | ~15:00 (按9335总量估) |

**注意：** CLS val sweep 的 ETA 取决于 `checkpoints_repo_cls_8b_s42_resume/` 目录中剩余多少 checkpoint 未评。CWM test eval 总样本数未知，按 9335 估算则完成约 44%。

### Eval 脚本确认

| 脚本 | 状态 | 内容 |
|------|------|------|
| `/root/autodl-tmp/scripts/cwm8b_val_sweep.sh` | **存在** (1644 bytes, 可执行) | CWM 8B v5 val sweep，3 GPU 并行评 val split，输出到 `cwm_8b_val/step_{STEP}/` |
| `/root/autodl-tmp/scripts/cwm8b_final_test_eval.sh` | **存在** (3864 bytes, 可执行) | CWM 8B v5 最终 test eval，找最高 step checkpoint 评 test split，输出到 `cwm_8b_final_test/` |

两个脚本均已就位，CWM 训练完成后可直接启动。

---
