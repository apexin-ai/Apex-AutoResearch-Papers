# reviewer / loop_11.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`12dcb13608f3e11fe519.json`](../../sessions/12/12dcb13608f3e11fe519.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-23T19:49:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-19183 cuda:0, cuda:1（仅此两张）
- C001 约束: Goal classification 实验必须 trained + untrained 对照齐全后才写 conclusion，单臂数据禁止下结论
- CF 数据必须全部使用标准化管线（`openvla_*_standardized_v1` / `tracvla_*/trained/` / `nora_*/trained/`），禁止混用旧 `counterfactual_10tasks` / `counterfactual_spatial` 数据
- 论文 R² 数值统一使用 bootstrap v3 MCCV 值（非 standardized pipeline 原始 probe 值），两者差异可达 3-5x

### 2. 🖥️ 基础设施快照
- 服务器: westd-19183，代码根目录 /root/vla-ssd，数据/结果 /root/autodl-tmp/vla-ssd/
- Python: /root/miniconda3/bin/python（conda base 环境）
- 本地 workspace: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/
- 论文 tex: `docs/paper/*.tex`，产出: `artifacts/`
- Bootstrap v3 结果: /root/autodl-tmp/vla-ssd/results/bootstrap_v3/（20 JSON，10 arch-suite × 2 conditions）
- CF 标准化结果: /root/autodl-tmp/vla-ssd/results/{libero_goal,libero_spatial,libero_object,libero_long,tracvla_*,nora_*}/counterfactual_combined.json
- 活跃进程: 无（GPU 空闲）
- 活跃 cron: 无

### 3. 📊 当前状态
刚完成一轮完整的数据一致性审查：
- **d=1.97 幻影数值**: 已修复为 d=1.52（5 处 tex 文件）✓
- **OpenVLA Goal CF 统一到标准化管线**: Table 2/3/appendix 全部更新 ✓
- **Appendix Spatial d 列更新**: ✓，但 **CV 列仍为旧管线值**（WARNING 已提交，Empty 0.185→0.087, Wrong 0.093→0.272）
- **R² Table 1**: 全部 14 个 delta 和 10 个正常 CI 与 bootstrap v3 原始 JSON 完全吻合 ✓
- **CF 排序变化**: Goal wrong>empty (Δ=0.012, p≈0.74) 在噪声范围内，"6/8 empty first" 表述已足够 ✓
- **ROADMAP 数值修正**: 0/3→0/4, Δ range 更新为 MCCV 值 ✓

Registry: 无 RUNNING/PREPARING 实验。152 total, 105 success。
等待: Worker 修复 Appendix Spatial CV 列 + fig2 R² profile 重画完成。

### 4. 📋 待办
- Appendix Spatial CV 修复 worker 完成 → 确认 CV 列更新为 [0.087, 0.272, 0.162, 0.179]，caption "All d > 0.8" 改为 "All global d > 0.8"
- 论文编译 + 新图整合完成 → 做 paper-visual-review（pdf_to_images 检查排版/图表/字体）
- Director 提交 fresh review 请求 → 按审查模式 B 做全文对抗审查（先 Read paper-quality-lessons.skill.md）
- checkpoint 完整性确认: `openvla_goal_standardized_v1` config 中 `"model": "openvla-7b-finetuned-libero-object"` 是否为 stale metadata（任务列表确认是 Goal 任务，但 config field 存疑）→ Agent 应确认实际加载的 checkpoint

### 5. 🎯 战略上下文
- **论文核心**: VLA fine-tuning 的 instruction routing 分解为 training-associated（R² exit collapse, CF sensitivity）和 inherited（L1 attention）两类，跨 3 架构验证
- **决策链**: D095（跨架构升级）→ D096（claim 降级 VLM→VLA）→ D100（NLP control）→ D102（effect size threshold）
- **DDL**: Abstract 5/26, Paper 5/29
- **易错点**:
  1. R² 数值有两套: standardized pipeline（原始 probe, 高值）vs MCCV bootstrap v3（demo-level splits, 低值）。论文 Table 1 用 MCCV，别混
  2. 两个 bootstrap CI 异常已正确用脚注披露: NORA Goal trained（CI=[0.91,1.61] 不含 delta 0.455）和 TracVLA Spatial untrained（CI=[-0.61,-0.46] 方向反转）
  3. CF metric 不可跨条件比较: trained 用 Cohen's d (action MSE), untrained VLM 用 cosine distance，不同 scale
  4. OpenVLA 的 reference 是 OXE-pretrained VLA（不是纯 VLM），这是 VLA→VLA vs VLM→VLA 区分的核心


---
