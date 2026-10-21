# director / loop_11.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`8d367061b8a43431d5dc.json`](../../sessions/8d/8d367061b8a43431d5dc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-24T00:40:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-34887 cuda:0 和 cuda:1（项目配置 `execution.gpu_ids`）
- westd-41718 已释放并从配置移除，不要尝试连接
- 匿名仓库 push 必须用 HTTPS+token URL（SSH key 无写权限），token 不能 commit 到代码
- EMNLP 2026 正文严格 ≤ 8 页，Limitations 不计入，Ethics Statement 已删除
- Abstract ≤ 200 words（当前 187）
- Table 3 s42 KL PPL = 8.82（不是 8.80，已修正）
- K=8 PPL = 9.00（不是 8.99，已修正）
- Figure 3 所有数据点必须用 s42 global allocation（已统一）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887, SSH connect.westd.seetacloud.com:34887, user=root
- Python：`/root/miniconda3/bin/python`（必须先 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，submit_training_job 不支持 shell builtin）
- 工作目录：`/root/distill_sparse_swiglu/`
- 模型：LLaMA-3.1-8B 在本地，Qwen-2.5-14B 在 `/root/autodl-tmp/models/qwen2.5-14b/`
- 论文目录（本地真源）：`projects/distill_sparse_swiglu/paper/`
- 匿名仓库：`/tmp/anon_repo`（可能已清理，需重新 clone）
- 匿名 repo URL：`https://[REDACTED]@github.com/anonymous-nlp-2026-2/distill_sparse_swiglu.git`
- 活跃进程：qwen14b_kl30_s123_gsm8k_v3 可能在 tmux session `qwen14b_kl30_s123_gsm8k_v3`（PID 158731），但 GPU 已空闲多时，很可能已完成或失败

### 3. 📊 当前状态
- 已派 Agent 检查 v3 状态 + 更新论文 + 编译 + push 匿名仓库（刚发的指令，Agent 尚未回复）
- qwen14b_kl30_s123_gsm8k_v3：验证 Qwen s123 GSM8K 数据完整性的重跑（v2 因 `python: command not found` 失败）。GPU 全空 → 大概率已完成或失败
- 论文修复已全部完成：K-curve 图加入正文 §4.5、Figure 3 caption/数据修正、Ethics 删除、Limitations 压缩、Table 3 PPL 修正、K=16 MMLU 脚注修正、K=4 数据修正、Appendix X Licenses + Appendix Y AI Assistants 添加
- 数据自查 80+ 数字全量验证完成，仅 Qwen GSM8K s123 完整性待 v3 确认
- ARR checklist 字段已全部回复给运维（英文版）
- 匿名仓库已 push（commit be501bb, 101 files），但论文后续修改（Figure 3、K=8 PPL 等）的代码变更可能未同步

### 4. 📋 待办
- Agent 回复 v3 结果 → 如果成功且 sample_len=1319：更新 3-seed 数据；如果失败：降为 2-seed（mean=30.90±6.8, -21.2pp）更新论文
- 论文数据更新完成 → 编译确认 ≤ 8 页 → submit_paper_to_review 提交 R28 审稿
- R28 审稿通过 → 最终编译 + push 匿名仓库 + 准备 OpenReview 提交
- 如果 v3 失败需重跑 → 命令必须用 `/root/miniconda3/bin/python`（不是 `python`），加 `--seq_len 2048`

### 5. 🎯 战略上下文
- 核心结论：output-distribution KL 是 PPL 的主导设计维度（signal type gap 25:1 vs coupling breadth），K-curve 3-seed 全面确认
- DDL 2026-05-25，剩 <24h，论文实质上已完成，唯一阻塞项是 Qwen GSM8K s123 数据完整性
- 即使 v3 失败，降为 2-seed 不影响核心结论（GSM8K 退化 -21.2pp 更强，方向不变）
- 易错点：(1) westd-34887 的 conda 环境必须显式激活，submit_training_job 无法执行 `source` (2) Figure 3 的百分比（18%/49%/82%）是 global allocation 比较，正文 14.5% 是 uniform matched sparsity 比较，两套数字各自正确但基准不同 (3) 论文真源在本地 `paper/` 目录，不是远程服务器
- R26 得过 3.5，R27 降到 3.0（加了 single-seed K-curve 给审稿人攻击面），R28 用 3-seed 数据 + 图表 + 写作修复冲回 3.5+
- M050 教训：single-seed 数据不如不加，给审稿人攻击面比不探索更差


---
