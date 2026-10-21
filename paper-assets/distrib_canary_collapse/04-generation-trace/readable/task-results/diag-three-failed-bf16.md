# diag three failed bf16

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_three_failed_bf16_20260518T210453_result.json`
- **Structured JSON:** [`cbee5ff9fb04f761d6d3.json`](../../sessions/cb/cbee5ff9fb04f761d6d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个全是 EXIT_CODE=129 假警报，Python 均正常完成。

| 实验 | 状态 | gen 完成数 | 最后输出 |
|---|---|---|---|
| **gen_gpt2m_a100_s43_bf16** | **complete** | 11/11 (gen_0~gen_10) | `ppl=55.49, entropy=3.0035, eff_rank=3.2, mauve=0.0227` → `all_metrics.json` 已写入 |
| **alpha_sweep_a060_s42_bf16** | **complete** | 11/11 (gen_0~gen_10) | `ppl=20.27, entropy=2.6404, eff_rank=65.9, mauve=0.0146` → `all_metrics.json` 已写入 |
| **interv_react_s43_bf16** | **complete** | 11/11 (gen_0~gen_10) | `ppl=16.51, entropy=2.8169, eff_rank=59.9, mauve=0.0336` → `all_metrics.json` 已写入 |

三个实验都是 tmux session 被 kill 导致 SIGHUP→129，但 Python 进程在收到信号前已正常完成全部 10 代训练 + metrics 计算 + `all_metrics.json` 写入。可安全标记为成功。

---
