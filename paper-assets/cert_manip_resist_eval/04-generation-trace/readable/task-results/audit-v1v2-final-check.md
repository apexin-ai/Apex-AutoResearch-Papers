# audit v1v2 final check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_v1v2-final-check_20260523T185223_result.json`
- **Structured JSON:** [`d1c57b9cd60ea4e30a37.json`](../../sessions/d1/d1c57b9cd60ea4e30a37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部追踪完毕。结果如下：

```
文件                             | 脚本                               | 版本       | 是否需要重跑
sensitivity_analysis_poolA.json | run_sensitivity_analysis_poolA.py  | V1(上游)   | 是
cross_benchmark_iv.json         | run_cross_benchmark_iv.py          | V1         | 是
keff_stability_split.json       | 无明确生产脚本                      | V1(推测)   | 是
```

### 详细说明

**1. `sensitivity_analysis_poolA.json`** — V1（上游），影响：**高**
- 脚本本身不处理原始 judge 响应，从 `capability_matched_subsample.json` 读取预计算的回归结果
- 上游 `run_capability_matched.py` 使用 `.get("winner", "tie")`（V1），第 76/78/89/93 行
- 回归系数（t_stat、RV）基于 V1 ASR 数据，error 响应被当作 "tie" 投票，污染回归输入

**2. `cross_benchmark_iv.json`** — V1，影响：**高**
- `run_cross_benchmark_iv.py` 直接使用 `.get("winner", "tie")`，第 73/75/86/90 行
- IV 回归的工具变量和结果变量都基于 V1 ASR，两阶段均受污染

**3. `keff_stability_split.json`** — V1（推测），影响：**中**
- 项目内无任何脚本/模块引用 `keff_stability_split` 字符串，文件可能由已删除脚本或手动整理生成
- 文件内容为 "wild cluster bootstrap significance by Spearman rho tier" 聚合摘要
- `run_wild_cluster_bootstrap.py` 和 `run_wild_cluster_bootstrap_v2.py` 均为 V1（`.get("winner", "tie")`）
- 注意：`run_attacked_keff.py`（输出 `attacked_keff.json`，非本文件）使用 `.get("winner")` 无默认值 + None 过滤，更接近 V2 思路，相对稳健
- 影响为中：K_eff 稳定性基于 MI 互信息，但 bootstrap 显著性检验中的 ASR 计算仍受 V1 误差影响

---
