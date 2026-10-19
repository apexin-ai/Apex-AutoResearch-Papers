# reviewer / loop_10.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`b72c4f1c7259aa827e1b.json`](../../sessions/b7/b72c4f1c7259aa827e1b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-16T02:31:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **cuda:0, cuda:1 only**（C001 约束）。任何进程跑在 cuda:2+ 立即 CRITICAL
- 服务器 `bjb1-17606(root)`，SSH 端口可能因 AutoDL 重启变化——连接失败先查端口
- 模型路径：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`（SFT checkpoint）。`/root/cost-verify-agent-rl/models/Qwen3-1.7B-Instruct` 已被删除（D047/D048 确认 Qwen3-1.7B 就是 instruct 版本）
- exp028b config 的 model_path 指向不存在路径，已废弃——只看 exp028c

### 2. 🖥️ 基础设施快照
- 服务器：`bjb1-17606`，代码根 `/root/cost-verify-agent-rl`
- Python：conda base `/root/miniconda3/bin/python`
- 模型：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`
- W&B：entity=`xiaoyucorynne-`，project=`cost-verify-agent-rl`，run_id=`4yu6qz1m`
- 训练日志：`/root/runs/cost-verify-agent-rl/exp028c_selfguide_recipe.log`
- Checkpoint 输出：`/root/autodl-tmp/checkpoints/exp028c/`（save_freq=5）
- 活跃进程：TaskRunner PID=827923（Ray workers PID 828110/828111），2×RTX PRO 6000 48GB
- 训练配置：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp028c_selfguide_recipe.yaml`

### 3. 📊 当前状态
**exp028c_selfguide_recipe** (RUNNING, 3/100 steps)：Self-Guide recipe 对齐实验，avg 2976s/step (~49.6min)，ETA ~80h。

已验证的训练指标：
| Step | success | pass@8 | KL | entropy | action_is_valid |
|------|---------|--------|----|---------|-----------------|
| 0 val | 6.25% | — | — | — | 74.5% |
| 1 train | 13.28% | 37.5% | 0.019 | 0.263 | 76.4% |
| 2 train | 6.25% | 25.0% | 0.017 | 0.247 | 83.2% |

**已知日志 bug**：step:2 summary 从未写入日志文件（日志直接跳到 step 3 progress bar），但 W&B 有完整数据。用 W&B 交叉验证，不要只依赖日志 grep "step:N"。

**本 session 已发送 7 次 reviewer_post_to_director**：
1. CRITICAL: exp028b model_path 不存在
2. WARNING: exp028b 8 个参数错配 + penalty 错误
3. INFO: exp028c launch 审计通过
4. INFO: Phase B prereq 分析通过 + step 1 指标
5. WARNING: 3 个 citation 错误未修
6. INFO: citation batch1 修复通过 + step 2 数据完整性待验证
7. WARNING: step 2 数据已验证 + 训练趋势令人担忧 + citation batch2 通过

**等待中**：无活跃 worker 回调。Step 5 val 是下一个关键评估点（~2-3h 后）。

### 4. 📋 待办
- step 5 val 出结果 → 对比 D037 MVP 阈值（<20% FAIL, 20-25% WEAK, 30%+ proceed Phase B）。如果 val success ≤6.25% → 立即 WARNING，建议 Director 评估是否需要早停或干预
- step 5 checkpoint 保存 → 检查 `/root/autodl-tmp/checkpoints/exp028c/` 有无 checkpoint
- 任何新实验启动 → 检查 CUDA_VISIBLE_DEVICES 在 C001 白名单内
- Director 转发 framing 提案 → Read `negative-framing-review.skill.md` 四维度审查
- 新 worker_done 通知 → 审查产出，特别关注 literature_map 的 arXiv ID 和作者准确性

### 5. 🎯 战略上下文
- **D039**：论文 framing 锁定 cost-efficiency（非 performance）。Baseline ≥50% 是 story 可信度前提
- **D044**：Recipe Gap 分析确认 3 个根因（SFT poisoning、binary reward zero gradients、mini-batch 太小）
- **D050**：停止 exp028a（与 exp027 功能等价），否定根因 #2，转向全面 recipe alignment
- **exp028c 核心风险**：success 在 step 2 已回落到 baseline 6.25%。KL 控制住了（0.017 vs exp027 的 0.413）但 success 更差。group_size=8 导致 pass@8 只有 25%（75% group 零奖励）。recipe alignment 可能不足以解决稀疏奖励问题
- **竞争格局**：PA-MoE+GiGPO 1.5B 在 ALFWorld 达 93.8%（新小模型 SOTA）；Agent-Omit (ICML 2026) 是互补竞争者（减法 vs B-IAVR 的加法）；ARES 是最近竞争者
- **易错判断**：不要因为日历时间紧就说"做不完"——这是 AI 团队 + 弹性 GPU，只有 GPU-hours 不够才是真风险。不要建议降级 venue。不要只看 success 数字——action_is_valid 持续提升是正面信号，模型在学习合法动作


---
