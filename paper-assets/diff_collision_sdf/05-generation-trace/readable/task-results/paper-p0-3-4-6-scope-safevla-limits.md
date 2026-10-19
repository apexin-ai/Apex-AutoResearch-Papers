# paper p0 3 4 6 scope safevla limits

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p0-3-4-6-scope-safevla-limits_20260528T060943_result.json`
- **Structured JSON:** [`8bb46747c3aa25626e68.json`](../../sessions/8b/8bb46747c3aa25626e68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。下面是修改汇总：

---

### related_work.tex

**新增** `\paragraph{SDF integration pathways.}`（第12行，"Signed Distance Functions in Robotics" 和 "Evaluation Metrics" 之间）：
- 区分三种 SDF 集成路径：(a) training-time auxiliary loss, (b) constraint-based planning (SafeVLA), (c) runtime filtering (VLSA)
- 明确本文负面发现仅适用于 pathway (a)
- 引用键 `zhang2025safevla` 和 `hu2025vlsa` 均已验证存在于 bib 中

---

### discussion.tex

**4 处修改**：

1. **第6行末尾新增** pathway-specific 句子：
   > "The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms."

2. **第11行新增** `\paragraph{Scope and generalizability.}`（Implications 和 Limitations 之间）：
   - 明确列出 scope：1 benchmark, 2 model families, 4 tasks, MuJoCo simulation
   - 区分 Claim 1 的结构通用性 vs. prevalence 的 benchmark-specificity
   - Claim 3 限定为 EE-only auxiliary loss pathway，引用 `\ref{sec:related}`

3. **第13-14行替换** Limitations 段落：
   - **新增**：sim-to-real gap 不确定性、sensor noise 影响、task diversity 限制、统计功效（n=3, ~5pp MDE at 80% power）
   - **保留**：原有的 oracle frozen model、full-body SDF untested、TSR degradation 内容

4. **第19-20行替换** Broader Impact 段落：
   - **改前**：2 句（dfCAR exposes gap）
   - **改后**：3 句——dfCAR 定位为 diagnostic complement、SDF redundancy 是 methodology insight 而非对 safety training 的否定、警告不要过度解读

---

### introduction.tex

未修改。"case study" 和 "we demonstrate" 在当前版本中均不存在（已被前一个 Worker 处理）。

---
