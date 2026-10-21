# ops exp021 metrics pull

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp021-metrics-pull_20260524T061238_result.json`
- **Structured JSON:** [`35fa7fd8bb9cb9b89ff3.json`](../../sessions/35/35fa7fd8bb9cb9b89ff3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## exp_021 — 已完成，metrics 已保存

文件：`artifacts/exp_021/full_metrics.json`

| Gen | r_eff | PPL | Distinct-4 | Train Loss |
|-----|-------|-----|------------|------------|
| 0 | 23.09 | 15.45 | 0.9127 | — |
| 1 | 121.17 | 11.47 | 0.8844 | 2.560 |
| 2 | 113.30 | 11.30 | 0.8701 | 2.478 |
| 3 | 134.49 | 11.21 | 0.8600 | 2.432 |

real-data control 下 r_eff 上升后稳定在 ~113-134，PPL 持续下降，没有出现 Phase II/III 的 collapse 加速——符合预期。

---

## exp_020 — 正在跑 Gen 9

**配置**：GPT-2-medium, pure collapse (r=0.0), 10 generations total, seed=42

**当前状态**：Gen 9 正在生成 synthetic samples，进度 ~5,440/50,000 (~11%)

**GPU**：GPU 0 — 85% 利用率，26.4GB 显存

**已完成 gen 0-8 的趋势**：

| Gen | r_eff | PPL | Distinct-4 | Loss |
|-----|-------|-----|------------|------|
| 0 | 23.09 | 15.45 | 0.9127 | — |
| 1 | 155.22 | 16.42 | 0.8907 | 2.358 |
| 2 | 185.37 | 18.94 | 0.8682 | 2.119 |
| 3 | 184.86 | 23.33 | 0.8368 | 2.052 |
| 4 | 169.56 | 32.11 | 0.7636 | 1.993 |
| 5 | 151.94 | 49.35 | 0.6583 | 1.913 |
| 6 | 136.09 | 76.81 | 0.5590 | 1.821 |
| 7 | 121.29 | 123.66 | 0.5008 | 1.740 |
| 8 | 110.92 | 198.01 | 0.4598 | 1.706 |

三阶段轨迹清晰：Phase I decompression (gen 1-2, r_eff 上升到 185)，Phase II onset (gen 3-4, r_eff 开始回落)，Phase III acceleration (gen 5+, PPL 指数级上升)。

**时间估算**：每代 ~2h24m。Gen 9 预计 ~16:20 完成，Gen 10（最后一代）预计 ~18:45 完成。

---
