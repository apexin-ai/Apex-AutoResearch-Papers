# agent / loop_7.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`c931a5205d45d19d716c.json`](../../sessions/c9/c931a5205d45d19d716c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T04:18:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 bjb1-17606 cuda:0, cuda:1（config 中无 gpu_ids 字段，但所有历史实验均使用这两张卡）
- checkpoint 路径必须含 "qwen" 字符串（train.py:137 断言），所有微调 checkpoint 需创建含 "qwen" 的 symlink
- submit_training_job 命令必须自带 conda 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python ...`（不能用 source activate，不能假设 .venv 存在）
- textworld/tatsu 线程不安全——**禁止 parallel_friendly=true / max_workers>1**，已在 exp023 验证崩溃，决策已定（见 memory.md）
- exp021 的 25% success 数字不可信（D024：4-ep 高方差 vs 16-ep 仅 6.25%），不要基于 25% 做乐观预判

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，2× RTX PRO 6000 Blackwell 94GB
- 工作目录：/root/cost-verify-agent-rl
- Python：/root/miniconda3/bin/python（conda base 环境，非 venv）
- 模型：Qwen3-1.7B（Instruct 变体，无 -Instruct 后缀）
- 最佳 checkpoint：/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/（symlink: qwen3_exp021_ragen_sft_v4）
- 数据：v4 RAGEN 格式 SFT 数据（2546 train + 133 val），由 convert_sft_to_ragen_format.py 从 v3 转换
- Checkpoints 目录：/root/autodl-tmp/checkpoints/
- TMPDIR：/root/autodl-tmp/tmp/（/tmp 只 30GB，必须重定向）
- W&B：未配置，cron 直接检查进程 + 日志
- 活跃进程：无（GPU 空闲）
- 活跃 cron：无（reconcile 返回 0）

### 3. 📊 当前状态
**GPU 空闲，无实验运行。** 上一轮 session 在 exp023 失败后派了 4 个 Worker 但尚未收到回调：

| Worker | 任务 | 状态 |
|--------|------|------|
| worker_diagnose_exp023_grpo_parallel | 诊断 exp023 crash 原因 | running |
| worker_research_verl-agent-migration | 调研 verl-agent 迁移（解决并行问题的长期方案）| running |
| worker_code_exp023c-serial-restart | 编写 exp023c 串行重启代码 | running |
| worker_code_exp023b-tatsu-fix-v2 | 尝试修复 tatsu 线程安全 v2 | running |

实验链最新进展：
- exp021_ragen_sft_v4 (success/inconclusive)：RAGEN 格式 SFT，val 25%（不可靠）/ 6.25%（16-ep）
- exp022_grpo_from_sft_v4 (killed)：step 0 val 12.5%（8-ep），step_time ~208s，因 D024 不确定性被 kill
- exp023_grpo_parallel (failed)：尝试多线程并行加速但 textworld/tatsu 崩溃
- exp020b_grpo_from_sft (negative)：entropy 坍缩 61%，train success 18.75%→4.69%，kl=0.1 太弱

### 4. 📋 待办（条件触发式）
- worker_code_exp023c-serial-restart 完成 → 审查代码 → 用 exp021 checkpoint + 串行 + kl_loss_coef≥0.5 提交 GRPO 实验（GPU 空闲是失职）
- worker_diagnose_exp023_grpo_parallel 完成 → 记录根因到 registry（已知是 tatsu 线程不安全，确认无其他问题）
- worker_code_exp023b-tatsu-fix-v2 完成 → 大概率无法修复（memory.md 已决定放弃），存档结论
- worker_research_verl-agent-migration 完成 → 评估迁移成本，写入 memory.md 作为 Phase B 参考
- 下一个 GRPO 实验（exp024?）step 0 val 出结果 → 如果 success < 10%，说明 SFT baseline 确实不够强，需要考虑：(1) 更多 SFT 数据 (2) SPEAR 替代 GRPO (3) 更大模型
- GRPO 30 步完成且 success ≥ 20% → MVP Phase A 通过，向 Director 汇报 + 准备 Phase B（selective verification）

### 5. 🎯 战略上下文
**核心假设**：B-IAVR — 训练 agent 学会选择性自我验证，用 action change 作为 verification informativeness 的 reward。基于 Self-Guide (arXiv 2604.03098)。

**决策链关键节点**：
- D006: 纯 GRPO 在 base success ~1-2% 下无法工作 → pivot to SFT warmup
- D012/D013: Dense reward gaming 证明 reward shaping 有风险 → 回归 sparse GRPO
- D021: SFT 数据必须与 RAGEN 格式精确匹配（根因已验证）
- D024: exp021 结果不可靠，但 RAGEN 格式对齐方向正确

**最容易判断错的事**：
1. **不要高估 SFT baseline**——exp021 的 25% 可能是 6.25%，exp022 step 0 给出 12.5%（8-ep），真实值可能在 10-15% 区间。GRPO 能否在此基础上提升到 20% 仍未验证
2. **不要再尝试并行 rollout**——textworld/tatsu 线程不安全已板上钉钉，串行 ~200-400s/step 就是当前上限
3. **kl_loss_coef 必须 ≥ 0.5**——0.1 导致 exp020b entropy 坍缩 61%，这是已验证的教训
4. **reward scale 不影响 GRPO**——norm_adv_by_std_in_grpo=True 下 0/10 和 0/1 等价，不要当变量调
5. **GRPO 替代算法 SPEAR 是 backup**——如果下一轮 GRPO 仍然失败（success 不提升或继续坍缩），应向 Director 提议 SPEAR（专门解决 sparse reward 冷启动）而非继续调参


---
