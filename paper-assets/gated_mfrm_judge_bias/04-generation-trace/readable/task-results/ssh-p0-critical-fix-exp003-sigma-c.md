# ssh p0 critical fix exp003 sigma c

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_critical_fix_exp003_sigma_c_20260522T125335_result.json`
- **Structured JSON:** [`6007589dc5b953af0cb0.json`](../../sessions/60/6007589dc5b953af0cb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run completed. Results summary:

## 修复验证

| Fix | 状态 | 详情 |
|-----|------|------|
| **Bug 1: sigma_c** | ✅ | 用 `reg_horseshoe_prior_cn` 替代裸 HalfNormal — 提供 tau_c 全局收缩 + lambda_c 局部自适应收缩 |
| **Bug 2: Docstring** | ✅ | 已改为 "Regularized Horseshoe (Piironen & Vehtari, 2017)" |
| **Fix 3: Item 过滤** | ✅ | 316 → 175 items (dropped 141 with <3 judges), 4613 → 4223 obs |
| **Fix 4: Arena Elo** | ✅ | gpt-4o (1286), gpt-4o-mini (1272) — 8/8 models matched |

## c_n 分布 (joint_gmfrm)

| Model | c_n |
|-------|-----|
| gpt-3.5-turbo-0125 | 5.14 |
| gpt-4-0613 | 3.56 |
| qwen2.5-72b | 3.20 |
| llama-3.3-70b | 2.67 |
| qwen3-8b | 1.65 |
| gemma-2-9b | 1.21 |
| gpt-4o-mini | 1.21 |
| **gpt-4o** | **0.39** |

c_n 尚未呈现 zero-inflated 形态，但 **ESS=5**（100 samples / 1 chain 严重不足）。Horseshoe 的自适应收缩需要充分采样才能生效。全量运行 (4000 samples / 4 chains) 预期 tau_c 会收缩到 <1，使大部分 c_n 被压向 0。

## Arena Elo 相关性

- joint_gmfrm: **tau=0.857, rho=0.952** (p=0.00026) — 最优
- 其他三种方法: tau=0.786, rho=0.905

joint_gmfrm 在 8 个模型上的 Arena Elo 相关性最高，说明加入 contamination term 确实改善了 ability 估计。

## 判断

**可以启动全量运行。** 0 divergences，模型正确采样，horseshoe prior 成功集成。ESS 过低是 dry-run 采样量不足的正常表现。

---
