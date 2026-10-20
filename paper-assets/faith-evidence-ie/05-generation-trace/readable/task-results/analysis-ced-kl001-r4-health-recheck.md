# analysis ced kl001 r4 health recheck

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ced-kl001-r4-health-recheck_20260514T163407_result.json`
- **Structured JSON:** [`5f7fc096f86d582ae146.json`](../../sessions/5f/5f7fc096f86d582ae146.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp2_grpo_ced_kl001_r4 — Step 45/100, 健康

**进程**: PID 68084 存活，运行 1h02m

### 关键指标（最近 4 个 step）

| 指标 | step ~42 | step ~43 | step ~44 | step 45 | 判断 |
|------|----------|----------|----------|---------|------|
| **kl** | 0.181 | 0.115 | 0.125 | **0.098** | 远低于 5，完全健康 |
| **grad_norm** | — | 0.357 | 0.242 | **0.158** | 策略稳定更新 |
| **f1_reward** | 0.028 | 0.089 | 0.082 | **0.240** | 稳步上升 |
| **ced_reward** | 0.015 | 0.058 | 0.120 | **0.236** | 与 f1 同步上升，无 hacking |
| **format_reward** | 0.296 | 0.300 | 0.293 | **0.220** | 略降（长输出格式变难） |
| **reward** | 0.339 | 0.447 | 0.494 | **0.695** | 总 reward 翻倍 |
| **reward_std** | 0.186 | 0.280 | 0.370 | **0.617** | 生成多样性大幅提升 |
| **frac_zero_std** | 0.7 | 0.6 | 0.4 | **0.0** | 所有 batch 都有方差，GRPO advantage 全部有效 |

### 核心判断

- **KL 稳定**: 0.1 量级，kl_coef=0.01 完美控制住了（对比 kl_coef=0.05 在 step 5 爆到 10^8）
- **无 reward hacking**: f1=0.240, ced=0.236 几乎同步，说明 CED 信号和 F1 一致
- **frac_zero_std 从 0.7→0.0**: 模型已完全摆脱 mode collapse，每个 batch 都有多样性
- **completions 变长**: 176→583 tokens，clipped_ratio=0.2 开始出现截断
- **step_time**: 37s→105s（因输出变长），预计还需 ~1.5h 完成

### 其他任务

- **sft_eval_r3** (PID 62352): 存活，运行 1h41m

### GPU 状态

| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| 0 | 13649 MiB | 63% | GRPO 训练 |
| 1 | 10303 MiB | 70% | sft_eval_r3 |
| 2 | 0 MiB | 0% | 空闲 |
| 3 | 15087 MiB | 57% | GRPO generation/NLI |

**结论**: 实验非常健康，所有指标趋势正确。建议不干预，等跑完 100 step。

---
