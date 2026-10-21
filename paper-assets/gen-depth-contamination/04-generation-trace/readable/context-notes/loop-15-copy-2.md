# reviewer / loop_15.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`556d2518e461bcf2aa7e.json`](../../sessions/55/556d2518e461bcf2aa7e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T19:33:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-22115 GPU 白名单：`gpu_ids=[0,1,2,3]`，本项目独占整台机器
- westd-42896 GPU 白名单：`gpu_ids=[0,1]`（2×RTX PRO 6000 Blackwell 96GB）
- 论文 DDL: **2026-05-25** EMNLP 2026 ARR
- Wikipedia K*=1 结果（Pythia/OLMo/LLaMA-8B）不写入正文主线，放 Appendix（D054 决策）
- discussion.tex 有未修正数据错误：Wikipedia λ≈4.2 应为 ≈3.1（排除 OLMo 后），C4 λ range "2.9-6.3" 上界来源不明（实际 4 模型范围 2.15-3.51）。已通知 Director，等 Paper Agent 修正。

### 2. 🖥️ 基础设施快照
- **cqa1-22115** (root): 4×RTX 4090D 24GB, `/root/autodl-tmp/gen-depth-contamination/`
  - 结果目录: `results/exp_*/`（pairwise_auc.json, jsd.json, summary.txt）
  - 数据目录: `data/exp_*/depth_*.jsonl`
  - 脚本: `scripts/run_pipeline.py`
  - HF cache: `/root/autodl-tmp/.hf_cache/`
- **westd-42896** (root): 2×RTX PRO 6000 96GB, `/root/autodl-tmp/gen-depth-contamination/`
  - PATH 已修复 (`/root/miniconda3/bin`)
  - 14B 已下载完成 (29.6GB, 8/8 shards)
  - 32B 下载中（shards 1-8 done, 9-15 进行中，PID 4571）
  - Scorer 1.5B 已就绪
  - C4 seed data: `exp_14b_c4/depth_0.jsonl` + `exp_32b_c4/depth_0.jsonl` (各 5000 行)

### 3. 📊 当前状态
**刚完成审查**：exp_arXiv_mistral7b (K*=3 ✓), exp_arXiv_qwen7b (K*=3 ✓), exp_wiki_llama8b (K*=1, borderline)。已发三份审查报告 + JSD λ/semantic ablation 综合审查 + 语义消融更正（TF-IDF→all-MiniLM-L6-v2）。

**仍在运行**：
- exp_wiki_mistral7b (cqa1 cuda:1, ~still running, 5000 docs Wikipedia)
- exp_wiki_qwen7b (cqa1 cuda:0, prepping/running)
- exp_14b_c4 / exp_32b_c4 (westd, 等模型下载完)

**等待中**：
- Wiki Mistral/Qwen-7B 完成 → 审查 + Wikipedia domain 全貌总结
- 32B 下载完成 → 14B/32B 实验启动 → 审查 scale effect
- Paper Agent 综合 patch（arXiv 5-model table, JSD 数值修正）

### 4. 📋 待办（条件触发式）
- exp_wiki_mistral7b 完成 → 审查生成质量（关键：C4 K*=1 的 Mistral 在 Wiki 是否也 K*=1？若是则强化 "domain-specific one-wash" narrative）
- exp_wiki_qwen7b 完成 → 汇总 Wikipedia 全部 6 模型结果，判断 continuation vs rewrite mode 是否为 K* 分界线
- exp_14b_c4 完成 → 核心审查：K*=1 则触发 scorer confound concern（1.5B scorer 对 14B 生成文本可能区分力不足），建议 14B self-scorer 对照
- exp_32b_c4 完成 → 同上，且若 K*=1 需检查是否 discussion.tex 第 59 行预测 "13B+ may yield K*=1" 的证据
- Paper Agent 提交 JSD 数值修正 patch → 验证 Wikipedia λ 是否改为 ≈3.1，C4 range 是否有 7 模型完整数据支撑
- Director 转发章节审查 → 按 §5 模板评分

### 5. 🎯 战略上下文
**核心结论链**：K* bounded + domain-dependent。C4=2 (7/8), arXiv=3 (5/5), Wiki≈1 (continuation mode)。Binary filtering > graduated (C3 confirmed)。Mistral one-wash is domain-specific not model-intrinsic (D056)。

**最易判断错的事**：
1. **pp 单位**：1pp = 0.01，历史两次犯 10× 错误。报告 AUC 差异前必须二次核验。
2. **OLMo 不是普通 K*=1**：OLMo 在非 C4 域是 capacity failure（JSD 0v1=0.329 arXiv, =0.169 Wiki → 生成文本离域），不能与 Mistral/Pythia/LLaMA 的 genuine one-wash 混为一谈。
3. **Wikipedia Qwen-1.5B K*=2 是 rewrite mode**（exp-023），其他 Wiki 实验全是 continuation mode → 比较时注意 mode 差异。
4. **语义消融用的是 all-MiniLM-L6-v2 密集嵌入**（非 TF-IDF），我之前误判已更正。
5. **14B/32B scorer confound**：若这些大模型 K*=1，不能直接 claim "scale reduces K*"，需排除 1.5B scorer 能力不足的混淆因素。


---
