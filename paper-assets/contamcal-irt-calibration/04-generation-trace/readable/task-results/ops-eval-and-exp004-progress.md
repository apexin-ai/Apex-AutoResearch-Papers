# ops eval and exp004 progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_and_exp004_progress_20260514T042501_result.json`
- **Structured JSON:** [`3c03d960369f1f1d8632.json`](../../sessions/3c/3c03d960369f1f1d8632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### 本地实验

| 实验 | PID | 状态 | 进度 | 预估剩余 |
|------|-----|------|------|----------|
| **exp-004 sim sweep** | 340553 | 运行中 | 2/12 conditions 完成，第3个 6/10 seeds | ~30-40h |
| **exp-005 noise prop v3** | 339838 | 运行中 | 1/25 完成，正在跑第2个 | ~18-20h |

- exp-004: 每个 condition 10 seeds，每个 seed (n=100) 的 Stan 拟合约 50-60min。当前在 `auc0.55_n100` 第7-8个 seed。results/ 目录有 4 个 JSON (含 summary)
- exp-005: 每个 condition 含 simple + ME 两次 Stan 拟合，每对约 40-50min。当前 σ_e=0.1 seed=43 的 ME 模型

### GPU 实验 (cqa1-21977)

| GPU | 利用率 | VRAM | 实验 | 进度 | 预估剩余 |
|-----|--------|------|------|------|----------|
| 0 | 11% | 10.1/24.6G | eval_3B_d000_s42 | GSM8K 1208/1319 (92%) | ~50min |
| 1 | 53% | 12.6/24.6G | eval_3B_d000_s123 | HumanEval 122/164 (74%) + GSM8K 待跑 | ~3.5h |
| 2 | 50% | 7.3/24.6G | eval_15B_d000_s123 | GSM8K 1132/1319 (86%) | ~55min |
| 3 | 16% | 13.5/24.6G | eval_05B_d005 + d000_s42_v5 | GSM8K ~53% (697-702/1319) | ~3h |
| 4 | 9% | 18.5/24.6G | sft_d100_15B_v2 | 2749/4159 (66%), epoch 0.57 | ~4.3h |
| 5 | 14% | 10.4/24.6G | sft_d005_15B | 621/3177 (20%), epoch 0.13 | ~7h |

### 异常检查

- **无异常**：所有进程存活，无 OOM，无卡住
- GPU 利用率偏低（eval 任务 9-16%）属正常——eval 主要是 forward pass 且有 I/O 等待
- SFT 训练 loss 正常下降：d100_15B_v2 loss ~1.27-1.35, d005_15B loss ~1.21-1.29
- eval_05B_d100_v5 日志显示训练输出而非 eval，可能是 SFT+eval 联合任务或命名不一致，需注意

### 完成时间线（预估）

1. **~13:15** eval_3B_d000_s42, eval_15B_d000_s123 完成
2. **~15:30** eval_05B 系列完成
3. **~16:00** eval_3B_d000_s123 完成
4. **~16:45** sft_d100_15B_v2 完成
5. **~19:30** sft_d005_15B 完成
6. **明天上午** exp-005 noise prop 完成
7. **明天晚间~后天** exp-004 sim sweep 完成

---
