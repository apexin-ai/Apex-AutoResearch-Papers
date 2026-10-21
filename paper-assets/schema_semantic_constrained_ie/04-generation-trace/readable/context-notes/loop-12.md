# agent / loop_12.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`e3837ee89389054b1dd7.json`](../../sessions/e3/e3837ee89389054b1dd7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-16T05:13:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 [cuda:0, cuda:1] + westd-21461 [cuda:0, cuda:1]，不可用其他设备
- EMNLP 2026 ARR 截止 **May 25**，距今 9 天，所有实验规划以此为硬 deadline
- D030 决策：第三模型锁定 **Mistral-7B-Instruct-v0.3**，不可自行更换
- submit_training_job 命令必须自带环境激活（`source /root/miniconda3/bin/activate && ...`），不要假设 .venv
- GPU 编号脚本内始终从 0 开始（框架注入 CUDA_VISIBLE_DEVICES 映射物理卡）

### 2. 🖥️ 基础设施快照
- **westd-16980**: 工作目录 `/root/schema_semantic_constrained_ie`，conda 环境 `/root/miniconda3`
  - cuda:0: w6_mistral_scierc_unconstrained RUNNING (PID 332156)
  - cuda:1: w5_qwen_docred_lora_constrained_eval RUNNING (PID 321568)
- **westd-21461**: 同项目路径，cuda:0 + cuda:1 均空闲（3 个 Mistral PREPARING 实验待提交）
- HF cache / 模型路径 / wandb config：未在本 session 探查，需 Worker SSH 确认
- **活跃 Cron**: 仅 1 个——w5_qwen_docred_lora_constrained_eval (pid 321568)
- ⚠️ w6_mistral_scierc_unconstrained (pid 332156) **无 cron 监控**，需要补注册或 spawn worker 检查

### 3. 📊 当前状态
**刚发生的关键事件**: w5_llama_docred_lora_constrained_eval 已转 **ANALYZING (conclusion=success)**，但 **Worker 池=0，无人处理**。这是最高优先级——Llama DocRED composability 2×2 的最后一格完成了，需要立即走 on-experiment-done 流程（提取 metrics → 更新 registry → 更新 ROADMAP/report → 汇报 Director）。

**Registry 快照** (44 总):
| exp_id | status | server | gpu | 说明 |
|--------|--------|--------|-----|------|
| w5_llama_docred_lora_constrained_eval | ANALYZING (success) | westd-16980 | 0 | ⚡ 需立即处理结果 |
| w5_qwen_docred_lora_constrained_eval | RUNNING | westd-16980 | 1 | cron 监控中，PID 321568 |
| w6_mistral_scierc_unconstrained | RUNNING | westd-16980 | 0 | PID 332156，⚠️ 无 cron |
| w6_mistral_scierc_constrained | PREPARING | westd-16980 | 1 | 等 cuda:1 空出 |
| w6_mistral_docred_unconstrained | PREPARING | westd-21461 | 0 | 可立即提交 |
| w6_mistral_docred_constrained | PREPARING | westd-21461 | 1 | 可立即提交 |
| 其余 38 | DONE | — | — | 33 success / 1 negative / 4 killed |

**等待中**: 无 Worker 回调；1 个 cron 回调（w5_qwen）；无 Director 决策待回。

### 4. 📋 待办（条件触发式）
- **立即** → spawn Worker 处理 w5_llama_docred_lora_constrained_eval 的 ANALYZING 结果（SSH 读 log/metrics → update_registry → on-experiment-done 全流程 → 汇报 Director Llama DocRED 2×2 完整数据）
- **立即** → 检查 w6_mistral_scierc_unconstrained 是否有 cron；若无，补注册 cron 或 spawn worker 查进度
- **立即** → westd-21461 两卡空闲，w6_mistral_docred_unconstrained + w6_mistral_docred_constrained 可并行提交（需先确认 Mistral 模型已下载到 westd-21461）
- w5_qwen_docred_lora_constrained_eval cron 回调到达 → on-experiment-done 流程 → Qwen DocRED 2×2 完整数据
- w6_mistral_scierc_unconstrained 完成 → cuda:0 空出 → 可提交 w6_mistral_scierc_constrained（或等 cuda:1 空出）
- Llama + Qwen DocRED 2×2 全部完成 → 更新论文 Table 3/5, §5.4/5.5, Appendix B（checklist 在 `artifacts/composability_update_checklist.md`）
- Mistral 全 4 格完成 → 三模型泛化性 claim 可写入论文 → 全文数字一致性审查 → May 25 提交

### 5. 🎯 战略上下文
**项目核心**: OntoCoDec = 两层约束解码（grammar + semantic）自动编译 IE ontology schema 为 token-level constraints，消除 LLM IE 的 ontology violations。目标 EMNLP 2026 ARR May 25。

**决策链关键节点**:
- D025/D028: Qwen + Llama SciERC 2×2 composability 双确认（FT+OntoCoDec DR→~0%, F1 中性）
- D030: 第三模型选 Mistral-7B-Instruct-v0.3，justify 为架构多样性（Qwen=custom, Llama=LlamaArch, Mistral=SlidingWindow）
- 当前阶段: Round 1 审稿应对，composability matrix 扩展

**Composability Matrix 进展**:
| | SciERC | DocRED |
|--|--------|--------|
| Qwen3-8B | ✅ 完整 | 🔥 constrained eval 跑中 |
| Llama3.1-8B | ✅ 完整 | ⚡ constrained eval 刚完成(ANALYZING) |
| Mistral-7B | 🔥 unconstrained 跑中 | ⏳ PREPARING (westd-21461) |

**易错点**:
- w5_llama_docred_lora_constrained_eval 已 success 但无人处理——**这是本 session 最紧急的事**，不要先搞 Mistral 而忽略它
- westd-21461 是新加的服务器，环境可能未完全就绪（Mistral 模型是否已下载？项目代码是否 sync？），提交前必须 Worker 探查
- w6_mistral_scierc_unconstrained 无 cron 监控，可能完成了但没人知道
- memory.md 记录了 DocRED composability 完成后需更新的论文位置 checklist（`artifacts/composability_update_checklist.md`），别忘了用
- CF Fallback ablation (D020) 是 analytical finding，已写入论文，不要重跑
- 目标分数路径：当前 Llama LoRA 成功 → 4.0/5，DocRED LoRA 全补完 → 4.25/5


---
