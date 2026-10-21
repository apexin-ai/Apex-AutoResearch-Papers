# analysis deepseek func error patterns

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-func-error-patterns_20260517T081937_result.json`
- **Structured JSON:** [`be0f1de44123c7810f2f.json`](../../sessions/be/be0f1de44123c7810f2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，JSON 已保存到 `/root/autodl-tmp/eval_results/error_analysis_deepseek_func_level.json`。

## 关键结果

### Overall (DeepSeek-coder-6.7B, seed42, n=1890)

| 指标 | DeepSeek | Qwen3-4B |
|---|---|---|
| CLS acc | 86.93% | 87.78% |
| CWM acc | 85.77% | 87.30% |
| Oracle ensemble | **91.53%** | 89.84% |
| Oracle gain | **+4.6pp** | ~2pp |
| Complementarity | **55.1%** | 31.2% |

### Per-label 不对称性（DeepSeek 特有）

CWM 在 fail 检测上远强于 CLS（93.86% vs 86.51%），但在 pass 上大幅落后（78.22% vs 87.32%）。CWM precision_pass 高（93.18%）但 recall_pass 低（78.22%），说明 CWM **偏保守，倾向判 fail**。

### By mutation type

| mutation_type | CLS | CWM | Oracle | Complementarity | CLS-CWM |
|---|---|---|---|---|---|
| boundary_removal | 94.44 | 86.11 | **100.0** | 100.0% | +8.33pp |
| off_by_one | 78.39 | 78.99 | 85.25 | 47.1% | -0.60pp |
| operator_swap | 83.22 | **86.24** | 92.62 | 68.1% | -3.02pp |
| original | **91.96** | 84.92 | 92.96 | 56.2% | +7.04pp |
| return_value | 96.27 | 96.02 | 98.01 | 65.2% | +0.25pp |
| variable_swap | **96.47** | 92.94 | 96.47 | 50.0% | +3.53pp |

### Cross-seed CWM (s42 vs s123)

- CWM s42: 85.77%, CWM s123: 87.88%
- Agreement: 93.44%, Oracle: 90.11%

### 跨模型 pattern 结论

**4/5 个 Qwen pattern 在 DeepSeek 上复现：**
1. CLS > CWM overall（两个模型都是）
2. CLS 在 variable_swap 上更强（DeepSeek +3.53pp, Qwen +5.9pp）
3. 有意义的 oracle gain（DeepSeek 甚至更大：4.6pp vs ~2pp）
4. return_value 高互补性（DeepSeek 65.2%, Qwen 61.5%）

**主要差异：** DeepSeek 的 CLS-CWM 互补性远高于 Qwen（55.1% vs 31.2%），意味着两个模型犯错的重叠更少，ensemble 潜力更大。这可能因为 DeepSeek CWM 有更强的 fail-bias（pass recall 仅 78.22%），与 CLS 的 error pattern 差异化更大。

---
