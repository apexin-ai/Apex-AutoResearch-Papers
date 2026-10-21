# director / loop_2.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`18b6a9ff67059011306b.json`](../../sessions/18/18b6a9ff67059011306b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T03:15:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb1-17606 的 cuda:0, cuda:1（C001 约束，CUDA_VISIBLE_DEVICES="0,1"）
- AutoDL 根分区仅 30G，所有大文件/checkpoint/cache 必须放 `/root/autodl-tmp/`
- 训练启动前必须确认 `RAY_TMPDIR=/root/autodl-tmp/ray_tmp`（exp007 因未设此项 /tmp 满崩溃，已发生 3 次磁盘事故）
- save_freq ≤ total_steps/3（exp007 save_freq=20 对 30 步训练导致 checkpoint 全丢）
- GRPO config `_alfworld_exp008_sft_grpo.yaml` 的 save_freq 已改为 5，GRPO 启动前再次确认

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，工作目录 `/root/cost-verify-agent-rl/RAGEN/`
- Python：conda base (`/root/miniconda3/bin/python`)，aml-train 镜像
- 模型：Qwen3-1.7B（HF cache 在 `/root/autodl-tmp/.hf_cache`）
- SFT 数据：`u-10bei/sft_alfworld_trajectory_dataset` 已下载（1200 条轨迹），转换脚本 `/root/cost-verify-agent-rl/scripts/convert_sft_data.py`，输出目录 `/root/autodl-tmp/sft_data/`（尚为空，转换未执行）
- GRPO config：`/root/cost-verify-agent-rl/RAGEN/configs/_alfworld_exp008_sft_grpo.yaml`（save_freq=5, lr=1e-6）
- 磁盘监控脚本已部署（PID 183184，30 分钟检查根分区）
- 活跃进程：无（exp007 已崩溃清理，GPU 空闲）

### 3. 📊 当前状态
Agent 正在修复 `convert_sft_data.py` 两个问题（我发了 urgent 指令）：
1. action 提取改用 `tool_calls[0].function.arguments` 而非正则反推
2. system prompt 加 `"You're a helpful assistant. "` 前缀匹配 RAGEN 运行时

Registry: exp008_sft PREPARING（SFT warmup），其余实验全 DONE/FAILED/KILLED。
等待 Agent 修复脚本 → 执行转换 → dry-run → 提交 SFT 配置供审批。

### 4. 📋 待办
- Agent 回报 convert_sft_data.py 修复完成 → 确认修复正确 → 等 SFT 配置提交
- Agent 提交 SFT 实验方案（epochs、LR、data size、save_freq）→ 审批 exp008_sft
- SFT 训练完成 → 验证 action_is_valid > 50% → 批准 exp009（SFT checkpoint → GRPO 30 步）
- exp009 step 10 → action_is_valid > 15%（kill 条件待根据 SFT 后起点调整）

### 5. 🎯 战略上下文
- 决策链：D001(ALFWorld+Qwen3-1.7B) → D002(全量微调) → D003(kill exp003) → D004(解析器修复) → D005(override kill→LR 5e-6，已撤回) → D006(SFT warmup→GRPO)
- 核心发现：Qwen3-1.7B 语法输出可解析但不知道 ALFWorld 合法命令集（action_is_valid 仅 8.35%），需要 SFT 教命令语义再接 GRPO
- **最容易判断错的事**：D005 的教训——kill 条件触发时不要仅看趋势就 override，先让 Agent 完成根因分析（是学习速度问题还是能力缺失）再决策
- **易踩坑**：(1) Agent 可能遗漏 save_freq 修复（已发生一次）(2) SFT 和 GRPO 的 system prompt 必须一致 (3) SFT checkpoint 格式需与 RAGEN FSDP 兼容，GRPO 启动前必须 dryrun 验证


---
