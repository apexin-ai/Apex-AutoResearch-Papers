# paper consistency check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency_check_20260523T002253_result.json`
- **Structured JSON:** [`a3862fe250c7ccd0ac24.json`](../../sessions/a3/a3862fe250c7ccd0ac24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕。逐项报告如下：

---

## 检查结果

### 1. "three of six" Bonferroni pass — PASS

- `experiments_c1.tex:46` — "three of six boundary configurations" ✓
- `conclusion.tex:9` — "three of six $\Kempirical{=}2$ configurations" ✓
- `main.tex:38` (abstract) — 等价表述 "Among the six nominal...three retain significance" ✓
- `appendix_extended.tex:155` — 补充描述 "three marginal K*=2 configurations" ✓
- 无 "four of six" 残留 ✓

### 2. Pythia 1v2 AUC = 0.6074 — FAIL

正确值已出现在 experiments_c1.tex:26, tab_domain_model_kstar_full.tex:14, appendix_extended.tex:170, appendix_extended.tex:196。

**旧值 .6539 残留：**

| 文件 | 行 | 当前值 | 应改为 |
|------|-----|--------|--------|
| `appendix.tex` | 139 | `.6539 & [.645,\,.663]\rlap{$^*$}` | `.6074 & [.598,\,.617]\rlap{$^*$}` |
| `appendix.tex` | 343 | `$.654\;[.645,.663]$` | `$.607\;[.598,.617]$` |

### 3. OLMo 1v2 AUC = 0.500/0.5001 — FAIL

正确值已出现在 experiments_c1.tex:26, tab_domain_model_kstar_full.tex:17, appendix_extended.tex:201。

**旧值 .5080/.508 残留：**

| 文件 | 行 | 当前值 | 应改为 |
|------|-----|--------|--------|
| `appendix.tex` | 139 | `.5080` | `.5001` |
| `appendix.tex` | 343 | `$.508\;[.496,.519]$` | `$.500\;[.496,.519]$` |
| `discussion.tex` | 37 | `0.508--0.598` | `0.500--0.598` |

### 4. OLMo K* = 1 — PASS

- `tab_domain_model_kstar.tex:15` — OLMo 1B, K*=1 ✓
- `tab_domain_model_kstar_full.tex:17` — OLMo 1B, K*=1 ✓
- 正文所有引用一致 ✓

### 5. K* 分布描述 (6/10 K*=2, 4/10 K*=1) — PASS

- `experiments_c1.tex:45` — "6/10 configurations yield K*=2 (Qwen ×4, LLaMA-8B, Pythia-1.4B)" ✓
- `discussion.tex:17` — "6/10 configurations K*=2" ✓
- `appendix.tex:129` — "K*=2 holds for 6/10 conditions...OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: K*=1" ✓
- Abstract/conclusion 用等价表述，一致 ✓

### 6. 破折号检查 — PASS

- Unicode em dash (—) 仅出现在注释行 `main.tex:1`（非正文）
- 无 Unicode en dash (–)
- LaTeX `---` 仅用于表格占位符（"not available"）
- LaTeX `--` 仅用于数值范围（标准用法）

---

## 总结

**3 处 FAIL，均在 appendix.tex 和 discussion.tex，涉及 D107 scorer 修正后的旧值残留：**

1. `appendix.tex:139` — Pythia .6539→.6074（含CI），OLMo .5080→.5001
2. `appendix.tex:343` — Pythia .654→.607（含CI），OLMo .508→.500
3. `discussion.tex:37` — OLMo 范围起始值 0.508→0.500

需要修正这 5 个数值点。是否现在修正？

---
