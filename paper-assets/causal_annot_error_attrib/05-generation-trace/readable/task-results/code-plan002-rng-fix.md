# code plan002 rng fix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-rng-fix_20260520T160418_result.json`
- **Structured JSON:** [`a6779b6b932a1e41fd2b.json`](../../sessions/a6/a6779b6b932a1e41fd2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。两次运行数值完全一致，确定性已验证。

**修改内容：**
- 两个文件都新增了 `_det_seed(topo_name, K, tag, base_seed=42)` 函数，用 SHA-256 从 `(topo|K|tag|seed)` 生成确定性 32-bit 种子
- 所有 `gen_random_C` 调用点的 seed 从 `seed=SEED` / `seed=SEED + int(thr * 1000)` 改为 `seed=_det_seed(topo, K, 'random')` / `seed=_det_seed(topo_name, K, f'wc_{thr}')`
- 每个 (topology, K, threshold) 组合现在有独立的确定性种子，不受调用顺序影响

**Worst-case bounds 表（7 topo × K={3,5,7} × threshold={0.5, 0.7, 0.9}）：**

| Topology | K | WC(d≥0.5) | WC(d≥0.7) | WC(d≥0.9) |
|---|---|---|---|---|
| confounding | 3 | 0.2993 | 0.2744 | 0.1614 |
| confounding | 5 | 0.2462 | 0.2156 | 0.1107 |
| confounding | 7 | 0.2264 | 0.1859 | 0.0933 |
| mediation | 3 | 0.3032 | 0.2510 | 0.1223 |
| mediation | 5 | 0.2396 | 0.1832 | 0.0867 |
| mediation | 7 | 0.1879 | 0.1421 | 0.0607 |
| collider | 3 | 0.1256 | 0.1064 | 0.0503 |
| collider | 5 | 0.1306 | 0.1087 | 0.0477 |
| collider | 7 | 0.1131 | 0.0826 | 0.0352 |
| exposure | 3 | 1.1438 | 0.7092 | 0.2726 |
| exposure | 5 | 0.8784 | 0.5782 | 0.2097 |
| exposure | 7 | 0.7441 | 0.4913 | 0.1853 |
| mbias | 3 | 0.0287 | 0.0226 | 0.0106 |
| mbias | 5 | 0.0487 | 0.0374 | 0.0154 |
| mbias | 7 | 0.0449 | 0.0319 | 0.0133 |
| iv | 3 | 14.0463 | 1.6444 | 0.2993 |
| iv | 5 | 9.6932 | 2.1036 | 0.4053 |
| iv | 7 | 8.2204 | 1.8132 | 0.3605 |
| frontdoor | 3 | 0.2966 | 0.2604 | 0.1407 |
| frontdoor | 5 | 0.2507 | 0.2066 | 0.1057 |
| frontdoor | 7 | 0.2119 | 0.1646 | 0.0785 |

---
