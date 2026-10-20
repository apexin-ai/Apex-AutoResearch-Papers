# reviewer / loop_17.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`24b3462ea1530fba01c5.json`](../../sessions/24/24b3462ea1530fba01c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-21T18:18:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 两台服务器：autodl-5090（4×RTX5090）和 autodl-5090-c（4×RTX5090），项目可用全部 8 卡
- E2 pretrained FewNERD s456 在两台服务器上重复启动（5090 GPU3 先跑，5090-c GPU2 后跑），结果取先完成的即可，但 registry 只记一份
- alpha_crit_table.md 中 SciERC 数据是 inclusive MV（≥4/8），论文已切 strict MV（>4/8, D227），两套数字不同——不要引用 alpha_crit_table 的 SciERC MV 数据到论文
- references.bib:472 `ma2024selfimproving` 作者全部错误（实际第一作者 Xie），已报 critical（Review #89），修复前不要引用该 bib key

### 2. 🖥️ 基础设施快照
- **autodl-5090**: root@autodl-5090, `/root/autodl-tmp/struct_self_consist_ie`
  - conda: `/root/miniconda3/bin/python`, `conda activate base`
  - 模型: `checkpoints/qwen3-8b-fewnerd-exp021-merged/`（3-epoch FT, 主力）, `checkpoints/qwen3-8b-fewnerd-5epoch-merged/`（5-epoch FT, 刚 merge）
  - 活跃进程: GPU0 PID 54567 fewnerd_n16_s456, GPU1 PID 63739 fewnerd_5epoch_s42, GPU2 PID 63893 fewnerd_5epoch_s123, GPU3 PID 48045 e2_pretrained_fewnerd_s456
- **autodl-5090-c**: root@autodl-5090-c, 同路径
  - 活跃: GPU2 e2_pretrained_fewnerd_s456（重复）, GPU3 e2_pretrained_fewnerd_s42（新）
  - GPU0/1 空闲
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文: `docs/paper/main.tex`, sections 在 `docs/paper/sections/`

### 3. 📊 当前状态
**刚做完**: Reviews #87-#90。核心发现：
- SciERC 3-seed recompute 完成，MV 方向从+0.37pp（inclusive）翻转为-0.73pp（strict）（Review #88）
- E2 pretrained CoNLL MV 捕获 98%+ oracle headroom，与 finetuned <2% 形成强对比（Review #90）
- Ma(2024) 引用 5 个作者全部幻觉，critical 级（Review #89）

**运行中实验**:
| 实验 | 服务器/GPU | 进度 | ETA |
|------|-----------|------|-----|
| fewnerd_n16_s456 | 5090/GPU0 | ~70% | ~1h |
| fewnerd_5epoch_s42 | 5090/GPU1 | ~10% | ~1.5h |
| fewnerd_5epoch_s123 | 5090/GPU2 | ~10% | ~1.5h |
| e2_pretrained_fewnerd_s456 | 5090/GPU3 | ~75% | ~45min |
| e2_pretrained_fewnerd_s456 | 5090-c/GPU2 | ~5% | ~2h（重复） |
| e2_pretrained_fewnerd_s42 | 5090-c/GPU3 | 刚启动 | ~2-3h |

**Registry**: exp_fewnerd_n16_s123 ANALYZING, exp_e2_pretrained_fewnerd_s123 RUNNING, 大量实验 PREPARING 但实际已完成（sync gap 持续）

### 4. 📋 待办（条件触发式）
- fewnerd_n16_s456 完成 → 核实 N=16 三种齐全（s42 ✓ s123 ✓ s456 pending），交叉验证 oracle headroom scaling
- fewnerd_5epoch_s42/s123 完成 → **关键审查**：对比 3-epoch vs 5-epoch 的 rho_SJ_cond / degeneracy / MV，判断 epoch confound 是否成立
- e2_pretrained_fewnerd_s42/s456 完成 → 核实 pretrained FewNERD 三种，确认 pretrained > finetuned correlation 模式
- Paper Agent R30 fix patches 到达 → 审查 causal language 清理（特别是 appendix 13+ instances of governs/controls/driven）+ SciERC 3-seed 表更新 + α_crit bound 措辞
- Director 回应 Review #89 → 确认 references.bib 全面审计是否启动

### 5. 🎯 战略上下文
**核心决策链**: D224（NER scope）→ D225（target 3.5-4.0）→ D226（E4 excluded）→ D227（strict MV >N/2）→ D228（"MV fails to improve" narrative）

**论文 story**: SC 在 NER 上的 capability ceiling——agreement signals 能预测质量（ρ>0）但 MV aggregation 捕获 <2% oracle headroom。原因是 finetuned 模型 degeneracy 高 + diversity 低。Pretrained 模型反而更好（E2 实验证实）。

**易错点**:
1. **不要混用 inclusive/strict MV 数据**。alpha_crit_table.md 用 inclusive（≥4/8），论文用 strict（>4/8, ≥5/8）。SciERC 方向会翻转。
2. **SciERC oracle F1 有两套数字**：旧 pipeline（s123=0.818, s456=0.821）vs MF4v2（s123=0.779, s456=0.780），差 4pp。论文必须统一用 MF4v2。
3. **Registry sync gap 是系统性问题**——不要因为 registry 显示 PREPARING 就认为实验没跑。SSH 核实服务器上是否已有 output 目录和 report.json。
4. **5-epoch 实验结果解读**：如果 5-epoch vs 3-epoch 差异 <1pp，结论是 epoch confound 不成立（好事）；如果 >2pp，需要在论文 Limitations 讨论。
5. **Causal language 清理范围**：main body 基本干净（R28 已修），但 appendix.tex 有 13+ instances（governs/controls/driven/determined），R30 Action Matrix 可能遗漏了这部分。


---
