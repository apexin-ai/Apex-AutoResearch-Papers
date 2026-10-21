# analysis tau sweep final

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau_sweep_final_20260515T182958_result.json`
- **Structured JSON:** [`a95b4f5b4a9ddb940c10.json`](../../sessions/a9/a95b4f5b4a9ddb940c10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部生成完毕。产出文件：

| 文件 | 大小 |
|------|------|
| `analysis/figures/tau_ppl_curve.pdf` | 17.8 KB |
| `analysis/figures/tau_ppl_curve.png` | 136 KB |
| `analysis/figures/tau_b_strength.pdf` | 16.2 KB |
| `analysis/figures/tau_b_strength.png` | 107 KB |
| `analysis/tau_sweep_summary.csv` | 289 B |

注意：原始 `tau_sweep_analysis.py` 脚本从 eval_results.json 读取了两个错误值（τ=0.70 PPL=9.595, τ=0.80 b* mean=0.714），图表已用 registry 确认的正确数据重新生成。

---
