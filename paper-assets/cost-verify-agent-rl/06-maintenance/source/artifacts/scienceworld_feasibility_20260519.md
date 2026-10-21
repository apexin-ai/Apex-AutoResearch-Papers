# ScienceWorld 环境可行性调研报告

**日期**: 2026-05-19  
**目的**: 评估 ScienceWorld 作为第二个实验环境，支撑论文 "environment-agnostic" claim 的可行性

---

## 1. 环境概述

ScienceWorld（Wang et al., EMNLP 2022, Allen AI）是一个文本交互式虚拟环境，任务来自美国小学科学课程。环境包含 10 个互联房间、218 种物品、25 种高层动作（每步可达 ~200K 种动作组合）。共 30 种任务类型（涵盖热力学、电路、化学、生物等 10 个主题），每个任务类型有多个参数化变体（不同物品/目标）。Episode 长度 10-120 步（均值约 40 步，显著长于 ALFWorld 的 ~15 步）。奖励为 0-100 连续值（基于子目标完成进度），完成全部子目标得 100 分。Python API 通过 py4j 桥接 JVM 运行。安装：`pip install scienceworld`。

**与 ALFWorld 的关键差异**：

| 维度 | ALFWorld | ScienceWorld |
|------|----------|--------------|
| 任务类型 | 6 种家务任务 | 30 种科学实验 |
| Episode 长度 | ~15 步 | ~40 步（10-120） |
| 奖励结构 | Binary sparse（0/1） | Dense continuous（0-100） |
| 动作空间 | ~50 可用动作/步 | ~200K 组合/步 |
| 底层引擎 | TextWorld (Python) | JVM via py4j |
| 科学推理 | 无（常识操作） | 需要（热力学/电路/化学） |

---

## 2. RL 适配性分析

### 2.1 RAGEN 框架兼容性

**已有适配器**：项目远程服务器（westd）上已存在 ScienceWorld 环境适配代码：

```
/root/autodl-tmp/cost-verify-agent-rl/RAGEN/ragen/env/scienceworld/
  __init__.py    # 导出 ScienceWorldEnvConfig, ScienceWorldTXTEnv
  config.py      # 配置 dataclass（task_names, score, max_steps, simplification_str）
  env.py         # 继承 BaseLanguageBasedEnv 的适配器
```

接口与 ALFWorld 一致（reset/step/available_actions），已对接 RAGEN 的环境注册机制。

**SFT 数据已存在**：`/root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl`（3000-4000 条专家轨迹）。

### 2.2 需要关注的适配问题

1. **奖励结构差异**：论文核心分析基于 binary sparse reward（成功/失败）。ScienceWorld 的 dense reward（0-100）需要二值化（如 threshold=100 视为成功）才能复用现有 advantage 计算和 sign misattribution 分析框架。
2. **JVM 依赖**：py4j 桥接需要 Java 环境，且 `parallel_friendly=false`（线程安全限制）。RAGEN 已用 `_ENV_CACHE + _ENV_LOCK` 处理，但多 worker 并行 rollout 效率可能受限。
3. **Episode 长度**：平均 40 步意味着 step-independent window h=2 的 information loss 会更严重（丢失更多历史 context）。这对论文 claim 是**有利的**：如果 h=2 在更长 episode 上同样坍缩，支持 "mechanism is environment-agnostic" 论点。
4. **动作空间巨大**：200K 组合需要 simplification 或 admissible action filtering。环境 API 支持 `simplification_str` 参数，现有适配器已处理。

### 2.3 适配工作量估算

| 工作项 | 预估工时 | 说明 |
|--------|----------|------|
| 环境适配器调试/验证 | 0.5 天 | 已有代码，需 dry-run 验证 |
| 奖励二值化 + config 对齐 | 0.5 天 | 修改 reward function 为 binary |
| SFT 训练 | 1 天 | 用现有 SFT 数据 fine-tune Qwen3-1.7B |
| RL 实验（Cell A: h=2 坍缩复现） | 2-3 天 | 核心验证实验 |
| 评估 + 分析 | 1 天 | OOD eval，sign agreement 分析 |
| **总计** | **5-6 天** | |

---

## 3. 已有 LLM Agent Baseline

### 3.1 经典方法（ScienceWorld 原始论文分数，满分 100）

