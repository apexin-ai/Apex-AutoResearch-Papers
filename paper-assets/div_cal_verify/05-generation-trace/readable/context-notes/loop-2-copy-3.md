# reviewer / loop_2.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`d9e57dee5afba59ead91.json`](../../sessions/d9/d9e57dee5afba59ead91.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-12T20:25:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`westd-11235` 的 `cuda:0` 和 `cuda:1`，越界即 critical
- GPU 0 有 ~49GB 僵尸显存（无对应进程），实际可用 ~49GB。当前实验跑在 GPU 1 以避开
- `diversity_selection.py` 的 `greedy_disf_selection` 已修复为 `compute_normalized_eigenvalue_variance`（`frob/trace²`），**不要回滚到旧版 `compute_cov_frobenius`**
- MVP gate 是二元 PASS/FAIL，**没有 SOFT PASS**（D002 明确删除）
- 参考集 5000（`data/meta.json` 已更新），不要重新生成 512 版本
- 结果目录必须在数据盘 `/root/autodl-tmp/`，根分区只有 30GB（68% 已用）

### 2. 🖥️ 基础设施快照
- 服务器：`westd-11235(root)`，工作目录 `/root/div_cal_verify`
- Python：`/root/miniconda3/bin/python`（conda base）
- 环境初始化：`source /root/div_cal_verify/env.sh`
- 模型：`/root/models/Qwen/Qwen3-1.7B`（student）、`/root/models/Qwen/Qwen3-4B`（generator）、GPT2/GPT2-medium（HF cache）
- Qwen 数据：`/root/div_cal_verify/data/`（train 237666, ref 5000, test 583）
- GPT2 数据：`/root/div_cal_verify/data_gpt2/`（train 232588, ref 5000, test 558）
- MVP 结果：`/root/autodl-tmp/div_cal_verify/results/`（rgds 4 代完整, external_only 4 代完整, uncurated gen_0 partial）
- Phase 1 结果：`/root/autodl-tmp/div_cal_verify/results_phase1/`（进行中）
- 活跃进程：PID 93704 — `run_phase1.sh` 跑 rgds（GPT2-125M, 6 代, GPU 1），通过 nohup 启动，日志 `~/runs/div_cal_verify/phase1_rgds.log`
- GPU：2× NVIDIA RTX PRO 6000 Blackwell 98GB

### 3. 📊 当前状态
**MVP 已判定 FAIL（D004）**。RGDS PPL 16.46 vs External-only 16.15——RGDS 更差 1.9%，未达 ≥5% 改善阈值。根因：每代 ~250K tokens 对 1.7B 模型训练强度不足，RankMe 仅降 1.56%，kNN 完全不变。

**Phase 1 GPT2 崩塌验证正在执行**（PID 93704, GPU 1）。GPT2-125M/medium, 1M tokens/gen, 5 epochs, lr=1e-4, 6 代。`run_phase1.sh` 串行跑 RGDS → uncurated。预计 1-2h 完成。

Registry 里无 RUNNING 条目（Phase 1 未注册——minor issue）。所有旧实验已标记 DONE。

uncurated bug 已修复：`run_evaluation` 中 `compute_rank_correlation` 加了 `if contriever_model is not None` 保护；GPT2 dtype 改为 float32。`run_phase1.sh` 已加 `set -o pipefail`。

### 4. 📋 待办
- Phase 1 完成 → 检查 RankMe 是否显著下降（>10%）。**如果 GPT2 也无崩塌 → 框架/代码问题，需 debug**
- Phase 1 有崩塌 → 启动 Phase 2（高强度 Qwen：5M tokens/gen, 3 epochs, lr=5e-5, 6 代, 3 方法）
- Phase 2 RGDS PPL ≥5% 优于 External-only → MVP PASS，进入 research 阶段
- Phase 2 RGDS ≈ External-only → 假设失败，pivot to AAAI 2027
- **注意 Phase 2 时间估算可能偏乐观**：我在 ROADMAP 审查中指出 5M tokens/gen 的 greedy selection 是 O(budget×n)，时间可能 54-72h 而非 24-48h。建议考虑 RGDS + External-only 双卡并行

### 5. 🎯 战略上下文
- 决策链：D001（MVP 方案）→ D002（二元 PASS/FAIL + ≥5%）→ D003（训练强度风险预判）→ D004（MVP FAIL，启动高强度验证）
- EMNLP 2026 ARR DDL: 2026-05-25（剩余 13 天）。Phase 1（~2h）+ Phase 2（保守 54-72h）= 3 天实验 + 10 天分析写作。**无重跑余量。**
- **最容易判断错的事**：Phase 1 GPT2 结果出来后，如果 RankMe 也只降几个百分点但 PPL 变化明显——不要等同于"无崩塌"。GPT2-125M 比 Qwen-1.7B 小 14 倍，相同 token 数的影响会更大。关注绝对值变化趋势，不要机械套用 Qwen 的 <2% 判断标准。
- **负 rank correlation（-0.37~-0.39）是稳定发现**：model-internal 与 Contriever 多样性评分方向相反。RGDS train_loss 一致低于 external_only（~0.87 vs ~0.93），暗示 internal selection 选出了"容易学"但泛化差的数据——这可能是 RGDS 劣于 external_only 的机制解释。
- rare_ngram_survival 跨方法完全相同（精确到 16 位小数），确认 generator 输出在 RGDS/external_only 间一致——差异仅来自 selection step。


---
