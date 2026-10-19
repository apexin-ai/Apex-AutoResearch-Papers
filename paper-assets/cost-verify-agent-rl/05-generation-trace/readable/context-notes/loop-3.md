# director / loop_3.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`3b051fc271e5e219b22f.json`](../../sessions/3b/3b051fc271e5e219b22f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T05:54:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb1-17606 的 cuda:0, cuda:1（RTX PRO 6000 Blackwell 94GB × 2）
- AutoDL 实例重启后 SSH 端口会变，连接失败先查端口不要反复重试
- conda 环境用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要创建 venv
- 大文件必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- pip install 前必须 `source /etc/network_turbo`

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，用户 root
- 工作目录：/root/cost-verify-agent-rl
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- HF cache：/root/autodl-tmp/.hf_cache
- Checkpoint 目录：/root/autodl-tmp/checkpoints/
- SFT checkpoint（exp008_sft 产出）：具体路径需 Agent 确认
- 活跃进程：无（exp011 已被 kill，GPU 空闲）

### 3. 📊 当前状态
**刚做完**：Reviewer 确认 exp011 静默崩溃（step 13），reward 分析预测完全验证（action_is_valid 反降 63.6%，entropy 0.089 策略坍缩）。已批准 D007（kill exp011 + reward 修复 + 从 step 5 恢复）并下发 Agent 执行。

**问题**：Agent 收到 D007 后空闲 3 小时未见产出，触发 RESET。**不确定 D007 是否已执行完毕**——下一轮必须先检查：
1. exp011 registry 是否已更新为 FAILED
2. reward 修复代码是否已实现
3. step 5 checkpoint 是否存在可用

**Registry 状态**：
- exp011: 名义 RUNNING 但实际已死（需确认是否已标 FAILED）
- exp008_sft: SUCCESS（SFT warmup 完成）
- exp001~exp010: 全部 FAILED/DONE
- 8 个 PREPARING 状态的旧实验（exp003 系列等历史残留）

### 4. 📋 待办
- 接手后立即 `get_project_status` → 确认 exp011 是否已标 FAILED、reward 修复代码是否已提交
- exp011 未标 FAILED → 让 Agent 更新 registry
- reward 修复未实现 → 重新下发 D007 指令：(a) format_penalty 降至 -0.01 或 0，(b) 用 `infos["score"]` 实现连续进度奖励，(c) 从 step 5 checkpoint 恢复（需先确认 checkpoint 存在）
- reward 修复已实现 → 审批新实验（exp012），分配 cuda:0+cuda:1，启动训练
- 两张 GPU 空闲 → 任何情况下都要尽快占满，不能空转

### 5. 🎯 战略上下文
**项目**：训练 agent 学会"何时验证"（B-IAVR），基于 Self-Guide 扩展，MVP 阶段。

**决策链**：
- D001: ALFWorld + Qwen3-1.7B 验证 B-IAVR
- D004: 修改解析器适配 Qwen3 格式
- D006: 撤回纯 GRPO，改 SFT warmup → GRPO 两阶段
- D007: Kill exp011，改 reward（连续 score + 降 format_penalty），从 step 5 恢复
- D008: Reviewer 确认 reward 分析正确

**核心瓶颈**：模型在纯 GRPO 下陷入 "format-penalty-only" 死区——score_max=0 连续 5 步，策略坍缩。SFT warmup (exp008_sft) 成功解决了格式问题，但后续 GRPO (exp009→exp010→exp011) 全部因 reward shaping 不当而失败。**reward 修复是当前唯一阻塞项**。

**易踩的坑**：
- step 5 checkpoint 可能不存在（exp011 从 step 10 启动，save_freq=5 下一次在 step 15；需查 exp009/exp010 是否有 step 5 checkpoint）
- 如果无可用 checkpoint，只能从 SFT checkpoint 重新开始 GRPO
- 不要把 PREPARING 状态的旧实验（exp003 系列）当作待执行任务，那些是历史残留


---
