# code failure mode analysis

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_failure-mode-analysis_20260513T044723_result.json`
- **Structured JSON:** [`b45cbfdd2b14977ff664.json`](../../sessions/b4/b45cbfdd2b14977ff664.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。脚本写入 `src/analyze_failure_modes.py`，覆盖全部 5 类分析：

1. **基本统计** — 总体成功率 + 6 种 task type 分别统计
2. **Divergence 分析** — d 分布统计、10-bin 直方图、early/mid/late 三组、per-type d 分布
3. **γ(d) 映射预览** — 线性插值 γ(d)=γ_min+d·(γ_max-γ_min)，各组均值 γ
4. **Expert/Failure 匹配** — exact match / template match / unmatched 统计
5. **轨迹长度** — failure vs expert 长度分布 + correction span

输出 `failure_mode_summary.json` + `failure_mode_report.md`，纯 CPU，无 GPU 依赖。divergence 计算逻辑直接复用 `build_dpo_pairs.py` 的 action 对比方式。

---
