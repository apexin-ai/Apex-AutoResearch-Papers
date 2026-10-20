# paper critical text fixes

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_critical-text-fixes_20260522T184546_result.json`
- **Structured JSON:** [`4bb0252fed9c9e155382.json`](../../sessions/4b/4bb0252fed9c9e155382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 处修复完成，编译验证通过。

### 修改汇总

| Fix | 文件 | Before | After |
|-----|------|--------|-------|
| **1** | `experiments_main.tex:89` | LP-best `+8` pp | LP-best `+1.4` pp |
| **2** | `experiments_main.tex:10` + `appendix.tex:412` | `51%` zero F1 | `53.7%` zero F1 |
| **3** | `experiments_main.tex:60` (Table 4 caption) | 无指标标注 | 添加 `(instance-averaged F1; ...)` |
| **4** | `limitations.tex:1` + `appendix.tex:1248` | `±0.57` | `±0.46` |
| **5** | `experiments_main.tex:75,114` | `+0.12`, `91%` collapse | `+0.09`, `94%` collapse |
| **6** | `experiments_main.tex:69` + `appendix.tex:1484` | `.667` | `.663` |
| **7** | `discussion.tex:6` | `$0.92$--$0.97×$` | `$≈0.97×$` (移除无法验证的下界) |

### 编译结果
- 0 LaTeX errors
- 47 pages (主文 8 页 + 附录), 页数未变
- Discussion section 在第 8 页，主文未超限

### 注意事项
- Fix 6: 仅修改了 Table 4 body 和 appendix 脚注中明确标注 "3-seed" 的 `.667`。其他表格中的 `.667`（如 tab:alpha_crit, tab:scale_comparison）保持不变，因为这些可能使用不同指标（macro F1 vs instance-averaged F1），修改会导致 ΔSC 等衍生值不一致
- Fix 5: appendix 的 epoch confound 表（Table 56）保留 `+0.12±0.04`（2-seed mean），因其标注明确；主文改为 3-seed mean `+0.09`

---
