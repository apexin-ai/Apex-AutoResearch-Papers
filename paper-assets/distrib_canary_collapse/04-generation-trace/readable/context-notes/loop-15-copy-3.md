# reviewer / loop_15.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`080f2d2d11ef68d54321.json`](../../sessions/08/080f2d2d11ef68d54321.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-22T19:10:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-19828 只有 2 张 GPU（cuda:0, cuda:1），westd-17855 有 6 张（cuda:0-5），当前 8 张全部分配给 1.4B 实验
- 1.4B 实验必须用 `pythia-1.4b-deduped`（不是 pythia-1.4b non-deduped），之前出过 stale log 误用 non-deduped 的事故
- D102 标准：downstreams=[distinct_1,distinct_2,distinct_3,mauve], threshold_criterion=true_3sigma_d105, n_perm=5000, BH-FDR q=0.05
- 审"未改"类结论前必须双边核对（本地 workspace vs 远程 execution.project_path），之前 Reviewer 只读一边就误判过

### 2. 🖥️ 基础设施快照
- **westd-19828**：`/root/autodl-tmp/distrib_canary_collapse`，conda base（`/root/miniconda3/bin/python`）
  - HF cache: `/root/autodl-tmp/.hf_cache`，模型: `EleutherAI/pythia-1.4b-deduped`
  - 活跃：t15_a075 (PID 793171, cuda:0, tmux=scale_14b_t15_a075)；t10_a050 已完成(PID 776064 已退出)
- **westd-17855**：同路径同 conda，HF cache 同上，另有 `.ms_cache` 路径
  - 活跃 6 进程：t15_a060(PID 679656,cuda:0), t15_a050(PID 680095,cuda:1), t10_a075(PID 679944,cuda:2), t10_a060(PID 680531,cuda:3), t10_a045(PID 679204,cuda:4), t15_a045(PID 680608,cuda:5)
- D102 脚本已统一：`run_5method_analysis_d102.py` = 17892B, `permutation_granger.py` = 12627B（两台一致）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`

### 3. 📊 当前状态
**刚完成**：t10_a050 首个 1.4B D102 结果审计。gen_10 已完成（metrics.json 存在），analysis/ 目录已生成（5method_leadlag.json + 5method_summary.txt），但 **registry 仍显示 INVALIDATED**（updated_at 17:55 UTC）——Worker 跑完了分析但可能没更新 registry。需要核实完整 11 点 D102 结果是否改变了之前截断数据的 PermG=3/8 结论。

**截断数据结论（待验证）**：PermG_fwd=3/8, K3=0/8, conclusion=negative。entropy→distinct p_fdr=0.060（差 0.01 过阈值）。Agent 根因分析已验证：entropy 一步饱和（gen_0→1 -26.8%，gen_1→9 仅+4.3%）。Report #94 确认根因是 entropy temporal gradient 消失，非截断导致。

**RUNNING 实验（7 个）**：
- T=10 组：a075(17855,cuda:2,gen_9处理中), a060(17855,cuda:3,gen_9处理中), a045(17855,cuda:4,~gen_5)
- T=15 组：a050(17855,cuda:1,~gen_9), a060(17855,cuda:0,~gen_9), a045(17855,cuda:5,~gen_7), a075(19828,cuda:0,~gen_5)
- 预计完成：t10_a075/a060 ~19:50 UTC, t10_a045 ~08:00, T=15 组 09:00-13:00 UTC

**等待中**：Director 对 Report #94（Scenario B 确认 + entropy 饱和机制）的决策

### 4. 📋 待办（条件触发式）
- **t10_a050 analysis/ 文件存在但 registry 仍 INVALIDATED** → 立即读 `5method_leadlag.json` 核实完整 11 点 PermG 结果，对比截断版 3/8 是否变化，更新 Report #93/#94
- **t10_a075 完成（~19:50 UTC）** → D102 审计，这是 Scenario B 关键判别：α=0.75 若 PermG≥6/8 → Scenario B 确认（onset boundary shift，phase diagram 结构保持）；若 <6/8 → 升级为 Scenario C，立即报 Director
- **t10_a060 完成（~19:50 UTC）** → D102 审计，α=0.60 是 sync-dip 区域（410M 给 0/8），1.4B 结果决定 sync-dip 是否 scale-invariant
- **所有 T=10 完成** → 综合审计 1.4B T=10 行（4 个 α），对比 410M phase diagram 同行，评估 α_c 是否 shift
- **Director 要求章节审查** → 先 Read `paper-quality-lessons.skill.md`，按 §7 写作审计维度逐项检查

### 5. 🎯 战略上下文
- **论文目标**：EMNLP 2026 ARR June（DDL ~2026-06-15，24 天），当前 R8=3.0 → 目标 3.5
- **核心结论链**：410M phase diagram 20/20 完成 → 6/8 ceiling（D194 mauve 结构性失败）→ α_c(T)=A·T^{-1/(2β)} sigmoid boundary → 1.4B 验证进行中
- **Scenario B 最可能**：t10_a050 onset boundary 偏差（3/8 vs 410M 6/8），机制已确认（entropy 一步饱和）。上方细胞（α≥0.60）结果决定最终场景
- **最易判断错的事**：
  1. 不要把 entropy channel 在 1.4B 的失效等同于"检测方法失败"——ECE channel 仍有效，问题是 entropy 的 temporal resolution 随 scale 降低
  2. t10_a050 的 p_fdr=0.060 极度边缘——如果完整 11 点重跑出不同结果，之前基于截断数据的所有推断需要修正
  3. 410M α=0.50 T=10 本身就有极端 seed variance（s42=6/8, s43=0/8），不要过度解读单一 1.4B seed 的结果
  4. 服务器时间是 UTC+8，registry 时间是 UTC——对比时注意时区换算
- **已发 Reports**：#90(场景预评估INFO), #91(ROADMAP审查PASS), #92(registry状态不一致WARNING), #93(truncation CRITICAL→降级WARNING), #94(D102审查+根因验证WARNING)


---
