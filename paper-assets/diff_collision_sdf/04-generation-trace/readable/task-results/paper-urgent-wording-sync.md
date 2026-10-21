# paper urgent wording sync

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_urgent-wording-sync_20260528T055424_result.json`
- **Structured JSON:** [`eac4f07ff753a35c16eb.json`](../../sessions/ea/eac4f07ff753a35c16eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--verify`: 21/21 OK. All files consistent.

---

## 修改报告

### 1. claim3.tex (7 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L7 caption | SDF adds no measurable CAR beyond LoRA-only across the full tested range | SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale |
| L26 body | Adding SDF supervision produces no measurable benefit across the full tested range: | Adding SDF supervision does not yield statistically significant improvement at the tested scale: |
| L26 body | CAR\,=\,57.5\% | CAR\,=\,58.0\% |
| L26 footnote | Single seed (s2); computational constraints precluded additional seeds for this ablation. | At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints. |
| L26 body | confirming that SDF gradients produce no lasting behavioral effect | suggesting that SDF gradients do not produce a lasting behavioral effect |
| L32 | SDF supervision is redundant with the demonstration signal across the full tested range | SDF supervision does not produce statistically significant benefit across the tested range |
| L46 caption | confirming full redundancy of EE-only SDF supervision across a 20×... | consistent with the absence of statistically significant improvement across a 20×... |

### 2. abstract.tex (2 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L5 | SDF supervision adds no measurable benefit across the full tested range... ($p > 0.05$ for all; | SDF supervision shows no statistically significant benefit at the tested scale... ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; |
| L6 | EE-only geometric supervision is fully redundant...confirming that collision avoidance arises from demonstration data, not geometric supervision | EE-only geometric supervision does not significantly improve collision avoidance...suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision |

### 3. introduction.tex (2 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L20 | produces no measurable benefit across the full tested range...($p > 0.05$ for all;...accounts for all observed avoidance | does not yield statistically significant improvement across the tested range...($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$;...primarily accounts for observed avoidance |
| L27 | account for all measured CAR gains...adds no measurable benefit across the full tested range...($p > 0.05$ for all, | account for nearly all measured CAR gains...shows no statistically significant benefit across the tested range...($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$, |

### 4. discussion.tex (3 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L3 | not geometric supervision, account for the measured avoidance gains | account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement |
| L6 | confirming that Level~A signal masking is not the binding constraint---the failure is architectural | suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway |
| L6 | Demonstration data subsumes | Demonstration data largely subsumes |

### 5. paper_switch.py 模板更新

- **old strings 更新**: 6 个块（#1, #2, #4, #6, #7, #8）+ 2 个 Scenario-C-only 块（#9, #10）
- **Scenario B new strings 更新**: 6 个块（#1, #2, #4, #6, #7, #8, #10）
- **Scenario C new strings 更新**: 5 个块（#1, #4, #6, #7, #10）—消除 "fully redundant"/"adds no measurable" 等绝对措辞
- **总计**: ~17 个模板文本更新

### 6. --verify 结果

```
Scenario B: 10/10 OK
Scenario C: 11/11 OK
```

---
