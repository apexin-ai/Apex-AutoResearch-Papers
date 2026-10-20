# cpu mv consistency check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_mv_consistency_check_20260521T122158_result.json`
- **Structured JSON:** [`b62169a077a41fe2b9e4.json`](../../sessions/b6/b62169a077a41fe2b9e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。核心发现：

**矛盾已确认，根因是代码库中 3 个 MV 实现使用了不同参数：**

| 差异 | `e3_mbr_micro_f1.py` (产出 0.6579) | `recompute_alpha_crit.py` (产出 0.670) |
|------|------|------|
| MV threshold | strict `>` N/2 (需≥5/8票) | inclusive `>=` N/2 (需≥4/8票) |
| entity match | 3-tuple `(start, end, type)` | 4-tuple `(text, type, start, end)` |
| 数据 | `scierc_mf4v2_seed456/` | `exp_001_seed456_v2/` (旧数据) |

**最关键的问题**: 论文 Proposition 1 定义 MV 为 $\hat{p}(e) > 1/2$ (strict)，但 alpha_crit 表的计算用了 `>= 1/2` (inclusive)。For N=8，strict 需 ≥5 票，inclusive 需 ≥4 票，差异 ~1.0pp。

论文 alpha_crit 表的数值 (.666/.668/.781) 不精确匹配任何现有脚本输出，可能来自已删除的中间脚本。

**建议方案 A**（修改量最小）: 统一为 inclusive `>=`，修改论文数学定义为 $\hat{p}(e) \geq 1/2$，然后在 mf4v2 数据上用统一参数重新计算 alpha_crit 表。详见 artifact `mv_consistency_check.md`。

---
