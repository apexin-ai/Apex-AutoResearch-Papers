# ops paper headline verification

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_paper-headline-verification_20260516T041928_result.json`
- **Structured JSON:** [`571b2b54f48b7c67e042.json`](../../sessions/57/571b2b54f48b7c67e042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整审计报告。

---

## Headline 数字一致性审计报告

### 结论：❌ **FAIL** — 大量旧 n=50 pilot 数字仍未替换为 n=500 registry 数字

---

### 一、旧 pilot 数字 0.32→9.94（必须消除）

| 状态 | 文件:行 | 当前值 | 应改为 |
|------|---------|--------|--------|
| ❌ | `results.tex:117` | DS Δ=**0.32** [0.20, 0.47] | **0.39** [需 n=500 CI] |
| ❌ | `results.tex:120` | DS Δ=**9.94** [8.39, 16.65] | **8.48** [需 n=500 CI] |
| ❌ | `appendix_disc_analysis.tex:46` | 注释 `median_diff=9.9436 at s030` | 8.48 |

### 二、segment-level 14.59 → 应为 per-problem paired 8.48（registry 定义）

registry 将 median_diff 定义为 `median(II_low_i − II_high_i)`（per-problem paired），Table 1 正确值为 **0.39→1.21→3.99→8.48**。当前全文仍用旧 segment-level 14.59。

| 状态 | 文件:行 | 当前值 | 应改为 |
|------|---------|--------|--------|
| ❌ | `abstract.tex:7` | `$14.59$ at $s{=}0.30$` | **8.48** |
| ❌ | `introduction.tex:14` | `$14.59$ at $s{=}0.30$` | **8.48** |
| ❌ | `results.tex:8` | `$14.59$ at $s{=}0.30$---a $37{\times}$` | **8.48**, 倍率→~22× |
| ❌ | `results.tex:19` (Table 1) | `0.39 & 1.48 & 7.16 & 14.59` | **0.39 & 1.21 & 3.99 & 8.48** |
| ❌ | `results.tex:49` (Table 2) | `14.639 & 14.59 & $\mathbf{274}$` | 需 n=500 per-phase 值 |
| ❌ | `appendix_disc_analysis.tex:46` | `median_diff=14.59 (segment-level)` | 更新注释 |
| ❌ | `appendix_moved.tex:59` | `0.39 & 1.48 & 7.16 & 14.59` | **0.39 & 1.21 & 3.99 & 8.48** |

### 三、Cohen's d_z（n=50: 0.44→0.80 → n=500 registry: 0.61→1.13）

| 状态 | 文件:行 | 当前值 | 应改为 |
|------|---------|--------|--------|
| ❌ | `abstract.tex:7` | `$0.44$ (small) to $0.80$ (large)` | **0.61→1.13** |
| ❌ | `introduction.tex:14` | `$0.44 \to 0.80$` | **0.61→1.13** |
| ❌ | `results.tex:106` | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | **0.61→1.13** |
| ❌ | `results.tex:117` (table) | DS d_z=0.44 | **0.61** |
| ❌ | `results.tex:120` (table) | DS d_z=0.80 | **1.13** |
| ❌ | `conclusion.tex:4` | `$d_z$: $0.44 \to 0.80$` | **0.61→1.13** |

### 四、Qwen 数字也需更新（Cohen's d table 中间行）

Registry (n=500): QW median_diff 0.07/0.31/1.07/3.16, d_z 0.37→1.44

| 状态 | 文件:行 | 当前 QW Δ | 应改为 |
|------|---------|----------|--------|
| ❌ | `results.tex:117` | 0.05 | **0.07** |
| ❌ | `results.tex:118` | 0.21 | **0.31** |
| ❌ | `results.tex:119` | 1.11 | **1.07** |
| ❌ | `results.tex:120` | 2.62 | **3.16** |
| ❌ | `results.tex:117` | QW d_z=0.28 | **0.37** |
| ❌ | `results.tex:120` | QW d_z=1.02 | **1.44** |

DS 中间行：
| 状态 | 文件:行 | 当前 DS Δ | 应改为 |
|------|---------|----------|--------|
| ❌ | `results.tex:118` | 1.15 | **1.21** |
| ❌ | `results.tex:119` | 3.97 | **3.99** |

### 五、样本量 n=50 → n=500

| 状态 | 文件:行 | 当前 | 应改为 |
|------|---------|------|--------|
| ❌ | `abstract.tex:6` | "using 50 MATH-500 problems" | **500** |
| ❌ | `results.tex:14` (Table 1 caption) | `$n{=}50$ MATH-500 problems` | **500** |
| ❌ | `results.tex:34` (Table 2 caption) | "across 50 problems" | **500** |
| ❌ | `methodology.tex:10` | "We use 50 problems" | **500** |
| ❌ | `appendix_moved.tex:26` | "Four of the 50 problems" | 需 n=500 有效 n |

### 六、级联影响（需重算的派生数字）

以下数字由 Table 1/2 的原始数据派生，换到 n=500 后全部失效：
- **37× amplification** (`results.tex:8`) — 14.59/0.39=37.4→ 8.48/0.39≈21.7×
- **G ratios 69×/103×/222×/274×** (`results.tex:28,42-49`, `discussion.tex:3`, `conclusion.tex:4`, figure caption `results.tex:58`) — 需 n=500 per-phase II 值重算
- **Table 2 全部 per-phase II 值** — 需 n=500 数据
- **Permutation test Δ values** (`results.tex:100`): "0.37 at s=0.15 to 9.85 at s=0.30" — 需 n=500 结果
- **QW d_z prose** (`results.tex:106`): "$d_z{=}0.28$" "$d_z \geq 0.55$" "$d_z{=}0.89$/$1.02$" — 需 n=500 中间值

### 七、已正确的部分

| 状态 | 项目 |
|------|------|
| ✅ | "n=50 pilot" 字样不出现（无 "n=50 pilot" 组合） |
| ✅ | paper_framing.md 已更新为 n=500 registry 数字 |
| ✅ | Crossover 数字 (0.032 vs 0.818, 7.196 vs 1.363) — 来自 segment-level n=50，是否需更新取决于 n=500 per-phase 数据 |
| ✅ | discussion.tex "pilot" 指的是 C5b mitigation pilot，不是旧数据 pilot |
| ✅ | Accuracy dose curve 数字 (0.46/0.42/0.36/0.33/0.19) 不在正文 tex 中，仅在 figure 中 |

---

### 总结

**paper_framing.md 已更新为 n=500 registry 数字，但 abstract.tex、introduction.tex 和其余所有 tex 文件的修复完全没有执行。** 论文当前全文仍使用 n=50 segment-level 统计量。需要一次完整的数字替换 pass，涉及至少 8 个 tex 文件、约 30+ 处修改，且 Table 2 的 per-phase 值和所有派生比率需要从 n=500 实验结果重新提取。

---
