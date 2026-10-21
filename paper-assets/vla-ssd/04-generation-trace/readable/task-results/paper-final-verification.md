# paper final verification

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final_verification_20260519T134242_result.json`
- **Structured JSON:** [`42b673b54f849b521743.json`](../../sessions/42/42b673b54f849b521743.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是完整汇报。

---

## 任务 1：编译验证

| 项目 | 结果 |
|------|------|
| LaTeX errors | **0** |
| Warnings | **20**：17× `h float specifier changed to ht`（浮动体位置，无害）+ 3× hyperref `Token not allowed in PDF string`（数学符号在 PDF bookmark，无害） |
| Conclusion 位置 | **page 8** ✓ |
| References 起始 | **page 8**（与 Conclusion 同页） |
| Appendix 起始 | **page 12** |
| 总页数 | **27 页** |

正文 ≤8 页约束满足。

---

## 任务 2：数值一致性 spot check

| # | 数值 | 论文位置 | Artifact 来源 | Artifact 值 | 判定 |
|---|------|----------|---------------|-------------|------|
| 1 | **24/32 instruction-dominant heads** | `experiments.tex:53,97`; `discussion.tex:7,15`; `appendix.tex:566,599` | `libero_finetuned_attention/data/libero_finetuned_attention_profile_summary.txt` → `openvla7b=24` | 24 | ✓ 完全一致 |
| 2 | **d = 0.65 (trajectory divergence)** | `experiments.tex:78,86`; `discussion.tex:7,12`; `appendix.tex:121,139` (tab:perhead_bootstrap), `appendix.tex:767` (tab:specificity_control = 0.650) | `matched_ablation_controls_diagnosis.md` → `Instruction-dominant-24 traj_d: 0.65` | 0.65 | ✓ 完全一致 |
| 3 | **specificity ratio 1.08×** | `discussion.tex:7` | `matched_ablation_controls_diagnosis.md` → instruction d=0.65, random d=0.601; tab:specificity_control caption: "8% over random" | 0.65/0.601 = 1.0815 | ✓ 合理四舍五入 |
| 4 | **counterfactual d = 0.63--0.97** | `abstract.tex:5`; `introduction.tex:18`; `discussion.tex:7` | `appendix.tex:189-192` tab:counterfactual → Shuffled 0.625, Empty 0.968 | 0.625–0.968 | ✓ 合理四舍五入（0.625→0.63, 0.968→0.97） |
| 5 | **probe accuracy L1 = 99.6%** | `experiments.tex:64` (99.7% for LIBERO), `experiments.tex:97` (99.6% for VLA), `appendix.tex:555` (OpenVLA-7B=99.6%, LIBERO=99.7%) | `libero_finetuned_probe_profile.json` → L1=0.997 (LIBERO-finetuned) | 99.7% (LIBERO) | ✓ LIBERO 99.7% 与 JSON 完全一致；OpenVLA-7B 99.6% 无独立本地 JSON，但论文 Tab 2 与 Tab 10 内部一致 |

**注意**：先前一致性报告（2026-05-18）曾标记 registry 中 head 数为 25 vs 论文 24 的不一致。但实际 attention profile summary 确认 openvla7b=24，且论文 tab:multilayer_attention caption 已说明 "bulk extraction 可能因 threshold boundary effects 与 dedicated per-layer analysis 略有差异"。当前论文值 24/32 与 attention profile 数据一致。

---

## 任务 3：Figure/Table 引用检查

| 项目 | 结果 |
|------|------|
| `\ref{}` 总数 | **62 个 unique** |
| 每个 `\ref{}` 有对应 `\label{}` | ✓ **全部匹配** |
| 悬空引用 ("??") | **0** |
| undefined reference 警告 | **0** |
| multiply-defined labels | **0** |
| 孤立 `\label{}`（有定义无引用） | 5 个 appendix figure labels + 22 个 appendix section labels（正常，不影响编译） |

**结论**：无断裂引用，所有交叉引用完整。

---
