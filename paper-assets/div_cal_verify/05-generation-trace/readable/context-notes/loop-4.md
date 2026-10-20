# reviewer / loop_4.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`a17dd909def499e3ae8c.json`](../../sessions/a1/a17dd909def499e3ae8c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T03:09:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目双卡：cuda:0 和 cuda:1，均属 westd-11235。无其他 GPU 白名单。
- medium 实验均为 n=1（seed=42）或 n=2（seed=42+123），不可标注 n=3。
- **medium_rgds PPL < medium_uncurated**（82.84 < 91.66）——与 125M 模式相反。论文 discussion.tex 中 "compound further" 预测已被证伪，scaling section 叙事必须修正，不可沿用旧预测。
- experiments.tex L16 "two of three seeds are complete" 仍未修复——3-seed 已全部完成，此句 stale。

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，代码根 `/root/div_cal_verify`，结果目录 `/root/autodl-tmp/div_cal_verify/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/`
- 论文 `.tex` 文件：`docs/paper/` 下（main, introduction, related_work, methodology, experiments, results, discussion, conclusion）
- 活跃进程（截至 handoff 时刻）：
  - cuda:0：medium_uncurated_seed123（tmux=chain_cuda0_s123），Gen 0/7 刚启动，后面串 rgds_seed123 → random50_seed123
  - cuda:1：medium_external_seed42（tmux=chain_cuda1），Gen 6/7 训练中（即将完成），之后串 medium_external_seed123

### 3. 📊 当前状态

**GPT2-125M（全部完成，n=3）**：论文数据已全部更新到 3-seed，最终一致性审查 PASS（已发 Director，3 个 minor warning）。

**GPT2-Medium 355M 完成情况**：
| 实验 | seed=42 | seed=123 |
|------|---------|----------|
| uncurated | DONE (91.66) | RUNNING Gen 0/7 |
| rgds | DONE (82.84) | PREPARING（串在 uncurated 后） |
| random50 | DONE (70.25) | PREPARING（串在 rgds 后） |
| external | RUNNING Gen 6/7 | PREPARING（串在 external_seed42 后） |

**已发 Director 的关键审查**：
1. 最终一致性审查（PASS with warnings）——W1 stale text, W2 Distinct-n/Self-BLEU 定义未报告, W3 gen0 ratio 小数值偏差
2. medium_rgds 结果与论文预测相反（初始 critical → 降为 warning，因 RGDS vs Random +18% 仍确认 alignment gap）

### 4. 📋 待办
- medium_external_seed42 完成 → 核实 Gen7 数据，确认 4-method 对比（n=1），检查 External PPL 是否在 Random-Uncurated 之间
- cuda:0 chain（uncurated→rgds→random50 seed=123）每个完成 → 逐一核实，关注 rgds_seed123 是否复现 rgds_seed42 的模式（PPL < Uncurated 但 > Random）
- medium_external_seed123 完成 → 4-method × 2-seed 全景对比，判断是否有统计检验能力
- 所有 medium 完成 → **强制审查 scaling section 叙事**：discussion.tex "compound further" 必须改、experiments.tex \placeholder 必须填、Table 3 需扩展为 4-method
- methodology.tex Distinct-n / Self-BLEU 定义仍需删除或补数据

### 5. 🎯 战略上下文
**核心 claim 状态**：C1-C3 在 125M 坚实（n=3）。355M 初步数据确认 C3（RGDS 劣于 Random +18%），但效应量大幅缩小（125M +72% vs 355M +18%）。最易判断错的点：**不要因为 medium_rgds < medium_uncurated 就认为 alignment gap 不存在**——正确对比是 RGDS vs Random（同 budget），而非 RGDS vs Uncurated（不同 budget）。

**355M 的新故事**：所有方法崩溃更严重（+169%~+245%），50% 数据裁剪本身提供极强正则化（Random 70.25 vs Uncurated 91.66 = -23%），alignment gap penalty 仍存在但 relative 减弱。论文需把这个 nuance 写进 scaling section，不能简单说 "scales up"。

**deadline**：EMNLP 2026 ARR，2026-05-25。论文 125M 部分基本就绪，355M 部分需等实验完成后 1-2 天写入。cuda:0 chain 约需 12-18h（3 个 8-gen 实验串行），cuda:1 external 约 4-6h（seed42 剩 1 gen + seed123 全 8 gen）。时间上可行但紧。


---
