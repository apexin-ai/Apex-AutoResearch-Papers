# ssh exp020 progress check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp020-progress-check_20260524T173551_result.json`
- **Structured JSON:** [`865f6a91dc4f25bf1499.json`](../../sessions/86/865f6a91dc4f25bf1499.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp-020 Judge Collection Progress (n17) ===
| Judge                  | Lines  | Target | %      | Method         | Status                              |
|------------------------|--------|--------|--------|----------------|-------------------------------------|
| LLaMA-3.3-70B-Instruct | 18,093 | 18,000 | 100.5% | local vLLM     | ✅ done                              |
| Qwen2.5-72B-Instruct   | 16,180 | 18,000 | 89.9%  | local vLLM     | 🔄 running (ETA ~94 min)            |
| Qwen3-235B-A22B        | 16,116 | 18,000 | 89.5%  | API (proxy)    | 🔄 running (ETA ~184 min)           |
| Claude Sonnet 4.6      | 14,255 | 18,000 | 79.2%  | API (OpenRouter)| ⛔ blocked (403)                    |
| DeepSeek-V4-Pro        | 12,531 | 18,000 | 69.6%  | API (proxy)    | 🔄 running (ETA ~542 min / ~9h)     |
| Gemini 2.5 Pro         | 11,253 | 18,000 | 62.5%  | API (OpenRouter)| ⛔ blocked (403)                    |
| Mistral-Large-2        |    118 | 18,000 |  0.7%  | local vLLM     | ⛔ stalled (no collect process)      |

Active collect processes:
- PID 584197: Qwen2.5-72B — [9950/13590], 0.6 items/s, ETA ~1.5h
- PID 592432: Qwen3-235B  — [4560/9969], 0.5 items/s, ETA ~3h
- PID 592328: DeepSeek-V4 — [2700/12057], 0.3 items/s, ETA ~9h
- tmux "orchestrator2": run_remaining.sh still active

vLLM status:
- LLaMA-3.3-70B — GPU 0,1, port 8001 (running, but collection already done)
- Qwen2.5-72B   — GPU 2,3, port 8002 (running, serving active collection)
- Mistral-Large-2 — NOT running (no vLLM process, no collect process)

Estimated completion timeline (UTC):
- Qwen2.5-72B: ~03:10 today
- Qwen3-235B:  ~04:40 today
- DeepSeek-V4: ~10:40 today
- Mistral/Claude/Gemini: need intervention

=== exp-017 Coverage Simulation ===
Status: ✅ Completed (cron finished 2026-05-24T07:05:49Z)
File: /root/gated_mfrm_judge_bias/exp017/results/coverage_simulation.csv
Lines: 252 (1 header + 251 data rows)
Columns: n_models, seed, c_coverage_rate, theta_coverage_rate, c_mean_ci_width, theta_mean_ci_width, r_hat, ess, elapsed_s
Range: n_models 8→20, seeds 0→50
Sample: c_coverage_rate 0.5–1.0, theta_coverage_rate 0.75–1.0, r_hat ≈ 1.0 (chains converged)
```

**需要关注的问题：**

1. **Mistral-Large-2**：只有 118 条，无 vLLM 进程也无 collect 进程，完全停滞。GPU 4-7 空闲，可以重启 Mistral vLLM + collect。
2. **Claude Sonnet / Gemini**：被 OpenRouter 403 封锁，分别卡在 79.2% 和 62.5%。需要换 API 渠道或等解封。
3. **LLaMA vLLM 占用 GPU 0,1**：collection 已完成，可以关掉释放显存给 Mistral。

---
