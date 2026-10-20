# agent / loop_1.md

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`b392fa613b73e1ca0a9a.json`](../../sessions/b3/b392fa613b73e1ca0a9a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-16T15:52:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb2-23165 的 cuda:0 和 cuda:1（两张 RTX 5090 32GB）
- 所有实验启动命令必须包含 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`（网络不通）
- 改 K 值时必须同步调 `GEN_BATCH_SIZE = max(1, 64 // K_CANDIDATES)`，否则 OOM
- 每个 K/配置变体必须有独立输出目录（outputs_k8/, outputs_fullft_k4/ 等），禁止复用 outputs/
- config 覆盖必须在 `import pipeline` 之前设置（pipeline import 时读 config）
- ArmoRM 需要 patch 4 处 modeling_custom.py（模型目录 + 2 个 HF cache modules）

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 `/root/autodl-tmp/carr/`
- Python：`/root/miniconda3/bin/python3`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-0___6B`
- Reward Model：`/root/autodl-tmp/models/RLHFlow/ArmoRM-Llama3-8B-v0___1`
- Embed Model：`/root/autodl-tmp/models/sentence-transformers/all-MiniLM-L6-v2`
- 数据集：openbmb/UltraFeedback（本地缓存，offline 模式）
- K=4 LoRA 结果：`/root/autodl-tmp/carr/outputs/` (已完成，归档保留)
- K=8 LoRA 输出：`/root/autodl-tmp/carr/outputs_k8/`
- Full-FT K=4 输出：`/root/autodl-tmp/carr/outputs_fullft_k4/`
- 活跃进程：
  - carr_quick_probe_k8_02: PID 507603, cuda:0, cron 监控中 (300s)
  - carr_fullft_k4_probe_01: Worker 正在创建脚本+提交, cuda:1（尚未确认 PID）

### 3. 📊 当前状态
刚完成 baseline no_curation 分析并汇报 Director。正在等两个实验:

| exp_id | GPU | 状态 | 说明 |
|--------|-----|------|------|
| carr_quick_probe_k8_02 | cuda:0 | RUNNING | K=8 LoRA, GEN_BATCH_SIZE=8, ~4-6h |
| carr_fullft_k4_probe_01 | cuda:1 | Worker 提交中 | Full-FT K=4, lr=5e-6, Worker `worker_run_fullft_k4_probe_20260516T155107` 尚未回调 |

等待中:
- Worker `worker_run_fullft_k4_probe_20260516T155107` 回调 → 确认 full-FT 实验启动成功，注册 cron
- carr_quick_probe_k8_02 cron 回调 → 提取 3 代 metrics，P1 判定
- carr_fullft_k4_probe_01 cron 回调 → 同上

### 4. 📋 待办（条件触发式）
- Worker fullft 回调到达 → 确认 PID + 注册 cron + update_registry 到 RUNNING + 汇报 Director
- K=8 probe 完成 → spawn worker 提取 metrics → 向 Director 报 P1 pass/fail（Vendi ≥5% 下降 = pass）
- Full-FT probe 完成 → 同上，对比 LoRA vs Full-FT Vendi 下降幅度
- K=8 P1 pass → Director 决策用 K=8 配置跑 Full MVP（4 条件 × 5 代）
- K=8 P1 fail + Full-FT P1 pass → LoRA 是 collapse 约束因素，用 Full-FT 配置跑 Full MVP
- 两者都 fail → 需要向 Director 提 K=16 或 pivot 讨论

### 5. 🎯 战略上下文
- **核心问题**: P1 前提验证——能否在 3 代内产生 ≥5% Vendi Score 绝对下降
- **已知**: K=4 LoRA 只产生 -0.28% (FAIL)。no_curation baseline 反而 +3.1%。相对差距 ~3.4pp 但绝对值不够
- **当前诊断阶梯**: K=8 LoRA (cuda:0) + Full-FT K=4 (cuda:1) 并行跑，哪个先 pass 就用哪个配置
- **DDL**: EMNLP 2026 ARR 2026-05-25（还剩 9 天）。如果 P1 诊断耗时 >2 天，DDL 压力极大
- **决策链**: D001(MVP 设计) → D002(Quick Probe 先行) → D003(代码修复) → D004(P1 FAIL, 加压诊断)
- **易错点**: 
  - outputs/ 目录千万不能被新实验覆盖（K=4 LoRA 的原始数据）
  - train_sft.py 修改必须向后兼容（`getattr(config, 'USE_LORA', True)` 默认 LoRA）
  - carr_quick_probe_k8_01 是 killed（数据污染），不要误读为有效结果；有效的是 k8_02
  - 第一个 fix worker (PID 507334) 缺少 batch size fix 可能留下残留进程，如果 outputs_k8/ 有 Gen 0 数据可能是污染的（第二个 worker 已 rm -rf 重建）


---
