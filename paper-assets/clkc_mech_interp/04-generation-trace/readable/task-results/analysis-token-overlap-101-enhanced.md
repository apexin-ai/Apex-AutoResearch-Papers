# analysis token overlap 101 enhanced

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_token-overlap-101-enhanced_20260522T013533_result.json`
- **Structured JSON:** [`9fc4cb88840f16e4e41d.json`](../../sessions/9f/9fc4cb88840f16e4e41d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

## 结果摘要

**RC2（共享 token 驱动 cross-lingual transfer）：排除**

| | Qwen (layer 22) | Llama (layer 13) |
|---|---|---|
| Type-level Jaccard | 10.4% | 15.1% |
| Per-sample Jaccard (mean) | 4.4% | 3.2% |
| Pearson r (overlap vs correctness) | 0.059 (p=0.45) | **-0.153 (p=0.012)** |
| Spearman r | 0.064 (p=0.41) | **-0.215 (p=0.0004)** |
| Tercile Δ(high-low) | +7.1pp | **-23.9pp** |

核心发现：
1. Per-sample overlap 极低（3-4%），type-level 统计膨胀了 3x
2. Qwen 无显著相关
3. Llama 显著**负**相关 — 高 overlap 反而降低准确率，方向与 RC2 假说完全相反
4. 不需要额外 masking 实验，tercile 分析已给出明确结论

产出文件：
- 脚本：`/root/clkc_mech_interp/src/token_overlap_enhanced.py`
- 结果：`/root/clkc_mech_interp/data/token_overlap_analysis.json`
- 项目知识：`memory.md` 已更新

---