| 方法 | 类型 | 平均分 | 备注 |
|------|------|--------|------|
| DRRN | RL agent | 16.7 | 最强传统 RL |
| KG-A2C | RL agent | ~10 | 知识图谱增强 |
| CALM | RL agent | ~8 | Language model guided |

### 3.2 LLM Prompting 方法

| 方法 | 模型 | 平均分 | 年份 |
|------|------|--------|------|
| SayCan | GPT-3/4 | 33.8 | 2023 |
| ReAct | GPT-3/4 | 36.4 | 2023 |
| Reflexion | GPT-3/4 | 45.3 | 2023 |
| SwiftSage | GPT-4 + T5-770M | **84.7** | 2023 (NeurIPS) |
| ReflAct | GPT-4 | ~45 | 2025 |
| ERL | GPT-4 | 56.1 | 2025 |

### 3.3 RL Fine-tuning 方法（与本项目最相关）

| 方法 | 模型 | 环境 | 关键发现 | 年份 |
|------|------|------|----------|------|
| EMPO² | Qwen 系列 | ScienceWorld | GRPO 基础上 +128.6% | 2026 (ICLR) |
| Paying Less Gen. Tax | Qwen-2.5-7B | SciWorld + 3 others | Sokoban→SciWorld 迁移优于 ALFWorld→SciWorld | 2026 |
| Can RL Improve Gen. | Qwen-2.5-7B | SciWorld + others | 域内泛化好，跨域迁移弱 | 2026 |
| Towards Generalizable | LLM + RL | ScienceWorld | 教育环境 RL 适配 | 2024 |

**关键发现**：已有多篇 2026 年论文在 ScienceWorld 上做 RL fine-tuning，说明技术路径可行。但**无人研究 step-independent credit assignment 问题**，这是我们的独特贡献点。

---

## 4. 可行性结论

### 4.1 判断：**可行，且工程量可控**

- RAGEN ScienceWorld 适配器已存在，SFT 数据已备好
- 核心验证只需一组实验：Cell A（h=2 step-independent）是否在 ScienceWorld 上同样坍缩
- 预计 5-6 个工作日可出结果

### 4.2 风险评估

| 风险 | 级别 | 缓解措施 |
|------|------|----------|
| JVM/py4j 不稳定（长训练 crash） | 中 | 设 checkpoint 频率，environment auto-restart |
| SFT baseline 太弱（1.7B 在 ScienceWorld 上 ~0%） | 中高 | 先跑 SFT eval 确认 baseline 合理后再启 RL |
| Dense reward 使 binary 转换后信号太 sparse | 低 | 可用 subgoal completion threshold（如 >50 视为 partial success）|
| Episode 过长导致 RL 训练不收敛 | 中 | 限制 max_steps=50，选简单任务子集 |
| GPU 资源竞争（与主线 ALFWorld 实验冲突） | 中 | 排期在 ALFWorld 实验完成后 |
| 适配器代码未经充分测试 | 中 | 先 dry-run 10 episode 验证 |

### 4.3 对论文的价值

- **强化核心 claim**：如果 h=2 step-independent 在 ScienceWorld（40 步 episode）上也坍缩，证明 information loss 和 sign misattribution 是 environment-agnostic 的
- **更长 episode 的额外证据**：ALFWorld ~15 步 vs ScienceWorld ~40 步，不同 episode 长度下的失败机制对比增加论文说服力
- **审稿人期望**：单环境实验容易被质疑 generalizability，第二个环境是 EMNLP 审稿人常见要求

---

## 5. 建议下一步

1. **立即**：在 westd 上 dry-run ScienceWorld 适配器（10 episode），验证环境能正常运行
2. **确认 SFT baseline**：用现有 SFT 数据训练 Qwen3-1.7B，eval OOD 分数。如果 <5%，考虑用 8B 或增加 SFT 数据
3. **核心实验设计**：只需 Cell A（h=2 step-independent, full_context baseline）对比，不需要完整 factorial
4. **排期**：在 ALFWorld 主线实验（8B Cell A）出结果后启动，预计 1 周完成

---

## 参考文献

- Wang et al. "ScienceWorld: Is your Agent Smarter than a 5th Grader?" EMNLP 2022
- Lin et al. "SwiftSage: A Generative Agent with Fast and Slow Thinking" NeurIPS 2023
- "EMPO²: Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization" ICLR 2026
- "Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents" 2026
- "Can RL Improve Generalization of LLM Agents? An Empirical Study" 2026
- RAGEN: "Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning" 2025
