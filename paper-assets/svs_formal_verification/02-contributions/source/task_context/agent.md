---
loop: 1
reason: max_wall_time
updated: '2026-05-14T10:32:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- autodl-5090 的 GPU 白名单需通过 `get_project_status` 确认，上次确认为 cuda:0-3
- mvp_003 用 vLLM TP=2 占 2 卡，剩余 2 卡空闲但未分配其他实验
- DeepSeek API key 通过 TUM 管理，不要硬编码；formalization 用远程 V3.2 API，chain sampling 用本地 vLLM DeepSeek-R1
- `run_mvp.py` 本地有两处改动（load_problems 多数据集 + max_workers=4）**未部署到服务器**，mvp_003 跑的是旧版。下次部署记得 scp 最新版

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/svs_formal_verification/`
- Python：conda 环境（aml-train 镜像），`/root/miniconda3/bin/python`
- 代码本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/svs_formal_verification/artifacts/svs_pipeline/`
- 模型：Qwen2.5-14B-Instruct 在 `/root/autodl-tmp/models/Qwen/Qwen2.5-14B-Instruct/`（28GB, 8/8 safetensors, 下载完成）
- vLLM 本地推理：DeepSeek-R1 用于 chain sampling
- 活跃进程：mvp_003 PID 37622（`python -m svs_pipeline.run_mvp`），Z3 sandbox worker PID 37936
- Cron：mvp_003 监控已注册（180s 间隔）

### 3. 📊 当前状态
刚完成 Director 指派的等待窗口三项检查并汇报：
1. mvp_003 正常运行，6/50 problems 完成，Z3 sandbox 无 crash 重启（隔离方案有效）
2. Qwen2.5-14B-Instruct 下载完成
3. Baseline 框架（SC / Binary Filter+SC / Self-Certainty）全部验证通过

Registry：
- mvp_003: RUNNING（Z3 subprocess 隔离 + 量词修复 + PCV，50 problems ProofWriter depth-5）
- mvp_002: DONE(failed) — Z3 SIGABRT 崩溃
- mvp_001: DONE(killed) — 量词错误+pseudo-constant

等待中：mvp_003 cron 回调（预估剩余 ~7hr）。无待处理 Worker。

### 4. 📋 待办
- mvp_003 cron 回调到达 → spawn worker 分析结果：IC 对正确/错误链的区分度（核心 hypothesis 验证）
- IC 区分显著（正确链 IC > 错误链 IC，p<0.05）→ success，推进 FOLIO 数据集 + Qwen2.5 cross-model 验证
- IC 无区分 → negative，按 red-section 产 Framing 调整提案，禁止默默跑下一个
- mvp_003 进程异常退出 → 读日志诊断，sandbox crash 则检查 z3_sandbox.py；API 超时则检查 V3.2 连通性
- 正式评估时 Binary Filter baseline 需处理 dict→SVSResult/ChainVerification 反序列化

### 5. 🎯 战略上下文
- 核心 hypothesis：正确推理链的 Z3 internal consistency (IC) 显著高于错误链。mvp_003 是首次在修复后的完整验证
- 本 session 修复了三个 P0 问题：量词 ForAll/Exists 混淆（49%→93%正确率）、pseudo-constant 泄漏、Z3 C-level crash。前两次 MVP 都因这些 bug 无法产出有效结果
- IC 计算方式：MCS size / total_claims。MCS 用 greedy 算法在 Z3 sandbox subprocess 内执行
- PCV (Premise-Conditioned Verification)：premises 作为固定 Z3 约束加入 IC 检查，区别于 mvp_001 的 raw IC
- CCLC (Cross-Chain Logical Coherence)：跨链一致性，在 cross_chain.py 中实现，依赖 Z3Checker 间接使用 sandbox
- 易错点：不要直接 `import z3` 在主进程做 eval——Z3 C++ 层 abort() 会杀死整个 Python 进程，必须走 z3_sandbox.py 的 subprocess 隔离
- 本地 run_mvp.py 的 load_problems + max_workers=4 改动还没部署，下次实验前必须 scp
