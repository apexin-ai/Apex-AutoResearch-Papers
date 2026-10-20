# ops check both experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_both_experiments_20260517T202954_result.json`
- **Structured JSON:** [`ecbe2122fe8508c8c311.json`](../../sessions/ec/ecbe2122fe8508c8c311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. DeepSeek head-2048：**已完成** ✓

- **进程状态**：dead（已结束）
- **结束时间**：Mon May 18 04:18:46 CST 2026
- **正常结束**：是，训练 + 评估全部完成
- **Final checkpoint**：`/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_head2048_seed42/final/`
- **Checkpoints 列表**：checkpoint-148, checkpoint-296, checkpoint-444, final
- **评估结果**：
  - Accuracy: **78.7%** (95% CI: [76.5%, 81.0%])
  - Majority baseline: 71.5%
  - Lift: +7.2pp
  - pass: P=0.84 R=0.86 F1=0.85
  - fail: P=0.63 R=0.60 F1=0.62
- **产出文件**：`predictions.jsonl`, `eval_results.json` 在 final/ 下

### 2. Qwen-1.5B tail-256：**训练中** ⏳

- **进程状态**：alive（PID 378373，GPU 1）
- **进度**：110/444 steps（约 **25%**）
- **速度**：~1.07 s/step
- **预估剩余**：(444-110) × 1.07 ≈ 357s ≈ **~6 分钟**完成训练部分
- **启动时间**：04:28，已跑约 2 分钟

### 3. GPU 使用情况

| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Black | 49175/97887 MiB | 0% | 28°C |
| 1 | RTX PRO 6000 Black | 51719/97887 MiB | 57% | 50°C |

GPU 0 有显存占用但利用率 0%（可能是之前 DeepSeek 进程留下的残留显存，或模型加载到了 GPU 0 但计算在 GPU 1）。Qwen 训练在 GPU 1 上活跃运行。

---
