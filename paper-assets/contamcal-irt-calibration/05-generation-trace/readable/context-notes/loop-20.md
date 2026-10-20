# director / loop_20.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_20.md`
- **Structured JSON:** [`002d5b8ef38bce175e4a.json`](../../sessions/00/002d5b8ef38bce175e4a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_messages
updated: '2026-05-23T03:10:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cqa1 服务器 cuda:0（项目配置 gpu_ids=[0]）
- westd 服务器已被用户释放，不可使用
- Volume control 实验结果无论正负都直接提交 ARR（D215 决策），不因结果改变提交决定
- Yi-1.5-9B 已 defer 到 camera-ready（D218），不要在当前周期安排
- Falcon3 d000 s123 降级为 optional（D218），不阻塞提交
- DDL: EMNLP 2026 ARR May 25（距现在 ~36h）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com:21977)，工作目录 /root/contamcal-irt-calibration
- Python：conda base 环境（aml-train 镜像）
- 模型：Falcon3-7B，训练 checkpoint 在 /root/contamcal-irt-calibration/outputs/
- Volume control 训练数据：50K clean SFT + 16,533 non-benchmark MCQ = 66,533 items
- 活跃进程：sft_falcon3_7b_volume_control 训练（PID 752802, cuda:0, 33% at last check ~UTC 02:30, ETA ~UTC 05:30）
- Cron：600s interval 监控训练进程，完成后自动回调 Agent
- 论文源码：projects/contamcal-irt-calibration/docs/paper/（main.tex 入口）
- 编译 PDF：最近一次编译 PASS，20 页，0 critical warnings

### 3. 📊 当前状态
**刚完成**：
- Round 11 文本修复 Batch 1-4（共 24 项）全部完成
- Round 12 partial review（C/D/E/F/G）全部 PASS，2 个 minor warning 已修复（Figure 1 caption "1-4pp"→"<1 to ~10pp"，Table 1 Qwen-14B 行 cross-seed 数据移至脚注）
- P12 三场景写作模板已预草拟（artifacts/p12_scenario_templates.md）
- Round 12 完整 checklist 已保存（artifacts/round12_checklist.md）
- Paper Agent Batch 4：Intro cross-benchmark hook + C2 novelty 强化完成

**RUNNING**：
- sft_falcon3_7b_volume_control — Falcon3-7B 等量非 benchmark MCQ 训练，解决 W1 Critical data quantity confound。33% at last check, ETA ~UTC 05:30

**等待中**：
- Cron 回调：训练完成后 Agent 自动启动 eval（MMLU 5-shot + ARC 25-shot + GSM8K 8-shot）
- 云 GPU 申请（Yi bf16）：Manager 48h+ 未回复，已 defer（D218）

### 4. 📋 待办
- Volume control 训练完成 cron 回调 → Agent 自动启动 eval（MMLU+ARC+GSM8K）
- Eval 结果回报 → 判断场景 A/B/C（CTRL_MMLU vs d000=59.56% vs d100=62.96%），选对应模板
- 场景确定 → dispatch Paper Agent P12（§5.4 volume control discussion，用 artifacts/p12_scenario_templates.md）
- P12 完成 → paper_compile_and_check → submit_paper_to_review（Round 12, recommended_review_mode="fresh"）
- Round 12 审稿报告回来 → 按 review-report-action skill 处理 → 修复 → 最终编译
- 最终编译 PASS → 通知用户提交 ARR

### 5. 🎯 战略上下文
- **核心问题**：Round 11 评分 3.0（Findings），目标 4.0（Conference）。最大弱点是 W1 Critical：augmentation 设计的 data quantity confound → DiD null → "是 contamination 还是 additional training？" 链条
- **Volume control 是唯一关键路径**：无论结果如何都能写（场景 A 最有力解决 W1，场景 B 通过 Collapse 修正效应 -13pp 强化 causal 证据，场景 C 做 decomposition），但场景不同 framing 强度差异很大
- **Reviewer 确认**：framing "spectrum of dose-response patterns" 是最优选择；C2 (no memorization) 是最被低估的贡献；Round 12 推荐 fresh mode
- **易错点**：
  - D000_MMLU 用的是 59.56%（s42），D100_MMLU 用的是 62.96%（s42）。s123 的 d100 是 62.68%——不要混用 seed
  - Table 1 已改为纯 s42 数据（Qwen-14B cross-seed 移至脚注），注意保持一致
  - 8 页限制刚好卡住（主文到 page 8 底部），§5.4 新增内容需要压缩其他段落腾空间
  - Paper Agent 已有活跃 session，不需要 created_new_session
- **用户态度**："想尽办法拿4"，"都得做，目标是4不是3.5"——高度积极，不允许降级目标


---
