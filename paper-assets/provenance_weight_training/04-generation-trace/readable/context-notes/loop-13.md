# director / loop_13.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`f4d5c44b68240c0b091f.json`](../../sessions/f4/f4d5c44b68240c0b091f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-17T21:41:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-30476 cuda:0-3 + westd-41312 cuda:0-3，共 8 张。禁止用其他服务器/GPU
- eval 参数不可变：`eval_perplexity.py --max_docs 5000 --stride 1024 --fp16`，PPL 基线 uniform=17.694
- 所有训练实验禁止加 `--eval_data_path`（inline eval 占 84% 时间，M012/M016 反复教训）
- batchsize16 实验必须 per_device_batch_size=16, grad_accum=1（不是 bs=4 accum=4，否则 n_min > micro-batch → b*≡0，M015）
- n_min 必须 ≤ micro-batch size（ESS 在 forward pass 粒度计算）

### 2. 🖥️ 基础设施快照
- **westd-30476**: connect.westd.seetacloud.com, root, 工作目录 /root/provenance_weight_training
- **westd-41312**: connect.westd.seetacloud.com, root, 工作目录 /root/provenance_weight_training
- Python: 服务器自带环境（无 conda activate）
- 模型: Qwen3-0.6B（主模型），checkpoints 在 output/{exp_name}/final_checkpoint
- 数据: /root/provenance_weight_training/data/human/eval_holdout.jsonl (eval), scored_data_*.jsonl (train)
- 活跃进程：**预计全部 8 个实验已完成**（ETA 最晚 00:36 UTC，现在已过 4h+），GPU 应全空闲
- 无 W&B 配置，无 HF cache 需求

### 3. 📊 当前状态
**关键问题：8 个实验完成但未 eval（Agent 连续 4 次 reset 后 idle）。** 这是最高优先级。

预计已完成的 8 个实验（需 eval_perplexity.py）：
| 实验 | 服务器 | Claim |
|------|--------|-------|
| qwen06b_uniform_seed42 | 41312:cuda:0 | baseline retrain |
| ess_only_seed456_r2 | 41312:cuda:1 | Claim 1 |
| ess_only_seed123_r2 | 41312:cuda:2 | Claim 1 |
| random_reweight_seed456 | 41312:cuda:3 | Claim 1 |
| grid_b0_3_seed456_r2 | 30476:cuda:0 | Claim 2 |
| grid_b0_3_seed123_r2 | 30476:cuda:1 | Claim 2 |
| rho02_adaptive_tau08_seed42 | 30476:cuda:2 | Claim 3 (D068) |
| batchsize16_nmin8_r3 | 30476:cuda:3 | D062 coupling |

Paper Agent 已完成 2 个 patch（n_min coupling rule + failure mode analysis）。3 个 patch 等数据。

### 4. 📋 待办
- Agent 启动 → 立即 nvidia-smi 两台服务器 → 对所有已完成实验跑 eval_perplexity.py（并行 4+ workers）→ 更新 registry
- eval 全部完成 → post-batch narrative review：Claim 1 (ess_only 3-seed + random 3-seed 显著性), Claim 2 (grid_b0_3 3-seed consistency), Claim 3 (rho02_tau08 safe default)
- 空闲 GPU → 启动: grid_b0_2_seed42 (b=0.2), lm-eval downstream (adaptive vs uniform on HellaSwag/ARC/PIQA/WinoGrande), contamination_60_seed123
- narrative review 完成 → update_roadmap + Paper Agent 剩余 3 patches (unified table + Claim 1 upgrade + random baseline)
- rho02_tau08 PPL < 17.694 → Claim 3 "safe default across ρ" 成立；PPL > 17.694 → Claim 3 降级为 "works at ρ≥0.4"

### 5. 🎯 战略上下文
- **投稿目标**: EMNLP 2026 ARR May 25（~7 天）
- **核心方法**: dual-constrained adaptive b* = inf{b≥0: α_eff(b)≥τ} s.t. ESS(b)≥n_min（最小干预准则）
- **D069**: MMLU +1.57pp (Llama-3B) 定位为 Discussion 观察，不升级 cross-model claim（HellaSwag -0.60pp 混合信号）
- **D068**: Claim 3 scope 调整——ρ=0.2+τ=0.9 negative 不否定方法，转为测试 τ=0.8 safe default
- **grid_b0_1_seed42**: 旧结果 PPL=17.657 已确认 eval 协议一致，可直接用，不需重跑
- **M016 是系统性问题**: Agent reset 后反复 idle 4h。新 session 启动后必须 10 min 内 check_agent_queue_status 确认 Agent 在工作。如果 idle > 15 min，urgent_agent_message 推一下
- **易错**: Agent 容易用错 checkpoint 路径（output/ vs autodl-tmp/output/），eval 前先 ls 确认 final_checkpoint 存在
- **Paper Agent session 已存在**: 直接 director_post_to_paper_agent 即可复用，不需重建


---
