# agent / loop_3.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`c3ce7134ecce293055e6.json`](../../sessions/c3/c3ce7134ecce293055e6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T06:12:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-5 on cqa1-21977，全部分配给本项目，禁止用白名单外 GPU
- 1.5B/3B SFT 必须 batch_size=1 grad_accum=16（batch_size=2 在 4090D 24GB OOM，已验证）
- 0.5B SFT 用 batch_size=4 grad_accum=4
- --gpu 参数必须匹配物理 GPU 编号，不能用 --gpu 0 代替（v1/v2 OOM 教训）
- Dosage >0% 数据已于 05-14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K），使用 ALL paraphrases（含 QC fail），即 "noisy contamination" condition（D010）
- IRT 推断必须用 CmdStanPy Bayesian MCMC，不能用 PyTorch MLE（D011）
- eval pipeline 有已知 bug：`load_paraphrased_benchmark` 中 `'list' object has no attribute 'get'`，paraphrased eval 受影响

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，6× RTX 4090D
- 工作目录：/root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（conda base env，不用 venv）
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}
- SFT 数据：/root/autodl-tmp/exp001/sft_data/sft_dosage_{005,025,050,100}.jsonl
- Checkpoints：/root/autodl-tmp/exp001/checkpoints/{Model}_d{dosage}_s{seed}/lora_adapter
- Eval 输出：/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage}_s{seed}/
- Stan 模型：contam_irt_4pl_simple.stan（已验证可用）
- 活跃进程（reconcile 05-14 02:23 确认）：
  - exp_001_sft_d100_15B_v2 — cuda:0, PID 251924
  - exp_001_eval_05B_d005 — cuda:1, PID 255322
  - exp_001_eval_3B_d000_s42 — cuda:1, PID 249294（⚠️ 与 d005 共享 cuda:1）
  - exp_001_eval_3B_d000_s123 — cuda:3, PID 242581
  - exp_001_eval_15B_d000_s42_v2 — cuda:4, PID 243290
  - exp_001_eval_15B_d000_s123 — cuda:5, PID 250600
  - exp_004_sim_sweep — CPU only, PID 219346

### 3. 📊 当前状态
收到 exp_001_eval_05B_d100 失败回调（SIGTERM exit 143，运行 ~52min 后被外部 kill），已派诊断 Worker `worker_diagnose_exp_001_eval_05B_d100_20260514T022332` SSH 查日志/内核日志/部分结果。Worker 尚未返回。

cuda:2 因该实验失败而空闲，待诊断结果决定是重跑 eval 还是启动 Phase 3 SFT。

已向 Director 汇报失败情况和资源状态。

**RUNNING (7)**：上述 6 个 GPU 实验 + 1 个 CPU sim sweep
**PREPARING (2 个有效)**：exp_001_sft_d005_15B（1.5B d005 SFT，Phase 3 优先级 #1）、exp_001_eval_3B_d000_s42_v3（3B baseline eval v3）

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读结果：若有部分 eval 结果可用则记录到 registry，确认 root cause 后在 cuda:2 重跑 exp_001_eval_05B_d100；若 eval 代码有 bug 需先修复
- cuda:2 长期空闲（诊断 Worker 确认无法快速重跑）→ 按 Phase 3 优先级启动 exp_001_sft_d005_15B（1.5B d005 SFT）
- exp_001_sft_d100_15B_v2 完成（cuda:0 释放）→ 立即启动 1.5B d100 eval
- 各 baseline eval 完成 → 记录 metrics 到 registry，与 exp_001_eval_05B_d000_s123 对齐格式
- 全部 0% baseline eval 完成 → Phase 3 contaminated SFT 全面铺开（12 runs，调度预案见 ROADMAP）
- exp_004_sim_sweep 完成 → 验证 identifiability 阈值 vs Fisher 理论

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 ARR May 25（距今 11 天），核心方向是 ContamCal（post-hoc 4PL IRT calibration for benchmark contamination）
- Critical path：0% baseline eval 完成 → Phase 3 contaminated SFT → Phase 4 eval → exp-002/003/006 主实验链
- Phase 3 调度：先跑极值 d005/d100，再填 d025/d050（Director 批准免审批）
- exp_005 γ bias 诊断结论：simple model 和 analytic ME model 都有 ~58% γ bias（σ_e=0.1 时），根因不在 ME 处理方式，D013 决策弃用 analytic ME model
- 易错点：cuda:1 当前同时跑两个 eval，可能因显存争抢导致其中一个 SIGTERM/OOM——这可能就是 d100 被杀的原因（d100 原先在 cuda:2 但需要确认是否有进程迁移/冲突）
- 易错点：exp_001_eval_05B_d000_s42 也失败了（FileNotFoundError in evaluate.py line 558），eval pipeline 可能有系统性问题需要修
- Table 2 风险：Related Work 表中 ContamCal "RL-robust partial✓" claim 唯一证据来源是 exp-008（未启动），若结果不支持需删除


---
