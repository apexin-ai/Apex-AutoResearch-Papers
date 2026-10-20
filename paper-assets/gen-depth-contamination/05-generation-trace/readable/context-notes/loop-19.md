# agent / loop_19.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`c558792762713f92b62a.json`](../../sessions/c5/c558792762713f92b62a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-22T00:33:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-22115 上 cuda:0/1/2/3，westd-42896 上 cuda:0/1。禁止使用白名单外 GPU
- Pythia-6.9B 实验**必须**用 Qwen-1.5B scorer（`--scorer_path`），不能用模型自身打分（D095 决策，v1 因此被紧急叫停）
- `submit_training_job` 后**不要**再 `update_registry(field="spec")` 覆盖，会竞态重置状态为 PREPARING
- Registry 状态不可回退（RUNNING→ALLOCATED 不行），需重跑则标 DONE(failed) 后创建 v2/v3
- Benchmark 指标标准：PIQA=acc_norm, ARC-C=acc_norm, HellaSwag=acc_norm, WinoGrande=acc, TruthfulQA=mc2, GSM8K=exact_match(strict-match)

### 2. 🖥️ 基础设施快照
- **cqa1-22115**: 4×RTX4090D，工作目录 `/root/autodl-tmp/gen-depth-contamination`，conda 环境（`/root/miniconda3/bin/python`，不用 venv）
- **westd-42896**: 2×Blackwell 98GB，空闲，无活跃进程，首次使用需完整 env setup
- 模型路径（cqa1-22115）：
  - Qwen2.5-1.5B scorer: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`
  - Pythia-6.9B: `/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23`
- 活跃进程：`exp_pythia69b_c4_depth_chain_v3`，PID 395575，tmux session，cqa1-22115 cuda:0
- Cron：刚在本轮注册了 v3 的 cron 监控（PID 395575, interval 120s）

### 3. 📊 当前状态
- **刚做完**：Loop #19 session-start 初始化——发现 v3 cron 缺失并重新注册，派 Worker 检查 v3 进程状态，向 Director 汇报了资源状态
- **正在跑**：`exp_pythia69b_c4_depth_chain_v3`（Pythia-6.9B C4 depth chain，Qwen-1.5B scorer），已跑 ~20h（预估 18-21h），可能即将完成或已完成
- **PREPARING**：37 个实验（gsm8k patch / seed2 / deberta filter / sweep 系列）——审稿期间候选预注册，等 Director 决定
- **Worker**：`worker_check_pythia_v3_status_20260521T055147` 正在检查 v3 进程状态，**尚未回调**
- **等待**：(1) Worker 回调确认 v3 状态 (2) v3 cron 完成回调 (3) Round 23 审稿报告

### 4. 📋 待办（条件触发式）
- Worker check 回调到达 → 如进程已结束但 cron 未触发，手动派 Worker 分析结果
- v3 cron 回调 conclusion=success → spawn Worker 分析：如 K*=2 则更新主表 Table 1 加 Pythia-6.9B 行、claim C1 升为 "8/10 configs"；如 K*≠2 则按 negative 流程汇报 Director
- v3 cron 回调 conclusion=failed → 这是第三次失败，需认真诊断根因（v1 缺 scorer、v2 未知原因），不要简单重试
- Round 23 审稿报告返回 → 按 action items 分配 Worker，优先 CRITICAL/MAJOR 类反馈
- Director 批准候选实验 → 可启动 Cross-domain DeBERTa arXiv / WinoGrande 负面分析 / SHAP feature importance

### 5. 🎯 战略上下文
- **核心结论**：K* discrimination boundary 在 prompt-chain recursive generation 下表现为 domain ordering invariance（arXiv>C4=Code>Wiki），K*=2 是 web text 在 θ=0.60 下的具体实例。论文 88 success / 11 negative / 13 failed
- **决策链关键**：D095（Pythia 必须用外部 scorer）、D094（Gemma LOFO 保守 θ）、D093（Round 22→23 冲刺三实验）、D092（revert D091 保留 OLMo C4 K*=2）
- **易判断错的事**：(1) Pythia v3 已 fail 两次，如再 fail 必须深度诊断不能盲目重试 (2) 37 个 PREPARING 不是"应该立即跑"的，是审稿候选，需 Director 决定 (3) westd-42896 是 Blackwell GPU，环境与 cqa1 不同，首次使用需完整 env setup (4) Worker check 可能回调说进程已结束——此时 cron 刚注册可能来不及捕获，需手动触发分析流程
- **论文状态**：8 页主文 + 29 页总计，编译通过，0 critical warnings。Round 23 已提交审稿，目标 3.5→4.0，EMNLP 2026 ARR May DDL 5/25


---
