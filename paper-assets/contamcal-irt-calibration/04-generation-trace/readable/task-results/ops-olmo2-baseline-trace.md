# ops olmo2 baseline trace

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_olmo2-baseline-trace_20260521T141009_result.json`
- **Structured JSON:** [`62dd89366a9f8edc0767.json`](../../sessions/62/62dd89366a9f8edc0767.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Shell escaping 问题。已有足够数据，直接汇总。

## 汇总报告

### 两个数据源

| 项目 | 53.79% 来源 | 58.60% 来源 |
|------|-----------|-----------|
| **文件** | westd: `/root/autodl-tmp/exp001/eval_results_v2/olmo2_d000/` | westd: `/root/autodl-tmp/exp001/eval_results_cross_family/olmo2_d000_s42_westd/` |
| **引用** | `phase2_summary.csv` → 论文分析脚本 | 独立 cross_family eval |
| **正确/总数** | 7553/14042 | 8229/14042 |
| **生成时间** | 05-19 20:18 | 05-19 18:04 |
| **Adapter** | 无日志，**无法确认是否加载** | **日志确认加载** adapter |
| **evaluate.py** | 未知版本（无日志） | 与 phase2 fix 同期 |

### 全 dosage 对比

| Dosage | v2 (论文用) | cross_family | Δ (pp) |
|--------|-----------|-------------|--------|
| d000 | 53.79% | 58.60% | **4.81** |
| d005 | 56.14% | 58.10% | 1.96 |
| d025 | 56.17% | 56.17% | **0.00** (复制) |
| d050 | 57.25% | 59.18% | 1.93 |
| d100 | 57.00% | 59.49% | 2.49 |

### 差异根因

1. **d025 v2 和 cross_family 完全一致** — v2 d025 是从 cross_family 直接复制的
2. **d005/d050/d100 差异 ~2pp** — evaluate.py 版本不同：旧版 mc_suffix 在 user turn，新版在 assistant turn（C009 记录的已知问题）
3. **d000 差异 4.81pp — 是其他 dosage 差异的 ~2.5 倍**。最可能原因：v2 d000 eval **未加载 SFT adapter**（评估了裸 base model）。佐证：
   - 无 eval log（其他 dosage 也没有，但 cross_family 有完整 log 确认 adapter 加载）
   - 53.79% 异常低于所有其他 d000 数据（s0=55.34%, s123=55.66%, cross_family s42=58.60%）
   - d000 adapter 只做 clean SFT，不含 contamination，理应比 base 高

### 对论文的影响

**严重**。论文当前 OLMo-2 分析基于 `eval_results_v2`，其中：
- d000 baseline 被低估 ~4.8pp（可能用了 base model）
- d025 是从另一个 eval pipeline 复制的，与 d000/d005/d050/d100 不在同一评估条件下
- **eval_results_v2 的 OLMo-2 数据集是混源的**，违反 C010

当前论文中 OLMo-2 contamination benefit = d100 - d000 = +3.21pp。如果用 cross_family 数据：59.49% - 58.60% = **+0.89pp**。OLMo-2 可能应从 "Benefit" 重分类为 "Immune"。

### 建议

**用当前标准化 evaluate.py (37775 bytes) 重跑 OLMo-2 全部 5 个 dosage s42 eval**，在同一台服务器上获得完全一致的数据集。

---
