# check paper v1v2 consistency

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_paper-v1v2-consistency_20260527T033604_result.json`
- **Structured JSON:** [`e53b64c4be3706204950.json`](../../sessions/e5/e53b64c4be3706204950.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。报告写入 `artifacts/_project/intermediate/paper_consistency_audit.md`。

发现 **3 个需要立即处理的问题**：

1. **appendix.tex:69 — v1 统计残留**：报告 Detach OCC vs Vanilla 的 d≈-0.04, p=0.91，这是 v1 数据。主文用 v2 数据报告 p=0.28，两者直接矛盾且未标注 v1。

2. **Detach+LN 数据源矛盾**：Table 1 表注说"midrule 以上用 v2 code"，但 Detach+LN 实际用 v1 数据（0.765, n=3）。v2 truth source 是 **0.802**（n=1）。后果严重——如果用 v2 值，LN factorial delta 从 -2.5pp 变成 **-6.2pp**，"BN deficit 大于 LN" 的 claim 会反转。同时，Random OCC（同为 v1 在 midrule 上方）的 ΔCAR 被正确省略，但 Detach+LN 的 ΔCAR（+2.0）却保留了，处理方式不一致。

3. **"LN cells have n=1 each" 与 Detach+LN n=3 矛盾**（results.tex:45）：文字说 LN cells 各 n=1，但表格中 Detach+LN 有 3 seeds。两种解读都有问题。

其余核心 v2 数据（Vanilla、Full OCC BN、Detach OCC BN、Full OCC+LN）全部正确。无 gradient collapse / CKA degradation 等 v1 残留 claim。补充条件的 ΔCAR 计算全部内部一致。

---
