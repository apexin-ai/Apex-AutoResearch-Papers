# harvest westd 49937 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_westd-49937-check_20260526T195929_result.json`
- **Structured JSON:** [`2bac9ba699eb64f8bce4.json`](../../sessions/2b/2bac9ba699eb64f8bce4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6/6 registry 已更新为 DONE。

## westd-49937 实验状态

| exp_id | PID | 状态 | SR | paired VLA-only | trigger_rate | 备注 |
|--------|-----|------|----|-----------------|-------------|------|
| **CRM K=2 always-on** |
| westd-pi05-crm-k2-object-s42 | 491271 | DONE | **87.0%** | 99.5% (Δ=-12.5pp) | N/A (always-on) | ketchup 50% 最差 |
| westd-pi05-crm-k2-object-s43 | 491696 | DONE | **87.0%** | 100% (Δ=-13pp) | N/A (always-on) | ketchup 65% 最差 |
| westd-pi05-crm-k2-object-s44 | 492088 | DONE | **88.0%** | 99.5% (Δ=-11.5pp) | N/A (always-on) | cream_cheese/ketchup 65% 并列最差 |
| **CRM K=2 avg** | | | **87.3%** | **99.7%** (Δ=-12.3pp) | | |
| **Adaptive (τ=0.25)** |
| westd-pi05-adaptive-object-s42-paired | 492479 | DONE | **83.5%** | 99.5% (Δ=-16pp) | 3.46% | ketchup 45% 最差 |
| westd-pi05-adaptive-object-s43-paired | 492867 | DONE | **87.0%** | 100% (Δ=-13pp) | 3.83% | ketchup 65% 最差 |
| westd-pi05-adaptive-object-s44-paired | 493251 | DONE | **87.0%** | 99.5% (Δ=-12.5pp) | 3.90% | ketchup 60% 最差 |
| **Adaptive avg** | | | **85.8%** | **99.7%** (Δ=-13.8pp) | **3.73%** | |

**关键发现：**
- CRM K=2 和 Adaptive 均显著 harm Object suite（-12~14pp），符合预期
- Adaptive 尽管 trigger rate 仅 ~3.7%，SR 反而比 CRM-always 略低（85.8% vs 87.3%），说明 adaptive gating 在 near-ceiling Object suite 上无法恢复 harm——即使少量触发也是有害的
- ketchup 在所有 6 个实验中一致最差（45-65%），是主要 failure mode
- westd 6 卡全部释放

---
