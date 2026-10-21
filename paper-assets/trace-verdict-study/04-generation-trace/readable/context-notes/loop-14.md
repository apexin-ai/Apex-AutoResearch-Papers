# agent / loop_14.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`76ba3dc86db24c7a344b.json`](../../sessions/76/76ba3dc86db24c7a344b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T20:28:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 cuda:0 + cuda:1，不得使用其他卡
- DeepSeek 模型路径极长：`/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`，不要猜短路径
- tail-truncation 数据可能在两个位置：`/root/trace-verdict-study/data/` 或 `/root/autodl-tmp/trace-verdict-study-data/`，Worker 生成时位置不一致，提交前必须 ls 确认
- DeepSeek head-2048 训练是 nohup 后台（非 tmux），训练完不会自动跑 eval，需要手动触发
- registry 状态机 PREPARING→DONE 必须逐级推进（PREPARING→PENDING→QUEUED→ALLOCATED→RUNNING→DONE），eval-only 实验也不能跳步
- zero-shot eval 脚本 `/root/trace-verdict-study/eval/zeroshot_eval.py` 和 few-shot 脚本 `fewshot_eval.py` 已部署在远程，复用即可

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 `/root/trace-verdict-study/`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 模型路径：
  - Qwen-7B: `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`
  - Qwen-1.5B: `/root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct`
  - DeepSeek-6.7B: `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
  - CodeLlama-13B: `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/`
- Checkpoints: `/root/autodl-tmp/trace-verdict-study-checkpoints/{exp_id}/`
- W&B project: `trace-verdict-study`
- 磁盘：root 80% (6.2G free), autodl-tmp 84% (42G free)
- 活跃进程：
  - cuda:0: DeepSeek head-2048 训练（PID 371041/371047, nohup, ~444 steps 接近完成）
  - cuda:1: Qwen-1.5B tail-256 训练（刚提交，worker `worker_code_qwen15b_tail256_20260517T202656` 可能还在跑或已回调）

### 3. 📊 当前状态
**刚做完**：本 session 完成了大量 baseline 实验：
- 3 模型 zero-shot (Qwen-7B 89.08%, DeepSeek 90.59%, CodeLlama-13B 51.01%)
- Qwen-7B 3-shot (90.84%)
- Qwen-1.5B zero-shot (93.45%)
- CodeLlama-13B SFT 两个条件（exception_only 99.83%, vota 98.57%）
- tail-2048 跨模型（DeepSeek 94.96%, Qwen-1.5B 97.90%）
- head-2048 跨模型（Qwen-1.5B 75.29%）
- Qwen-7B tail-256 (78.9%, negative)

**RUNNING in registry**：
- `deepseek_full_trace_head2048_seed42` — 训练 ~95% 完成，status=ALLOCATED（我推进到 ALLOCATED 后没来得及推 RUNNING，需先确认训练完成+跑 eval）
- `qwen15b_full_trace_tail256_seed42` — 刚提交，status=PREPARING（Worker 可能已提交训练）

**等待中**：
- Worker `worker_code_qwen15b_tail256_20260517T202656` 回调
- DeepSeek head-2048 训练完成后需手动跑 eval

### 4. 📋 待办
- `worker_code_qwen15b_tail256` 回调 → 确认训练已提交，等 cron 回调
- DeepSeek head-2048 完成（检查进程/日志）→ 手动触发 eval → 收割结果 → update_registry → 汇报 Director 完整 head vs tail 跨模型表
- Qwen-1.5B tail-256 完成 → 收割 → 与 7B tail-256 (78.9%) 对比，验证 phase transition cross-scale 一致性
- 两卡都空闲时 → 汇报 Director 完整 budget curve + 跨模型矩阵，请求下一步指示
- Director 要求写论文 → 将所有 baseline（zero-shot/few-shot/regex/SFT）+ budget curve + 跨模型矩阵写入 paper

### 5. 🎯 战略上下文
**项目核心**：Exception events 是 test verdict prediction 的 minimal sufficient signal，跨 4 模型 3 架构 1.5B-13B 达到 ≥99.33%。

**三个 Core Claims**：
1. Exception sufficiency（exception_only 99.33-99.83%）— 充分验证
2. Signal positional concentration（tail >> head）— 跨模型验证中，DeepSeek head-2048 是最后缺失的数据点
3. SFT necessity（zero-shot 51-93% → SFT 99%+）— 已有完整 3 模型 zero-shot + few-shot 数据

**Budget curve 关键发现**：256→512 存在 14.7pp phase transition，exception traceback 需要 ~500 tokens 才能完整捕获。tail-256 (78.9%) ≈ head-2048 (81.76%)，说明 256 tokens 不论从哪端截都不够。

**易错点**：
- Qwen-1.5B zero-shot (93.45%) 高于 7B (89.08%)，不要套 "bigger=better" 直觉。论文 framing 已从 "scale normalization" 调整为 "architecture normalization"
- tail-1024 之前是 negative（低于 tail-512），存在 non-monotonicity，论文已解释为 "中等长度 trace 积极有害"
- DeepSeek 有 format collapse 倾向（seed123 教训），DeepSeek 实验结果比其他模型更不稳定
- registry 中有 ~13 个 killed 的旧实验（no_trace_seed42, vota_seed42 等 v1/v2/v3），这些是历史残留已被替代，不要尝试恢复


---
