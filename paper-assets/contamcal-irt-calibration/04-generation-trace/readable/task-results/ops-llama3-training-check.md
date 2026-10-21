# ops llama3 training check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-training-check_20260521T110629_result.json`
- **Structured JSON:** [`31fdeb2c2703b6441448.json`](../../sessions/31/31fdeb2c2703b6441448.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇报

### 3 个进程全部存活，无异常

| 任务 | GPU | PID | 进度 | Epoch | Loss | 速度 | 预计剩余 |
|------|-----|-----|------|-------|------|------|----------|
| **d000_s0** | cuda:1 | 508651 | 1563/3125 (50%) | 0.50 | ~1.32 | ~2.5s/it | **~65 min** |
| **d025_s0** | cuda:0 | 509578 | 1426/3384 (42%) | ~0.27 | ~1.38 | ~2.5s/it | **~82 min** |
| **d100_s0** | cuda:3 | 510203 | 1224/4159 (29%) | ~0.22 | ~1.43 | ~2.8s/it | **~137 min** |

**预计完成时间（UTC+8）：**
- d000_s0: ~19:15
- d025_s0: ~19:35
- d100_s0: ~20:30

### GPU 利用率

| GPU | 利用率 | 显存占用 | 任务 |
|-----|--------|----------|------|
| 0 | 98% | 50981/97887 MiB | d025_s0 |
| 1 | 78% | 44479/97887 MiB | d000_s0 |
| 2 | 0% | 0 MiB | **空闲** |
| 3 | 75% | 37911/97887 MiB | d100_s0 |

### Loss 曲线

- d000: 2.25 → 1.32，收敛正常，warmup 后稳定下降
- d025: 类似轨迹，当前 ~1.38，正常
- d100: 当前 ~1.43，略高于 d000/d025——符合预期（d100 含更多 contaminated 数据，entropy 更高）
- 无 OOM、loss spike 或进程死亡

### Eval 脚本

已创建 `scripts/eval_llama3_s0.sh`，包含：
- 3 个 dosage (d000/d025/d100) × 2 个 benchmark (MMLU 5-shot + ARC 25-shot) = **6 个 eval**
- 使用 GPU 2（当前空闲）
- 包含 C004/C006/C009 合规检查（CUDA_VISIBLE_DEVICES 显式设置、lora_alpha=32 校验、evaluate.py md5 校验）
- 输出到 `results/mmlu_eval/llama3/` 和 `results/arc_eval/llama3/`（与现有目录结构一致）
- 基模型路径: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B`

**训练最早完成 ~19:15（d000），最晚 ~20:30（d100）。d000 完成后即可开始跑 eval，无需等全部结束。**

---
