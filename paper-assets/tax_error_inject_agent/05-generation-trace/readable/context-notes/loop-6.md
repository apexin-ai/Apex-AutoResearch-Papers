# agent / loop_6.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`42b8af8eacdaeb6f09b4.json`](../../sessions/42/42b8af8eacdaeb6f09b4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-16T10:21:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090:cuda:0/1/2/3，不可用其他卡
- ms-swift 训练命令必须带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 前缀
- TaxEI-RP eval 必须用 recovery-paired checkpoint，不要混淆 v4-taxei (full injection) 和 v4-taxei-rp (recovery-paired) 的 checkpoint
- 所有 RP seed 共用同一数据集 `sft_taxei_rp.jsonl`（14,437 samples），不要和 dose-response 的 fixed-size 4,358 混淆

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 /root/autodl-tmp/tax_error_inject_agent/
- Python：/root/miniconda3/bin/python（conda base）
- 模型：/root/autodl-tmp/models/Qwen/Qwen3-8B
- LLaMA：/root/autodl-tmp/models/... （已下载 LLaMA-3.1-8B-Instruct, 15GB verified）
- RP 训练数据：/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl
- Eval 脚本：eval/injected_eval.py + scripts/run_injected_eval.sh（已 dryrun PASS）
- HF_HOME=/root/autodl-tmp/.hf_cache
- 活跃进程：无（全部 GPU 空闲）
- Worker running：worker_analysis_v4-taxei-rp-s0_20260516T061331（正在分析 s0 日志）

### 3. 📊 当前状态
刚收到 v4-taxei-rp-s0 训练完成 cron 回调，已派 Worker SSH 提取指标+checkpoint 路径。

Registry 关键状态：
- v4-taxei-rp-s0: ANALYZING（Worker 正在处理）
- v4-taxei-rp-s1/s42/s123: DONE(success)，train_loss≈0.385，duration≈226min
- v4-taxei-rp-s7: 未注册（ROADMAP batch 2b，~3h 训练）
- 3 个 QUEUED 实验（inject25 s0/s123, random-inject25 s0）有 conclusion=success 但 status 未推进，可能是 stale
- 4 张 GPU 全空闲 — 资源饱和违规

等待中：Worker 回调（分析 s0 指标+找 checkpoint 路径）

### 4. 📋 待办
- Worker 回调确认 s0 metrics + checkpoint → 立即注册 4 个 TaxEI-RP eval 实验（s0/s1/s42/s123），4 GPU 并行提交，~30min
- RP eval 需要确认 checkpoint 路径格式（Worker 正在查找，其他 3 seed 的 checkpoint_path 也是 None 需补）
- RP eval ×4 提交后 → 同时在 GPU 3 启动 v4-taxei-rp-s7 训练（seed=7，同样 sft_taxei_rp.jsonl）
- RP eval 全部完成 → 汇总 5 条件 recovery rate 对比（Vanilla/TaxEI/Random/RP 各 seed），更新 paper_framing.md Claim 7
- LLaMA 跨模型验证（batch 2a）：3 GPU 跑 Vanilla/TaxEI/Random s42，依赖 RP eval 完成后的 GPU 释放
- Director 未回复确认执行链 → 按 ROADMAP 默认顺序推进

### 5. 🎯 战略上下文
- 这是 negative result paper（EMNLP 2026 Findings 8p），核心结论：TaxEI 在 embodied planning 无效
- D039: Recovery-Paired SFT 是 Claim 7 的支撑——假设用 recovery 配对数据训练能否教会模型真正的 error recovery（而非 passive resilience）
- D041 关键发现：recovery eval ≈ normal eval（模型是 resilient 而非 recovering），RP 训练需要打破这个 null
- 易错点：不要把 "recovery eval"（用 injected errors 测试已训练模型）和 "recovery-paired training"（用配对数据训练）搞混——前者是评估方式，后者是训练方式
- 当前 RP 4 seed 训练全部一致（loss≈0.385），如果 eval 也显示 RP ≈ Vanilla recovery rate，则 Claim 7 转 negative，需要新 Framing 提案
- 3 个 stale QUEUED 实验不紧急，是 dose-response 扩展（已有 5-seed 完整数据），别浪费 GPU 在上面


---
