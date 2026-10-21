# agent / loop_19.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`aab7219877f4bfc15eb8.json`](../../sessions/aa/aab7219877f4bfc15eb8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-21T19:41:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x 的 cuda:0, cuda:1, cuda:2, cuda:3（4张），无其他服务器可用
- LLaMA SFT s42 ign_f1=0.5384（D130 审计修正值，不是 0.5514）
- LLaMA RSFT s42 ign_f1=0.5714（D129 修正值，不是 0.5839），3-seed mean=0.5654±0.0052
- LLaMA SFT 脚本 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}` 会覆盖框架注入，必须通过 `GPU=X` 传物理 GPU 编号
- Evidence tax 必须用 matched@2048 方法论（D137），@1024 数据仅作历史参考
- read_registry API 有索引问题：registry.yaml 尾部的实验（line 12353+）不被 API 返回，需直接 Read YAML 文件或用 reconcile_crons 确认状态

### 2. 🖥️ 基础设施快照
- **主服务器 westd-37389**: SSH alias `rtx5090-4x`, 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB disk (~46% used, 190GB free)
- 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3
- 工作目录: ~/autodl-tmp/ (数据/模型), ~/faith-evidence-ie/ (代码)
- HF cache: /root/autodl-tmp/.hf_cache
- 活跃进程（cron 确认全部存活）:
  - eval_llama_rsft_s42_with_evidence_2048 (pid=70706, cuda:0)
  - plan017_14b_rsft_eval_2048 (pid=70388, cuda:1)
  - eval_llama_sft_s43_with_evidence_2048 (pid=64391, cuda:2)
  - eval_llama_sft_s44_with_evidence_2048 (pid=64023, cuda:3)
- bjb2-12179: 数据源，208G 数据完好，迁移主体完成

### 3. 📊 当前状态
Session 19 启动，完成了：session-start 初始化、d112 stale RUNNING 条目清理（→DONE）、派 2 个 CPU Worker、向 Director 汇报。

**Registry RUNNING**（实际活跃，但 API 不返回——在 registry.yaml line 12353-12451）:
- eval_llama_sft_s44_with_evidence_2048 (cuda:3) — SFT s44 matched@2048 with-evi
- eval_llama_sft_s43_with_evidence_2048 (cuda:2) — SFT s43 matched@2048 with-evi
- plan017_14b_rsft_eval_2048 (cuda:1) — 14B RSFT matched@2048 with-evi
- eval_llama_rsft_s42_with_evidence_2048 (cuda:0) — LLaMA RSFT s42 matched@2048 with-evi

**Worker 运行中**（等回调）:
- worker_analysis_qwen-truncation-audit_20260521T033603 — Qwen 1.7B/4B/8B 截断不对称审计
- worker_analysis_matched-tax-data-compilation_20260521T033625 — 编译所有 matched@2048 evidence tax 数据

已向 Director 汇报当前状态（Session 19 启动报告），无待决策项。

### 4. 📋 待办
- s43/s44 SFT with-evi@2048 cron 回调 → 提取 metrics → 与已有 no-evi@2048 数据计算 matched SFT tax 3-seed → update_registry + memory.md
- RSFT s42 with-evi@2048 cron 回调 → 与 @1024 (0.5714) 对比 delta → 验证 RSFT tax 在 matched budget 下是否稳定
- 14B RSFT with-evi@2048 cron 回调 → 与 @1024 (0.5886) 对比 → 14B 截断影响评估
- Qwen 截断 Worker 回调 → 若不对称 >5pp 的 scale 存在 → 向 Director 汇报需要 Qwen @2048 批次（需 GPU）
- Matched tax Worker 回调 → 整合数据表 → 为 Director 出完整 evidence tax dashboard
- 全部 matched@2048 数据齐备 → 向 Director 提交 evidence tax narrative 最终版 + Reviewer 审查请求
- 空闲 GPU 出现 → 按 ROADMAP 优先级：Qwen @2048（若需要）> test set eval 准备 > EDCR 人工验证样本生成

### 5. 🎯 战略上下文
- 项目核心：FREIGE 论文 3 贡献——(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression
- 投稿：EMNLP 2026 Main（ARR July，~55天）
- D137 pivot: 所有 evidence tax 必须 matched@2048，因为 @1024 有截断伪影（D136 发现 SFT tax "方向不稳定"被推翻为截断假象）
- D139/D140: Qwen 8B evidence tax @1024 也不可信（截断不对称 31.8%），全尺度截断审计 critical——Qwen 截断 Worker 正在做这件事
- 当前 critical path: 4 个 matched@2048 eval → 3-seed matched SFT tax → 确定"magnitude instability vs consistent benefit"最终 claim → 更新论文所有 evidence tax 数字
- 易错点: (1) read_registry API 看不到最新 4 个实验——必须 reconcile_crons 或直接 Read registry.yaml 确认 (2) s42 SFT with-evi@2048 和 RSFT s42 with-evi@2048 是不同实验，别混淆 (3) report.md 告警区大量 mvp2_ 前缀实验是历史遗留，已 killed/failed，不需要处理


---
