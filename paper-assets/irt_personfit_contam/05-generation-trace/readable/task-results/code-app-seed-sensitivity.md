# code app seed sensitivity

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_app-seed-sensitivity_20260521T021633_result.json`
- **Structured JSON:** [`0b6b566daf468880b3b9.json`](../../sessions/0b/0b6b566daf468880b3b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。输出文件在 `artifacts/seed_sensitivity/` 下：

| 文件 | 内容 |
|------|------|
| `seed_sensitivity_tables.tex` | 3 个 LaTeX 表格（seed sensitivity / Cohen's d CI / cross-family consistency） |
| `seed_sensitivity_analysis.json` | 完整数值数据 |
| `generate_seed_sensitivity.py` | 生成脚本 |

关键发现：

- **Qwen**: acc 和 θ\_MLE 跨 seed 极稳定（CV < 0.12），ℓz\* 变异稍大（CV=0.16，std=1.41）但远小于 contamination 造成的偏移
- **Llama**: ℓz\* 均值接近 0（mean=-0.14），CV 被放大到 6.86——但绝对 std=0.97，和 Qwen 同量级
- **Analytic CI** 因 df=2 极宽（t\_crit=4.303），均跨 0——这是 n=3 的固有局限
- **Bootstrap CI** 更紧且全部不含 0，支持 contamination detection 结论在所有条件下成立
- **跨家族一致性**：两个模型在 15% 和 50% contamination 下 d 均为负且 |d|>0.8，detection 方向一致

---
