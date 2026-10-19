# director / loop_20.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_20.md`
- **Structured JSON:** [`df601c7bd22b1fd0890a.json`](../../sessions/df/df601c7bd22b1fd0890a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_messages
updated: '2026-05-23T22:14:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-18228(4×4090), bjb1-32546(6×4090), bjb2-28827(6×4090), bjb2-40593(1×4090D), cqa1-32758(6×4090D)。不得使用其他项目的卡。
- CRM checkpoint 分两个版本：3-suite (Spatial/Object/Goal) 用 `crm_3suite_obs_only.pt`，4-suite (含Long) 用 `crm_4suite_obs_only.pt`。不要混用。
- Object 实验输出文件名必须包含 exp_id 或方法标识，禁止通用名（M070 教训：VLA-only 和 K2mean 同名覆盖丢数据）。K2mean 必须用 `--output_file` 指定。
- τ=0.25 是论文锁定参数。Object Adaptive 正确 trigger rate 是 3-5%。若看到 >50% trigger → 用了错误 τ 值，结果作废。
- p<0.05 已从论文移除（n=3 vs n=3 不够）。不要在汇报中声称统计显著性。
- Long VLA-only s43=59.5% 已确认合法（cqa1 孤儿进程产出）。bjb1-32546 同名文件 `eval_long_vla_only_seed43.json` 实际是 K2mean（baseline_mode="mean"）——查数据必须看 baseline_mode 字段。

### 2. 🖥️ 基础设施快照
- 5 台服务器，工作目录均为 `/root/acr-vla-conformal-refinement/`
- Python: conda base (`/root/miniconda3/bin/python`)
- CRM 3-suite checkpoint: `/root/acr-vla-conformal-refinement/crm_checkpoints/crm_3suite_obs_only.pt`
- CRM 4-suite checkpoint: 同目录 `crm_4suite_obs_only.pt`
- eval 脚本: `scripts/wrapper_eval.py`，n_rollouts=20
- π0.5 precompute: bjb1-18228 全 4 卡（ETA 5/24-25），不要打断
- 当前 23/23 GPU 满载运行

### 3. 📊 当前状态
Long 3-seed（VLA-only/Adaptive/CRM 的 s42-s44）全部收割完毕，Table 1 Long 行定稿。D134 叙事精化已完成：移除 "Adaptive ≥ VLA-only everywhere"，聚焦 "Adaptive ≥ CRM on ALL suites + gating correctly modulates"。ROADMAP 已更新。

**运行中实验：**
- bjb1-32546 (6/6): obj-crm-s46, long-vla/adapt/crm/reconvla-s45, goal-adapt-s45
- bjb2-28827 (6/6): goal-vla/crm/reconvla-s45, long-reconvla-s44(~85%), long-k2mean-s44(~80%), long-k2mean-s45
- bjb2-40593 (1/1): obj-crm-s45（8/10 tasks，~15min 完成 → 完成后部署 Spatial Adaptive s45，已批准）
- cqa1-32758 (6/6): obj-reconvla-s45/s46, goal-k2mean-s45, spatial-vla/crm/reconvla-s45
- bjb1-18228 (4/4): precompute-pi05

**即将完成（按 ETA）：**
1. bjb2-40593 obj-crm-s45 → ~15min → 部署 Spatial Adaptive s45
2. bjb2-28827 long-reconvla-s44 → ~2-3h → Long Reconvla 3-seed 收齐
3. bjb2-28827 long-k2mean-s44 → ~3h → Long K2mean 3-seed 收齐
4. bjb2-28827 goal-vla/crm/reconvla-s45 → ~5-6h → Goal 4-seed

### 4. 📋 待办（条件触发式）
- bjb2-40593 obj-crm-s45 完成 → 收割 + registry 更新 + 立即部署 Spatial Adaptive s45（3-suite checkpoint）
- bjb2-28827 long-reconvla-s44 + long-k2mean-s44 完成 → 收割 → Long 5-method 3-seed 全部收齐 → 汇报完整表。释放的 cuda:3/5 部署 Long Reconvla/K2mean s46 或其他 gap
- 所有 Table 1 数据稳定 → Paper Agent Patch：(1) 更新 Table 1 Long 行为 5-method 3-seed, (2) D134 措辞更新, (3) 新增 trigger-rate vs improvement scatter Figure, (4) Appendix per-seed table
- π0.5 precompute 完成 (ETA 5/24-25) → 训练 π0.5 CRM → eval → 验证跨模型泛化性
- 全部数据 + Paper Agent Patch 完成 → submit_paper_to_review 最终审稿

### 5. 🎯 战略上下文
- **D134 叙事（核心）**: "Gating correctly modulates intervention intensity — improves where VLA uncertain (Spatial +2.1, Goal +1.3), preserves where VLA confident (Object ≈0, Long ≈-0.3pp within noise)。Adaptive ≥ CRM on ALL 4 suites (+1.0 to +1.8pp)。" 这比 D133 的 "positive everywhere" 更强更诚实。
- **不能说的**：(1) "Adaptive ≥ VLA-only on all suites"（Long -0.3pp, Object 0.0pp）(2) "Adaptive ≥ CRM on every seed"（Long s44 反转 -0.5pp）(3) "no degradation"（Long mean 确实低了 0.33pp）。安全词："comparable to" / "within noise"。
- **Trigger-rate vs Improvement Figure**：Reviewer 强烈推荐。4 suite 散点图 (trigger_rate → Δ SR)，Pearson ~0.95+。这是论文的 killer figure，直接回答 "when does Adaptive help?"。
- **Object 5-seed 分析**：Adaptive 77.8%±2.1% vs VLA-only 77.7%±1.3%。CRM std=2.3% > Adaptive std=2.1% > VLA-only std=1.3% — 支撑 "gating reduces CRM-induced variance"。
- **易错点**：(1) 不要把旧 pipeline (lerobot eval) 数据和新 pipeline (wrapper eval) 混淆；(2) bjb2-40593 只有 1 张卡且之前缺 CRM checkpoint 反复崩溃；(3) Agent session reset 后容易长时间空转，必须立即发 pickup 指令；(4) 同名文件陷阱——不同服务器上相同文件名可能是不同方法的输出（看 baseline_mode 字段）。
- **CoRL DDL 2026-05-29**，剩 ~4 天。核心 Table 1 数据已足够投稿（4 suite 3-seed），当前跑的是加固 variance + 扩展 coverage。


---
