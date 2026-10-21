# code plan 016 within subject injection

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_016_within_subject_injection_20260520T223139_result.json`
- **Structured JSON:** [`c1172eadee753ba2a8ef.json`](../../sessions/c1/c1172eadee753ba2a8ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 016 完成。核心结果：

**成功标准达成（2/3 subjects ΔTPR > 0.3 at p=0.5）**

| Subject | N items | ΔTPR(p=0.5) | ΔTPR(p=1.0) | Fisher p(0.5) |
|---------|---------|-------------|-------------|---------------|
| human_aging | 203 | **+0.385** | +0.685 | 0.0013 |
| professional_medicine | 248 | **+0.327** | +0.694 | 0.006 |
| business_ethics | 93 | -0.078 | +0.400 | 0.60 |

关键发现：
- **≥200 items 的 subject**：within-subject MH-DIF 在 p=0.5 即可显著检测注入信号，ΔTPR 与 plan_011 全局结果量级一致
- **business_ethics（93 items）**：baseline FPR 已达 56%（matching variable 只有 93 项，精度不足），p=0.5 信号被噪声淹没，但 p=1.0 仍能完美检测（TPR=1.0, Fisher p=0.001）
- 这验证了 plan_014 发现的 ~38% within-subject temporal C% 是真实信号，而非方法缺陷

---
