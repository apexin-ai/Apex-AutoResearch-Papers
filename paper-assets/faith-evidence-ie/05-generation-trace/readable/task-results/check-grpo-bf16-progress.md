# check grpo bf16 progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_grpo_bf16_progress_20260518T140357_result.json`
- **Structured JSON:** [`a39af7cfafadce2e1f2f.json`](../../sessions/a3/a39af7cfafadce2e1f2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练状态已收集完整。以下是 GRPO bf16 G=4 训练进度报告：

## 训练进度

| 指标 | 值 |
|------|------|
| **当前 step** | ~37/200（进度条显示，checkpoint 只到 20） |
| **已运行时间** | 1h19m（PID 542126 on cuda:2） |
| **平均 step 耗时** | ~125s/step |
| **预估剩余** | ~5.5-6h（进度条估计 6:21） |
| **预估完成时间** | ~今晚 03:30-04:00（北京时间） |

## Step 100 checkpoint 预估可用时间

当前 step ~37，还需 ~63 steps × ~125s/step ≈ **2h11m**，约 **今晚 00:15** 可用。

## Reward 趋势（每 5 steps 记录，来自 trainer_state）

| Step | Loss | Total Reward | F1 Reward | CED Reward | Format Reward | Completion Len |
|------|------|-------------|-----------|------------|---------------|----------------|
| 5 | -0.053 | 1.375 | 0.949 | 0.164 | 0.262 | 471 |
| 10 | 0.289 | 1.467 | 1.065 | 0.139 | 0.263 | 543 |
| 15 | 0.101 | 1.558 | 1.089 | 0.190 | 0.279 | 384 |
| 20 | 0.329 | 1.601 | 1.123 | 0.197 | 0.280 | 472 |

## 关键观察

1. **Total reward 稳步上升**：1.375 → 1.601（+16.4%），训练在学习
2. **F1 reward 上涨**：0.949 → 1.123，抽取质量在改善
3. **CED reward 波动但趋升**：0.164 → 0.197，忠实度有提升但增幅小（tau 从 0.30 逐步升至 0.50 增加难度）
4. **Format reward 稳定**：~0.26-0.28，格式已基本学会
5. **clip_ratio 全零**：KL=0.0 设置下 PPO clip 未触发，正常
6. **frac_reward_zero_std**：step 15 有 5% 出现 zero-std（所有 generation 获得相同 reward），其余为 0

## GPU 状态

- cuda:2: 16.6GB/32.6GB（训练中，41% 利用率）
- cuda:3: 18.4GB/32.6GB（被其他进程占用，0% 利用率）
- cuda:0, cuda:1: 空闲

---
