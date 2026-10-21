# reviewer / loop_8.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`5c87e1f6761cdcf6395c.json`](../../sessions/5c/5c87e1f6761cdcf6395c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-16T15:34:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0 和 cuda:1（westd-11235）。越界 → severity: critical
- Qwen-7B 模型路径：`/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`（不是 `/root/autodl-tmp/models/`，那里没有 7B）
- 所有 Qwen-7B 训练必须加 `--gradient_checkpointing`，否则 OOM（已踩坑两次）
- 论文路径：`/root/trace-verdict-study/docs/paper/`（不是 `/root/trace-verdict-study/paper/`）

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，代码根 `/root/trace-verdict-study`
- Python��`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：
  - Qwen-7B: `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`
  - Qwen-1.5B: `/root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct`
  - DeepSeek-6.7B: `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct`
  - CodeLlama-13B: `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/`
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/`
- HF_HOME：`/root/autodl-tmp/.hf_cache`
- W&B project：`trace-verdict-study`
- 活跃进程：codellama13b_vota_seed42 (PID 279473, tmux, cuda:1)
- GPU 0：空闲（49175 MiB 残留内存待清理，进程已死）

### 3. 📊 当前状态
**刚完成的关键里程碑**：codellama13b_exception_only_seed42 = **99.83%**，与 Qwen-7B/1.5B 完全一致（同 2 个错误样本 id=901,905）。已报告 Director："signal-limited" claim 可从 Discussion 观察升级为正式 finding。

**RUNNING**：
- codellama13b_vota_seed42 (cuda:1, 约 14:23 开始，预计 ~2.5h)

**阻塞**：
- exception_only_nomarker_seed42 两次失败（路径错 → OOM），registry status=QUEUED retry_count=1。已报 Director：缺 `--gradient_checkpointing` + GPU 0 残留内存��等待 fix worker。
- GPU 0 空闲 ~45min，等 Director 派 fix

**QUEUED**：
- exception_only_nomarker_seed123, exception_only_nomarker_seed456（同样需要修正命令）

### 4. 📋 待办（条件触发式）
- GPU 0 nomarker 修复后重跑 → 验证 GPU 合规 + 确认加了 `--gradient_checkpointing`
- codellama13b_vota_seed42 完成 → ��证 accuracy（预期 ≥99%，与 exception_only 接近），检查 id=901,905
- nomarker × 3 seeds 全部完成 → 审查：format marker 对 accuracy 的影响（如果 nomarker ≈ 有 marker → marker 不是关键信号；如果 nomarker 显著下降 → marker 贡献了判据信号）
- 论文 discussion.tex L21 仍写 "two models at ~7B scale" → 现在有 4 个模型 1.5B-13B，需更新 Limitations 段
- codellama 全部完成后 → 推动 Agent 更新 Table 1（跨模型对比表）加入 CodeLlama-13B 行

### 5. 🎯 战略上下文
**核心结论链**：
1. Exception events alone → 99.83% across ALL tested models/scales (signal sufficiency)
2. no_trace → 67-76% even at 13B (signal necessity)
3. Same 2 errors (id=901,905) universal → irreducible ceiling from GeneratorExit mechanism
4. 综合："verdict prediction is signal-limited, not capacity-limited"

**易错点**：
- 别把 DeepSeek exception_only (99.33%) 和其他模型 (99.83%) 直接等同 — DeepSeek 有 seed 不稳定问题（seed123=91.09%），2/3 seeds 99.33%
- nvidia-smi 显示内存占用 ≠ 有活跃进程。GPU 0 现在有 49GB 残留但 0% util = 死进程残留
- `--gpu 0` 在命令里是逻辑 GPU 编号（CUDA_VISIBLE_DEVICES 映射后），spec 里的 `cuda:1` 是物理编号。两者不矛盾
- nomarker 实验是为回应审稿人 R1-N1 关于 format marker 贡献的质疑，优先级高


---
