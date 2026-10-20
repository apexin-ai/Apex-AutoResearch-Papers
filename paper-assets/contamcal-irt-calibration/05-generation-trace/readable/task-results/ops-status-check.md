# ops status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check_20260513T235522_result.json`
- **Structured JSON:** [`253f194311507fbdb92b.json`](../../sessions/25/253f194311507fbdb92b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验均 **ALIVE**。汇总如下：

## 实验状态

| exp_id | PID | 状态 | 进度 | ETA | 关键指标 | GPU |
|--------|-----|------|------|-----|---------|-----|
| exp_001_sft_0pct_3B_s123 | 216935 | ALIVE | 2882/3125 (92%) | ~17min | loss=1.12, tok_acc=0.75, ep=0.88 | cuda:3, 17.3G |
| exp_001_eval_15B_d000_s42 | 221376 | ALIVE | GSM8K 1231/1319 (93%) | ~10min | - | cuda:4, 5.8G |
| exp_001_eval_05B_d000_s42 | 229370 | ALIVE | GSM8K 615/1319 (47%) | ~1h05m | - | cuda:1, 3.7G |
| exp_001_eval_05B_d000_s123 | 229516 | ALIVE | GSM8K 589/1319 (45%) | ~1h08m | - | cuda:2, 3.7G |
| exp_001_sft_d100_05B | 235243 | ALIVE | 929/4159 (22%) | ~55min | loss=1.58, tok_acc=0.67, ep=0.19 | cuda:0, 22.0G |

## GPU 使用

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 21995/24564 MiB | 99% | exp_001_sft_d100_05B |
| 1 | 3667/24564 MiB | 33% | exp_001_eval_05B_d000_s42 |
| 2 | 3667/24564 MiB | 32% | exp_001_eval_05B_d000_s123 |
| 3 | 17327/24564 MiB | 28% | exp_001_sft_0pct_3B_s123 |
| 4 | 5829/24564 MiB | 47% | exp_001_eval_15B_d000_s42 |
| 5 | 0/24564 MiB | 0% | **空闲** |

## 备注

- 3B SFT 和 1.5B eval 即将完成（~10-17min），完成后 GPU 3 和 4 将释放
- 三个 eval 任务启动时都遇到 HuggingFace 连接超时（gsm8k 数据集），但均已自动恢复
- 1.5B eval 日志实际路径在 `/root/autodl-tmp/exp001/eval_results/eval_15B_d000_s42.log`
- **GPU 5 完全空闲**，可立即调度新任务

---
