# monitor phase1 r5 verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_phase1-r5-verify_20260513T205535_result.json`
- **Structured JSON:** [`2da36c345cf90321bbbf.json`](../../sessions/2d/2da36c345cf90321bbbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## R5 验证报告

### 1. 进程存活
两个进程均在运行，elapsed ~1h19m：
- PID 75890 (exec-only) → CUDA_VISIBLE_DEVICES=0
- PID 75968 (exec-sta) → CUDA_VISIBLE_DEVICES=1

### 2. GPU 隔离
正确隔离，各占一卡：
| GPU | PID | 显存占用 | GPU-Util |
|-----|-----|---------|----------|
| 0 (RTX PRO 6000) | 75895 | 78920MiB / 97887MiB | 85% |
| 1 (RTX PRO 6000) | 75973 | 78920MiB / 97887MiB | 88% |

### 3. 训练推进
两者均推进到 **step 12**。注意 reward_log.jsonl **未清空旧数据**（包含前几轮 run 的记录），文件总行数 107/112 行，其中 r5 数据在尾部。

### 4. ISR 连续值验证 — 关键改动生效

**exec-only**（对照组）— isr_mean 始终等于 prove_rate（二值 0/1 平均）：
| step | prove_rate | isr_mean | reward_mean |
|------|-----------|----------|-------------|
| 3 | 0.500 | 0.500 | 0.500 |
| 4 | 0.125 | 0.125 | 0.125 |

**exec-sta**（实验组）— isr_mean 出现连续值，与 prove_rate 解耦：
| step | prove_rate | isr_mean | reward_mean |
|------|-----------|----------|-------------|
| 3 | 0.500 | **0.1667** | **0.3333** |
| 4 | 0.125 | **0.0357** | **0.0804** |

isr_mean = 0.1667 (1/6)、0.0357 (1/28) 等连续值确认 **continuous ISR reward 已生效**，不再是 binary 0/1。

### 5. Step 速度对比

从 r5 区间（step 3→7）估算：
- exec-only: ~9 sec/step
- exec-sta: ~8.75 sec/step

**两者速度几乎一致**，原因：step 5-7 的 prove_rate=0（无 proved sample），不触发 STA ablation。在有 proved sample 的 step 3→4（prove_rate=0.5），两者也都是 ~15 sec，STA overhead 暂未明显体现。可能需要更多 high-prove-rate 的 step 才能看到差异。

### 6. 潜在问题
- **reward_log.jsonl 未隔离**：旧 run 数据仍在文件中，后续分析时需按 timestamp 过滤 r5 区间（r5 起始 timestamp ≈ 20:54 UTC）
- **prove_rate 偏低**：step 5-12 大量 prove_rate=0，如果持续如此，exec-sta 的 STA 信号会很稀疏，K=8 的增益不明显
- 无报错，训练正常推进

---
