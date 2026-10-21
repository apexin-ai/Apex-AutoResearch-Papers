# audit tex wording consistency

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tex_wording_consistency_20260524T063738_result.json`
- **Structured JSON:** [`9b0d66de02d62c925426.json`](../../sessions/9b/9b0d66de02d62c925426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here is the full audit:

---

## CIVO Rate 声明清单

| 文件:行 | 声明原文 | 注释 |
|---------|---------|------|
| `introduction.tex:12` | "6/6 seeds, two locomotion environments" | CIVO onset。**一致** |
| `results.tex:77` | "Three trajectory types emerge: early collapse (seed~0), late-onset collapse (seed~3), and self-correction (seed~2)" | 描述 Walker 4 seeds 中的 3 种轨迹。**一致** |
| `results.tex:81` | "CIVO onset is universal across all six tested seeds (n=6) with 5/6 progressing toward collapse" | onset=6/6, collapse=5/6。**一致，措辞精确** |
| `results.tex:109` | "1/6 CIVO prevention (1/4 Walker, 0/2 Cheetah)" | obs-decoder SGS 的 prevention rate。**一致** |
| `results.tex:139` | "5/5" (embedding removed prevention) | 移除 embedding 的 prevention。**一致** |
| `results.tex:143` | "Walker 2/4 (s2 NVE 2.11×; s3 late-onset CIVO)" | partial gradient blocking。**一致** |
| `results.tex:146` | "Walker 3/3 (nve ≤ 1.4×; 1/3 non-CIVO eval collapse)" | wide dual-critic。**一致** |
| `results.tex:147` | "Walker 5 + Cheetah 2" frozen seeds, 2/7 transient | **一致** |
| `results.tex:179` | "TPR=5/5, FPR=2/9, predictive alerts in 2/5 cases" | detector 性能。**一致** |
| `introduction.tex:15` | "100% sensitivity (5/5) with predictive warning in 2/5 cases" | detector。**一致** |
| **`analysis.tex:8`** | **"sustained CIVO (6/6 trained locomotion, NVE 1.53--108×)"** | **⚠️ 不一致** |
| `appendix.tex:105-106` | "Walker Walk 4/4, Cheetah Run 2/2" | CIVO onset。**一致** |
| `appendix.tex:117` | "Task B1 restricts to sustained CIVO... Transient CIVO (e.g., exp 009b) classified as negative in B1" | 明确区分 sustained vs transient |
| `appendix.tex:132-133` | "006 sustained CIVO B1+; 008d sustained CIVO B1+" | B1 labels。**一致** |
| `appendix.tex:136` | "009b transient CIVO B1−, B2+" | seed 2 是 transient，非 sustained |
| `appendix.tex:224` | "Task B1 (sustained CIVO only), n_pos = 3" | 10 个 factorial 中只有 3 个 sustained |
| `appendix.tex:596` | "Walker s2 (009b): Transient CIVO" | post-CIVO outcome table |
| `appendix.tex:608` | "Full collapse is the majority outcome (5/6), with one self-correction case (Walker seed 2)" | **一致** |
| `rebuttal_notes.md:17` | "5/6 collapse, 1/6 self-correction (Walker seed 2, 29.3% of baseline)" | **一致** |

---

## 核心矛盾

**`analysis.tex:8` 说 "sustained CIVO (6/6 trained locomotion)"，但论文自身的 B1/B2 分类体系明确将 Walker seed 2 (009b) 归为 transient CIVO (B1 negative)。**

- `results.tex:81` 正确表述为 "CIVO **onset** is universal across all six tested seeds"，用 onset 而非 sustained
- `appendix.tex:608` 正确表述为 "5/6 collapse, 1/6 self-correction"
- `appendix.tex:117` 明确定义 sustained = "persistent, accelerating value overestimation that progresses to performance collapse"，seed 2 不符合

**修正建议**：`analysis.tex:8` 应改为 "CIVO (6/6 trained locomotion)" 或 "CIVO onset (6/6 trained locomotion)"，去掉 "sustained"。

---

## "onset" vs "sustained" 是否区分清楚？

论文 **确实做了区分**，但不够一致：
- **onset** = NVE 超过 1.5× 阈值（6/6 都有）
- **sustained** (B1) = 持续加速的 value overestimation 并导致 collapse（排除 seed 2）
- **transient** = onset 后自我纠正（seed 2, 009b）

`results.tex` 和 `appendix` 的用词是准确的，唯独 `analysis.tex:8` 把 "sustained" 错误地扩展到了 6/6。

---
