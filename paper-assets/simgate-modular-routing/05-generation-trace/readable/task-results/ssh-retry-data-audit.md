# ssh retry data audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-data-audit_20260518T031355_result.json`
- **Structured JSON:** [`ffb617898e0feffd7448.json`](../../sessions/ff/ffb617898e0feffd7448.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是结构化排查报告。

---

## 排查报告：Retry Per-Trial 数据异常

### 1. 分析脚本逻辑

**脚本路径**: `/root/autodl-tmp/simgate-modular-routing/analyze_retry_dose_response.py`

**DR(N) 计算逻辑**:
```
DR(N) = P(前 N 次 trial 全部 is_death=True)
```
- 取 `trials[:N]`，检查 `all(t["is_death"] for t in first_n) and len(first_n) == N`
- 若 episode 因 early success 只有 < N 次 trial，`len(first_n) < N` → 不计为 death（正确）
- `is_death` 定义：`score <= -100`（DEATH_THRESHOLD = -100）
- 正确排除了 `find-non-living-thing`

**Bug 检查结果：无 bug**。逻辑正确，off-by-one 无误（trial_idx 从 0 开始，N 从 1 开始）。

**独立验证的 per-trial 和 cumulative DR（retry, death-prone 200 eps）**:

| 指标 | 值 |
|------|-----|
| **Per-trial DR** | Trial 0: 93/200=46.5%, Trial 1: 93/185=50.3%, Trial 2: 90/184=48.9% |
| **Cumulative DR(N)** | DR(1): 93/200=46.5%, DR(2): 89/200=44.5%, DR(3): 83/200=41.5% |
| **Cumulative rescue** | 1→2: 4/93=4.3%, 2→3: 6/89=6.7% |
| **Conditional rescue** | 0→1: 4/93=4.3%, 1→2: 6/93=6.5% |

**Score vs is_death 一致性**: 0 个不一致。

**关键发现**: per-trial DR 在 3 次 trial 间高度稳定（46.5%→50.3%→48.9%），trial 1/2 略高是因为分母只含"未早期成功"的更难 episode。cumulative rescue 1→2 (4.3%) 和 2→3 (6.7%) 差异不大，**不存在 Reviewer 所述的 9 倍差异（4.3% vs 39.3%）**。

### 2. 种子/配置

- `random.seed(42)` 仅在 `main()` 开头设置一次，不影响 trial 行为（代码中无 `random.choice` 等调用）
- LLM 随机性来自 `temperature=0.3`（vLLM server-side sampling），每次 trial 独立采样
- ScienceWorld 环境：`create_env(task_name, variation_idx)` 创建新 JVM 进程，无 seed 参数，同 task+variation 的初始状态**确定性相同**
- 每次 trial 环境完全重置（新 JVM），不携带前序 trial 状态

**结论**: 3 次 trial 之间 LLM 采样独立，环境初始状态相同。不存在种子导致的高度相关结果。low temperature (0.3) 限制了采样多样性，但仍有足够随机性产生不同 action trajectory。

### 3. 数据来源一致性

| 数据集 | 首文件时间 | 末文件时间 |
|--------|-----------|-----------|
| reflexion_baseline_part1 | 2026-05-17 22:01 | — |
| reflexion_baseline_part2 | — | 2026-05-18 00:20 |
| retry-control | 2026-05-17 22:58 | 2026-05-18 00:33 |

- 所有数据在同一 session（~2.5 小时内）生成
- 使用相同 vLLM server（Qwen2.5-7B-Instruct, localhost:8000）
- `results/retry_dose_response/` 目录不存在 — N=1,5,10 的独立 dose-response 实验未运行
- **数据来源一致，无多批混合问题**

### 4. Table 4 DR 定义

**答案：(A) 和 (B) 都不准确。实际是：**

> **Table 4 "Retry (3×): DR = 40.9%" = `final_is_death` across ALL 220 episodes（含 find-non-living-thing）**

验证：
- final_is_death (all 220): **90/220 = 40.9%** ← 完全匹配
- all-3-death cumulative (all 220): 83/220 = 37.7% ← 不匹配
- all-3-death cumulative (DP 200): 83/200 = 41.5% ← 不匹配
- final_is_death (DP 200): 90/200 = 45.0% ← 不匹配

**关键区别**: Table 4 的 40.9% 是 "最终 trial 结果为 death"，而 dose-response 分析的 DR(3)=41.5% 是 "3 次 trial 全部 death"。两者差 7 个 episode — 这 7 个 episode 中某次 trial 得分 0（非 death 非 success），但最终 trial 仍为 death。

具体的 7 个 episode 的 death pattern：
```
chemistry-mix var=3:   [False, True, True]  scores=[0, -100, -100]
chemistry-mix var=16:  [True, False, True]  scores=[-100, 0, -100]
grow-fruit var=5:      [False, True, True]  scores=[0, -100, -100]
grow-fruit var=12:     [False, True, True]  scores=[0, -100, -100]
lifespan-ll-then-sl var=9:  [True, False, True]  scores=[-100, 0, -100]
lifespan-ll-then-sl var=12: [True, False, True]  scores=[-100, 0, -100]
measure-melting var=16: [False, True, True]  scores=[0, -100, -100]
```

### 5. 结论

**数据可信。分析脚本无 bug。**

| 问题 | 结论 |
|------|------|
| 脚本逻辑 bug？ | 无。DR(N)="前 N 次全 death" 逻辑正确 |
| 4.3% vs 39.3% 异常？ | **无法复现**。retry 内部 rescue rate 1→2=4.3%, 2→3=6.7%，差异在正常范围 |
| 种子问题？ | 无。环境确定性，随机性仅来自 LLM sampling |
| 数据一致性？ | 同一 session 生成，无多批混合 |
| Table 4 定义混淆？ | **是的**。Table 4 (40.9%) = final_is_death/220; dose-response DR(3) (41.5%) = all-3-death/200。两个定义不同 |

**Reviewer 所述 39.3% 的可能来源**:
1. Reflexion 的 per-trial DR trial 1 = 73/185 = **39.5%**（接近 39.3%），可能被误读为 rescue rate
2. 可能来自 Table 4 定义（final_is_death）和 dose-response 定义（cumulative all-death）之间的混淆

**建议**:
1. 论文中明确 DR 的定义 — "final-outcome death rate"（Table 4）vs "cumulative all-trial death rate"（dose-response）
2. 如果 dose-response 分析要与 Table 4 对比，统一使用 final_is_death 定义，或明确标注区别
3. Retry 的 per-trial rescue rate（4.3%~6.5%）vs reflexion（26.1%~21.9%）的对比是有效的 — 证明 retry 几乎无 rescue 效果而 reflexion 有效

---
