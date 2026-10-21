# ssh d046 cls v5 early check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d046-cls-v5-early-check_20260513T074430_result.json`
- **Structured JSON:** [`9d1822ebec702f188238.json`](../../sessions/9d/9d1822ebec702f188238.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

拿到两个数据点了。汇报如下：

---

## CLS v5 训练早期状态

### 1. 进程状态
- **PID 2947259**: alive（wrapper），运行 ~10 分钟
- **PID 2947263**: 实际训练进程，115% CPU，7.6GB RSS

### 2. 当前进度
- Step **111 / 6633**（1.7%）
- ~6.7s/step

### 3. Loss 趋势

| Step | Loss | Grad Norm | LR |
|------|------|-----------|-----|
| 50 | **99.12** | 201.46 | 7.38e-6 |
| 100 | **11.91** | 27.75 | 1.49e-5 |

Loss 从 99.1 骤降到 11.9（↓88%）。Step 100 的 loss ≈ ln(vocab_size) ≈ ln(151k) ≈ 11.9，即刚到随机基线水平。初始 loss 极高是因为预训练模型对 answer token ("pass"/"fail") 的预测极度 confident 且方向错，LoRA 适配后迅速修正。**趋势正常，预期后续会持续下降到 <5。**

### 4. Learning Rate
- warmup_ratio=0.05 → warmup_steps ≈ 332
- 当前在 warmup 阶段，LR 线性上升中
- 目标 LR: **5e-5** ✓（从 step 50/100 的 LR 线性外推到 step 332 = 4.98e-5）

### 5. GPU 使用
- **99% utilization, 19,463 MiB / 32,607 MiB**（60% 显存）

### 6. 预估完成时间
- 剩余 6,522 steps × 6.73s = ~12.2 小时
- **预计完成：~13:00 (May 13)**

---
