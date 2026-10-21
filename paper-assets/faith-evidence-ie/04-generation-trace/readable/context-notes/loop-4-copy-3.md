# reviewer / loop_4.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`ec1010df9e2581f1e63f.json`](../../sessions/ec/ec1010df9e2581f1e63f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T23:46:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配为 rtx5090-4x 全部 4 卡 (cuda:0-3)，但需核对 registry 中每个实验声明的 gpu 字段与实际 CUDA_VISIBLE_DEVICES 是否一致
- eval 脚本必须 `cd /root/autodl-tmp`（不是 `cd /root/autodl-tmp/freige`），后者会导致 Python path 找到内层空 `freige/freige/` 包，ckpt-60 已因此踩坑
- GRPO+QLoRA 方向已判死 (D031)，剩余 ckpt eval 仅收集轨迹数据，不作为后续方向决策依据
- cron 监控存在误判问题（PID 不匹配导致 5x dead 误判、conclusion 被误标 killed），审查时必须 SSH 独立验证进程状态，不能只信 registry status/conclusion

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，4× RTX 5090 32GB
- 工作目录：`/root/autodl-tmp/freige`（代码），`/root/autodl-tmp/` 下各子目录放模型/数据/输出
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`（base），`/root/autodl-tmp/sft_output`（SFT adapter）
- GRPO checkpoints：`/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-{20,40,60,80,100,...}`
- 数据：`/root/autodl-tmp/data/docred/`（train_annotated.json, dev.json）
- NLI 模型：`/root/autodl-tmp/models/nli-deberta-v3-base`（CED 打分用）
- HF cache：`/root/autodl-tmp/.hf_cache`
- W&B run：`grpo-s3-ced-lr5e6-r1`（GRPO 训练）
- RSFT 代码：`/root/autodl-tmp/freige/training/rsft_{generate,score_filter,trainer}.py`（已就绪，pyc 存在）

### 3. 📊 当前状态
**我刚完成的审查**：
- ckpt-40 eval 结果核实 (rel_f1=0.0071, FAIL) ✓
- ckpt-80 eval 启动核实 (cuda:2, PID 111739) ✓
- RSFT 三阶段代码审查 (generate/score_filter/trainer) ✓
- SFT baseline eval 结果核实 (rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118) ✓

**Registry RUNNING**：
- `mvp2_grpo_ced_lr5e6_r1`：GRPO 训练 cuda:0, PID 90085, step ~113/200, ~2.5h 剩余
- `mvp2_eval_lr5e6_r1_ckpt80`：ckpt-80 eval cuda:2, PID 111731/111739
- `mvp2_eval_lr5e6_r1_ckpt60_r2`：ckpt-60 eval cuda:1, PID 108185（conclusion 被 cron 误标 killed，实际在跑）
- `mvp2_eval_sft_baseline`：已完成但 status 未更新为 DONE（conclusion=success, metrics 已填充）

**QUEUED**：`mvp2_eval_lr5e6_r1_ckpt100`（等 GPU 释放）

### 4. 📋 待办
- ckpt-60 _r2 完成 → 验证 metrics.json，核对 rel_f1 是否继续 flat (~0.007)
- ckpt-80 完成 → 验证 metrics.json，**重点关注 reward-metric disconnect**：W&B 显示 step 80 reward=0.283 回升，如果 eval rel_f1 仍 < 0.05 则确认 reward hacking
- ckpt-100 完成 → 关键验证点：W&B 显示 step 100 f1_reward 拐点 (0.016→0.093)，eval F1 > 0.15 说明拐点真实，< 0.05 则确认 reward hacking，写入 D031 补充证据
- RSFT generation 启动 → 审查：数据用 train split（不是 dev）、CED 打分用正确的 tau、筛选比例合理
- RSFT training 启动 → 审查：GPU 边界、lr 合理（默认 2e-5）、与 SFT baseline 用同一 eval 协议

### 5. 🎯 战略上下文
- **核心决策链**：MVP-1 PASS (CED margin 0.4827) → SFT warmup 完成 → GRPO+QLoRA 6 次全败 (D022-D031) → Pivot 到离线 RL (Rejection Sampling FT + DPO)
- **SFT baseline 已锁定**：rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118。RSFT pass criteria: evi_f1 ≥ 0.8179 (即 +2pp)
- **最易判断错的事**：GRPO 训练 reward 在 step 80-100 回升，但这几乎确定是 reward hacking 而非真实能力恢复（ckpt-20/40 eval 已确认 catastrophic forgetting）。不要因为 reward 回升就对 GRPO 方向重燃希望
- **RSFT 代码有一个 warning**：reward 函数在 rsft_score_filter.py 中是从 grpo_trainer 拷贝的而非 import，如果 grpo_trainer 的 reward 逻辑改了这边不会同步
- **cron 误判是常态**：ckpt-40 被误判 5x dead、ckpt-60 被误标 killed，审查时务必 SSH 看 `ps -p &lt;PID>` 和 `nvidia-smi`，不能只信 registry


---
