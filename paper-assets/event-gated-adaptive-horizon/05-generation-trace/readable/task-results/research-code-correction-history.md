# research code correction history

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_code-correction-history_20260528T010710_result.json`
- **Structured JSON:** [`5abdbe5c45dcf13ab49c.json`](../../sessions/5a/5abdbe5c45dcf13ab49c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。调查结果已写入 `artifacts/code_correction_history.md`。核心发现：

## Bug: `subsample_variable_dt` 参数路由错误 (BF1)

**`models.py:172`** 将 `gate_max_dt=8`（embedding 架构维度）传给 `subsample_variable_dt`，**完全忽略** `gate_subsample_max_dt=2`（用户配置的采样范围）。

- **旧代码**: dt 从 {1,2,3,4,5,6,7,8} 采样（73% dt≠1），训练/imagination 分布严重不匹配
- **新代码**: dt 正确限制为 {1,2}

## 影响

| 配置 | 旧代码 | 新代码 | 原因 |
|---|---|---|---|
| **008e_v3** | 2/5 CIVO collapse | **0/4 CIVO** | 修复后 dt 分布匹配，消除 mismatch |
| **008f** | eval 503.0, NVE 0.97× | eval 139.5, NVE 1.69× | dt 分布改变训练动态 |
| 008a/008c | 不受影响 | — | subsample OFF，不调用此函数 |
| 008d | 受影响但结论不变 | — | Bug 放大了 CIVO，未削弱 |

两个配置**同一个 bug**。旧 008e_v3 的 "Pathway B"（dt=1 mitigation 有 40% 失败率）是 bug 伪影，已从论文删除。

**辅助修复**: BF2（replay seed 硬编码为 0）、BF3（gate_fixed_dt>0 时不必要的 gate loss 计算）。

当前代码（HEAD）是修正后的版本。

---
