# code seed123 full

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed123_full_20260513T090039_result.json`
- **Structured JSON:** [`190a1313531a76e99489.json`](../../sessions/19/190a1313531a76e99489.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

**1. seed123 external_only 当前进度**
- 完成 gen_0–gen_3（4/8 代），当前在 gen_4 step [3/5] Training student
- 启动时间：2026-05-13 15:32:17 CST

**2. 脚本路径**
- `/root/div_cal_verify/run_seed123_remaining.sh` ✓ 已创建，chmod +x
- 参数与 `run_ext_seed123.sh` 完全一致（seed=123, --self_iterate, --no_quality_filter, gpu_ids=0）
- output_dir 按已有 seed123 惯例：`results_phase2_seed123/uncurated` 和 `results_phase2_seed123/rgds`

**3. 是否可以立即启动**
- **不可以。** external_only 仍在 cuda:0 上运行（gen_4/8），需等其完成。

**4. 启动命令**（external_only 完成后）
```bash
nohup bash /root/div_cal_verify/run_seed123_remaining.sh 0 > /root/runs/div_cal_verify/phase2_seed123_remaining.log 2>&1 &
```

---
