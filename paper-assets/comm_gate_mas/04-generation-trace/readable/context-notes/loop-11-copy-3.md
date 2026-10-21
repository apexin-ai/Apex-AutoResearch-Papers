# director / loop_11.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`683f50037b50c0629c66.json`](../../sessions/68/683f50037b50c0629c66.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-04-29T20:36:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb2-4x5090-b 只能用 cuda:0, cuda:1（cuda:2,3 是 pseudo_label_bias_decomp 项目的）
- westb-4x6000-a 只能用 cuda:1（cuda:0 有其他项目进程，Manager 未分配给我们）
- vLLM 启动必须 `--max-model-len 8192 --enforce-eager`（2048 导致过 100% silent failure，D237 教训）
- vLLM pre-flight 必须发真实 prompt 验证推理输出（不能仅检查 HTTP 200）
- 每个 seed 跑完后 sanity check baseline accuracy > 50%（脚本把 400 错误标记为 completed 不报 error）
- suppress rate ~37% 是 Llama oracle 正确值（论文已从错误的 ~45% 修正，commit 8a880f2）

### 2. 🖥️ 基础设施快照
**bjb2-4x5090-b** (connect.bjb2.seetacloud.com, root)
- 工作目录: `/root/autodl-tmp/comm_gate_mas`
- Python: `/root/miniconda3/bin/python` (conda base)
- 模型: `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- vLLM cuda:0 port 8001, cuda:1 port 8002（均 max_model_len=8192, enforce_eager）
- 活跃: Llama StratQA seeds 3+5 (cuda:0), seeds 4+6 (cuda:1), 96% util
- 日志: `/tmp/gpu0_seeds.log`, `/tmp/gpu1_seeds.log`
- 输出: `outputs/stratqa_llama_4seed_v2/`

**westb-4x6000-a** (connect.westb.seetacloud.com, root → account comm_gate)
- 工作目录: `/root/autodl-tmp/comm_gate_mas`
- Python: conda base
- 模型: Qwen2.5-7B-Instruct（已在 HF cache）
- vLLM cuda:1 port 8001 (PID 134958, 89GB, 0% util — 空转等修复)
- 🚨 Qwen StratQA 脚本 FAILED: `--mode e2e` 应改为 `--mode online_pruning --detection-mode heuristic`
- 本地论文: `artifacts/paper/` HEAD=8a880f2

### 3. 📊 当前状态
**刚完成**：
- Manager 调研：梳理 8+12 个实验异常，Reviewer 评估完毕
- 论文 9 项 framing 修改（commits 9c9ebc9 + 8a880f2）：suppress rate 修正、position reversal、Llama beneficial CI、StratQA comparison、Gemma t=0.7 披露、N=1000 弃用说明、topology-ack emergence、temperature-typology、variance collapse
- Llama seed_3072 outlier 分析写入 appendix（Grubbs G=2.137 < 2.290，非 outlier，ceiling effect）
- 论文已提交 Review Director 二审（pending 用户确认 review mode）

**RUNNING**：
- `stratqa_llama_heuristic_4seed_v2` (bjb2 cuda:0,1): seeds 3,4 已完成（+2.5pp, +0.5pp），seeds 5,6 运行中，预计 ~30-50min
- `qwen_heuristic_stratqa_4seed` (westb cuda:1): FAILED，脚本模式错误待修复

**等待中**：
- bjb2 seeds 5+6 完成 → 8-seed 聚合分析（`stratqa_8seed_analysis.py` 已准备好）
- Review Director 二审结果
- westb 脚本修复后重跑

### 4. 📋 待办（条件触发式）
- bjb2 seeds 5+6 完成 → 运行 `stratqa_8seed_analysis.py` 计算 8-seed mean±SD/CI → 如果 CI 仍正向，更新 Table 1 去掉 $^\ast$ 脚注 → post_to_reviewer 验证
- 8-seed 均值 > +2pp 且 CI 不含 0 → 强化 Discussion beneficial claim → commit
- 8-seed 出现负 seed 或 CI 含 0 → 保留原 4-seed 数据加 caveat
- westb Qwen StratQA → 修复 `--mode e2e` 为 `--mode online_pruning --detection-mode heuristic` → 重跑 4 seeds → 与 Llama StratQA 组合形成双 backbone × 双任务矩阵
- Review Director 二审报告到达 → 按 `review-report-action` skill 处理（Holistic Pass → Per-Comment Action Matrix）
- Manager 问新研究方向 → 最有潜力方向是 "Backbone Communication Signature"（异常 3+6），可做 IDEA_BRIEF

### 5. 🎯 战略上下文
- 论文核心：Dissociation finding（perturbation sensitivity ≠ pruning safety）+ reusable analysis protocol
- 目标：NeurIPS 2026 Datasets & Benchmarks Track，abstract 5/3，paper 5/5-6
- Round 1 评分 5/10，30 项修改 + 9 项 framing 强化全部完成，预估 Round 2 → 6.5-7.5
- 决策链：D235（收到审稿）→ D236（framing 强化 batch 1）→ D237（batch 2 + 数字修正）→ D238（StratQA 补种）→ D239（Qwen StratQA 并行）
- **易错点**：(1) vLLM max_model_len 必须 8192 不是 2048（本轮踩过坑）(2) 脚本 `--mode` 参数：在线实验用 `online_pruning` 不是 `e2e`（本轮也踩过）(3) Registry 经常与实际状态不同步，先 SSH 查实际再信 registry (4) Llama heuristic suppress ~75% vs oracle ~37%，不要搞混 (5) StratQA 4-seed 含 discovery seed（$^\ast$ 脚注），补种就是为了消除这个攻击面


---
