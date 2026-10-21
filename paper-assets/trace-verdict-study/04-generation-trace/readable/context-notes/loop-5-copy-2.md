# agent / loop_5.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`188a2391830dfbc40b0b.json`](../../sessions/18/188a2391830dfbc40b0b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T12:55:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **只有 westd-11235:cuda:0 和 cuda:1**，project config 明确。不要用其他设备
- **bash -c 内部必须显式 `export CUDA_VISIBLE_DEVICES={N}`**——submit_training_job 注入的 CVD 会被 conda activate 覆盖（vota_seed123 v1 OOM 事故根因）
- **所有训练必须加 `--gradient_checkpointing`**——RTX PRO 6000 98GB 对 7B full fine-tune 仍不够，已两次 OOM
- **HF 下载优先 ModelScope CDN**，HF 必须设 `HF_HUB_DISABLE_XET=1`（xet_get 在 westd-11235 反复 timeout，plan_004 v1 Worker 卡 8 小时教训）
- QUEUED 状态的旧实验（vota_seed42/v2、no_trace_seed42/v2）是 killed 遗留，**不要重试**——它们是早期 debug 版本，v5 版本已完成
- DeepSeek 模型路径有嵌套目录：`/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`（注意下划线转义）

### 2. 🖥️ 基础设施快照
- **服务器**: westd-11235, 2x RTX PRO 6000 Blackwell 94GB, CUDA 12.8
- **工作目录**: `/root/trace-verdict-study`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: Qwen2.5-Coder-7B-Instruct = HF cache; DeepSeek = `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
- **数据**: `/root/autodl-tmp/trace-verdict-study-data/` (train/test jsonl per condition, 4720/1190)
- **Checkpoints**: `/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/`
- **HF cache**: `HF_HOME=/root/autodl-tmp/.hf_cache`
- **W&B**: project=trace-verdict-study
- **活跃进程**: deepseek_vota_seed42 (PID 93484, tmux, cuda:0)
- **活跃 Cron**: deepseek_vota_seed42（监控 PID 93484）
- **活跃 Worker**: worker_code_calibration_fix_20260515T124057（正在 SSH 做 full_trace calibration 推理，25 turns）

### 3. 📊 当前状态
**刚完成**: plan_001-003 全部 ablation + plan_007 calibration analysis + ae_only pairwise bootstrap。Qwen-7B 上 3/3 core claims 全部确认。

**RUNNING (1)**:
- `deepseek_vota_seed42` — DeepSeek-Coder-6.7B VOTA 条件 (plan_004), cuda:0, PID 93484。这是跨模型泛化的关键实验。

**QUEUED (1, 待提交)**:
- `vota_seed123` — seed robustness (plan_008), cuda:1。v1 因 CVD 覆盖落到 cuda:0 OOM，v2 spec 已修正（显式 export CVD=1），等 cuda:1 空闲后提交。

**PREPARING (4, 未提交)**:
- `vota_seed456` — plan_008 第三个 seed
- `deepseek_no_trace_seed42` / `deepseek_full_trace_seed42` / `deepseek_exception_only_seed42` — plan_004 其余 3 条件，等 deepseek_vota 完成后串行跑 cuda:0

**等待中**:
- calibration fix Worker 正在做 full_trace 推理（plan_007 补充），完成后应有更新
- deepseek_vota_seed42 cron 回调 → 触发 plan_004 下一条件
- cuda:1 当前空闲（vota_seed123 QUEUED 但未 submit）——**应立即提交**

### 4. 📋 待办（条件触发式）
- **cuda:1 空闲（现在就是）** → 立即 submit vota_seed123 v2（spec 已在 registry，用 submit_on_allocated）；完成后提交 vota_seed456
- **deepseek_vota_seed42 cron 回调（完成）** → 分析结果 → 串行提交 deepseek_no_trace → deepseek_full_trace → deepseek_exception_only（全部 cuda:0）
- **calibration fix Worker 完成** → 读取产出，更新 calibration_analysis_seed42 registry 补充 full_trace reliability diagram
- **plan_004 全部 4 条件 DONE** → 与 Qwen 结果对比，更新 paper_framing.md，向 Director 汇报跨模型泛化结论 → 启动 Paper Agent
- **plan_008 全部 3 seeds DONE** → 计算 seed 间 variance，McNemar test，确认 <2pp 差异
- **DeepSeek 结果 + seed robustness 均确认** → 论文写作正式启动（5/16-17 按 ROADMAP 冲刺计划）
- **plan_005 (DebugBench 第二任务)** → 时间允许 5/21-23 加入，不阻塞主线

### 5. 🎯 战略上下文
**核心发现**: Verdict prediction 的决定性信号是 diagnostic-moment information（assertion 断言点处的 exception + actual/expected），而非 full execution trace。ae_only (99.92%) ≈ exception_only (99.83%) >>> loop_only (85.6%) > full_trace (81.8%) > no_trace (75.1%)。

**决策链**:
- D004-D006: full_trace v2 28.4% collapse 是 chat template truncation bug，非 genuine negative
- D008: actual/expected 冗余确认（VOTA w/o ae 99.4%），Claim 1 走 positive framing
- D009: gradient dilution real but minor（4.5pp），info overload 是主因（13pp）
- D010-D013: exception dominance 确立 + ae_only Tier 1 确认

**易错点**:
1. **不要把 QUEUED 的 killed 旧实验（vota_seed42/v2、no_trace_seed42/v2）当作待提交**——它们是早期 debug 版本遗留，conclusion=killed
2. **DeepSeek 4 条件必须串行跑 cuda:0**（只有 1 张空闲卡），不要试图并行
3. **calibration analysis (plan_007) 在 experiment_plan.yaml 里 registry_id=null**（未关联），实际结果在 calibration_analysis_seed42 registry entry 中
4. **ae_only 88% fallback locals 不是 data leakage**（D013 已裁定），不要重新质疑
5. **EMNLP ARR DDL = May 25**，今天 5/15，只剩 10 天。DeepSeek 跨模型结果是论文门票——如果 DeepSeek 上 VOTA 不显著优于 no_trace，需要立即向 Director 报告走 Framing 调整


---
