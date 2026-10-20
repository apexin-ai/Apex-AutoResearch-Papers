# analysis paper registry consistency

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_registry_consistency_20260521T194443_result.json`
- **Structured JSON:** [`349fa5f1590c7672a27e.json`](../../sessions/34/349fa5f1590c7672a27e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。98 个定量 claim 已比对，结果写入 `artifacts/paper_registry_audit.md`。

**关键发现：**

**⚠️ 3 个 N=5 steering 数字与 registry/原始数据不符：**
- **β=0 GAR**: 论文 0.029 vs registry **0.028**（5 处引用）
- **β=2 GAR**: 论文 0.075 vs registry **0.062**（21% 偏差，影响 "∼9× recovery" 计算）
- **β=5 GAR**: 论文 0.697 vs registry **0.6795**（疑似数字转位 0.6795→0.6975→0.697，出现在 abstract 等 5 处）

**⚠️ "30×" gap 与 registry 的 32× 不一致**，且论文其他地方用 "20–33×"，内部矛盾。

**其余 91 个数字全部匹配**，包括 Table 1 五方对比、N=50 steering、scheduled sampling、Llama cross-model、instruction retention、gradient conflict、TRC 分析等核心结果。

**建议优先**：到服务器核查 N=5 steering 的 per-conversation 原始数据，确认 β=2 和 β=5 的真实值后再修论文。

---
