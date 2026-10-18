# code mvp framework

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-framework_20260521T170853_result.json`
- **Structured JSON:** [`70858d634ba64e70efa3.json`](../../sessions/70/70858d634ba64e70efa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 12 个文件已写完，所有模块导入和 smoke test 通过。

**文件清单：**

| 文件 | 功能 |
|------|------|
| `src/__init__.py` | 包初始化 |
| `src/config.py` | 4 个 judge 模型配置、数据集、实验参数、panel 组合 |
| `src/utils.py` | logging、seed、JSON 结果保存 |
| `src/judge_service.py` | vLLM 加载 AWQ 模型，pairwise/Likert 评分，batch 推理，JSON 解析 |
| `src/eval_pipeline.py` | 加载 MMLU/ARC，生成好/差 response pair（随机 A/B 位置），多 judge 打分 |
| `src/correlation.py` | agreement rate、MI（Miller-Madow 校正）、Gaussian copula rho、bootstrap CI、cross vs within family 验证 |
| `src/attacks.py` | 3 种攻击（PromptInjection/Sycophancy/ScoreManipulation）× 多 variant = 7 个攻击实例，ASR 计算 |
| `src/panels.py` | homo/hetero panel 生成、majority vote 聚合、panel-level ASR |
| `src/keff.py` | empirical effective rank（eigenspectrum）、formula K_eff、两者对比验证 |
| `src/scaling.py` | Spearman ρ、log-log regression + bootstrap CI、homo vs hetero ASR 对比 |
| `scripts/` | 4 个 step 脚本 + run_all + deploy_judges |
| `requirements.txt` | 依赖列表 |

**SSH 问题**：服务器 `seetacloud-rtx6000` 配置的密钥 `~/.ssh/id_ed25519` 不存在，需要添加密钥或更新 SSH config 后再同步代码到服务器。

---
