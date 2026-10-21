# ops kill epsilon retrain check gpu

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-epsilon-retrain-check-gpu_20260524T122226_result.json`
- **Structured JSON:** [`7d79c01fe9562b8ad1b6.json`](../../sessions/7d/7d79c01fe9562b8ad1b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 结果

**PID 885408/885409/885060 (replay_svd_gen10.py)** — 已全部杀掉。GPU 0 从 57431MiB 降到 19349MiB，释放了约 38GB 显存。这两个脚本是冗余的，因为 Gen 10 的完整数据（effective_rank=97.02, log_det=320.61, perplexity=545.97, top_10_singular_values 等）已存在于 `results/phase1_gpt2m_pure_collapse_seed42_results.json` 中。

**实验状态：**
- **exp_022c** (PID 881066, GPU 0, 19340MiB) — 正常运行，95% GPU 利用率
- **exp_023** (PID 868285, GPU 1, 26422MiB) — 正常运行，94% GPU 利用率

两个实验现在各独占一块 GPU，不再有资源竞争。

---
