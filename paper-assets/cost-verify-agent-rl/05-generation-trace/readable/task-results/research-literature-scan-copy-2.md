# research literature scan

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260516T000327_result.json`
- **Structured JSON:** [`2083f99ce57df87741d8.json`](../../sessions/20/2083f99ce57df87741d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。以下是结果摘要：

## 新增 9 篇论文到 literature_map.yaml

**ALFWorld 新 baseline（4 篇）：**
- **PA-MoE** (2602.17038) — 93.8% ALFWorld，1.5B 小模型新 SOTA，超过 ReflAct prompting (93.3%)
- **SDAR** (2605.15155) — +9.4% over GRPO，May 2026 刚出
- **HCAPO** (2603.08754) — +13.8% over GRPO (7B)，hindsight credit assignment
- **SKILL0** (2604.02268) — +9.7% over GRPO，skill internalization

**方法相关（3 篇）：** ACT (2603.08706), RWML (2602.05842), Fission-GRPO (2601.15625)

**背景（2 篇）：** SelfBudgeter (2505.11274), CoVe (2603.01940)

## 竞争格局判断

**核心 novelty 安全。** 未发现新的直接竞争者。没有论文同时做到 RL-trained binary verify decision + interactive agent + action-change reward signal。ARES 仍是最近的竞争者，但区分点清晰（SFT router + token efficiency reward vs pure RL + action-change signal）。

**ALFWorld 格局大变。** 准确率已饱和至 93.8%（PA-MoE），进一步支持 B-IAVR 聚焦 cost-efficiency 的定位。论文中需更新 baseline 表格。

## 行动项
1. 论文 ALFWorld baseline 表加入 PA-MoE (93.8%)
2. Related Work 加入 SDAR、HCAPO、SKILL0
3. 可选：探索 HCAPO credit assignment 改善 verification reward signal

详细简报已保存到 `artifacts/literature_scan_20260516.md`。

---
