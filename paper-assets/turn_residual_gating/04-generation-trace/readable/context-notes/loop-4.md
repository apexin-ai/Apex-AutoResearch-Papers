# director / loop_4.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`eb57ceb1b361c19c4be4.json`](../../sessions/eb/eb57ceb1b361c19c4be4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-22T22:49:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **westd-20861:cuda:0** 一张卡，用户明确说"单卡跑就行"，不要申请扩容或使用其他服务器的 GPU
- **任何涉及模型加载/梯度计算的脚本 = GPU 工作**，绝不在训练期间启动（M023 教训：gradient_conflict_analysis.py 占 72 GiB 撞死 SS s42）
- 训练启动必须 **tmux + 日志重定向 + 启动后 15s 三项验证**（nvidia-smi/tmux ls/tail log），三项全 PASS 才算成功（M024 教训：两次中断）
- DDL **ARR May 2026-05-25**，不是 August 2026-08-03
- GAR 全名是 "Goal **Accessibility** Ratio"（不是 Attention），来自 Dongre et al.

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861 (connect.westd.seetacloud.com)，工作目录 `/root/turn_residual_gating`
- GPU：1× RTX PRO 6000 Blackwell 102GB
- 活跃进程：**d048_ss_s42 resume v3**，PID 33402，tmux session `ss_s42_v3`，日志 `runs/d048_ss_s42_resume_v3.log`，Epoch 1 ~52%，预计 ~4.7h 完成
- Cron 已注册监控 PID 33402（120s interval）
- 论文本地路径：`projects/turn_residual_gating/paper/main.tex`（编译 PDF 在同目录 main.pdf）
- 附录图片：`projects/turn_residual_gating/artifacts/fig_*.pdf`（已从远程同步到本地）
- 数字更新脚本：本地 `projects/turn_residual_gating/scripts/update_paper_numbers.py`（14 条规则，33 处替换，dry-run 模式）

### 3. 📊 当前状态
**刚完成**：
- Round 3 全部 13 项写作修复 + writing skill 对照优化（Gap A Table 1 格式 / Gap B Intro 断段 / Gap E caption）
- Appendix D：6 个可视化（gate heatmap / cross-model / AR GAR decay / gate distribution / loss curves / β-steering table）
- Table 2 扩展 Failure Mechanism 列
- queue_runner.sh 截断至 8 项必做（从 14 项砍掉 LO/UG/PCGrad multi-seed）
- 编译验证：13 页（主文 8 页），0 error，视觉检查通过
- **已提交 Round 4 审稿**（apr_20260522T224837_ewgs，pending 等用户审批卡片确认，推荐 continue 模式）

**RUNNING**：d048_ss_s42（SS scheduled sampling seed 42，resume v3 从 epoch_0）

**等待中**：
- 审稿审批卡片（用户点击后 Group C 启动 Round 4）
- SS s42 训练完成 cron 回调 → 自动触发 eval + queue_runner

### 4. 📋 待办
- SS s42 cron 回调"训练完成" → Agent 执行 `d048_eval_ss_s42.sh`（TF + AR N=50 + bootstrap CI）→ 接着 queue_runner 自动串行后续（AR N=50 existing → SS s123 → SS s456 → Base s123/s456 → TG s123/s456）
- SS s42 eval 结果出来 → 检查 GAR gap 是否与单 seed 一致（期望 ~1.57×），如果 variance 异常大（CoV>50%）→ 需要降级 SS claim 为 promising-but-unstable
- 审稿审批通过 → Group C Round 4 启动，不需要 Director 额外操作
- 审稿报告回来 → **必须** Read `review-report-action.skill.md` 做 Holistic Pass + Action Matrix，禁止"已知悉"
- 全部 multi-seed 完成 → 运行 `update_paper_numbers.py --dry-run` 检查 → `--apply` 更新论文数字 → 重新编译 → 可能需要 Round 5 审稿
- 梯度冲突热力图 → 等全部训练完成后 GPU 空档再做（CPU 不行，需要 GPU 计算梯度）

### 5. 🎯 战略上下文
- **核心发现**：ThreadGate 的 auxiliary attention loss 在 exposure bias 下泛化失败（TF GAR 0.50 → AR GAR 0.016，~31× gap）。双路缓解：inference-time steering（β=5, GAR→0.727）+ training-time SS（gap→1.57×）。跨模型在 Llama 确认（27× gap）
- **审稿历史**：Round 1-3 Overall 3.0 (Findings)，目标 3.5 (Conference)。用户指令"不要保守，打硬仗"——不降级 claim，补实验补证据
- **决策链**：D048（修复计划）→ D049（Round 3 不降级 SS contribution，补 3 seeds）
- **用户 曹晓玉** 是 PI，**陈卓凡** 是合作者（要求附录 fancy + 按 writing skill 写）
- **易错点**：(1) 不要把 westd-22162/home-1x5090 的空闲 GPU 当成本项目资源 (2) 不要在训练期间启动任何 torch 相关分析脚本 (3) bootstrap CI 用 `curve[2:]`（turns 3-T），不是 `curve[1:]` (4) SS s42 已中断 2 次（OOM + SSH 断连），第 3 次稳定运行中，不要动它


---
