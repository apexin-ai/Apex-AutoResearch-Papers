# reviewer / loop_2.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`42367609d1ec17eac74e.json`](../../sessions/42/42367609d1ec17eac74e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T03:17:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0, cuda:1 @ bjb1-17606（C001 约束）
- 所有 checkpoint / 大文件必须存 `/root/autodl-tmp/`，根分区只有 30GB
- RAY_TMPDIR 必须设为 `/root/autodl-tmp/ray_tmp`，否则 Ray session 文件填满 /tmp 导致训练崩溃（exp007 step 11 教训）
- AutoDL 网络需 `source /etc/network_turbo` 才能访问外网，否则 pip/HF 全超时

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606(root)，工作目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：`/root/cost-verify-agent-rl/models/Qwen3-1.7B`
- HF cache：`/root/autodl-tmp/.hf_cache`（u-10bei 数据集已下载，1200 条）
- SFT 数据目录：`/root/autodl-tmp/sft_data/`（已创建，尚为空，转换脚本未执行）
- SFT 脚本：`/root/cost-verify-agent-rl/scripts/convert_sft_data.py` + `sft_train.py`
- GRPO 配置：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp008_sft_grpo.yaml`（save_freq=5 已修复）
- 磁盘：根分区 25%（7.3G/30G），数据盘 12%（29G/250G）
- 活跃进程：无训练进程，GPU 双卡完全空闲（0% util）
- disk_monitor.sh 在后台运行（PID 183184）

### 3. 📊 当前状态
刚完成 SFT pipeline worker 审查（convert_sft_data.py + sft_train.py），发现并报告了以下问题：

**已报告但未修复的 warning（2 个）：**
1. `convert_sft_data.py` 的 `extract_action()` 从 env response 正则反推 action，但源数据 `tool_calls[0].function.arguments.action` 直接有准确 action——当前做法会丢数据
2. `RAGEN_SYSTEM_PROMPT` 缺少 `"You're a helpful assistant. "` 前缀（RAGEN ctx_manager.py:580 会加）

**发现但尚未报告的问题（2 个）：**
1. SFT 保存路径 `exp008_sft/final` vs GRPO 配置期望 `exp008_sft/checkpoint-final/` — 路径不匹配，GRPO 阶段会加载失败
2. `sft_train.py` 用 `dtype=torch.bfloat16`，正确参数名应为 `torch_dtype` — 可能导致模型以 fp32 加载

Registry 状态：
- exp008_sft: PREPARING（SFT warmup，尚未启动）
- exp008: PREPARING/killed（D006 撤回）
- exp007: DONE/failed（disk full step 11）

### 4. 📋 待办
- **立即**：将 sft_train.py 的路径不匹配 + dtype 参数名两个新发现报告给 Director
- convert_sft_data.py 执行后 → 检查 `extract_fail` 过滤比例，若 >20% 则升级为 critical
- SFT 训练启动后 → 验证 GPU 合规（cuda:0/1）+ RAY_TMPDIR 设置 + 模型实际精度（bf16 vs fp32）
- SFT 训练完成后 → 验证 action_is_valid > 50%，检查 checkpoint 路径是否与 GRPO 配置匹配
- exp009 (GRPO) 启动前 → 确认 checkpoint 路径、save_freq=5、RAY_TMPDIR 全部正确

### 5. 🎯 战略上下文
- 决策链：D001(ALFWorld+Qwen3-1.7B) → D002(全量微调) → D003(kill exp003) → D004(parser fix) → D005(LR 5e-6, 6分钟后被D006撤回) → D006(pivot到SFT warmup→GRPO两阶段)
- 核心诊断：exp007 证明 parser fix 有效（invalid_action 95%→1.6%），但 action_is_valid 仅 8.35%——模型不知道 ALFWorld 命令语义，需 SFT 教
- D005→D006 6 分钟急转弯是过程隐患（D005 分析不充分就决策），但 D006 的 SFT 方向本身数据支撑充分
- 最容易判断错的事：**不要把"GPU 长时间空闲"当 critical**——当前处于 SFT pipeline 代码开发阶段，空闲是正常的。但如果代码 bug（路径不匹配/dtype 错误）导致 SFT 失败再返工，那才是真浪费
- Phase A 目标：ALFWorld success ≥ 76%（匹配 Self-Guide 论文），SFT 中间目标 action_is_valid > 50%
- Phase B (B-IAVR) 被 Phase A 阻塞，代码已就绪（61 tests passed）


---
