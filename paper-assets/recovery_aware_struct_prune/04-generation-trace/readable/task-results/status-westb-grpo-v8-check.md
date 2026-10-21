# status westb grpo v8 check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westb-grpo-v8-check_20260515T170406_result.json`
- **Structured JSON:** [`23fd81eb41357efe3484.json`](../../sessions/23/23fd81eb41357efe3484.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRPO v8 双卡实验状态报告

### 基础设施 ✅
| 项目 | 状态 |
|------|------|
| RASP (PID 532861) | 运行中 2h30m, 114% CPU, 2.7GB RSS |
| Standard (PID 534667) | 运行中 2h21m, 114% CPU, 2.7GB RSS |
| cuda:0 | 100% 利用率, 71.7/97.9 GB |
| cuda:1 | 100% 利用率, 71.7/97.9 GB |
| /root/autodl-tmp | 88GB 可用 (65%) ✅ |
| /root | 22GB 可用 (29%) ✅ |

### W&B 关键指标 (Step 10 → 20)

| 指标 | RASP v8 | Standard v8 |
|------|---------|-------------|
| reward/mean | 0.009 → 0.026 | 0.058 → 0.061 |
| grad_norm | 0.013 → 0.011 | 2.906 → 1.586 |
| loss | 0.009 → -0.005 | 0.060 → 0.056 |
| frac_zero_std | **0.9 → 0.9** | 0.5 → 0.675 |
| completion_length | 1003 → 996 | 749 → 762 |
| clipped_ratio | **0.975 → 0.963** | 0.625 → 0.638 |
| entropy | **0.060 → 0.065** | 0.148 → 0.145 |
| terminated_length | 74 → 124 | 294 → 281 |
| kl | 0.0008 → 0.0010 | 0.0029 → 0.0024 |

### 判断

**RASP v8 — ⚠️ 严重 collapse 风险**
- `frac_zero_std = 0.9`：90% batch 组内 reward 方差为零，DAPO loss 近乎无效
- `grad_norm ≈ 0.01`：梯度接近零，模型没有在学
- `clipped_ratio = 0.97`：97% 生成被截断到 max_length，模型在产出无意义重复文本（output.log 可见数字翻倍循环）
- `entropy = 0.06`：输出高度确定/重复
- reward 虽非零但极低 (0.026)，不构成有效学习信号
- **和 v2/v5 pattern 一致：collapse**

**Standard v8 — ✅ 目前健康，但有早期预警**
- grad_norm 正常 (1.6)，reward 合理 (0.061)，模型在学
- `frac_zero_std` 从 0.5 升至 0.675，趋势不好，需持续观察
- completion 长度合理 (762)，37% 自然终止
- 整体表现远优于 RASP

**结论**：RASP 剪枝模型在 GRPO 阶段再次出现 collapse，和之前版本同样问题。Standard 模型目前正常但 `frac_zero_std` 上升趋势需警惕。建议到 step 30-40 时再次检查 Standard 是否稳定。

---
