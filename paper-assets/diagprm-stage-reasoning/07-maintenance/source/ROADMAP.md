# diagprm-stage-reasoning — Research Dashboard

> 最后更新: 2026-05-11 14:54 UTC | 更新原因: 采纳 Reviewer 建议：三档判定标准 + 云 GPU 预申请

## 核心方向
DiagPRM: 3阶段认知 PRM（localize→diagnose→patch）评估 code repair 轨迹推理质量，实现 targeted resampling——从诊断出的失败阶段重采样，保留已验证推理前缀。详见 IDEA_BRIEF.md。

## 当前阶段
**MVP 验证** — 验证核心假设：LLM judge 能否可靠分割诊断阶段并评估各阶段推理质量。

## 当前进展
- 2026-05-11 立项，Agent 已收到 MVP 准备任务（数据 + pipeline 代码）
- 等待用户提供 API keys（Anthropic + OpenAI）
- 目标：EMNLP 2026 ARR DDL 2026-05-25（14 天）
- 独立评估 28%（高风险），用户仍批准

## MVP 计划：Annotation Pilot（三档判定）

**核心假设**: LLM judge 可靠分割 code repair 轨迹为 localize/diagnose/patch 3 阶段并评估各阶段推理质量

**设计**:
1. 获取 SWE-smith 轨迹（30-50 条，resolved/unresolved 混合）
2. 两个 LLM judge（Claude + GPT-4o）分别做阶段分割 + 质量评估
3. 计算 inter-judge Cohen's kappa + partially-good 比例
4. 简单 stage-weighted reranking vs random

**三档判定标准**:
| 档位 | 分割 kappa | 质量 kappa | Partially-good | 后续行动 |
|------|-----------|-----------|----------------|---------|
| PASS | ≥ 0.6 | ≥ 0.5 | ≥ 15% | 全速推进 research |
| CONDITIONAL | ≥ 0.4 | ≥ 0.4 | ≥ 10% | 推进但投入 prompt 改进，research 阶段目标 kappa 0.7 |
| FAIL | < 0.3 任一 | < 0.3 任一 | < 5% | 方向需 pivot |

**预计**: 2-3 天 | 无 GPU | 需 LLM API key

## 近期任务
- [ ] 获取 LLM API keys（Anthropic + OpenAI）— 等用户
- [ ] Agent 完成数据准备 + annotation pipeline 代码
- [ ] 云 GPU 预申请（已发 Manager）
- [ ] 运行 pilot 并分析结果
- [ ] MVP 三档判定

## GPU 预算
- 已分配：home-1x5090 cuda:0（1x RTX 5090, 32GB）
- MVP 不需 GPU
- 已向 Manager 预申请云 GPU：4x A100 80GB, ~200h
- RTX 5090 可作 QLoRA 训练 fallback（慢但可行）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D002 | 2026-05-11 | MVP 判定标准从二档改三档（PASS/CONDITIONAL/FAIL），提前申请云 GPU | — |
| D001 | 2026-05-11 | MVP 策略：annotation pilot 验证阶段分割和推理质量评估可靠性 | — |

