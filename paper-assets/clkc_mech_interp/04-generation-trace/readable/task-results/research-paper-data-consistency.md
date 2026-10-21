# research paper data consistency

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-data-consistency_20260524T065859_result.json`
- **Structured JSON:** [`8ded4025f78e3f7ee40f.json`](../../sessions/8d/8ded4025f78e3f7ee40f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. Table 3 (tab:steering) 当前内容

文件：`docs/paper/experiments.tex:168-200`

**Llama-3.1-8B (隐式标题，N=136):**
| Layer | Depth | α | Steer% | Ctrl% | Fisher p | Dir |
|-------|-------|---|--------|-------|----------|-----|
| **L13** | 41% | +5 | 19.9 | 6.6 | **0.002** | 4 p→c |
| **L13** | 41% | -20 | 36.0 | 17.6 | **<0.001** | 5 c→p |
| L16 | 50% | +5 | 8.8 | 8.1 | 1.000 | |
| L16 | 50% | +10 | 18.4 | 11.0 | 0.123 | |
| L16 | 50% | +20 | 22.8 | 24.3 | 0.886 | |
| L18 | 56% | +2 | 3.7 | 1.5 | 0.447 | |
| L28 | 88% | -20 | 14.7 | 16.9 | 0.740 | |
| L28 (all) | 88% | -20 | 11.8 | 11.8 | **1.000** | |

**Qwen3-8B (N=84):** L14 p=0.682, L23 p=1.000
**Gemma-2-9B-IT (N=158):** L17 p=0.104, L21 p≥0.623

Table 3 不含 probe accuracy 列、不含 N 列。

---

## 2. Appendix 内容

`main.tex` 中有三个 Appendix：

- **Appendix A** (app:ai-assistants) — AI 使用声明
- **Appendix B** (app:boundary) — Fine-Grained Causal Boundary Analysis (tab:boundary, N=201, 独立复制实验)

  | Layer | Depth | Probe Acc | Best α | Best p | Bonf. Sig. |
  |-------|-------|-----------|--------|--------|------------|
  | L12 | 38% | 91.75% | +20 | 0.085 | 0/6 |
  | **L13** | 41% | 90.00% | +10 | **<0.001** | **2/6** |
  | L14 | 44% | 91.75% | +10 | 0.002 | 1/6 |
  | L16 | 50% | 91.50% | +10 | 0.005 | 1/6 |
  | L18 | 56% | **90.75%** | +5 | 0.010 | 0/6 |
  | L28 | 88% | 85.25% | +10 | **0.284** | 0/6 |

- **Appendix C** (app:steering_config) — Complete Steering Configuration (tab:steering_config, 汇总所有模型)

  Llama L18 行：probe acc = **---**（缺失），best p = 0.447
  Llama L28 行：probe acc = 77.6，best p = 0.740

---

## 3. L18 probe accuracy 出现位置

- **Appendix B** `main.tex:78`：L18 probe acc = **90.75%** ✓（N=201 新数据）
- **Appendix C** `main.tex:102`：L18 probe acc = **---**（N=136 旧数据，未填写）
- **Qwen L18** `main.tex:107`：73.8%（这是 Qwen 的 L18，不是 Llama 的）
- **Table 3**：无 probe accuracy 列

结论：L18 的 90.75% 仅出现在 Appendix B（N=201），Appendix C 的 Llama L18 probe accuracy 缺失。

---

## 4. L28 p 值一致性

各处 L28 p 值：

| 位置 | 实验 | p 值 | 一致？ |
|------|------|------|--------|
| Table 3 L28 行 | N=136 | 0.740 | ✓ |
| Table 3 L28 (all) 行 | N=136 | **1.000** | ⚠️ |
| Appendix C (tab:steering_config) | N=136 | 0.740 (best) | ✓ |
| Appendix B (tab:boundary) | N=201 | **0.284** | ✓ |
| 正文 `experiments.tex:151` | N=201 | 0.284 | ✓ (正确归因) |
| 正文 `experiments.tex:154` | N=136 | "all p > 0.3" | ✓ |
| `artifacts/_project/paper/experiments.tex:159` | N=136 | **0.370** | ⚠️ 与 docs 版不同 |

N=201 (0.284) 和 N=136 (0.740) 是不同实验，不构成不一致。文中正确区分了来源。

---

## 5. 发现的数据不一致问题

### ⚠️ 问题 1：L28 (all) p 值在两版 experiments.tex 中不同
- `docs/paper/experiments.tex:185`：L28 (all) p = **1.000**
- `artifacts/_project/paper/experiments.tex:159`：L28 (all) p = **0.370**
- 两处的 flip rate 完全相同（steer 11.8%, ctrl 11.8%）
- 如果 flip rate 真的相等，Fisher p 应为 1.000，0.370 可能是旧版错误
- 但也可能是百分比四舍五入掩盖了实际计数差异——需要回查原始数据确认

### ⚠️ 问题 2：Appendix C 中 Llama L18 probe accuracy 缺失
- `main.tex:102`：`L18 & 56\% & --- & 0.447`
- 其他层都有 probe accuracy 值，唯独 L18 标记为 ---
- 旧实验 (N=136) 的 L18 probe accuracy 应该有数据，建议补充

### ⚠️ 问题 3：用户报告的旧数据 best p 与论文不匹配
- 用户提供：N=136 旧数据 L28 best p = **0.31**（steering_107）
- 论文 Appendix C：L28 best p = **0.740**
- 差异很大（0.31 vs 0.740），需要回查实验日志确认哪个是正确值

### 注意项：L18 p=0.010 的"non-significance"措辞
- `experiments.tex:151`：*"diminishing to non-significance at L18 ($p = 0.010$)"*
- p=0.010 在名义 α=0.05 下是显著的，仅在 Bonferroni 校正后才不显著（0/6）
- 当前措辞可能让读者误解，建议加上 "after Bonferroni correction" 限定

---
