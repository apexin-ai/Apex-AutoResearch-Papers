# knowledge refresh supp summary

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_refresh-supp-summary_20260528T162015_result.json`
- **Structured JSON:** [`fe7b3cc937bc3d1e21d6.json`](../../sessions/fe/fe7b3cc937bc3d1e21d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`supplementary_summary.md` 已从 registry 实际数据重建。

**核心修复**：旧版漏读了 `overall_success_rate` 字段（只认 `success_rate`），导致大量实验被误判为无 SR。

**数据变化对比**：

| 类别 | 旧版 | 新版 |
|------|------|------|
| **B. Bonus seeds** | | |
| long / adaptive | 0 valid | **4 seeds** (s44-47, SR=57.4±2.3) |
| long / crm_obs_only | 1 seed | **6 seeds** (s42-47) |
| long / reconvla | 2 seeds | **6 seeds** (s42-47) |
| long / vla_only | 3 seeds | **6 seeds** (s42-47) |
| object / adaptive | 1 seed | **6 seeds** (s42-47) |
| object / crm_obs_only | 1 seed | **6 seeds** (s42-47) |
| goal / reconvla | 2 seeds | **5 seeds** (s43-47) |
| goal / crm_obs_only | 5 seeds | **7 seeds** (+s43,s48) |
| **C. Pi05** | | |
| long / crm_obs_only | 1 seed | **3 seeds** (s42-44) |
| **E. CRM always-on** | | |
| pi05 / goal | 1 seed | **3 seeds** |
| smolvla / long | 3 seeds | **4 seeds** (+s45) |

**剩余真实缺口**（Section F）：
- goal / reconvla: 5 seeds（差1）
- long / adaptive: 4 seeds（差2）
- pi05 / long CRM always-on: 2 seeds（差1）
- pi05 / spatial CRM always-on: 1 seed（差2）

---
