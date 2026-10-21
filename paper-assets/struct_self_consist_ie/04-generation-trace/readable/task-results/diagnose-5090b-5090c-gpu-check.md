# diagnose 5090b 5090c gpu check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_5090b_5090c_gpu_check_20260520T233136_result.json`
- **Structured JSON:** [`8ac1359ac65dda1226d7.json`](../../sessions/8a/8ac1359ac65dda1226d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 registry 全部更新完毕。汇总如下：

---

## CoNLL T-ablation 结果（全部完成，PASS）

| Metric | T=0.5 (5090-b) | T=0.5 (5090-c) | T=0.8 | T=1.2 |
|--------|:-:|:-:|:-:|:-:|
| greedy F1 | 0.908 | 0.908 | 0.907 | 0.907 |
| oracle F1 | 0.938 | 0.937 | **0.946** | **0.951** |
| oracle headroom | 2.9% | 3.0% | 4.0% | **4.4%** |
| fleiss kappa | 0.896 | 0.895 | 0.820 | 0.709 |
| softjaccard rho (cond) | 0.448 | **0.454** | 0.437 | 0.394 |
| fleiss rho (cond) | 0.444 | **0.452** | 0.413 | 0.349 |
| logprob rho (cond) | 0.356 | — | — | — |
| degen % | 5.6% | 5.6% | 6.6% | **9.2%** |
| sample F1 mean | 0.899 | 0.899 | 0.885 | 0.845 |

**核心趋势**：
- greedy F1 对温度不敏感（~0.907 across all T）
- 升温 → oracle headroom 增大（2.9% → 4.4%）但 rho 下降、degen 升高
- T=0.5 的 structural rho (0.448) 明显优于 logprob baseline (0.356)
- 两个 T=0.5 跑出的结果高度一致（greedy F1 差 0.001）

## 仍在运行

| 实验 | 服务器 | 进度 | ETA |
|------|--------|------|-----|
| FewNERD T=0.5 | 5090-b:cuda:0 | **49%** (147k/301k) | ~51min |
| FewNERD T=0.8 | 5090-b:cuda:1 | **50%** (150k/301k) | ~51min |
| FewNERD T=1.2 | 5090-b:cuda:2 | **53%** (158k/301k) | ~48min |
| 14B inference | 5090-c:cuda:0 | 运行 3h23m, 160% CPU | 未知 |

5090-c:cuda:1/2/3 和 5090-b:cuda:3 现在空闲。

---
