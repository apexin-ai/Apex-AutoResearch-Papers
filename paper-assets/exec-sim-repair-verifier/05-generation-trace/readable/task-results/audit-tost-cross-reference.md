# audit tost cross reference

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tost-cross-reference_20260519T065539_result.json`
- **Structured JSON:** [`b5a2cdf5ba368196f4b4.json`](../../sessions/b5/b5a2cdf5ba368196f4b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

问题确认。以下是完整分析：

```
## 脚本分析
- 脚本路径: /home/ubuntu/.../tost_sensitivity.py (本地)
- 实际比较的对: CLS vs CWM（仅此一对）
- gap 值来源: 硬编码 mean_diff = 1.24（CLS 88.43 - CWM 87.19）
- p-values 是否独立计算: NO — 没有任何脚本计算 CLS-TRAJ 的 TOST

## Appendix Table (tab:tost_sensitivity, 编译后为 Table 13)
- caption: "TOST equivalence sensitivity (Qwen3-4B, 5 seeds). Observed mean CLS–CWM difference: 1.24pp."
- 比较的对: CLS vs CWM
- gap 值: 1.24pp

## §Equivalence 引用 (experiments.tex:95-100)
- 讨论的比较: CLS vs TRAJ（gap -0.45pp, 523 variant-level instances）
- 引用的 table: Appendix Table~\ref{tab:tost_sensitivity}
- 声称的 p-values: ±2pp p=0.007, ±1pp p=0.871, min margin ±1.63pp
- 这些数字与 CLS-CWM table 完全一致

## 结论
- 交叉引用是否正确: NO
- p-values 一致是巧合还是引用错误: **引用错误**
  - tost_sensitivity.py 只计算了 CLS-CWM (gap 1.24pp)
  - §Equivalence 讨论 CLS-TRAJ (gap -0.45pp) 但直接复用了 CLS-CWM 的 p-values
  - min margin 1.63pp 与 gap 1.24pp 匹配，与 gap -0.45pp 不匹配
  - tost_sensitivity_full.json 的 header 写 "CLS vs TRAJ" 但 mean_diff_pp=1.24（CLS-CWM 的值），说明 header 是错误标注
- 需要几张 TOST table: 2（CLS-CWM 已有；CLS-TRAJ 需要新建）
```

**根本问题**：从未有脚本计算过 CLS-TRAJ 的 TOST 分析。`tost_sensitivity_full.json` 试图把 CLS-CWM 的结果重新标记为 "CLS vs TRAJ"（header 改了但 `mean_diff_pp` 还是 1.24），然后 §Equivalence 直接引用了这些数字。gap -0.45pp 对应的 TOST p-values 会完全不同——以 -0.45pp 的 gap 和相似的 SE，±2pp 处的 p 会远小于 0.007（等价性更容易确认），±1pp 处的 p 也不会是 0.871。

---
