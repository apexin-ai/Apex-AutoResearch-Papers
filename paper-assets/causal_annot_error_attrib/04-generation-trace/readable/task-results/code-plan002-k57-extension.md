# code plan002 k57 extension

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-k57-extension_20260520T150023_result.json`
- **Structured JSON:** [`0935c99afd76ff135b21.json`](../../sessions/09/0935c99afd76ff135b21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 002 完成，13 秒跑完（RTX 5090 GPU 加速）。

## 结果摘要

### Cross-K 对比表
| Topology | K | sign_flip | τ bias mean | worst-case (diag≥0.9) |
|---|---|---|---|---|
| confounding | 3→5→7 | 99.3%→100%→100% | +0.272→+0.236→+0.228 | 0.162→0.113→0.092 |
| mediation | 3→5→7 | 83.8%→96.6%→100% | +0.256→+0.225→+0.197 | 0.123→0.085→0.060 |
| collider | 3→5→7 | 66.6%→95.5%→99.2% | +0.097→+0.111→+0.104 | 0.048→0.046→0.036 |
| exposure | 3→5→7 | 99.0%→100%→100% | — | 0.253→0.269→0.282 |

violation 和 amplification 在所有 K 下均为 ~100%。

### 关键发现
1. **sign_flip 随 K 增大恶化** — mediation 从 83.8% 升至 100%，collider 从 66.6% 升至 99.2%，更多类别意味着更多错分模式可导致符号反转
2. **τ bias 均值随 K 减小** — 每个类别的错分权重降低（confounding: 0.272→0.228）
3. **worst-case bounds 随 K 下降**（除 exposure） — 高精度约束（diag≥0.9）下，K=7 的最大偏差反而小于 K=3
4. **bias 方差更分散** — top-1 PC 解释方差从 78% 降至 61%，K 增大后 bias 不再集中在单一方向
5. MC 验证通过（K=3 所有拓扑理论值与 MC 均匹配）

### 输出文件
- 脚本: `/home/sonny/causal_annot_error_attrib/plan_002_k57_extension.py`
- 日志: `plan002_run.log`
- 可视化: 13 张 PNG（4 拓扑 × 3 K 的 sensitivity heatmap + 1 combined）

---
