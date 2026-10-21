# monitor r2 wandb check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_r2_wandb_check_20260514T112016_result.json`
- **Structured JSON:** [`c9d8fa25857f90b5333d.json`](../../sessions/c9/c9d8fa25857f90b5333d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。以下是分析报告：

---

## mvp2_grpo_ced_r2 训练进度报告

### 基本状态
- **当前 step**: 20 / 378（5%）
- **运行时间**: ~29 分钟，预计总时长 ~9.5 小时
- **W&B**: 未启用（服务器无 WANDB_API_KEY）
- **注意**: 第一次 r2 run 在 step 18 被 SIGKILL (exit 137)，当前是自动重启的孤儿进程继续跑，日志因 stdout 缓冲写入缓慢

### 关键指标趋势

| Step | format_reward | f1_reward | ced_reward | total_reward | mean_length | frac_zero_std |
|------|--------------|-----------|------------|-------------|-------------|---------------|
| 5    | 0.102        | **0.021** | 0.123      | 0.246       | 771         | 0.250         |
| 10   | 0.138        | **0.007** | 0.139      | 0.284       | 831         | 0.188         |
| 15   | 0.172        | **0.011** | 0.232      | 0.415       | 765         | 0.146         |
| 20   | 0.197        | **0.006** | 0.305      | 0.508       | 754         | 0.063         |

**对比 r1 同阶段:**

| Step | r1 format | r1 f1   | r1 ced  | r2 format | r2 f1   | r2 ced  |
|------|-----------|---------|---------|-----------|---------|---------|
| 5    | **0.554** | 0.008   | 0.085   | 0.102     | 0.021   | 0.123   |
| 10   | **0.886** | 0.012   | 0.048   | 0.138     | 0.007   | 0.139   |
| 15   | 0.853     | 0.043   | 0.427   | 0.172     | 0.011   | 0.232   |
| 20   | 0.834     | 0.028   | 0.469   | 0.197     | 0.006   | 0.305   |

### Mode Collapse 判定：**尚未 collapse，但有两个严重警告**

**正面信号：**
- format_reward 受控（0.20 vs r1 同期 0.83），format_reward_weight=0.3 生效
- 输出长度稳定（754-831），未缩短
- frac_reward_zero_std 从 0.25 降到 0.06，生成多样性在改善
- entropy 相对稳定（0.07-0.08），r1 同期已从 0.076 跌到 0.040

**严重警告 1 — KL/loss 数值爆炸：**
| Step | KL | Loss |
|------|------|------|
| 5    | 3.77×10⁹ | 2.87×10⁸ |
| 10   | **4.8** (正常) | **0.34** (正常) |
| 15   | 3.40×10¹¹ | 2.19×10¹⁰ |

KL 在正常值（4.8）和天文数字之间交替振荡。这是 DeepSpeed + QLoRA + GRPO 的数值稳定性问题，可能导致训练后期崩溃。

**严重警告 2 — F1 reward 持续下降趋零：**
- 0.021 → 0.007 → 0.011 → **0.006**
- CED reward 持续上升（0.12→0.30）但 F1 不涨，说明模型在学习"引用 NLI 友好的证据句"而**不提取正确的关系三元组**
- 这与 r1 是不同的 collapse 模式：r1 是 format hacking，r2 可能是 **CED reward hacking**（引对证据但抽错关系）

### 建议干预方案

1. **最紧急 — KL 数值爆炸**：检查 grpo_trainer.py 中 KL 计算是否有 log(0) 或 inf 溢出。考虑加 `torch.clamp` 或切换 KL 计算为 log-ratio 的 safe 版本
2. **F1 持续归零**：如果到 step 40 仍低于 0.01，考虑提早停止并提高 `f1_reward_weight`（当前 3.0 可能不够，试 5.0）或降 `ced_reward_weight`（当前 1.0 降到 0.5）
3. **孤儿进程风险**：当前训练进程的 shell wrapper 已被 kill，进程以孤儿状态运行，save_steps=20 的 checkpoint 可能不会被正确写入（output_dir 中只有 dry run 的旧 checkpoint）。建议到服务器上确认 checkpoint 保存是否正常工作

---
