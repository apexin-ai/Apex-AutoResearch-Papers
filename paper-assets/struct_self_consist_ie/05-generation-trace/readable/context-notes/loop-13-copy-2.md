# agent / loop_13.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`2ae8a0d0be6a7492442f.json`](../../sessions/2a/2ae8a0d0be6a7492442f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-16T14:04:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0/1/2/3（4×RTX 5090），不可用其他卡
- exp-021 Few-NERD full **必须用 rank=32, α=64**（不是 exp-020 smoke test 的 rank=16）
- Few-NERD 数据必须用 `supervised` config（不是 `intra`，`intra` 的 train/test entity type 零重叠）
- AUROC 计算已统一为 `>=` median（不是 `>`），evaluation.py 已修复，不要回退
- Table 2 Greedy F1 = 0.645（macro），不是 0.663（micro），已修复 11 处引用

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/struct_self_consist_ie/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型路径：`checkpoints/qwen3-8b-scierc-merged-v2`（rank=32 主模型）、`checkpoints/qwen3-8b-scierc-rank8-merged`（rank=8 消融）
- Few-NERD 数据：`data/fewnerd/`（supervised config，8 coarse types，train 131,767 / dev 18,824 / test 37,648）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：**全部已终止**（exp_022_seed789、exp_025_n32、exp_020_fewnerd_smoke 的 tmux session 均不存在）
- Cron：reconcile 返回 0 条活跃

### 3. 📊 当前状态
**刚做完**：Session-start 初始化 — registry/cron 同步、experiment_plan.yaml registry_id 对齐修复（exp-020/022/023/019/025）、向 Director 汇报 GPU 全空闲。

**Registry RUNNING**（实际进程已死，等 Worker 确认产出）：
- `exp_022_seed789`：3rd seed SciERC inference (seed=789, N=8)
- `exp_025_n32`：N=32 SciERC inference

**Registry ANALYZING**（进程已死，等 Worker 确认）：
- `exp_020_fewnerd_smoke`：Few-NERD LoRA smoke test training
- `exp_026_t05`、`exp_026_t08`：T-ablation inference（t12 已 conclusion=success）

**等待中的 Worker 回调**：
- `worker_analysis_batch_completion_check_a`：检查 exp-022/025/020 产出
- `worker_analysis_batch_completion_check_b`：检查 exp-026 t05/t08 + exp-019 verifier 精确指标

**已完成但未入 registry**：
- exp-027 MLP verifier：MLP≈LR（AUROC Δ=-0.013），RF 更差，所有 supervised verifier selection F1 < unsupervised LP baseline（0.647）。特征是瓶颈，不是模型容量。结果在 `output/exp_027_mlp_verifier/`
- exp-019 registry 仍为 killed，Director 要求更新为 success（等 Worker B 带回精确指标）

### 4. 📋 待办
- Worker A 回调 + exp-020 smoke **通过** → 立即 spawn worker 在 cuda:1+2 启动 exp-021 Few-NERD full（rank=32, α=64, 3-epoch）
- Worker A 回调 + exp-022 **成功** → update_registry DONE/success + 纳入 3-seed bootstrap 分析
- Worker A 回调 + exp-025 N=32 **成功** → update_registry + spawn worker 计算 5 signals + 扩展 N-ablation 表到 N=32
- Worker B 回调 + exp-019 指标 → update_registry conclusion=success with metrics
- Worker B 回调 + exp-026 t05/t08 确认 → update_registry DONE/success
- exp-027 MLP verifier → update_registry（新建 entry 或挂到 exp-019 下）+ 结果写入论文
- 所有上述完成后 → 刷新 report.md + 第三次 Dream 验证

### 5. 🎯 战略上下文
- **核心论文**：EMNLP 2026 Main，DDL 2026-05-25（9 天）。主题：IE 中 5 种 confidence signals 的 QE-selection gap
- **Dream #2 得分**：Best 3.0 / Median 3.0 / Worst 2.5，目标 3.5。D117 已完成 28 页论文 10 项修复 + N/T ablation 写入
- **最大缺口**：Few-NERD（第三 NER 数据集）是 Main Conference 的硬门槛，exp-020 smoke 是 gate
- **易错点**：
  - exp-020 smoke 用的是 rank=16（快速验证），exp-021 full 必须切 rank=32, α=64
  - VC paradox：VC 的 ρ/AUROC 最好但 selection F1 最差，这是论文核心发现之一，不要把 VC selection 差当 bug
  - LP 压缩是跨数据集普遍现象（SciERC 60% tied, CoNLL 更严重），entity-token LP 已验证无效（strictly worse）
  - Within-instance ρ 实际是正的（SciERC SJ median=0.47），旧版论文 claim "within 不相关" 已被 D109 推翻并 reframe
  - 决策链关键节点：D108(Round 13 分析) → D109(within-ρ 矛盾) → D112(Main 冲刺策略) → D113(Table 2 bug fix) → D114(AUROC 统一) → D116(Dream verifier) → D117(写作修复)


---
