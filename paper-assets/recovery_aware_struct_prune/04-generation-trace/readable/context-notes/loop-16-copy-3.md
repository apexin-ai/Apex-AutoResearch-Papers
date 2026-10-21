# reviewer / loop_16.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`3cac955e623f16863636.json`](../../sessions/3c/3cac955e623f16863636.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-21T01:43:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C005：westd-29022 cuda:0/1/2/3 + westb-23072 cuda:0/1。越界立即 CRITICAL。
- westd 是 AutoDL 实例：根分区 30GB（禁止存大文件），所有 checkpoint/模型必须在 `/root/autodl-tmp/`。
- HF 下载必须 `source /etc/network_turbo` + 设 `HF_HOME=/root/autodl-tmp/.hf_cache`。`HF_DATASETS_OFFLINE=1` 会阻断 eval——CKA-only 15% eval 的旧命令带了这个变量但靠缓存幸存，新提交必须去掉。
- Cron 监控有误判倾向：eval 遇到长序列 stall（100-180s/sample）会被 cron 标 "failed"。**确认进程死亡前必须 `ps -p PID` + 读日志尾部**，不能只看 cron 通知。

### 2. 🖥️ 基础设施快照
- **westd-29022** (root)：`/root/recovery_aware_struct_prune`（代码），`/root/autodl-tmp/recovery_aware_struct_prune`（checkpoints/results）
- **westb-23072** (root)：`/root/recovery_aware_struct_prune`（代码），checkpoints 在本地
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`（westd），GSM8K cached at `/root/autodl-tmp/.hf_cache/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866`
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/`
- 活跃进程：**全部 6 GPU 空闲**（westd 0/1/2/3 + westb 0/1 均 0% util，0 MiB）
- 25% pipeline worker 刚完成探查，尚未看到实际训练启动

### 3. 📊 当前状态
**刚完成**：15% multi-seed GRPO eval 全部 4 个实验成功完成并验证：
- CKA-only 15%: 72.76% ± 0.57pp (seeds: 73.09/73.09/72.10)
- Standard 15%: 65.56% ± 0.50pp (seeds: 66.11/65.13/65.43)
- Gap: 7.20pp, p<0.001

**Registry DONE/success**：eval_gsm8k_grpo_cka_only_15_seed123, seed456, eval_gsm8k_grpo_standard_15_seed123_v3, seed456_v3

**已向 Director 提交**：
1. Table 5 reward 修复验证通过（peak reward 统一）
2. 15% 三种子完整结果 + 统计
3. Standard 15% GRPO delta per-seed 超 1pp 的 warning（decoupling claim 需弱化措辞）
4. 全景 ROI 评估（推荐 15% CKA heatmap + 25% 单种子）

**等待中**：Director 对 25% pipeline 和 15% heatmap 的决策；Round 2 审稿结果

### 4. 📋 待办（条件触发式）
- 25% 训练启动 → 核实 GPU 在 C005 白名单内 + 确认 checkpoint 写入 autodl-tmp
- 25% eval 出结果 → 验证 accuracy，计算 CKA-only vs Standard gap，判断是否半 collapse
- 15% CKA heatmap 完成 → 与 20% heatmap 对比 diagonal mean（20% 是 0.62 vs 0.88-0.92）
- Round 2 审稿报告到 → 按 review-report-action skill 评估，标注哪些 finding 需要补实验
- 论文 appendix 15% 表格更新 → 核实 3-seed mean/std 数值一致性
- Decoupling claim 措辞修改 → 审查是否从 "universally |Δ|<1pp" 改为 "mean |Δ|<1pp"

### 5. 🎯 战略上下文
- **核心结论**：CKA-only >> importance-based pruning for GRPO recovery capacity。证据链完整：20% 3-seed (4.55pp, p=0.0009) + 15% 3-seed (7.20pp, p<0.001) + recovery gradient (4 methods) + cross-architecture (Qwen-Math SFT 30.5pp gap)
- **决策链关键节点**：D084(scenario A 确认) → D086(Standard 15%) → D088(SFT 15%) → D090(3-seed 恢复) → D091(维持 3-seed)
- **最易判断错的事**：
  1. Cron "failed" 通知 ≠ 进程死亡。本 session 中两次 cron 误报（eval stall 被误判为 kill）。**始终独立验证 PID + 日志**。
  2. Registry 可能被 worker 错误更新（如诊断 worker 把 RUNNING 改成 DONE/failed）。**读 registry 后如有疑点，SSH 核实实际进程状态**。
  3. 论文有两个 SFT Standard 20% 模型（westb 59.21% vs westd 59.29%），D090/D091 决定保留 3-seed mean（含跨服务器 seed）。不要重新质疑这个决策。
  4. Table 5 的 1.5B 列用 "training mean" reward（非 peak），7B 列用 peak。两套约定在 caption 中明确标注，不要标为 inconsistency。


---
