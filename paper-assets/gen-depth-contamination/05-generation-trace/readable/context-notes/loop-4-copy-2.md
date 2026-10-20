# agent / loop_4.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`deb04d57026e90ffebdb.json`](../../sessions/de/deb04d57026e90ffebdb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T02:50:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 **1 块 GPU: westc-26893 的 cuda:0**（config gpu_ids=["cuda:0"]），禁止使用其他设备
- 服务器别名已从 `autodl-4090d` 改为 `westc-26893`，所有 SSH/cron 必须用新名，旧名会连接失败
- **exp_015 和 exp_006 目前同时跑在 cuda:0 上**——exp_015 于 05-14T02:23Z 被上一轮提交，但 exp_006 仍在跑（PID 46129）。接手后第一件事 SSH 检查两个进程是否存活、是否 OOM。如果冲突，kill exp_015 等 exp_006 结束再提交
- conda 环境，不是 venv：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 根分区 30GB，大文件全放 `/root/autodl-tmp/`，HF_HOME=/root/autodl-tmp/.hf_cache
- AutoDL 上 pip/HF 操作前必须 `source /etc/network_turbo` + 设 SSL_CERT_FILE + HF_HUB_DISABLE_XET=1

### 2. 🖥️ 基础设施快照
- **服务器**: westc-26893（RTX 4090D × 1）
- **工作目录**: /root/autodl-tmp/gen-depth-contamination
- **Python**: /root/miniconda3/bin/python（conda base, torch=2.10.0+cu128, transformers=4.57.6）
- **模型缓存**: /root/autodl-tmp/.hf_cache（Qwen2.5-1.5B-Instruct, pythia-1.4b, OLMo-1B-hf）
- **数据目录**: data/ (mvp Qwen-rw), data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/（各 5000 samples × 6 depths）
- **活跃进程**:
  - exp_006: PID 46129, tmux=exp_006_graduated_filtering, cuda:0, 50 runs (LoRA CPT + eval), ~46min/run
  - exp_015: PID 56559, tmux=exp_015_neural_probe, cuda:0, frozen LLM → MLP probe
- **Cron**: exp_006 有 cron 监控（reconcile 确认 still running）
- **Worker**: worker_code_exp004_7b_prep_20260514T022738 (running, 准备 Qwen-7B cross-scale 代码)
- **OpenRouter 代理**: http://47.94.22.126/v1（Claude 用裸 ID `claude-opus-4-6`，GPT 用 `openai/gpt-5.5`）

### 3. 📊 当前状态
上一轮完成了 10 个实验的全部分析和 registry 更新，提交了 exp_015 neural probe，论文写了 4/6 章节初稿。

**RUNNING 实验**:
- **exp_006_graduated_filtering**: C3 核心实验，6 filtering strategies × 5 seeds × α sweep = 50 runs LoRA CPT + MMLU/HellaSwag eval。截至 05-13 22:35 UTC 完成 3/50 (4%)，ETA 05-15 11:00 UTC
- **exp_015_neural_probe**: C1' evidence gap 填补，测试 learned representations 是否突破 K*=2。刚提交，可能与 exp_006 显存冲突

**等待中**:
- exp_006 cron 回调（预计 05-15 11:00 UTC）
- exp_015 完成回调
- Worker exp004_7b_prep 完成回调（准备 optional 的 Qwen-7B 跨规模实验代码）
- 无 pending Director 决策

### 4. 📋 待办（条件触发式）
- **接手立即** → SSH 检查 exp_015 (PID 56559) 和 exp_006 (PID 46129) 是否共存正常，若 OOM/死进程则处理冲突
- **exp_006 cron 回调到达** → spawn worker 分析 50 runs 结果（per-strategy MMLU/HellaSwag, α 最优点），更新 registry + report.md，汇报 Director，写 Experiments C3 章节
- **exp_006 结果 graduated > binary 显著** → C3 claim 成立，headline result 填入具体 improvement %
- **exp_006 结果 graduated ≈ binary** → D013 预案启动，C3 降级为 analysis，论文退守 C1'-only story（仍可投 EMNLP）
- **exp_015 完成** → 对比 K*_neural vs K*_15D：若相同 → 加强 information-theoretic impossibility 论证（DPI）；若 K*_neural > K*_15D → 15D projection 是 K*=2 的部分原因，需调整 C1' 措辞
- **exp_004_7b_prep worker 完成** → 代码就绪后等 GPU 空闲（exp_006 + exp_015 结束后），提交 Qwen-7B 跨规模验证（optional, ~3h）
- **全部实验完成** → Discussion + Conclusion 写作 → re-dream 全文 story → Reviewer 审查 → ARR 05-25 提交

### 5. 🎯 战略上下文
- **核心发现**: K*=2 across 8 conditions（4 model-mode + 4 decoding），universality narrative (D016)
- **论文结构**: 2+1 claims — C1'(K* characterization, 4 子组件 a-d) + C3(graduated filtering) + supporting analysis
- **D015 判定**: exp-015 是"论文生死实验"——如果 neural probe 打破 K*=2 universality，需要 framing 调整
- **最容易判断错的事**:
  - K*=2 边缘性极强：Qwen-cont 1v2 CI lower=0.6015（仅 +0.15pp 高于 θ=0.60），Qwen-rw 2v3 CI upper=0.5991（仅 -0.09pp 低于 θ）。**不要用强措辞**，论文用 "established as consistent"，外推用 "suggesting"
  - 不要跨 generation mode 直接对比数值（rewrite 0.6957 vs cont 0.6114 不是 apple-to-apple）
  - "universality" 限定 ≤1.5B scale，审稿人必问规模泛化——这是已知最大 limitation
  - exp_006 是 C3 的单点依赖（D013），失败则整个 claim 需调整
- **决策链关键节点**: D012(2+1 结构) → D016(universality narrative) → D017(措辞两层策略) → D015(exp-015 P0)
- **DDL**: ARR 05-25，剩余 11 天，按倒排 05-17 完成完整初稿，时间充裕


---
