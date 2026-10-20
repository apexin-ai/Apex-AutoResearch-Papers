# audit table1 edcr spectrum

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-edcr-spectrum_20260523T141600_result.json`
- **Structured JSON:** [`486ec44a49296578d0f0.json`](../../sessions/48/486ec44a49296578d0f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data verified. Here is the complete audit report.

---

## 数据审计报告

### 审计项 1: Table 1 (tab:main) — Qwen3-4B

| # | 值 | 论文值 | Registry/源文件值 | 状态 | 源文件 |
|---|---|--------|-------------------|------|--------|
| 1 | SFT Ign-F1 | 43.58±3.80 | s42=39.74, s43=43.65, s44=47.34 → mean=43.58, std=3.80 | **PASS** | d111_4b_sft_s42_reeval, wave1_sft_4b_s43/s44_eval_r2 |
| 2 | SFT Rel-F1 | 44.39 | mean(40.49, 44.29, 48.38)=44.39 | **PASS** | 同上 |
| 3 | SFT Evi-F1 | 79.61 | mean(79.86, 80.21, 78.75)=79.61 | **PASS** | 同上 |
| 4 | SFT EDCR | 0.6797 | mean(0.6982, 0.6827, 0.6581)=0.6797 | **PASS** | 同上 |
| 5 | No-evi Ign-F1 | 47.21 | 47.21 | **PASS** | eval_plan_014_no_evidence_r2 |
| 6 | No-evi Rel-F1 | 48.76 | 48.76 | **PASS** | 同上 |
| 7 | RSFT Ign-F1 | 44.82±0.51 | s42=44.23, s43=45.12, s44=45.11 → mean=44.82, std=0.51 | **PASS** | reeval_ced_s42, eval_rsft_ced_s43, reeval_ced_s44 |
| 8 | RSFT Rel-F1 | 45.80 | mean(45.17, 46.01, 46.21)=45.80 | **PASS** | 同上 |
| 9 | RSFT Evi-F1 | 80.96 | mean(81.75, 80.63, 80.50)=80.96 | **PASS** | 同上 |
| 10 | RSFT EDCR | 0.6487 | mean(0.6569, 0.6542, 0.6350)=0.6487 | **PASS** | 同上 |

---

### 审计项 1b: Table tab:spectrum (appendix)

| # | 值 | 论文值 | 源文件值 | 状态 | 源文件 |
|---|---|--------|----------|------|--------|
| 11 | GRPO QLoRA Rel-F1 | 1.38 | 1.38 | **PASS** | mvp2_eval_lr5e6_r1_ckpt100 |
| 12 | GRPO QLoRA Evi-F1 | 85.04 | 85.04 | **PASS** | 同上 |
| 13 | GRPO QLoRA EDCR | 0.9876 | 0.9876 | **PASS** | 同上 |
| 14 | GRPO bf16 Rel-F1 | 45.49 | 0.45494→45.49 | **PASS** | grpo_g8_bf16/summary.json ckpt-100 |
| 15 | GRPO bf16 Evi-F1 | 80.86 | 0.80864→80.86 | **PASS** | 同上 |
| 16 | GRPO bf16 EDCR | 0.6318 | 0.63182 | **PASS** | 同上 |
| 17 | DPO 1ep Rel-F1 | 33.38 | f1=0.33375→**33.37** | **FAIL** | dpo_rebuilt_1ep_eval/metrics.json |
| 18 | DPO 1ep Evi-F1 | 80.90 | 0.80896→80.90 | **PASS** | 同上 |
| 19 | DPO 1ep EDCR | 0.8123 | 0.81229 | **PASS** | 同上 |
| 20 | DPO 3ep Rel-F1 | 31.45 | f1=0.31446→31.45 | **PASS** | dpo_rebuilt_3ep_eval/metrics.json |
| 21 | DPO 3ep Evi-F1 | 84.84 | 0.84838→84.84 | **PASS** | 同上 |
| 22 | DPO 3ep EDCR | 0.7503 | 0.75030 | **PASS** | 同上 |

---

### 审计项 1c: Table tab:scaling

| # | 值 | 论文值 | 源文件值 | 状态 | 源文件 |
|---|---|--------|----------|------|--------|
| 23 | 1.7B SFT | 44.64±2.79 | s42=47.86, s43=42.86, s44=43.21 → 44.64±2.79 | **PASS** | plan_006/plan019 eval files |
| 24 | 1.7B RSFT | 51.19±0.09 | d102 k=1 s42=51.22, s43=51.09, s44=51.25 → 51.19±0.09 | **PASS** | d102_1_7b_k1_s42/metrics.json + registry |
| 25 | 4B SFT | 43.58±3.80 | (same as tab:main) | **PASS** | -- |
| 26 | 4B RSFT | 44.82±0.51 | (same as tab:main) | **PASS** | -- |
| 27 | 8B SFT | 50.19±3.23 | s42=50.51, s43=53.24, s44=46.81 → 50.19±3.23 | **PASS** | plan_006/plan019 eval files |
| 28 | 8B RSFT | 54.33±0.50 | d102 k=1 s42=53.76, k=1 s43=54.71, k=1 s44=54.51 → 54.33±0.50 | **PASS** | d102_8b_k1_s42/s43, rsft_8b_k1_s44_eval |
| 29 | 14B SFT | 55.07 | 55.07 | **PASS** | plan017_14b_sft_eval_r2 |
| 30 | 14B RSFT | 58.86 | 58.86 | **PASS** | plan017_14b_rsft_eval |
| 31 | LLaMA SFT | 51.09±2.92 | s42=53.84, s43=51.42, s44=48.02 → 51.09±2.92 | **PASS** | plan_016/llama_sft_s43/s44 eval files |
| 32 | LLaMA RSFT | 56.54±0.64 | d102 k=1 s42=57.14, k=1 s43=56.62, k=1 s44=55.87 → 56.54±0.64 | **PASS** | d102_llama_k1_s42/s43, rsft_llama_k1_s44_eval |

**注**: Registry 中 1.7B/8B/LLaMA RSFT s42 仍为旧 k=3 值 (50.50/54.33/55.63)，但服务器上 d102_*_k1_s42 源文件确认了论文使用的 k=1 值。Registry 需要更新以反映 k=1 结果。

---

### 审计项 1d: Table tab:ablation_full

| # | 值 | 论文值 | 源文件值 | 状态 |
|---|---|--------|----------|------|
| 33-36 | SFT s42 (Ign/Rel/Evi/EDCR) | 39.74/40.49/79.86/0.6982 | 一致 | **PASS** |
| 37-40 | RSFT s42 | 44.23/45.17/**81.74**/0.6569 | registry=81.75, paper=81.74 | **PASS*** |
| 41-44 | RSFT s43 | 45.12/46.01/80.63/0.6542 | 一致 | **PASS** |
| 45-48 | RSFT s44 | 45.11/46.21/80.50/0.6350 | 一致 | **PASS** |
| 49-52 | RSFT s45 | 44.16/45.14/81.74/0.6550 | 一致 | **PASS** |

*s42 Evi-F1: registry=81.75 vs paper=81.74 (0.01pp 四舍五入差异，不影响任何均值计算)

---

### 审计项 2: Method section EDCR 公式示例

| # | 值 | method.tex 值 | 来源 | 对应表格值 | 状态 |
|---|---|---------------|------|-----------|------|
| 53 | SFT EDCR | 0.6982 | d111_4b_sft_s42_reeval (s42 only) | tab:main=0.6797 (3-seed mean) | **FAIL** |
| 54 | GRPO QLoRA EDCR | 0.9876 | mvp2_eval_lr5e6_r1_ckpt100 | tab:spectrum=0.9876 | **PASS** |
| 55 | RSFT EDCR | 0.6503 | tab:ablation_full 4-seed mean | tab:main=0.6487 (3-seed mean) | **FAIL** |

**问题**: method.tex 说 "The SFT baseline EDCR (0.6982)" 和 "RSFT at 0.6503"，但未标明这是 s42-only 和 4-seed mean。读者对比 tab:main（SFT=0.6797, RSFT=0.6487）会发现数值不一致：
- SFT: 0.6982 vs 0.6797 (差 0.0185)
- RSFT: 0.6503 vs 0.6487 (差 0.0016)

**修正建议**: 统一使用 3-seed mean (0.6797/0.6487) 与 tab:main 保持一致；或在 method.tex 中明确标注 "(s42)" 和 "(four-seed mean)"。

---

### 审计项 3: fig_spectrum 坐标 vs tab:spectrum

| # | Method | 脚本坐标 (x, y) | 对应值 (Rel-F1, Evi-F1) | tab:spectrum 值 | 状态 |
|---|--------|-----------------|------------------------|-----------------|------|
| 56 | SFT | (0.4439, 0.7961) | 44.39, 79.61 | 44.39, 79.61 | **PASS** |
| 57 | RSFT | (0.4580, 0.8096) | 45.80, 80.96 | 45.80, 80.96 | **PASS** |
| 58 | GRPO bf16 | (0.4549, 0.8086) | 45.49, 80.86 | 45.49, 80.86 | **PASS** |
| 59 | DPO 1ep | (0.3338, 0.8090) | 33.38, 80.90 | 33.38, 80.90 | **PASS** |
| 60 | DPO 3ep | (0.3145, 0.8484) | 31.45, 84.84 | 31.45, 84.84 | **PASS** |
| 61 | GRPO QLoRA | (0.0138, 0.8504) | 1.38, 85.04 | 1.38, 85.04 | **PASS** |
| 62 | **Figure caption** | xlabel='Rel-F1', ylabel='Evi-F1' | x=Rel-F1, y=Evi-F1 | Caption says "Evi-F1 (x-axis) and Rel-F1 (y-axis)" | **FAIL** |

**问题**: experiments.tex 第51行 Figure caption 写 "Each method is plotted by Evi-F1 (x-axis) and Rel-F1 (y-axis)"，但实际绘图脚本 (`plot_spectrum.py`) 中 x轴=Rel-F1, y轴=Evi-F1 (TP)。**轴标签在 caption 中被反了。**

**修正建议**: 改为 "Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis)."

---

## 汇总

| 统计 | 数量 |
|------|------|
| 总审计项 | 62 |
| PASS | 58 |
| PASS* (微小四舍五入差异) | 1 |
| **FAIL** | **3** |

### FAIL 清单

| # | 位置 | 问题 | 严重程度 | 修正 |
|---|------|------|---------|------|
| **F1** | tab:spectrum DPO 1ep Rel-F1 | 论文=33.38, 源文件=33.37 (0.01pp) | 低 | 改为 33.37，或确认是否有其他 eval 产出 33.38 |
| **F2** | method.tex §5.5 EDCR 示例 | SFT EDCR 用 s42-only (0.6982)，RSFT 用 4-seed mean (0.6503)；与 tab:main 的 3-seed mean (0.6797/0.6487) 不一致，读者会困惑 | 中 | 统一为 3-seed mean 或明确标注聚合范围 |
| **F3** | fig_spectrum caption (experiments.tex L51) | 轴标签写反：caption 说 "Evi-F1 (x-axis) and Rel-F1 (y-axis)"，实际 x=Rel-F1, y=Evi-F1 | **高** | 改为 "Rel-F1 (x-axis) and Evi-F1 (y-axis)" |

### Registry 维护建议（非论文错误）
- d102 k=1 eval 结果 (1.7B s42, 8B s42/s43/s44, LLaMA s42/s43/s44) 未注册到 registry
- DPO 3ep registry 缺少 rel_f1 字段
- 部分实验使用 `evi_f1` vs `evi_f1_tp` 字段名不统一

---
