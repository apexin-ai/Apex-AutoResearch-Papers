# analysis nli combo recompute pw

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-combo-recompute-pw_20260521T052024_result.json`
- **Structured JSON:** [`80a255f950221dd7b644.json`](../../sessions/80/80a255f950221dd7b644.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 重算结果

### PW600 (alphabetical tiebreaking)

| Generator | SC (alpha) | w1 | w3 | w5 |
|---|---|---|---|---|
| **Mistral-7B** | 39.33% (236) | 40.17% (+0.83pp, p=.36) | **46.00% (+6.67pp, p=1.1e-5)\*** | **50.33% (+11.0pp, p=6.2e-7)\*** |
| LLaMA-3.1-8B | **72.50%** (435) | 73.33% (+0.83pp, p=.36) | 73.33% (+0.83pp, p=.66) | 72.00% (−0.50pp, p=.87) |
| Qwen2.5-14B | **74.00%** (444) | 74.17% (+0.17pp, p=1.0) | 74.67% (+0.67pp, p=.50) | 75.17% (+1.17pp, p=.36) |
| Qwen3-14B | **85.83%** (515) | 86.00% (+0.17pp, p=1.0) | 86.33% (+0.50pp, p=.45) | 87.00% (+1.17pp, p=.21) |

\* = significant after BH correction (m=12)

### 关键变化

1. **SC baseline 上移**：alphabetical + filtering invalid answers 使 LLaMA SC 从 420→435 (+15), Qwen2.5 441→444 (+3), Qwen3 510→515 (+5)。Mistral 不变。

2. **Combo gain 大幅变化**：
   - Mistral w3: +3.50pp → **+6.67pp**（gain 增大，因为 combo 本身从 257→276）
   - LLaMA w3: +4.17pp → **+0.83pp**（gain 缩小，SC 上移更多）
   - 其余类似缩小

3. **BH significant: 4 → 2**（仅 Mistral w3、w5 存活）

4. **Spearman ρ = 1.0**（n=4, exact permutation p = 0.083）: capability gap 与 combo gain 完全单调

5. **FOLIO (Mistral)**: SC=55.88%(114/204), w1=56.37%(+0.49pp), w3=58.82%(+2.94pp, p=.21)

### 代码修复
9 处 `Counter.most_common()` / `max(dict, key=dict.get)` 已替换为 alphabetical tiebreaking（westd-16639: 4处, westd-25068: 5处）。

---
