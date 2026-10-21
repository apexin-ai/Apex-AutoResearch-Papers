# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260514T020734_result.json`
- **Structured JSON:** [`d973214d253387cdce45.json`](../../sessions/d9/d973214d253387cdce45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### PID 存活状态：全部 ALIVE

| exp_id | GPU | PID | 运行时间 | 当前进度 |
|--------|-----|-----|---------|---------|
| exp_001_sft_d100_15B_v2 | cuda:0 | 251924 | 59min | SFT training: step 1098/4159 (**26%**), loss~1.30, ETA ~2h45m |
| exp_001_eval_3B_d000_s42 | cuda:1 | 249294 | 1h14m | GSM8K: 490/1319 (**37%**), ETA ~1h54m |
| exp_001_eval_05B_d100 | cuda:2 | 256503 | 35min | GSM8K: 274/1319 (**21%**), ETA ~1h47m |
| exp_001_eval_3B_d000_s123 | cuda:3 | 242581 | 1h49m | GSM8K: 781/1319 (**59%**), ETA ~1h15m |
| exp_001_eval_15B_d000_s42_v2 | cuda:4 | 243290 | 1h44m | GSM8K: 957/1319 (**73%**), ETA ~41m |
| exp_001_eval_15B_d000_s123 | cuda:5 | 250600 | 1h09m | GSM8K: 610/1319 (**46%**), ETA ~1h23m |

所有 eval 已完成 MMLU，当前均在跑 GSM8K（之后还有 arc_challenge、humaneval）。

### GPU 利用率

| GPU | 利用率 | 显存占用 | 温度 |
|-----|-------|---------|------|
| 0 | 95% | 13716/24564 MiB | 41°C |
| 1 | 100% | 12620/24564 MiB | 50°C |
| 2 | 99% | 10993/24564 MiB | 50°C |
| 3 | 60% | 8957/24564 MiB | 52°C |
| 4 | 99% | 9492/24564 MiB | 54°C |
| 5 | 46% | 5829/24564 MiB | 46°C |

### 已完成的 eval 结果

仅 **Qwen2.5-0.5B_d000_s123** 有 eval_results.json：
- MMLU: **41.82%** (5873/14042)
- HumanEval 结果也在内

其余 eval 目录均为空（正在运行中）。

### 空闲 GPU
**无**——6 块 GPU 全部在用。

### 异常发现

1. **GPU 争用**：发现 2 个未跟踪的 0.5B_d000_s42 eval 进程：
   - PID 257034 在 cuda:2（与 exp_001_eval_05B_d100 共享）
   - PID 257853 在 cuda:0（与 SFT 训练共享）
   
   这两个额外进程可能拖慢 cuda:0 的 SFT 训练和 cuda:2 的 eval。

2. **HF 连接超时**：exp_001_eval_05B_d100 启动时遇到 HuggingFace GSM8K 数据集下载超时（重试 5 次），已恢复。

3. **GPU 3/5 利用率偏低**（60%/46%）：3B 和 1.5B 模型做 generation 时计算与访存交替，属正常现象。

4. **bitsandbytes 警告**：所有 eval 进程有 `libnvJitLink.so.13` 加载失败，不影响运行。

---
