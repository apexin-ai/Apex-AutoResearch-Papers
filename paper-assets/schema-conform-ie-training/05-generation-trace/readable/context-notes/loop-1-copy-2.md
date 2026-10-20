# agent / loop_1.md

**schema conform ie training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`4c8b8c0e0484cfcf53b5.json`](../../sessions/4c/4c8b8c0e0484cfcf53b5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T19:43:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：westb-23072 (即 seetacloud-westb-2xpro6000) cuda:0 + cuda:1，不得使用其他卡
- A 训练完成后 merge LoRA 前不能删 /root/autodl-tmp/output/formal_A 下的 adapter 文件
- B 评估结果在 /root/autodl-tmp/output/eval_B/，C 推理结果在 /root/autodl-tmp/output/base_zero_shot/——路径不同于 run_eval.sh 中定义的路径，读结果必须用实际路径
- TRL v0.18 API: reward_fn completions 是 list[list[dict]] 不是 list[str]，改 reward 代码时注意
- Qwen3 thinking mode 已在 tokenizer chat_template 中禁用，不要恢复

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westb-2xpro6000 (SSH alias westb-23072)，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/autodl-tmp/schema-conform-ie-training/code
- Python：/root/miniconda3/bin/python，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：/root/autodl-tmp/models/Qwen/Qwen3.5-9B
- 数据：/root/autodl-tmp/data/ (scierc/, crossner/)
- HF_HOME=/root/autodl-tmp/.hf_cache
- 输出：/root/autodl-tmp/output/{formal_A, formal_B, eval_A, eval_B, base_zero_shot}
- 日志：/root/autodl-tmp/logs/{train_A.log, eval_B.log}, /tmp/base_zero_shot.log
- 活跃进程：
  - exp_001 A 训练：PID 25842, cuda:0, 381/500 steps (~2h 剩余)
  - B 组评估：PID 44652, cuda:1, scierc_test 123/551 (~5h total)
  - C 组推理：PID 29235, cuda:0 (shared), crossner_science 125/543 (~2h 剩余)
- Cron：系统 cron 监控 exp_001 (crons.yaml)；session cron 8d74f180 (10min 循环检查三进程，session-only 已失效)

### 3. 📊 当前状态
Session 恢复后完成了：registry 读取、cron reconcile、三进程日志 tail、Director 汇报。
- exp_001_grpo_baseline: RUNNING, 381/500, ~2h
- exp_002_grpo_conformance: ANALYZING (training done, B eval PID 44652 running but未注册为独立实验)
- exp_003_base_zero_shot: RUNNING, crossner_science 125/543

C 组部分结果已获取：scierc_test 全 0，crossner_politics valid_json_rate=0.39 其余全 0。符合预期（base model 不能产 valid JSON）。

等待中：三个进程各自完成的回调。Worker 池 = 0（全部 GPU 阻塞）。

### 4. 📋 待办
- A 训练完成 (PID 25842 退出) → spawn Worker: merge LoRA (`/root/autodl-tmp/output/formal_A` → `formal_A/merged`) → 启动 A eval on cuda:0 (`CUDA_VISIBLE_DEVICES=0 python -m src.evaluate --model_path /root/autodl-tmp/output/formal_A/merged --eval_datasets scierc_test crossner_politics crossner_science --data_dir /root/autodl-tmp/data --output_dir /root/autodl-tmp/output/eval_A --model_label group_A_baseline --max_new_tokens 512`) → update_registry exp_001 status=ANALYZING conclusion=success
- C 推理完成 (PID 29235 退出) → 读 `/root/autodl-tmp/output/base_zero_shot/base_model_results.json` → update_registry exp_003 → 汇报 Director
- B 评估完成 (PID 44652 退出) → 读 `/root/autodl-tmp/output/eval_B/eval_results.json` → 汇报 Director
- 三组结果全部就绪 → 生成 MVP 对比表 → 判断 pass criteria: B ≥ A + 2pp on CrossNER, SciERC drop ≤ 3pp, A/B > C

### 5. 🎯 战略上下文
- 项目核心：验证 schema-conformance rewards (5 component + GDPO) 在 zero-shot IE transfer 的有效性
- MVP pass criteria：B 组在 CrossNER zero-shot 上超 A 组 ≥ 2pp，SciERC in-domain 掉分 ≤ 3pp
- C 组已确认是极低 baseline（base model 几乎无法产出 valid JSON），A/B 大概率高于 C
- B 训练已 500/500 完成并 merge 成功，评估在跑；A 训练是最后一个瓶颈
- 易错点：B 评估进程 (PID 44652) 不在 registry 中作为独立实验，也没有系统 cron 监控，必须手动 check_job_status 或 tail 日志判断完成
- 易错点：run_eval.sh 中的输出路径 (/root/autodl-tmp/eval_results/) 与实际运行路径不同，读结果用实际路径
- 时间线：B 评估 ~5h 是 MVP 对比的关键路径瓶颈，A eval 也需 ~5h 但可在 A 训练完后与 B eval 并行跑


---
