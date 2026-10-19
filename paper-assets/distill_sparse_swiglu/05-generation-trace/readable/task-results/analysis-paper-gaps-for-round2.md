# analysis paper gaps for round2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_gaps_for_round2_20260518T010621_result.json`
- **Structured JSON:** [`f7e58617fa946eef46d5.json`](../../sessions/f7/f7e58617fa946eef46d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here is the complete gap analysis:

---

## Data Gap List (Priority-Ranked)

### 1. 14B KL Uniform — All Metrics Missing
- **位置**: `experiments.tex:245` (commented-out TBD row), `experiments.tex:228` ("uniform results pending")
- **缺什么**: Qwen-14B KL 30% uniform allocation 的 PPL, ARC-c, WG, MMLU, GSM8K 全部缺失
- **当前状态**: 运行中 (4-task eval，无 GSM8K)
- **影响**: **Critical** — 论文 8B 部分的核心叙事是 "uniform allocation 消除 global top-k 的 MMLU 崩塌"。14B KL global MMLU 63.7% 远低于 TEAL 71.8%，如果 uniform 不能恢复，reviewer 会直接质疑 allocation 建议的 generality。结论中写 "three architectures" 但 14B 缺 uniform 数据，claim 不完整。

### 2. 30% KL 3-Seed PPL (8B)
- **位置**: `experiments.tex:49-50` (Table 1 中 30% KL global PPL=8.98, uniform PPL=8.82，均为单 seed)
- **缺什么**: 30% sparsity 的 PPL mean±std (s123, s456)
- **当前状态**: s42 done, s123/s456 训练中
- **影响**: **Important** — 50% 已有 3-seed PPL (11.92±0.07)，30% 作为推荐 operating point 却只有单 seed PPL，reviewer 可能质疑 robustness claim 的一致性。Table 1 caption 已经说明 MMLU 是 3-seed，PPL 不是，这个不对称性容易被注意到。

### 3. BCE ISO-Compute 3-Seed
- **位置**: `experiments.tex:66` (PPL 27.97 单 seed)
- **缺什么**: BCE 2700-step 的 mean±std PPL
- **当前状态**: s456 eval PPL 28.35, s123 eval PPL 28.06, s42 eval 缺失
- **影响**: **Important** — ISO-compute 是回应 "BCE 只是训练不够" 的核心证据。单 seed 对比 (27.97 vs 11.79) 可能被质疑为 cherry-pick。三 seed 均值更有说服力，且现有两个 seed 已确认结论不变 (28.06, 28.35 vs ~11.8)。s42 eval 缺失需确认是否有数据。

### 4. C4 OOD 30% TEAL Baseline
- **位置**: `appendix.tex:161-173` (Table OOD)
- **缺什么**: 30% sparsity 下 TEAL vanilla 的 C4 PPL。50% 有 TEAL baseline (38.75)，30% 只有 KL (16.05) 没有 TEAL 对照
- **当前状态**: 未开始
- **影响**: **Important** — 30% 是推荐 operating point，OOD 只报 KL 不报 TEAL，reviewer 无法判断 OOD 下 KL 的相对优势。50% 可以算出 52.5% advantage，30% 无法算。

### 5. Abstract/Introduction 未提及 14B
- **位置**: `abstract.tex` (全文), `introduction.tex:19` (只提 Mistral-7B)
- **缺什么**: 14B 结果不在 abstract/intro 中，但 `conclusion.tex:5` 写 "three architectures"
- **当前状态**: 文字 gap，不需要新数据
- **影响**: **Important** — Conclusion 声称 "three architectures" 但 abstract 和 intro 只说 Mistral。一旦 14B uniform 数据到位，需要更新 abstract/intro 以包含 scale generalization claim，否则叙事断层。

### 6. 14B Uniform Allocation 缺 GSM8K
- **位置**: `experiments.tex:245`
- **缺什么**: 14B KL uniform 的 GSM8K 评测
- **当前状态**: 当前运行的 4-task eval 无 GSM8K
- **影响**: **Nice-to-have** — 14B global 已有 GSM8K=48.82，如果 uniform 行缺此列会在表格中留空或需要 footnote。但 8B 50% GSM8K 都 <2.2% 近乎随机，reviewer 对此 metric 关注度较低。14B 30% 场景下 GSM8K 差异可能有意义 (global 48.82 vs dense 87.57)。

### 7. 14B 50% Sparsity 数据
- **位置**: 无 — 论文未写 14B 50% 数据
- **缺什么**: 14B 在 50% sparsity 下的表现
- **当前状态**: 未开始
- **影响**: **Nice-to-have** — 8B 的核心故事在 50% 处展开 (49% advantage)。14B 只有 30% 一个点，reviewer 可能问 "14B 在 50% 也有类似 advantage 吗？" 不过这可以在 limitations 中 acknowledge，当前 limitations.tex:5 已写 "scaling behavior to 13B or 70B models remains untested"。

### 8. Limitations 中 14B 表述过时
- **位置**: `limitations.tex:5` — "All experiments use 7--8B parameter models"
- **缺什么**: 文字与 14B 实验矛盾
- **当前状态**: 文字 gap
- **影响**: **Nice-to-have** — 小问题，但 reviewer 会注意到论文自己说 "all 7-8B" 同时有 14B 表格。

---

## 总结

| 优先级 | Gap | 阻塞程度 |
|--------|-----|---------|
| Critical | 14B KL uniform 全指标 | 阻塞 conclusion "three architectures" claim |
| Important | 30% KL 3-seed PPL | 等 s123/s456 训练完成 |
| Important | BCE iso-compute 3-seed | s42 eval 缺失需排查 |
| Important | C4 OOD 30% TEAL baseline | 未开始，需一次 eval |
| Important | Abstract/Intro 加 14B mention | 等 #1 数据到位后改文字 |
| Nice-to-have | 14B uniform GSM8K | 当前 eval 未包含 |
| Nice-to-have | 14B 50% sparsity | 未开始 |
| Nice-to-have | Limitations 文字修正 | 纯文字 |

---
