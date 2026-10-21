# code keywords v2 fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_keywords-v2-fix_20260513T211918_result.json`
- **Structured JSON:** [`a47a20f37bf8a17386ec.json`](../../sessions/a4/a47a20f37bf8a17386ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组数据都有了。

## v1 vs v2 对比

| 指标 | v1 | v2 |
|------|----|----|
| Keywords 数量 | 20 | 17 |
| Avg keyword match rate | **86.1%** | **4.9%** |
| Det-preferred prediction % | **97.5%** (199/204) | **0.5%** (1/203) |
| Overall accuracy (excl no-pref) | 97.7% (83/85) | 1.2% (1/84) |
| Top 3 keywords by hit count | connect(3963), activate(250), freeze(36) | activate(250), freeze(36), mix(2) |

### 分析

v2 成功消除了 `connect`/`disconnect` 造成的虚高命中（3963 次 → 0），匹配率从 86.1% 降到 4.9%。

但问题反转了：v1 退化为 always-det（97.5% 预测 det），v2 退化为 **always-internal**（99.5% 预测 internal）。由于大多数 ground truth 是 det-preferred，v2 accuracy 跌至 1.2%。

核心原因：v2 的 17 个科学动词在 ScienceWorld action text 中出现极少（仅 `activate` 有显著命中，但 250 次分散在 204 个 episode 中不足以让单 episode match rate 超过 50% 阈值）。

### 产出

1. `src/rule_based_keywords_v2.json` — 已创建（服务器 + 本地）
2. `src/rule_based_accuracy.py` — 默认指向 v2，`load_keywords` 兼容 v1/v2 格式
3. `src/rule_based_routing.py` — 默认指向 v2，启动时打印 keyword version + MD5
4. `results/rule_based_accuracy_v2_test.json` — v2 完整报告
5. `results/rule_based_accuracy_v1_rerun.json` — v1 对照报告

---
