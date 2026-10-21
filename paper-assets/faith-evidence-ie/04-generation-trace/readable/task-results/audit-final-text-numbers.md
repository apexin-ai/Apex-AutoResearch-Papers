# audit final text numbers

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final-text-numbers_20260524T042713_result.json`
- **Structured JSON:** [`b6260b91c20e20e2a895.json`](../../sessions/b6/b6260b91c20e20e2a895.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入并注册。

**审计结果概要：**

- **~150+ 定量声明** 全部追溯到 registry experiment ID 或 table cell
- **0 个错误**
- **2 个 ⚠️ 轻微 rounding 问题**（均为 0.01pp）：
  - DPO 1ep Rel-F1: 论文写 33.37，registry 值 0.33375 标准四舍五入应为 33.38
  - tab:ablation_full RSFT CED s42 Evi-F1: 表中 81.74，registry 值 81.75
- **3 个 ❓ 无法从 registry 完整验证**（不一定有误）：
  - 8B RSFT dev inference-time tax (−0.78pp)：s42 k=1 with-evi eval 未在 registry 中找到
  - LLaMA RSFT dev inference-time tax (−2.17±0.76pp)：std 匹配但 mean 无法从可用数据重建
  - tab:cross_detail 14B 混用 @1024/@2048 protocol（数值正确但未在表注说明）
- **跨位置一致性**：所有在 abstract/intro/experiments/conclusion 中重复出现的数字完全一致
- **小数位数**：全篇统一（Ign-F1 2位、EDCR 4位等）
- **最近修改值**（1.7B test tax −5.01±0.59pp、14B +0.43±0.49pp、8B Evi-F1 81.54）均已正确更新

---
