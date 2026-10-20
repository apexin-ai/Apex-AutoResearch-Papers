# agent / loop_4.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`558f4d6a495467bdbbec.json`](../../sessions/55/558f4d6a495467bdbbec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T09:59:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 的 cuda:0-5（共 6 张 4090D），全部分配给本项目，禁止用白名单外 GPU
- GPU 编号从 0 开始：submit_on_allocated 的脚本内 `--gpu 0` = 分配到的第一块卡，框架自动注入 CUDA_VISIBLE_DEVICES
- `server: local` 实验（exp_004, exp_005）禁止用 ssh_read_only 查进程，必须用本地 `ps -p PID`，不注册 cron
- 1.5B/3B SFT 必须 batch_size=1 grad_accum=16（batch_size=2 在 24GB 4090D 上 OOM，已多次验证）
- 0.5B SFT 用 batch_size=4 grad_accum=4
- eval 脚本不接受 `--gpu` 参数（多次因此崩溃），GPU 分配只能通过 CUDA_VISIBLE_DEVICES 环境变量

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，6× RTX 4090D (cuda:0-5)
- 工作目录：/root/contamcal-irt-calibration/exp001
- Python：/root/miniconda3/bin/python（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型缓存：/root/autodl-tmp/.hf_cache/Qwen/（Qwen2.5-0.5B, 1.5B, 3B）
- SFT 数据：/root/autodl-tmp/exp001/sft_data/sft_dosage_{005,025,050,100}.jsonl
- Checkpoints：/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_d{dosage}_s{seed}/lora_adapter
- Eval 输出：/root/autodl-tmp/exp001/eval_results/Qwen2.5-{size}_d{dosage}_s{seed}/
- 日志：~/runs/contamcal-irt-calibration/
- Stan：contam_irt_4pl_simple.stan（CmdStanPy 1.3.0 + CmdStan 2.38.0）
- 本地实验：exp_004 PID 340553（sim sweep），exp_005_v3 PID 339838（noise prop）

### 3. 📊 当前状态
**刚做完**：收到 exp_001_eval_05B_d005 失败回调 + 发现 exp_001_eval_3B_d000_s42 也在异常（miss 4/5）。已派两个诊断 Worker（均 SSH 到 cqa1-21977 查日志），等待回调。

**RUNNING**（registry）：
- exp_001_sft_d100_15B_v2 — GPU 0, PID 251924, 1.5B 100% dosage SFT
- exp_001_sft_d005_15B — GPU 4(?), PID 271916, 1.5B 5% dosage SFT（cron 确认 running）
- exp_001_sft_d100_3B — GPU 3, PID 291373, 3B 100% dosage SFT
- exp_001_eval_05B_d000_s42_v5 — GPU 2, PID 266511, 0.5B baseline eval
- exp_001_eval_05B_d100_v5 — GPU 2, PID 266780, 0.5B d100 eval（注意：与上一个共享 GPU 2）
- exp_001_eval_3B_d000_s42 — GPU 1, PID 249294（进程已消失，即将 auto-fail）
- exp_005_noise_prop_v3 — local, PID 339838, CPU 实验

**空闲 GPU**：cuda:4（1.5B d005 可能在用）, cuda:5

**等待中**：
- Worker worker_diagnose_exp_001_eval_05B_d005_20260514T064705 回调
- Worker worker_diagnose_exp_001_eval_3B_d000_s42_20260514T064711 回调
- exp_001_eval_3B_d000_s42 即将被 cron auto-resolve 为 failed（miss 5/5）

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 更新 registry failure_reason + notes → 判断是否 GPU 冲突导致（两个实验都在 cuda:1）→ 汇报 Director
- 0.5B eval (v5) 完成（GPU 2 释放）→ 立即跑 exp-002 signal pipeline on 0.5B {d000, d005, d100}（优先级高于 d025 SFT）
- 1.5B d100 SFT 完成（GPU 0 释放）→ 排 3B d005 SFT（P1）或 3B d100 SFT（P1，如果 GPU 3 的 3B d100 还没完成则等）
- 3B d100 SFT 完成（GPU 3 释放）→ 启动 3B eval
- exp_005_v3 完成（本地 CPU，ETA 今天 ~14:30 UTC）→ 验证 noise propagation 结果
- exp_004 sim sweep 继续跑（ETA May 16-17），每 AUC 条件完成后增量分析
- exp-002 + exp-006 代码 Worker 应该在跑或需要派——这是 critical path 瓶颈（软件依赖而非算力）

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（距今 11 天）
- **核心方法**：ContamCal = post-hoc 4PL+γ IRT calibration for benchmark contamination
- **Critical Path**：exp-002 signals → exp-003 RRF → exp-006 IRT calibration + 7 baselines = 核心结果。瓶颈是代码（exp-002/006），不是算力
- **已完成 SFT checkpoints**：0.5B (d000×2, d005, d100), 1.5B (d000×2), 3B (d000×2)
- **已完成 Eval**：0.5B-d000-s123, 1.5B-d000-s42 (有指标)
- **高失败率**：30 个 DONE 中 13 个 failed，主要原因是 CUDA_VISIBLE_DEVICES 注入失效 + GPU 冲突 OOM + eval --gpu 参数 bug
- **易踩坑**：(1) cuda:1 反复出问题（两个 eval 撞车），重提交时确保该 GPU 只有一个实验；(2) eval.py 绝对不要传 --gpu；(3) GPU 2 上跑了两个 eval（v5 版本），注意是否也会冲突；(4) d050 已降优先级，不要主动排
- **D013**：正式实验用 Simple IRT model（Stan），弃用 Analytic ME model
- **D016**：Min-K++ reference model 用 0% dosage fine-tuned model，不是裸基座


---
