# sync d134 analysis v3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sync_d134-analysis-v3_20260518T145822_result.json`
- **Structured JSON:** [`f1c084e188702278cc58.json`](../../sessions/f1/f1c084e188702278cc58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模式都成功执行，无 scipy 版本问题。汇总：

### `--mode d134_only`
- 找到 **4 ISR** seeds (s47/s48/s49/s50)，**0 RANDOM**
- ISR 侧：PR 86.8±14.9, H7 rate 89.0±7.3%, Genuine rate 2.6±2.7%
- RANDOM 0 个 seed，统计检验跳过（符合预期）

### `--mode all`
- 找到 **5 ISR** (s42/s47/s48/s49/s50) + **2 RANDOM** (s42/s44) = 7 runs
- ISR: PR 87.4±13.0, H7 rate 90.6±7.2%, Genuine 2.3±2.4%
- RANDOM: PR 84.0±7.1, H7 rate 0.0±0.0%, Genuine 11.0±6.0%
- 统计检验全部跑通：
  - **Fisher exact**: OR=∞, 95% CI [0.65, ∞], p=0.048
  - **Permutation** (genuine rate): Δ=−8.67 pp, p=1.000（ISR genuine < RANDOM，方向相反所以 p=1）
  - **Mann-Whitney U** (H7 rate): U=10.0, p=0.039, r=−1.000
  - **Bayes Factor**: BF₁₀=9.33 (moderate evidence for H1)
  - **BCa CI**: ISR H7% [85.3, 96.4], RANDOM H7% N/A（n=2 且 constant=0 导致 degenerate warning）；ISR Genuine% [0.9, 5.1], RANDOM Genuine% [6.7, 15.2]

两个注意点：
1. RANDOM 侧 H7 rate 全为 0，BCa 无法计算（DegenerateDataWarning），输出 N/A
2. d134_only 模式缺少 RANDOM seeds（d134_4b_random 系列尚未产出 taxonomy 数据）

---
