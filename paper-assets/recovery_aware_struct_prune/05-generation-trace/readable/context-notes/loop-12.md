# director / loop_12.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`e20c7a22986fb60af207.json`](../../sessions/e2/e20c7a22986fb60af207.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-17T07:17:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：westb-23072 cuda:0/1 + westd-11672 cuda:0/1/2/3（共 6 张）
- westd 刚从宕机恢复，连接可能不稳定，提交 job 后必须 verify PID 存活
- GRASPrune baseline 数据已存在 (D033/D034)，**不要重新启动 plan_005**
- scoring ablation 必须加 `--skip_attention` 参数（否则 magnitude/random 会剪 attention groups 导致 load_pruned_model 崩溃）
- eval 脚本必须带 `--output_path`（之前遗漏导致结果未保存）
- Agent 有"写代码但不执行"的模式——收到 Worker done 后必须确认 GPU 进程实际启动（要 PID）

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (connect.westb.seetacloud.com) + westd-11672 (connect.westd.seetacloud.com)，user=root
- 代码路径：`/root/recovery_aware_struct_prune`（两台均有），数据/模型在 `/root/autodl-tmp/recovery_aware_struct_prune/`
- SFT 模型路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_{rasp,standard}_20_westb` (westb) 或 `sft_{rasp,standard}_20_westd` (westd)
- eval 脚本：`src/eval_gsm8k.py`, `src/eval_math500.py`, `src/eval_humaneval.py`
- 活跃进程 westb：scoring_ablation_v2 (cuda:0/1, --skip_attention fix 中) + multi-seed serial eval (cuda:0)
- 活跃进程 westd：MATH-500 × 3 (cuda:0/1/2, unpruned+sft_rasp+sft_standard, ETA ~2h) + HumanEval sft_rasp_20 即将提交 (cuda:3)
- 磁盘：westb 43GB 可用（已删 grpo_stage2_rasp_20_v9/checkpoint-10）；westd 未检

### 3. 📊 当前状态
刚完成：eval_grpo_rasp_25 (53.15%, C1 25% 确认) + COS metric 分析 + negative 实验深度复盘 + Manager hypothesis 自检。

RUNNING/进行中：
- Plan_012 extended eval：MATH-500 unpruned/sft_rasp/sft_standard (westd cuda:0/1/2, ~2h)；HumanEval grpo_rasp 已完成 (10.37%! 意外高于 unpruned 1.83%)
- Plan_007 scoring ablation v2：--skip_attention fix 后重跑 (westb)
- Plan_006 multi-seed：westb cuda:0 串行 4×N=200 (seed=123/456 × RASP/Standard)
- Plan_017 unstructured baseline：eval_unstructured_20 (westb cuda:1)

等待：multi-seed cron 回调 (~30min)；MATH-500 完成 (~2h)；scoring ablation 全程 (~6-8h)

### 4. 📋 待办
- multi-seed 4 个结果到齐 → 计算 seed=42/123/456 的 mean±std，判断是否需要 seed=789
- MATH-500 完成 → 比较 unpruned vs sft_rasp vs sft_standard，验证 C1 在 MATH 上是否成立（post-GRPO ≈ post-SFT）
- HumanEval sft_rasp_20 完成 → 如果 ≈10% 则 GRPO 对 code 无增量 (confirms C1 cross-benchmark)；如果远低于 10% 则 GRPO 意外提升 code（改论文 story）
- scoring ablation 4 methods 完成 → 构建 Table: magnitude/gradient/random/cka_only post-SFT accuracy 对比
- 全部 Plan_007/012/017 完成 → 更新 experiment_plan.yaml coverage + 跑 dream_simulate(review_mode="full") 评估最终论文强度
- Qwen Math 25%>20% paradox：如果 DeepSeek eval_grpo_rasp_25 (53.15%) ≈ 20% (60.65%)差距大，说明 DeepSeek 无 paradox，Qwen Math 是特例 → footnote 处理

### 5. 🎯 战略上下文
- 论文核心 framing (D048/D050 后)：C1 = GRPO reward-accuracy decoupling (cosmetic collapse)，C2 = collapse dynamics as diagnostic (COS metric 刚量化)，C3 降级为 descriptive finding
- pass@k 2×2 矩阵完整：RASP 91.5%/89% vs Standard 91%/85.5%，C1 diversity 证据到位
- RLVR-aware scoring 是 negative ablation (D050)，不是独立贡献
- HumanEval 意外发现：pruned+SFT 模型 (10.37%) >> unpruned (1.83%)。原因可能是 SFT 激活了 instruction-following。需要 sft vs grpo 隔离实验确认
- DDL: ARR May 25 (~8 天)。算力充足 (768h 可用，需求 <100h)，瓶颈是执行速度
- Manager 刚推了 hypothesis-driven methodology：每个新实验必须有可证伪 hypothesis + parent 推导链
- 易错点：Agent 容易"写脚本不执行"——必须要 PID 确认；westd 可能再次不稳定


---
