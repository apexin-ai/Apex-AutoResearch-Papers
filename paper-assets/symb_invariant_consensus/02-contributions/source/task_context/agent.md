---
loop: 10
reason: max_wall_time
updated: '2026-05-21T17:56:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd-16639 GPU 白名单**: cuda:0,1,2,3 全部属于本项目。cuda:0+1 跑 cross-model SICA (vLLM Mistral:8000 + Qwen3-14B:8001)，cuda:2 跑 70B SICA (vLLM:8002)，cuda:3 刚部署 Mistral:8004 做 gpt-5.5 extraction
- **westd-25068**: 4×H800 全属于本项目。gemini-2.5-pro 在跑（无 GPU 占用，API-only）。70B AWQ 下载中，完成后部署 tp=4 port 8002
- **Worker 连错服务器是高频 bug**: 已发生 3 次（Worker 默认连 westd-25068 而非 westd-16639）。spawn_worker 时必须在 prompt 中 ⚠️ 加粗强调目标服务器
- **R1-Distill 论文定位 (D131)**: 仅用于 (1) Diagnostic C₀ 验证 + (2) cross-model extraction case study。**不作为 reasoning model SCB 证据**
- **Alphabetical tiebreaking**: 所有 SC/combo 必须用 `sorted(tied_candidates)[0]`，全项目统一标准
- **EMNLP 2026 ARR 截止 May 25**

### 2. 🖥️ 基础设施快照
**westd-16639** (4×H800 98GB):
- 工作目录: `/root/symb_invariant_consensus/`
- Python: `/root/miniconda3/bin/python` (conda base)
- vLLM 0.21.0, `VLLM_USE_FLASHINFER_SAMPLER=0` (Blackwell sm100)
- 模型: Mistral-7B `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`, Qwen-72B-AWQ `/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ`, Qwen3-14B, R1-Distill-8B
- 活跃 vLLM: Mistral:8000 (cuda:0), Qwen3-14B:8001 (cuda:1), 70B-AWQ:8002 (cuda:2), Mistral:8004 (cuda:3, 刚部署)
- 活跃进程: cross-model SICA PID 414515 (cuda:0+1), 70B SICA PID 436084 (cuda:2, ~12/204 极慢), gpt-5.5 PID 444813, o3 PID 444814
- 结果目录: `results/exp_d135_frontier_scb/` (gpt-4.1/gpt-5.5/o3/gpt-4o), `results/exp_r1_distill_8b_sica/`

**westd-25068** (4×H800 98GB):
- 工作目录: `/root/symb_invariant_consensus/`
- Python: `/root/miniconda3/bin/python` (conda base)
- 磁盘: `/root/autodl-tmp` 122G/250G (49%)
- 模型: Mistral-7B, R1-Distill-Llama-8B（Qwen-72B BF16 已删，AWQ 下载中）
- 活跃: gemini-2.5-pro PID 19972 (~10/204, ETA ~8h)

**Artifacts 目录**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/`

### 3. 📊 当前状态

**刚完成**:
- gpt-4.1 全管线 ✅: SC=82.84%, SICA=81.37%, Δ=-1.47pp, BR=2.70×, Process-κ=0.792, Answer-κ=0.862
- gpt-4o BR ✅: SC=73.91%, SICA=72.05%, BR=2.94×
- R1-Distill cross-model 204 题 ✅: SC=74.51%, SICA=76.47%, Δ=+1.96pp, BR=2.85×
- Qwen14B canonical audit ✅: SC=74.00% (exp032), Oracle=91.17%, CIL ρ=0.881
- R11 reviewer tasks ✅: 3-verifier BH (10/15 sig), SBERT Process-κ (0.907), Relative TOST (8/2/6)

**Running Workers**:
- `worker_experiment_gpt55-extraction-pipeline`: Kill R1 vLLM → 部署 Mistral cuda:3:8004 → gpt-5.5 extraction+SICA+BR
- `worker_analysis_o3-data-cleaning`: o3 数据清洗，计算 SC@K_effective
- `worker_experiment_70b-awq-westd25068-deploy`: westd-25068 下载 AWQ → 部署 tp=4 → pipeline from folio_12

**Registry 实验状态**:
- exp-d135-frontier-scb: PREPARING (gpt-4.1 done, gpt-5.5 extraction中, o3 cleaning中, gemini running)
- exp-d126-r1-distill-sica: conclusion=success (204题完成)
- exp-d126-crossmodel-sica: PREPARING (PID 414515, ~100/204)
- exp-d126-70b-sica: PREPARING (westd-16639 PID 436084 ~12/204; westd-25068 AWQ下载中)
- exp-d134-e6-closed-model: conclusion=success (gpt-4o 161/204)
- exp-d134-cil/process-br/baf-decoupled: 全完成

### 4. 📋 待办（条件触发式）
- gpt-5.5 extraction Worker 完成 → 更新 registry metrics，汇报 Director 完整指标表（SC/SICA/BR/κ）
- o3 cleaning Worker 完成 → 汇报 SC@K_effective + 有效 trace 分布
- 70B AWQ Worker 完成 → 确认 vLLM 部署 + pipeline 启动，注册 cron 监控
- 70B westd-25068 pipeline 跑到 30-50 题 → 可以开始计算初步 BR（Director 说只需 30-50 题做 BR 分析）
- cross-model SICA (PID 414515) 完成 → spawn Worker 计算 metrics
- gemini 完成 (~10h) → extraction + SICA + BR
- gpt-5.5/o3 完成后 → 更新论文 main table：所有 frontier 模型 SCB 数据

### 5. 🎯 战略上下文
**项目核心**: 论证 Symbolic Confirmation Bias (SCB) 是 LLM self-verification 的结构性问题。BR≈2.5-3× 跨 7 个模型 family 一致（Mistral-7B, Qwen-14B, Qwen-72B, LLaMA-8B, R1-Distill, gpt-4o, gpt-4.1）。

**决策链关键节点**:
- D131: R1-Distill 仅做 diagnostic，不做 reasoning model 证据
- D134: CIL 统一 metric，Spearman ρ=0.881 (p=0.004)
- D135: Frontier 闭源模型用 OpenRouter API，cross-model extraction 用 Mistral-7B

**易错点**:
1. Worker 默认连 westd-25068——每次 spawn 必须明确指定服务器
2. exp-d135-frontier-scb 的 cron 会反复触发（因为 PID 监控的是 extraction 进程而非整个实验）。如果收到 cron 告警但实验实际在跑，直接 poll_cron 让它自然清理
3. Registry 中 exp-d126-r1-distill-sica 和 exp-d135-frontier-scb 被 cron 自动标为 "failed"，但实际是 success——conclusion 字段已手动修正，但 failure_reason 字段残留
4. 两台服务器的 70B 模型不同（westd-16639=AWQ, westd-25068=AWQ下载中），论文统一写 "Qwen2.5-72B"
5. gpt-4.1 的 SICA 是 cross-model (Mistral提取)，不是 self-extraction——论文需注明
