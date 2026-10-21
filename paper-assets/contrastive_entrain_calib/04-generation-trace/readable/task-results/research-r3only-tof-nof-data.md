# research r3only tof nof data

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r3only-tof-nof-data_20260522T142150_result.json`
- **Structured JSON:** [`9a857adab00641535d9a.json`](../../sessions/9a/9a857adab00641535d9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完成。汇总如下：

---

## 任务 1: R3-only ToF / NoF / SYCONScore 分项数据

### Seed 1 (exp-003) — 12 个 checkpoint

| Checkpoint | ToF | NoF | SYCONScore |
|------------|-------|--------|------------|
| 1000 | 0.0387 | 0.9448 | 0.0743 |
| 2000 | 0.0442 | 0.9834 | 0.0846 |
| 3000 | 0.0497 | 0.9724 | 0.0946 |
| 4000 | 0.0608 | 0.9669 | 0.1144 |
| 4500 | 0.0718 | 0.9613 | 0.1337 |
| 5000 | 0.0608 | 0.9669 | 0.1144 |
| 5500 | 0.0608 | 0.9724 | 0.1144 |
| 6000 | 0.0442 | 0.9724 | 0.0846 |
| 6500 | **0.0829** | **0.9834** | **0.1529** |
| 7000 | 0.0552 | 0.9724 | 0.1046 |
| 7500 | 0.0552 | 0.9724 | 0.1046 |
| 8000 | 0.0773 | 0.9724 | 0.1433 |

### Seed 2 (exp-003-s2) — 15 个 checkpoint

| Checkpoint | ToF | NoF | SYCONScore |
|------------|-------|--------|------------|
| 500 | 0.0442 | 0.9503 | 0.0845 |
| 1000 | 0.0442 | 0.9448 | 0.0844 |
| 1500 | 0.0552 | 0.9503 | 0.1044 |
| 2000 | 0.0442 | 0.9779 | 0.0846 |
| 2500 | 0.0552 | 0.9724 | 0.1046 |
| 3000 | 0.0497 | 0.9503 | 0.0945 |
| 3500 | 0.0387 | 0.9724 | 0.0744 |
| 4000 | **0.0773** | 0.9392 | **0.1429** |
| 4500 | 0.0552 | 0.9503 | 0.1044 |
| 5000 | 0.0552 | 0.9503 | 0.1044 |
| 5500 | 0.0608 | 0.9724 | 0.1144 |
| 6000 | 0.0497 | 0.9503 | 0.0945 |
| 6500 | 0.0552 | 0.9779 | 0.1046 |
| 7000 | 0.0497 | 0.9503 | 0.0945 |
| 7500 | 0.0608 | 0.9669 | 0.1144 |

**"High NoF, near-zero ToF" 模式完全成立：**
- ToF 范围：3.9%–8.3%（极低，模型几乎不接受正确纠正）
- NoF 范围：93.9%–98.3%（极高，模型几乎完美拒绝错误诱导）
- 两个 seed 的模式高度一致：R3-only 训练让模型变得极度 stubborn，NoF 接近 ceiling 但 ToF 接近 floor

---

## 任务 2: Stubbornness Taxonomy 百分比

找到 `/root/contrastive_entrain_calib/results/mechanistic_analysis/stubbornness_taxonomy/taxonomy_summary.json`（基于 exp008v3_ckpt500，181 个 valid correction case，ToF=0 即全部 stubborn）：

| Category | Count | Pct | Description |
|----------|-------|-----|-------------|
| **deliberate_inconclusive** | 52 | **28.7%** | 模型长篇推理、提到正确答案，但始终不 commit |
| **surface_compliance** | 44 | **24.3%** | 用 "you're right" 等语表面服从，实际未改答案（sycophantic stubbornness）|
| **acknowledge_but_maintain** | 43 | **23.8%** | 用 "however/but" 承认用户输入后坚持原答案 |
| **genuine_accept_missed** | 34 | **18.8%** | NLI entailment >0.5，可能确实接受了但被 truncate 或 eval 漏判 |
| refute_user | 3 | 1.7% | 直接反驳用户纠正 |
| deliberate_but_ignore | 3 | 1.7% | 推理中完全没提到正确答案 |
| other | 2 | 1.1% | 不属于以上任何类别 |

已知的 53%（sycophantic stubbornness 24.3% + deliberation traps 28.7%）之外，剩余 47% 的分布：
- **acknowledge_but_maintain: 23.8%** — 最大一块，承认但不改
- **genuine_accept_missed: 18.8%** — eval 可能漏判（95.6% 的回答被 truncate 在 max_new_tokens=512）
- refute_user + deliberate_but_ignore + other: 4.5% — 边缘类别

额外发现：95.6% 的 response 在 512 token 处被截断，158/181 以 "Ah" 开头，模型在 `enable_thinking=False` 时仍输出推理式内容。

---

## 任务 3: Checkpoint 数量

| Seed | Eval 数量 | Checkpoint 编号 |
|------|----------|----------------|
| Seed 1 | **12** | 1000, 2000, 3000, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000 |
| Seed 2 | **15** | 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500 |
| **合计** | **27** | |

数据分布在三个目录：
- `results/exp003_d027_eval/` — Seed 1 全部 12 个 + Seed 2 的 ckpt2000–7000（11 个）
- `results/exp003_s2_unified_eval/` — Seed 2 的 ckpt500, 1000, 1500（3 个）
- `eval_results/exp-003-s2-ckpt7500/` — Seed 2 的 ckpt7500（1 个）

---
