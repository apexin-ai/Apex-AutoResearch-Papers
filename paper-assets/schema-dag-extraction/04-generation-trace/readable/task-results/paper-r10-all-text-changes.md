# paper r10 all text changes

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r10-all-text-changes_20260517T082316_result.json`
- **Structured JSON:** [`255af3adeb79c9501092.json`](../../sessions/25/255af3adeb79c9501092.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clean. Here's the summary of all modifications:

## 产出汇报

### STEP 0: references.bib
- **L367**: `Srinivas, Sber` → `Sunkara, Srinivas`; `Guber, Raghav` → `Gupta, Raghav`; `Nakhost, Mehran` → `Khaitan, Pranav` (applied by linter on first pass)
- **末尾**: 添加 `bogdanov2024nuner`, `xie2024selfimproving`, `zhang2023llmaaa`, `wellek2010testing` 共 4 个新 entry
- `lakens2017equivalence` 跳过（已存在为 `lakens-2017-equivalence`，TOST 引用使用现有 key）

### STEP 1a: \enlargethispage
- **sdgd_negative.tex:19**: 删除 `\enlargethispage*{9\baselineskip}`

### STEP 1b: §5 压缩
- **sdgd_negative.tex**: 完整重写。原 44 行 → 33 行（含 table）
- 保留：SDGD 方法简介 (2 句)、merge amplification 核心发现 (4 句)、oracle routing (+29.8pp, +1.4pp n.s.)、practical routing failure (1 句 + appendix ref)
- 移除：4 种 NER mode 逐一对比、routing strategy 描述、confidence gating 段落、"Why NER fails but RE does not" 段落（均已在 appendix）
- Table caption 精简（删除末句冗余解释）

### STEP 2: 因果语言
- 全部 **已经正确**（前序 worker 或原始写作已完成）。grep 验证：driven/drive=0, bounded interaction=0, mechanism(非Causal)=0

### STEP 3: C2 — 聚合推理链重构
- **results.tex L67**: 重写 practical magnitude 段落，开头直接给 primary claim："Direct regression on 100 random 16-type batches...BCS explains 22% ($R^2 = 0.218$, $p < 0.001$), scaling to 53% at DocRED"。Simulation 标注为 post-hoc
- **discussion.tex**: 无 "yielding" 残留 ✓

### STEP 4: C3 — TOST margin Lakens SESOI
- **supplementary.tex L152**: 扩展 margin justification，加入三条 anchor (Empirical/Practical/Statistical) + `\citealt{lakens-2017-equivalence}`
- **supplementary.tex L150**: 2×2 factorial 改为 "sensitivity check" 措辞
- **main.tex L191, L189**: 同步修改

### STEP 5: Batch 1 残余
- **C4**: 已完成（contribution #2 已是 "First controlled validation..."，无 em-dash）
- **W3**: 已完成（abstract 无 TOST 参数）
- **W4**: 已完成（contribution list 无冗余技术细节）
- **W5**: 已完成（BCS qualifier 已在 contribution #3）
- **W7**: 无空 placeholder sections
- **"r < -0.47" → "r ≤ -0.47"**: results.tex:73, supplementary.tex:261, main.tex:300 三处修正

### STEP 6: W2 — Future directions
- **sdgd_negative.tex**: 在 §5 末尾加 `\paragraph{Future directions.}` 含 3 个方向：coarse-to-fine pipeline, retrieval-based routing, calibrated generation

### STEP 7: Prompt sensitivity
- **已存在**: results.tex:73 已有 "BCS--accuracy correlation holds across four structurally distinct prompt variants at count 32" + Appendix H.1 有完整 table

### STEP 8: Minor items
- **m1 seed SD**: supplementary.tex L443 + main.tex L453 加入 "Under greedy decoding (temperature=0), model inference is deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity."
- **m2 U-shape**: discussion.tex:8 "reflects" → "We hypothesize that...reflects"
- **m3 Related Work**: related_work.tex L5 加入 NuNER/LLMaAA/Self-Improving NER 三引用
- **m4 Multiple comparisons**: main.tex L57 重写，区分 cross-dataset (independent replications, no adjustment) vs within-dataset (multiple looks, individual p-values)
- **m5 GPU**: experimental_setup.tex "single 96\,GB GPU" → "single NVIDIA RTX PRO 6000 GPU (96\,GB)"; checklist.tex 删除 "Blackwell"

### STEP 9: 编译验证
- main.tex: 20 pages, 无 LaTeX 错误，body text ≤ 8 pages（Limitations 从 page 8 开始）
- supplementary.tex: 9 pages, 无错误（cross-ref warnings 预期内）
- 因果语言/em-dash/enlargethispage grep 全部清零 ✓
- 新引用格式正确 ✓（仅 `guo-2021-label-confusion` 有 volume+number 风格 warning，非 error）

---
