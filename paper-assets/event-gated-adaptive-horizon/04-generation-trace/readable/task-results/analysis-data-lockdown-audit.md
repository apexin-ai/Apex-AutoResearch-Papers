# analysis data lockdown audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_data-lockdown-audit_20260526T063759_result.json`
- **Structured JSON:** [`f3f5f4a46a6bdc704d6f.json`](../../sessions/f3/f3f5f4a46a6bdc704d6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/_project/report/data_lockdown_audit.md`。

核心结论：

**8/8 Claims 均有已完成实验支撑，无高风险项。**

关键发现：
- **证据最强**：C2 (0/19 controls vs 7/8 trained, Fisher p<0.0001)、C7 (SGS 1/17)、C8 (三层 Hierarchy)
- **2 个 RUNNING 实验** (exp_097 Cheetah s3 @65K, exp_100 Walker 008a s1) 预计 ~4h 后完成，补充而非填补证据
- **exp_097 已检测到 CIVO onset @45K**，完成后 Cheetah onset rate 大概率升至 3/4
- **exp_102/103 非必须** — 已有 008a_cheetah_unexposed_s0/s1 覆盖 C3 Cheetah
- **待整合**：RSSM fidelity v3 Walker 数字（已分析完）需替换论文旧值；Cheetah v3 需 exp_097 checkpoint

锁定前 action items：确认 097/100 完成 → NVE 分析 → RSSM v3 合并 → 论文数字更新 → 锁定声明。

---
