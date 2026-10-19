# agent / loop_14.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`aa873dd071d61d0ea78f.json`](../../sessions/aa/aa873dd071d61d0ea78f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-21T17:23:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41718 cuda:0/1, westd-34887 cuda:0/1（共 4 卡，全部已分配给本项目）
- 启动训练前必须 `pgrep -af 'train.*seed'` 检查重复进程（已因重复进程被 Director 警告 3 次，M046）
- AutoDL 实例间 SCP 不可靠（会挂起 16min+），eval 必须安排在 checkpoint 所在服务器
- 训练完成后 eval 已预授权：s42→41718:cuda:1, s123→34887:cuda:1，不等 Director 指令直接启动
- submit_training_job 命令必须用 `bash -c "..."` 包裹（含 source/conda activate 等 bash builtin）
- GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）

### 2. 🖥️ 基础设施快照
- **westd-41718**: connect.westd.seetacloud.com:41718, root, 工作目录 /root/distill_sparse_swiglu
- **westd-34887**: connect.westd.seetacloud.com:34887, root, 工作目录 /root/distill_sparse_swiglu
- Python: /root/miniconda3/bin/python（conda base env，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型: /root/autodl-tmp/models/llama-3.1-8b（两台服务器都有）
- HF cache: /root/autodl-tmp/.hf_cache（需设 HF_HOME）
- lm-eval: v0.4.12（两台服务器都已验证）
- 活跃进程:
  - perlayer_kl_30_s42_v6: PID 328295, westd-41718:cuda:0, cron 已注册(300s)
  - perlayer_kl_30_s123_v4: PID 284767, westd-34887:cuda:0, cron 已注册(300s)
- Eval 脚本: src/benchmark_eval.py（两台都有，17817 bytes）
- 训练脚本: src/train_perlayer_kl.py（--save_every 2000 产出中间 checkpoint ~455MB）

### 3. 📊 当前状态
刚完成：
- perlayer_kl_s456_boolq_v2 → DONE(success), boolq_acc=51.25%（Director 标记为"重要发现"）
- perlayer_kl_s456_ppl_repro → DONE(success), PPL=9.0282（确认确定性）
- diag_eval_env_34887 → DONE(success), westd-34887 eval 环境就绪
- 已向 Director 汇报上述全部结果 + 训练进度

正在跑：
- perlayer_kl_30_s42_v6: Step 2900/10000, avg_kl=0.0134, westd-41718:cuda:0, ETA ~19:00 UTC
- perlayer_kl_30_s123_v4: Step 2900/10000, avg_kl=0.0137, westd-34887:cuda:0, ETA ~19:00 UTC

空闲 GPU：westd-41718:cuda:1, westd-34887:cuda:1（预留给 eval）

等待中：两个训练的 cron 完成回调。Worker API rate-limited until May 22 18:00 UTC。

### 4. 📋 待办（条件触发式）
- perlayer_kl_30_s42_v6 cron 回调(进程退出) → 立即在 westd-41718:cuda:1 启动: (1) PPL eval (wikitext2, seq_len 2048), (2) 7-task downstream (arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa, boolq)。Checkpoint 在 /root/distill_sparse_swiglu/checkpoints/perlayer_kl_30_s42/predictor_perlayer_kl.pt
- perlayer_kl_30_s123_v4 cron 回调(进程退出) → 立即在 westd-34887:cuda:1 启动同样的 PPL + 7-task eval。Checkpoint 在 /root/distill_sparse_swiglu/checkpoints/perlayer_kl_30_s123/predictor_perlayer_kl.pt
- 两组 eval 全部完成 → 汇总 3 seeds (s42/s123/s456) 的 PPL + 7-task metrics → 向 Director 汇报完整 coupling hierarchy 对比表
- 如果训练失败(exit code !=0) → 检查 step 2000 checkpoint 是否存在 → 如果有则用 --resume 从 checkpoint 恢复

### 5. 🎯 战略上下文
- 核心实验：Coupling Hierarchy（C1 claim）。KL (8.81) ≈ JSD (8.90) > Per-layer KL (s456: 9.03) > RevKL (9.26) >> TEAL (10.82) >> BCE (15.09) >> MSE (18.52)
- Per-layer KL 的 3-seed 数据是论文 Table 4 的关键缺口：s456 完成（PPL=9.0282, BoolQ=51.25%），s42/s123 训练中
- Per-layer KL s456 BoolQ=51.25% 显著低于 RevKL s42 BoolQ=65.29%——Director 标记为重要发现，说明 per-layer 独立训练在 downstream 上劣化更严重
- DDL: EMNLP 2026 ARR 2026-05-25（4 天后）
- 易错点：(1) registry filter by exp_id 不工作，需用 grep 直接搜 registry.yaml；(2) 状态转换不能跳步，必须走完 PREPARING→PENDING→QUEUED→ALLOCATED→RUNNING→DONE；(3) 转换过程中 hypothesis/conclusion/metrics 字段会被清空，转完后需重新设置
- perlayer_kl_s456_boolq (v1) 已标记 failed（SCP 挂起），v2 是替代


---
