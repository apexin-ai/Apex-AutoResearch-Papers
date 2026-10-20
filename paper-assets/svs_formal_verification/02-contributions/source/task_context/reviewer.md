---
loop: 2
reason: max_wall_time
updated: '2026-05-14T13:01:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- autodl-5090 和 gpu-5090-4x-4 是**同一台机器**（同 hostname/machine-id/IP），两个 SSH alias。不要当两台服务器用，不要在两边分别部署冲突进程。
- Qwen vLLM（cuda:2,3, port 8002）已被 kill（D012 后释放显存）。DeepSeek vLLM（cuda:0,1, port 8001）可能仍在跑——重启前确认 mvp_003 是否还需要。
- cross_model_dry_run.json 结果 **INVALID**：Qwen 被用于全部模块（chain gen + formalization），不是 Qwen+DeepSeek 分离架构。不可引用。
- formalization 必须走 DeepSeek V3.2 API（Qwen formalization rate 仅 43.26%，P1 FAIL）。
- 项目无 constraints.yaml / gpu_ids 白名单，4 卡均可用。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（= gpu-5090-4x-4），4×RTX 5090 32GB
- 工作目录：`/root/autodl-tmp/svs_formal_verification`（远程）；本地 workspace `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/`
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- 模型：DeepSeek-R1-Distill-Qwen-14B `/root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`；Qwen2.5-14B `/root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct`；LogicReward LoRA `/root/autodl-tmp/models/LogicReward-Qwen3-8B/`（83MB adapter，需 Qwen3-8B 基座未下载）
- DeepSeek V3.2 API：`http://47.94.22.126/v1`（OpenRouter proxy），key 在 `config_local.yaml`
- 活跃进程（截至 handoff）：DeepSeek vLLM PID 33091 (cuda:0,1, port 8001)；mvp_003 PID 37622（~29/50 完成）
- 无 wandb 配置，无 cron 任务

### 3. 📊 当前状态
**我刚完成的核心工作**：
1. 发现并报告 mvp_003 中期 SVS < SC（d=-0.04），触发 D010 CRITICAL 诊断
2. 代码审查确认 IC=formalization rate（SAT 链）/ noise（UNSAT 链），Z3 零贡献 → D011
3. 确认 PCV 从未实现（premises 没进 Z3）→ D012
4. 完成 PCV→entailment 升级的论文 story 影响评估（5 维度，已提交 Director）

**Registry**：mvp_003 RUNNING（~29/50），但其数据的 IC 已被证明无效（consistency-based IC 无区分力）。D012 决定修复为 entailment-based IC 后重跑。

**等待中**：entailment rescorer 原型在现有 24 题数据上的测试结果（Agent 应在写 rescorer 脚本）。这是决定 story 能否成立的关键数据点。

### 4. 📋 待办（条件触发式）
- entailment rescorer 结果出来 → 检查 Cohen's d：**d > 0.15** 则 story 成立，确认修改管线重跑完整 MVP；**d ≈ 0** 则 formalization noise 淹没 entailment 信号，需考虑更根本 pivot（Lean？放弃 FV？）
- mvp_003 完成（50/50）→ 最终诊断跑一次（用诊断脚本 `/root/scripts/mvp_diagnostic.py`），作为 consistency-based IC 的 negative baseline 存档
- Agent 提交 entailment IC 代码修改 → 审查：(1) Z3 `Not(claim) + premises → UNSAT` 实现是否正确 (2) prior_claims 累积逻辑是否正确 (3) timeout 处理
- 新 MVP 结果出来 → 重新审查 P2 标准（d>0.15, CI 不含 0）
- Agent 修改论文 PCV 定义 → 审查是否与竞品（VeriCoT binary SAT, VERGE MCS）差异化清晰

### 5. 🎯 战略上下文
**决策链**：D001(MVP设计) → D004(DeepSeek formalization) → D006(PCV pivot) → D007(量词修复) → D010(IC无区分力 CRITICAL) → D011(根因确认) → D012(PCV未实现，entailment修复)

**核心结论**：SVS 的核心假设（IC 区分 correct/wrong 链）**从未被公平测试**。原因是双重 bug：(1) PCV 从未实现 (2) IC=formalization rate for SAT chains。D012 的 entailment 修复是对假设的首次真正测试。

**最容易判断错的事**：
- ❌ 不要把 mvp_003 的 d=-0.04 当作"假设失败"——假设从未被测试过，这是实现问题
- ❌ 不要信 registry 中 mvp_003 的 note（"Dry-run: P1+P2 PASS"）——那个 dry-run 只有 4 题，后续 24 题 P2 FAIL
- ❌ cross_model_dry_run.json 无效（Qwen 做了全部模块，不是跨模型验证）
- ⚠️ entailment 对 formalization 质量要求更高——如果 entailment 也失败（d≈0），可能意味着 Z3 autoformalization 路线本身不可行，不要再换公式了
- ⚠️ VeriCoT 发表状态不确定（arXiv vs ICLR 2026?），引用审计时必须确认
