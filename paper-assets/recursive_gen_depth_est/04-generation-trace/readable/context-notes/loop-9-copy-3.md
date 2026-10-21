# reviewer / loop_9.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`67730c3cbbb0325bdb88.json`](../../sessions/67/67730c3cbbb0325bdb88.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-16T05:08:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：gpu-6000pro-2 上只能用 cuda:0 和 cuda:1（config gpu_ids=[0,1]）
- 论文文件真源在本地 workspace `projects/recursive_gen_depth_est/docs/paper/`，远程服务器无 docs/paper/ 目录——审查论文改动只读本地
- Sub-B LOGO 数据（appendix L57-62）基于 buggy global counter 分组，重跑前所有 LOGO claim 不可引用（RR3-W4 critical）
- Sub-A per_class_recall ≈1.0 是 train-set 记忆，不可引用（RR3-W5）

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，工作目录 `/root/autodl-tmp/recursive_gen_depth_est`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型缓存：`/root/autodl-tmp/.ms_cache/`（Qwen2.5-7B-Instruct 等）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- 论文 tex：`docs/paper/*.tex`（本地），结果 JSON：`results/`（远程）
- 活跃进程：cross_scale_qwen7b_001 pipeline（PID 变化中，GPU 0，QLoRA d0→d5 链）——最后一次看到在 depth-3 finetune / depth-4 generation 阶段

### 3. 📊 当前状态
**刚完成的审查**（本轮 session）：
- worker_writing_w4_zeroshot_verification → PASS（双 LLM baseline 数字一致）
- worker_code_cross_scale_qwen7b_001 → WARNING（实验仍在运行，registry 待补）
- worker_writing_paper-fixes-batch3 → PASS（验证性质，4 项已修复）
- worker_writing_r3_final_text_updates → PASS（multi-τ 写入 + R3-N5 关闭，数字一致）
- worker_writing_r3_paper_fixes → WARNING（数字一致但 generalization.tex L4 "four axes" 应改为 five）
- worker_exp_r3n5_strategy_classify → WARNING（数字一致，registry 缺失，strategy classification 57.5%）
- worker_writing_bibliography_audit → PASS（47 条目，0 orphan，NeurIPS venue 统一）

**Registry RUNNING**：
- cross_scale_qwen7b_001：Qwen2.5-7B nucleus d0-d5，500 samples/depth，验证 7B scale depth signal

**等待回调**：
- cross_scale_qwen7b_001 完成 → 需全面审查（数字、EDD、与 1-1.5B 对比）

### 4. 📋 待办
- cross_scale_qwen7b_001 完成通知到达 → 核查 registry metrics 与服务器 results JSON 一致性 + 验证 EDD 计算 + GPU 合规
- 有 worker 写入 cross_scale 结果到论文 → 核查 discussion.tex "Scaling predictions" 段落 claim 是否与 7B 数据一致（当前 L42 说 "based on the mechanism identified at the 1–1.5B scale studied here"）
- Sub-B LOGO bug 修复完成 → 核查新 LOGO 数据替换 appendix L57-62 旧数据 + RR3-W4 是否可关闭
- generalization.tex L4 "four axes" 修复到达 → 确认改为 five 或 restructured
- 任何新写作 worker → 检查 appendix multi-τ 与 §4.5 叙事是否去重

### 5. 🎯 战略上下文
- 项目目标：EMNLP ARR May 25, 2026 投稿（距 DDL ~9 天）
- 核心结论链：perplexity tail features (p90_ppl + var_surprisal) → 70-85% 4-class depth estimation → EDD_{0.75}=4 → cross-model 66.4% / cross-strategy 59.1% → 特征决定性能天花板（5 种分类器收敛 78-79%）→ end-to-end PLM 差 19pp（缺乏 tail 特征的线性结构）
- 关键决策：D017→D021→D028 z-score 链——z-score 只对 LR 有效，RF 不受影响；"geometry-level shift" 已全文弱化为 "residual gap"
- **易错点**：
  - 论文文件在本地、训练代码/结果在远程——审查 "未改" 类结论必须双边核对
  - review_issues.yaml R1-W2 / RR3-W4 / RR3-W5 仍 in_progress/open——Sub-B LOGO bug 是遗留 critical
  - discussion.tex "automatic strategy identification is technically feasible" 现在有定量数据了（57.5%），如 worker 写入论文需确保 claim 强度匹配
  - cross_scale_qwen7b_001 是 7B 实验，如果 depth signal 衰减会影响 "Scaling predictions" 段落的 claim


---
