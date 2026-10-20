# reviewer / loop_1.md

**redundancy compound sparsity 2** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`c5584bcfcb2f290c0e1a.json`](../../sessions/c5/c5584bcfcb2f290c0e1a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T15:30:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`cuda:0` 和 `cuda:1`，两张卡均属本项目，无越界风险
- D003 脚本用 `CUDA_VISIBLE_DEVICES=0/1` 重映射，脚本内 `--gpu 0` 实际对应物理卡 0/1
- `carc_kv_eviction.py` 的 `apply_eviction()` **不得**修改 `_seen_tokens`（已删除该行），position tracking 由调用方（CARCGenerator / eval 脚本）通过 explicit `position_ids` 管理
- sanity_check_eviction.py 已验证 RoPE position 处理正确，其结果可信；carc_generate.py 的 RoPE fix 也已验证

### 2. 🖥️ 基础设施快照
- 服务器：`westd-16980`，工作目录 `/root/carc/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/carc/models/DeepSeek-R1-Distill-Qwen-14B`（本地，max_position_embeddings=131072，支持 128K）
- HF cache：`/root/.cache/huggingface/`（wikitext-2 已缓存，hendrycks/competition_math 网络不通需 `source /etc/network_turbo`）
- kvpress v0.5.3 已安装，R-KV repo 在 `/root/carc/r_kv_baseline/`
- 分析脚本：`/root/carc/analysis/`（A1-A4 四个脚本已就绪）
- 图表输出：`/root/carc/figures/`（A1 heatmap 3 张图已生成）
- 活跃进程（截至 handoff 前）：
  - `d003_reasoning_traces`：PID 28311, tmux=d003_reasoning_traces, cuda:0, ~30GB
  - `d003_wikitext_32k`：PID 28390, tmux=d003_wikitext_32k, cuda:1, ~32GB
  - EXP2 已完成 full + ema_0.7，正在跑 ema_0.5；EXP1 正在跑 full 策略 eval

### 3. 📊 当前状态
**项目处于 D003 等待阶段**——EMA eviction 的最后验证机会（reasoning traces + 32K context）。

Registry 关键实验：
- `d003_reasoning_traces`: RUNNING — MATH reasoning traces 上 EMA vs random vs recency（6 策略含 gamma 0.9/0.7/0.5）
- `d003_wikitext_32k`: RUNNING — WikiText-2 32K prefill 上同样 6 策略对比
- `sanity_kv_eviction`: DONE, conclusion=negative（EMA vs random gap 仅 0.9%）
- `carc_mvp_seed42/1337`: 均 DONE, conclusion=negative（cross-axis FAIL）

已完成的准备工作：
- Plan B (analysis paper) 叙事框架已审阅并获 Director 采纳
- A1 heatmap 已生成（spatial decoupling 可视化）
- A2-A4 分析脚本已就绪待 GPU
- Baseline 框架（eval_baselines.py + kvpress）已部署
- experiment_plan.yaml 已写入 14 个实验

### 4. 📋 待办（条件触发式）
- **D003 两个实验完成（cron 回调）→ 独立核实结果数据，重点看 `ema_vs_random_gap_pct` 是否 ≥5%**
- D003 FAIL（极大概率）→ 向 Director 确认 Plan B 启动，审查 A2 (attn vs EMA) 实验设计的公平性
- D003 意外 PASS → 审查数据可信度（D003 脚本经历 3 次崩溃修复，需确认最终版本无残留 bug）
- A2 实验提交 → 重点审查：attention-score eviction 是否在同等条件下对比（同 budget/grace_window/数据）
- B1 (Qwen2.5-7B) 实验提交 → 检查 GPU 分配、模型下载路径
- experiment_plan.yaml Phase 1+ 实验提交 → 确认 Phase 0 gate 条件已满足

### 5. 🎯 战略上下文
**决策链**：
- D001: MVP 定义（cross-axis 假说验证）
- D002: MVP 双 seed FAIL → Path C pivot（O(1) KV eviction）
- D003 pending: EMA eviction sanity gate FAIL (0.9%) → 在 reasoning+32K 上重试

**核心判断**：cross-axis 假说已确定证伪。EMA 作为 KV eviction 信号也几乎确定无效（sanity check 0.9% gap）。D003 是最后机会但概率很低。项目大概率走 Plan B（analysis paper targeting EMNLP Findings）。

**易错点**：
1. D003 脚本经历了 3 轮崩溃修复（网络→API兼容→device mismatch），如果结果异常（如某个策略 PPL 极高），先怀疑代码 bug 而非科学结论
2. D003 reasoning_traces 用的是内嵌 60 道数学题（非原始 hendrycks/competition_math），与 MVP 的数据来源不完全一致
3. Director 已确认 A2（attention-score vs EMA 对比）是 Plan B 最高优先级——其结果决定论文 claim 是"EMA specifically fails"还是"no O(1) signal suffices"
4. 不要混淆 sanity_check_eviction.py（独立脚本，position 处理正确）和 carc_generate.py（AR 生成循环，已修但未在实验中实际使用）
5. 模型支持 128K context，64K 实验无需 RoPE scaling


---
