# exp qwen fewnerd seed456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_fewnerd_seed456_20260518T092846_result.json`
- **Structured JSON:** [`9f18e2f7bb12190a7a36.json`](../../sessions/9f/9f18e2f7bb12190a7a36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理状态总结：

**seed=456 Few-NERD 推理已启动**
- tmux session: `fewnerd_s456`
- GPU: cuda:2 (autodl-5090)
- 配置: Qwen3-8B merged, N=8, T=1.0, seed=456, XGrammar constrained
- 进度: 3,392/301,184 prompts (~1.1%)
- 速度: 正在升温，最近 35-60 it/s
- 预计完成: ~2-3 小时后（约 19:30-20:30 CST）
- 日志: `output/exp_021_fewnerd_n8_seed456_run.log`
- 完成后自动运行 `analyze_fewnerd_results.py`

**seed=42 参考值（目标复现）:**
| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.7478 |
| LP_sel_f1 | 0.7614 |
| LP_delta | +1.36pp |
| degen% | 10.13% |
| LP_rho | 0.4215 |
| n_total | 37,648 |

推理完成后需要：验证 samples.jsonl 行数 → 运行分析 pipeline → 汇总 metrics。需要我定时检查进度吗？

---
