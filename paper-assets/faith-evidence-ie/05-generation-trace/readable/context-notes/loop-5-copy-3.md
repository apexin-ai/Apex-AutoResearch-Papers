# reviewer / loop_5.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`9cf56517d9d74ce67606.json`](../../sessions/9c/9cf56517d9d74ce67606.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-15T04:00:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目使用 rtx5090-4x 的 4 张 GPU（cuda:0-3），均已分配给 RSFT generation shards，不可越界到其他项目的 GPU
- SFT adapter 路径固定 `/root/autodl-tmp/sft_output`，RSFT 训练必须从此 adapter merge 后再训新 LoRA，不可跳过 merge 步骤
- RSFT 训练启动时**必须传 `--eval_data_dir /root/autodl-tmp/data/docred`**，否则无 rel_f1 监控——这是 GRPO catastrophic forgetting (D031) 的核心教训
- `merge_shards.py` 和 `load_generations()` 均已统一为 last-wins（shard 覆盖 root），不可改回 first-wins

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，备用 bjb2-12179 (root)
- 工作目录：`/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：base `/root/autodl-tmp/models/Qwen3-4B`，SFT adapter `/root/autodl-tmp/sft_output`
- NLI 模型（CED 用）：HF cache `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base`
- 数据集：`/root/autodl-tmp/data/docred`（train_annotated 3027 docs）
- 生成输出：`/root/autodl-tmp/rsft_generations/`（root + shard_0-3）
- 活跃进程：4 shard generation — s0 PID 135867 cuda:0, s1 PID 136270 cuda:1, s2 PID 136649 cuda:2, s3 PID 137985 cuda:3

### 3. 📊 当前状态
4 shard RSFT generation 持续运行中。最后一次检查（~02:55 UTC）进度：
- shard_0: 2392 lines = 299 docs / ~757 (39%)
- shard_1: 2664 lines = 333 docs / ~757 (44%)
- shard_2: 2648 lines = 331 docs / ~757 (44%)
- shard_3: 2176 lines = 272 docs / ~756 (36%)
- 总计: ~1235/3027 docs (41%), 4 GPU 均正常（util 55-65%）

shard_3 一直偏慢（早期 duplicate process 事件导致 data gap + 重启）。

已完成的审查：
- pipeline-prep-verify: PASS（merge_shards.py + diversity_analysis.py）
- fix-dedup-strategy: PASS（统一为 last-wins）
- rsft-train-config: WARNING（eval_data_dir 默认不启用）
- verify-ced-pipeline: PASS（NLI 模型在 HF cache，CED pipeline 就绪）
- 多个 progress monitor workers: 确认进度正常

Registry: mvp2_rsft_gen_s0/s1/s2/s3 全部 RUNNING。

### 4. 📋 待办
- 任一 shard 完成（registry status → DONE）→ 验证该 shard 数据完整性（JSONL 行数 = progress.json doc 数 × 8）
- 全部 4 shard 完成 → 验证：(1) diversity cross-check 用 diversity_metrics.py，(2) 数据完整性全量检查，(3) shard_3 之前的 data gap 是否已填补
- CED scoring 启动时 → 验证分数分布有意义方差（不全是 0 或 1），验证 F1 gate 生效（无 gold match → CED=0）
- RSFT training 启动时 → **核查是否传了 --eval_data_dir**，核查 GPU 设备号在白名单内，监控前几步 rel_f1 是否维持在 SFT baseline 附近（0.4057）

### 5. 🎯 战略上下文
- 决策链：GRPO+QLoRA 判死（D031/D033，rel_f1<0.02 catastrophic forgetting）→ pivot 到 RSFT（D031）→ diversity crisis 是监控 bug 非真问题（D036）→ 恢复 4 卡并行 RSFT generation
- SFT baseline: rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118。RSFT 的目标是在此基础上提升
- 核心方法论：CED reward（DeBERTa NLI 区分 gold evidence vs entity-sharing distractors）→ 筛选高质量生成 → SFT 训练
- **易错点**：(1) generation_config.json 会覆盖代码参数（D034 已修复，但要警惕类似问题）；(2) 监控指标可能有 bug 导致误报（D034/D036 前车之鉴）；(3) root generations.jsonl 是修复前（T=0.6, top_k=20）生成的，质量低于 shard 输出——去重已统一为 shard 优先
- **最大风险**：RSFT 训练后 rel_f1 不升反降（重蹈 GRPO 覆辙）。TaskEvalCallback 是唯一防线，必须确保启用


---
