# research backup plan expert sft

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_backup-plan-expert-sft_20260514T081623_result.json`
- **Structured JSON:** [`873727e7819d97153700.json`](../../sessions/87/873727e7819d97153700.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 调研报告：Expert Trajectory SFT 作为 GRPO 冷启动 Backup Plan

### 问题诊断

当前 SFT warmup (1200条) 教会了格式但未教策略，导致 GRPO 初始 success rate 仅 4-8%。GRPO 在 sparse reward 下因 zero-reward symmetry 无法产生有效梯度信号，grad_norm→0, pg_loss→0，策略崩塌。核心需求：**提升 GRPO 初始 success rate 到 >5%，打破 zero-reward 死锁**。

### 可行方案（按可行性排序）

**方案 1：ALFWorld 自带 Expert Walkthrough 生成完整轨迹 SFT 数据**
- 数据来源：`alfworld` 包自带 rule-based expert，用 `alfworld-generate` 可对每个 game 生成 expert solution。每个 task 被分解为子目标序列（find→pick→find→heat→find→place）
- 工作量：**1-2 天**。写脚本调 ALFWorld expert 在 3000+ train games 上跑通，收集成功轨迹，转为 multi-turn SFT 格式
- 预期效果：3000+ 条 expert 完整轨迹 SFT 后，初始 success rate 预计 15-30%（参考 MACLA 用 1425 条轨迹达 82%，但那是大模型）
- **推荐度：最高**。数据质量有保证（100% 成功），数量充足，无需外部依赖

**方案 2：HuggingFace 现成 SFT 数据集**
- 数据来源：`u-10bei/sft_alfworld_trajectory_dataset` (v1-v5) — 模板生成的 expert 轨迹，支持 ReAct 和 function-calling 格式；`yijunyang/alfworld-sft-dataset` — 数据查看器有报错，质量待验证
- 工作量：**半天**。下载 → 格式转换 → SFT
- 预期效果：取决于数据与你的环境/prompt 格式对齐程度。模板生成数据可能与真实 ALFWorld 交互有 gap
- 风险：格式不匹配需要大量适配工作，v1-v5 多个版本说明作者也在迭代质量

**方案 3：Reflexion/ReAct GPT-4 轨迹蒸馏**
- 数据来源：[Reflexion repo](https://github.com/noahshinn/reflexion) 的 `alfworld_runs/root` 有 GPT-4 运行日志；[Emma-Alfworld](https://github.com/stevenyangyj/Emma-Alfworld) 有 LLM teacher 轨迹
- 工作量：**1-2 天**。解析日志 → 筛选成功轨迹 → 格式化
- 预期效果：GPT-4 轨迹质量高但风格可能不适合小模型直接模仿，需要 filtering
- 风险：日志格式非标准 SFT 格式，解析工作量不确定

**方案 4：XRPO 式 In-Context Seeding（不改 SFT，改 GRPO）**
- 做法：在 GRPO rollout 时注入 few-shot expert 示例，打破 zero-reward symmetry
- 工作量：**半天**。修改 prompt 模板，加入 2-3 个 expert 示例
- 预期效果：不改变模型权重但能提升 rollout 中的成功概率，让 GRPO 有正样本可学
- 风险：增加 context 长度，可能影响训练效率

**方案 5：SuperRL 式 SFT-RL 动态切换**
- 做法：当 GRPO batch 中所有 rollout 失败时，fallback 到 expert trajectory 做 SFT 更新
- 工作量：**2-3 天**。需要修改训练循环，实现 RL/SFT 动态切换逻辑
- 预期效果：理论上最优——防止崩塌同时保留探索。[SuperRL](https://arxiv.org/html/2506.01096) 和 [BREAD](https://arxiv.org/html/2506.17211v1) 均验证有效
- 风险：工程复杂度高，调参难度大

### 关于数据量

- DeepSeek-R1 冷启动用 "thousands" 条 CoT 数据
- 对 1.7B 小模型 + ALFWorld 6 类任务：**每类 200-500 条完整成功轨迹（共 1200-3000 条）** 应足够将初始 success rate 提到 10-20%
- 必须是 **multi-step 完整轨迹**（含 observation-action 交互），单步 action-only 不够教策略

### 推荐

**首选方案 1**（ALFWorld 自带 expert）+ **方案 4**（in-context seeding）组合：先用 expert 生成 3000 条高质量轨迹做 SFT warmup 替换现有 1200 条，同时在 GRPO 中加 few-shot seeding。两者工作量合计 2 天，互相正交，效果叠加。

Sources:
- [Rethinking Expert Trajectory Utilization in LLM Post-training](https://arxiv.org/abs/2512.11470)
- [SuperRL: RL with Supervision](https://arxiv.org/html/2506.01096)
- [BREAD: Branched Rollouts from Expert Anchors](https://arxiv.org/html/2506.17211v1)
- [XRPO: Targeted Exploration for GRPO](https://arxiv.org/html/2510.06672v2)
- [GRPO++ Tricks](https://cameronrwolfe.substack.com/p/grpo-tricks)
- [ALFWorld GitHub](https://github.com/alfworld/alfworld)
- [Reflexion GitHub (ALFWorld runs)](https://github.com/noahshinn/reflexion)
- [Emma-Alfworld](https://github.com/stevenyangyj/Emma-Alfworld)
- [u-10bei ALFWorld SFT Dataset](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset)
- [Task Phasing: Curriculum from Demonstrations](https://arxiv.org/abs/2210.10999)
- [DeepSeek-R1](https://arxiv.org/html/2501.12948v1)

---
