# ops check experiments final

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-experiments-final_20260515T043627_result.json`
- **Structured JSON:** [`6edcc99078458bca7a63.json`](../../sessions/6e/6edcc99078458bca7a63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Status Summary

### GPU 占用
| GPU | PID | Experiment | Memory |
|-----|-----|------------|--------|
| 0 | 68373 | plan_006_s42 | 14382 MiB |
| 1 | 73742 | a050_s42 | 14382 MiB |

---

### a050_s42 — 仍在跑
- **路径**: `results/alpha_sweep/a050_s42/`
- **配置**: synthetic_ratio=0.50, num_generations=10, steps_per_gen=5000, data=wikitext103_5k
- **进度**: 8/10 完成 (gen_0–7 有 metrics)，当前在 gen_8
- **启动时间**: 今天 09:20

| gen | entropy | ece | ppl | d1 | d2 | d3 |
|-----|---------|------|-------|--------|--------|--------|
| 0 | 3.2342 | 0.0108 | 26.95 | 0.0982 | 0.5178 | 0.8127 |
| 1 | 2.5174 | 0.0669 | 22.96 | 0.0975 | 0.5141 | 0.8104 |
| 2 | 2.4984 | 0.0871 | 26.38 | 0.0827 | 0.4311 | 0.7153 |
| 3 | 2.5644 | 0.0880 | 27.48 | 0.0756 | 0.3838 | 0.6401 |
| 4 | 2.5486 | 0.0933 | 28.69 | 0.0706 | 0.3346 | 0.5493 |
| 5 | 2.5461 | 0.0978 | 29.94 | 0.0675 | 0.3089 | 0.5048 |
| 6 | 2.5670 | 0.0981 | 30.19 | 0.0658 | 0.2897 | 0.4663 |
| 7 | 2.6084 | 0.0963 | 30.77 | 0.0639 | 0.2727 | 0.4305 |

**趋势**: entropy 从 3.23 降到 ~2.5 后稳定。ECE 缓慢上升到 ~0.10。PPL 温和上升 (27→31)。**Distinct-N 持续下降** (d3: 0.81→0.43)，多样性在稳步丧失但未崩塌。

---

### plan_006_s42 — 仍在跑
- **路径**: `results/extended_20gen/s42/`
- **配置**: synthetic_ratio=1.0, num_generations=20, steps_per_gen=10000, data=wikitext103
- **进度**: 10/20 完成 (gen_0–9 有 metrics)，当前在 gen_10
- **启动时间**: 今天 07:41

| gen | entropy | ece | ppl | d1 | d2 | d3 |
|-----|---------|------|---------|--------|--------|--------|
| 0 | 3.2342 | 0.0108 | 26.95 | 0.0982 | 0.5178 | 0.8127 |
| 1 | 1.5253 | 0.3268 | 185.68 | 0.0975 | 0.5141 | 0.8104 |
| 2 | 1.2962 | 0.3781 | 380.41 | 0.0846 | 0.4390 | 0.7141 |
| 3 | 1.2141 | 0.3986 | 568.76 | 0.0798 | 0.4025 | 0.6606 |
| 4 | 1.2192 | 0.4093 | 734.41 | 0.0782 | 0.3890 | 0.6390 |
| 5 | 1.1711 | 0.4223 | 930.22 | 0.0780 | 0.3867 | 0.6358 |
| 6 | 1.1343 | 0.4322 | 1187.47 | 0.0780 | 0.3865 | 0.6353 |
| 7 | 1.1313 | 0.4371 | 1389.60 | 0.0780 | 0.3865 | 0.6352 |
| 8 | 1.1402 | 0.4384 | 1566.03 | 0.0780 | 0.3865 | 0.6351 |
| 9 | 1.1456 | 0.4406 | 1786.72 | 0.0779 | 0.3860 | 0.6342 |

**趋势**: 严重崩塌。Entropy 一代就从 3.23 暴跌到 1.53，之后稳定在 ~1.14。ECE 飙到 0.44。**PPL 指数级爆炸** (27→1787)。Distinct-N 在 gen_5 后完全饱和不再变化 (d1≈0.078, d2≈0.386, d3≈0.635)。100% 合成数据的崩塌远比 50% 混合剧烈。

---
