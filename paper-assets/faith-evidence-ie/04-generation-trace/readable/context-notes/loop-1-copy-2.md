# agent / loop_1.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`ab47f355341d5f4ca7e3.json`](../../sessions/ab/ab47f355341d5f4ca7e3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T10:20:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- rtx5090-4x 和 gpu-5090-4x-1 是**同一台机器**（4×RTX 5090 32GB），三路 GRPO 必须串行，不能并行
- GPU 白名单: cuda:0-3（只有这 4 张），不存在第二台服务器
- submit_training_job 的 command 必须用 `bash -c "..."` 包裹（tmux 用 sh 不支持 source/conda）
- grpo_trainer.py 的 p.get() 已修复为 `str(p.get("x") or "")`，不要回退到旧写法
- ZeRO-3 + QLoRA 不兼容，只能用 ZeRO-2；attention 只能用 SDPA（无 flash-attn）
- TRL 1.1.0：`processing_class=` 不是 `tokenizer=`；`max_length` 不是 `max_seq_length`

### 2. 🖥️ 基础设施快照
- 服务器: rtx5090-4x, 工作目录 `/root/autodl-tmp/`
- Python: `/root/miniconda3/bin/python` (conda base), Python 3.12
- 模型: `/root/autodl-tmp/models/Qwen3-4B` (7.6GB, ModelScope 下载)
- SFT checkpoint: `/root/autodl-tmp/sft_output` (LoRA adapter, QLoRA 4-bit)
- 数据: `/root/autodl-tmp/data/docred/` (train 3027 docs, dev 985 docs)
- NLI cache: `/root/autodl-tmp/data/docred/train_nli_cache.json` (38180 samples)
- NLI 模型: `cross-encoder/nli-deberta-v3-base` (HF 在线加载，AutoDL 代理有超时需 retry)
- HF cache: `/root/autodl-tmp/.hf_cache`
- 网络必须: `source /etc/network_turbo` + SSL cert env vars
- GRPO 输出: `grpo_s3/` (CED), `grpo_s2/` (flat-NLI), `grpo_s1/` (extraction-only)
- 链式脚本: `/root/autodl-tmp/run_mvp2_chain.sh` (6 phase, 已验证)
- 推理脚本: `/root/autodl-tmp/freige/eval/inference.py` (dry-run 通过)
- 活跃进程: mvp2_grpo_ced_r1 (tmux session, PID 24122, cuda:0-3)
- Cron: mvp2_grpo_ced_r1 (300s interval)

### 3. 📊 当前状态
**CED r1 训练出现 mode collapse**，Director 已知。Worker `ced-collapse-diagnosis` 正在执行诊断（检查 checkpoint、clip_ratio=0 根因、早停判断）。**等待该 Worker 回调**。

关键指标走势：step 35 附近达到峰值 (total_reward ~1.79, f1=0.098)，step 50+ 退化到 total_reward ~1.1, f1=0.012, truncation 40%。clip_ratio 全程 0.0 是核心问题——PPO 裁剪从未触发。

Registry 状态:
- mvp2_grpo_ced_r1: RUNNING (可能需要 kill)
- mvp2_grpo_ced: DONE(failed) — None 值 crash
- mvp2_grpo_flatnli: PREPARING
- mvp2_grpo_extract: PREPARING
- mvp2_sft_eval: PREPARING
- mvp2_sft_warmup: DONE(success) — eval_loss 0.72, acc 83.5%
- precompute_nli_train: DONE(success)
- smoke_test_grpo: DONE(success)
- mvp1_ced_signal: DONE(success) — margin 0.48, acc 81.5%

grpo_s3/ 目录当前为空（save_strategy="epoch"，还没跑完一个 epoch），**没有 checkpoint 可 resume**。

### 4. 📋 待办（条件触发式）
- `ced-collapse-diagnosis` Worker 回调 → 读取诊断结果（clip_ratio 根因 + 是否已 kill）→ 立即汇报 Director，附修复方案
- Director 决策修复方案（预期选项: 加 cliprange/KL penalty/降 lr）→ 修改 grpo_trainer.py → 重新提交 CED r2
- CED 训练完成（无论 r1 还是 r2）→ 立即用 `run_mvp2_chain.sh` 启动后续链（SFT eval → flat-NLI → eval → extraction-only → eval）
- 任一 GRPO 实验 DONE → on-experiment-done skill 分叉处理（success/negative/failed）
- 三路 GRPO + eval 全部完成 → 汇总 MVP-2 判定（pass criteria: CED Evi-F1 > SFT Evi-F1 ≥ 2pp; F1 > 45）

### 5. 🎯 战略上下文
- 项目目标: FREIGE — 用 CED reward 训练 LLM 做文档级关系抽取，同时生成可验证证据。目标 EMNLP 2026 / AAAI 2027
- MVP-1 PASS (D002): CED 信号验证通过，margin 0.48, acc 81.5%，非词汇重叠驱动
- MVP-2 进行中: 三路 GRPO 对比（CED vs flat-NLI vs extraction-only），证明 CED 的增量价值
- **最容易判断错的事**: clip_ratio=0 不一定是 cliprange 参数问题——TRL GRPO 可能默认不启用 PPO clipping（GRPO ≠ PPO），需要查 TRL 源码确认 GRPO 是否天然无 clip。如果是设计如此，则 collapse 原因在别处（lr 过高 / reward scale / 无 KL penalty）
- **易踩的坑**: grpo_s3/ 空目录 = 无 checkpoint，只能从 SFT 重跑；step time 会从 ~120s 逐渐增到 ~155s，时间估算别用初始速度
- 44.4% DocRED 样本无 hard negatives，CED 退化为 flat NLI（p_neg=0），分析结果需分层
- D004: 两个 SSH endpoint 是同一台机器，这个错误导致了早期并行计划失败


---
