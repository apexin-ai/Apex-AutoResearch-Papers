# reviewer / loop_14.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`a88b36b7237f4dbdf9a5.json`](../../sessions/a8/a88b36b7237f4dbdf9a5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-23T19:52:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：`gpu_ids` 需从 project config 确认（此前未见越界，但每次审查训练实验必查 CUDA_VISIBLE_DEVICES）
- 服务器只有一台 `westd-11235(root)`，cuda:0 有 49GB orphan 进程占用不可用，cuda:1 空闲
- 论文已进入提交 pipeline（DDL 2026-05-25），**禁止任何改动 experiments.tex / main.tex 除非 Director 明确授权**——所有数字已通过完整交叉核查
- DeepSeek masking 只报 seed42（99.33%），seed123（93.95%）不入论文——D121 决议
- Qwen-1.5B no_trace 保持 3-seed 均值 72.35±4.48——D120 决议，我此前错误声称 data_count 不一致已正式撤回

### 2. 🖥️ 基础设施快照
- 服务器：`westd-11235`，账号 `root`
- 代码根目录：`/root/trace-verdict-study`
- 论文目录：`/root/trace-verdict-study/docs/paper/`（main.tex + 分文件 introduction/method/experiments/discussion/related_work/conclusion/appendix.tex）
- 最新 PDF：`/root/trace-verdict-study/docs/paper/main.pdf`（436KB, 2026-05-24 01:10 CST）
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/`
- Figures：`/root/trace-verdict-study/figures/paper/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/`
- 活跃进程：无（两 GPU 均空闲，无 RUNNING 实验）
- ssh_read_only 注意：`|` 被安全过滤器拦截，grep 多模式用 `-e` flag 或分开调用

### 3. 📊 当前状态
所有 188 个实验已完成，论文已编译，进入 ARR submission form 填写阶段。

我刚完成的工作：
- **Final pre-submission quality check**：数字一致性全文交叉核查 PASS，历史 flag 全部解决，评估 quick-win 后建议不追加实验
- **CodeLlama masking 预案**：已发给 Director（正向/负向均可被现有 framing 覆盖，不建议阻塞提交）
- **叙事线最终审查**：4 条 contribution 与 experiments 一一对应，无漂移，证据充分
- 审查了 AI Assistants appendix 新增（Appendix 最后一节，披露 Claude 使用）
- 审查了 appendix tables / main text tables / tail256+gradmask source 审计 worker——均无变更

Registry: 0 RUNNING, 0 PREPARING。无待回调 Worker/Cron。

### 4. 📋 待办
- Director 说"提交" → 确认远程 main.pdf 是最终版（当前 2026-05-24 01:10），提醒本地 submitted.pdf 需同步
- 若 Director 决定跑 CodeLlama masking seed123 → 审查结果：≥98% 无需改文；<95% 建议 rebuttal 加一句 architecture-dependent variance
- 若收到章节审查请求 → 先检查 Agent 是否看过 red-section skill（L1 合规），再按 §5 对抗审查
- 若收到 Framing 调整提案 → 立即 Read `negative-framing-review.skill.md` 四维度审查

### 5. 🎯 战略上下文
- **核心结论**：complete traces hurt SFT（77-82%），exception_only 近乎完美（≥99.33%），gradient masking 证实 ≤4% dilution / ≥96% content quality，phase transition at 384→512 tail tokens
- **决策链关键**：D116（reframe 从"exceptions help"到"traces hurt"）→ D117（gradient masking 证实 content quality）→ D121（DeepSeek masking seed123=93.95% 不入论文）
- **易错点**：
  1. DeepSeek exception_only 在 Appendix full_results 表里是 3 seed（99.33/99.50/99.33），mean=99.39±0.10——不要和 gradient masking 的 DS 99.33%（单 seed）混淆
  2. CodeLlama full_trace 在 Table 1 是 head-2048 proxy（79.9%），不是真正的 full_trace——脚注 $^\S$ 标注
  3. Qwen-1.5B no_trace 有两个 checkpoint 目录（`qwen15b_` 和 `qwen1.5b_`），前者 67.31%（May 16 旧代码），后者 72.61%（May 21 新代码）——论文用 3-seed 均值 72.35±4.48，不是任何单一 run
  4. ssh_read_only 不支持 pipe `|`，grep 多模式必须用 `-e` 或分多次调用
  5. **"Frontier model crossover" 是论文最有冲击力的结果之一**——GPT-4o 在 no_trace 下赢 SFT，exception_only 下 SFT 反超 12pp。已在 Abstract 提及但 Intro 尚未显式引用，若有下一轮 polish 可建议加入


---
