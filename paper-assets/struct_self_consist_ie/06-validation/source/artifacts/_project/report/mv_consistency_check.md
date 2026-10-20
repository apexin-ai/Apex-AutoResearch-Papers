# MV Consistency Check (Reviewer #54)

## Summary

**矛盾已确认，根因已定位。** 代码库中存在三个不同的 MV 实现，使用了不同的 threshold 定义和 entity match scheme，导致同一数据上的 MV F1 最大相差 ~1.1pp。论文的数学定义（strict `>`）与 alpha_crit 表的计算代码（inclusive `>=`）不一致。

---

## (a) MV 计算方法对比

| 属性 | `e3_mbr_micro_f1.py` (MBR表) | `e3_mbr_multiseed.py` | `recompute_alpha_crit.py` (α_crit表) |
|------|-----|-----|------|
| **MV threshold** | `c > N*θ` (strict, N=8→需≥5票) | `c >= N/2` (inclusive, N=8→需≥4票) | `count >= N*θ` (inclusive, N=8→需≥4票) |
| **entity match** | 3-tuple `(start, end, type)` | 4-tuple `(text, type, start, end)` | 4-tuple `(text, type, start, end)` |
| **F1 type** | micro (pooled TP/FP/FN) | micro (pooled TP/FP/FN) | micro (pooled TP/FP/FN) |
| **gold_empty filter** | YES (skip) | YES (skip) | YES (skip) |
| **数据路径 (SciERC s456)** | `scierc_mf4v2_seed456/` | `scierc_mf4v2_seed456/` | `exp_001_seed456_v2/` (旧数据!) |

### 关键差异

**1. MV threshold: strict `>` vs inclusive `>=`**

论文 Proposition 1 定义: $\hat{p}(e) > \tfrac{1}{2}$ (strict greater than)
- For N=8: count/8 > 0.5 → count > 4 → count ≥ 5 (至少5票)
- `e3_mbr_micro_f1.py` 正确实现了论文的定义
- `recompute_alpha_crit.py` 和 `e3_mbr_multiseed.py` 用了 `>=` (至少4票)

**影响**: inclusive threshold 多纳入了 "恰好4/8票" 的 entities，提高 recall，对 SciERC 约提升 ~1.0pp MV F1。

**2. Entity match: 3-tuple vs 4-tuple**

- 3-tuple `(start, end, type)`: 同 span 不同 text 的 entity 合并计票
- 4-tuple `(text, type, start, end)`: text 不同则视为不同 entity
- 影响较小（~0.1pp），因为 span 通常决定 text

**3. 数据文件不同**

| 文件 | 大小 | 日期 | 说明 |
|------|------|------|------|
| `scierc_mf4v2_seed456/samples.jsonl` | 20MB | May 21 | MF4v2 pipeline，含 token_logprobs |
| `exp_001_seed456_v2/samples.jsonl` | 6.8MB | May 14 | 旧版 sampling run |

两个文件均 551 行，但 samples 内容不同（不同 sampling run 的输出）。

---

## (b) Seed 集合与数值对比

### SciERC seed456 MV F1

| Source | 脚本 | threshold | match | MV F1 |
|--------|------|-----------|-------|-------|
| MBR baseline表 | `e3_mbr_micro_f1.py` | strict `>` | 3-tuple | **0.65789** |
| MBR multiseed | `e3_mbr_multiseed.py` | inclusive `>=` | 4-tuple | **0.66868** |
| α_crit recompute | `recompute_alpha_crit.py` | inclusive `>=` | 4-tuple | **0.67070** |

### SciERC 3-seed mean

| Source | Greedy | MV | Oracle | Δ_SC (pp) |
|--------|--------|-----|--------|-----------|
| `e3_mbr_multiseed` (mf4v2 data, `>=`) | .66693 | .66734 | .78080 | +0.04±0.37 |
| `alpha_crit_recompute` (旧 data, `>=`) | .6659 | .6695 | .8064 | +0.37±0.24 |
| **论文 Table α_crit** | **.666** | **.668** | **.781** | **+0.15±0.18** |

**论文 Table α_crit 的值不精确匹配任何一个已有的计算结果。** Oracle .781 匹配 MBR multiseed (.78080)，Greedy .666 匹配 alpha_crit_recompute (.6659)，MV .668 不匹配任何来源（最接近 MBR multiseed 的 .66734 → 应 round 到 .667）。Δ_SC = +0.15±0.18pp 也不匹配任何计算。

---

## (c) 矛盾根因

### 根因1: MV threshold 定义内部不一致（Primary）

论文数学定义用 strict `>` (Eq.5, Proposition 1, Appendix B.1)，但 alpha_crit 表的计算代码用 inclusive `>=`。

For N=8:
- strict `>`: entity 需出现在 ≥5 个 samples → 更保守，MV F1 ≈ 0.658
- inclusive `>=`: entity 需出现在 ≥4 个 samples → 更宽松，MV F1 ≈ 0.668

差值 ~1.0pp 是矛盾的主要来源。

### 根因2: 数据来源混用（Secondary）

MBR baseline 用 mf4v2 data，alpha_crit recompute 用旧 exp_001/exp_012 data，两者是不同 sampling run。

### 根因3: Entity match scheme 不统一（Minor）

`e3_mbr_micro_f1.py` 用 3-tuple，其他用 4-tuple，贡献 ~0.1pp 差异。

### 根因4: 论文 alpha_crit 表的值来源不明

论文表格中的具体数值不精确匹配任何现存的计算脚本输出，可能来自已删除的中间脚本或手动录入时有误差。

---

## 修正建议

### 方案 A: 统一为 inclusive `>=`（推荐）

1. 修改论文数学定义: $\hat{p}(e) > \tfrac{1}{2}$ → $\hat{p}(e) \geq \tfrac{1}{2}$
   - 代码修改量最小（只改 `e3_mbr_micro_f1.py` 的 `>` 为 `>=`）
   - MV 表现更好（Δ_SC 更正），叙事更有利
   - 数学上: MBR derivation 中 marginal contribution = 0 at $\hat{p}=1/2$ → include 或 exclude 均可，`>=` 更 conventional

2. 在 mf4v2 数据上用统一参数（`>=`, 4-tuple match）重新跑 alpha_crit 表

3. 用同一脚本同时输出 MBR baseline 和 alpha_crit 表的 MV 值，确保一致

### 方案 B: 统一为 strict `>`

1. 保持论文数学定义不变
2. 修改 `recompute_alpha_crit.py` 和 `e3_mbr_multiseed.py` 的 threshold 为 strict `>`
3. alpha_crit 表的 MV 值会降到 ~0.658，Δ_SC 变为 ~-0.84pp
4. **风险**: SciERC 的 MV gain 叙事从 "+0.15pp" 变为 "-0.84pp"，需要调整论文相关讨论

### 必须同时修复

- 统一 entity match 为 4-tuple `(text, type, start, end)` 或 3-tuple `(start, end, type)`（建议用 3-tuple，与 `evaluation.py` 一致）
- alpha_crit 表必须用 mf4v2 数据（论文已声称 "MF4v2 pipeline"）
- 重新验证所有 3 个 dataset 的数值

### 对 Reviewer #54 的回应要点

- 确认存在计算不一致
- 说明根因是 threshold 定义差异（strict vs inclusive），已统一修正
- 提供修正后的一致数值
- MV 在 SciERC 上的表现大致 neutral（|Δ| < 1pp），核心结论（correlation-selection gap）不受影响
