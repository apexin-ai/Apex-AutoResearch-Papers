# research ref verify websearch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-verify-websearch_20260526T104021_result.json`
- **Structured JSON:** [`5efe0641dd961cf1dbed.json`](../../sessions/5e/5efe0641dd961cf1dbed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证报告已写入 `artifacts/ref-audit/websearch_verification.md`。

**9 条引用中 7 条需修改，2 条待核对 bib 确认**。关键发现：

| 论文 | 核心问题 |
|------|----------|
| **ToolACE** | 第一作者是 Liu, Weiwen，不是 Zhang |
| **Reflexion** | Edward Berman **确实是**第三作者，Director 疑虑可排除 |
| **Agent-SafetyBench** | 实际 7 人，bib 多了 3 个不存在的作者；第五作者是 Junxiao 非 Junhao |
| **AutoMix** | 实际 13 人，bib 仅 6 人，多处姓名错误，Tandon 不在作者列表中 |
| **SALT** | 第三作者是 Qiaojing Yan，不是 David Yan |
| **Amitai 2024** | 第二作者是 Yael Septon，不是 Guy Septon |
| **Bonagiri 2025** | 作者顺序确认为 Bonagiri → Kumaraguru → Nguyen → Plaut |
| **Pona 2025** | 已被 NeurIPS 2025 正式接收，venue 需从 arXiv 更新 |
| **Gajcin 2023** | 是 Doctoral Consortium 论文，非正式会议论文 |

---
