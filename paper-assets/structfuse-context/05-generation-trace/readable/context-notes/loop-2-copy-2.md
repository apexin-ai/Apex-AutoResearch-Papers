# agent / loop_2.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`6cdfb8d3e80f8635e027.json`](../../sessions/6c/6cdfb8d3e80f8635e027.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-13T01:27:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 **cuda:4** (cqa1-21977)。即使 Director 指令用其他 GPU 也必须 push back，不例外。(D005 事故教训)
- 训练脚本路径是 `/root/structfuse/training/train.py`（不是 `/root/structfuse/train.py`）
- CLI 参数：`--learning-rate`（不是 --lr）、`--hard-negative-strategy`（不是 --strategy）、策略名 `embedding_distance`（不是 `embedding`），用错 EXIT_CODE=2
- 所有大文件必须放 `/root/autodl-tmp/`，根分区只有 30GB
- `eval_results_p50/` 已被 Director 自己的指令删除（2026-05-12 Step 1），不要再找或重建，metrics 在 registry `p2b_eval_4runs_pool50`
- M1 元数据必须用 `swe_smith_metadata_fixed.jsonl`（原始文件 buggy_function 为空）

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977, 账号 root
- **工作目录**: `/root/structfuse/`
- **Python**: `/root/miniconda3/bin/python`, 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**:
  - Qwen2.5-Coder-3B: `/root/structfuse/models/Qwen/Qwen2.5-Coder-3B`（本地）
  - StarCoder2-3B: `/root/autodl-tmp/.hf_cache/starcoder2-3b/`（HF cache, 12GB, 完整验证通过）
- **数据路径**: `/root/autodl-tmp/structfuse/`（checkpoints / m1_extraction / m1_training_data）
- **HF_HOME**: `/root/autodl-tmp/.hf_cache`
- **活跃进程**: M1 extraction PID 577864（cron 已注册, interval 600s）
- **磁盘**: 数据盘 169G, 上次检查可用 38G (78% used)

### 3. 📊 当前状态
**刚做完**:
- Director 3 个任务全部完成: (1) StarCoder2-3B 适配 ✅ 无需改代码, (2) dynamic mining 代码实现 ✅ build_m1_training_data.py + train.py 已改, (3) M1 磁盘监控 ✅ cron 已注册
- 已向 Director 汇报上述结果 (main_agent_post_to_director)
- memory.md 已更新

**RUNNING 实验**:
- `m1_extraction`: 全量 CodeQL 提取, PID 577864, 上次检查 21/131 repos (4656 instances), cron 监控中

**等待中**:
- 2 个 Worker 仍在运行: `worker_monitor_m1_progress_and_z_check` (含 Z% 计算) + `worker_monitor_m1_urgent_status` (紧急状态检查) — 结果回来后需要汇报 Director
- Director 最新指令是紧急检查 M1 状态，上述 2 个 Worker 就是为此派出的
- M1 cron (interval 600s) 会在进程结束时回调

### 4. 📋 待办（条件触发式）
- Worker `m1_urgent_status` / `m1_progress_and_z_check` 完成 → 汇报 Director M1 状态 + 磁盘 + Z%（Director 在等这个回复）
- M1 extraction 完成（cron 回调 on_complete）→ 立即计算全量 Z% → 决定 framing 走向（≥35% best, 20-35% pivot Claim 2, <20% 重大调整）→ 启动 M2 训练 (cuda:4)
- M2 启动 → `python scripts/build_m1_training_data.py` 构建 3 策略训练数据 → 9 runs (3 策略 × 3 seeds) 用 `submit_training_job`
- plan_013 (StarCoder2-3B) 可与 M2 Qwen 训练串行跑（同一 GPU），代码已验证兼容
- plan_015 (dynamic mining) 代码已就绪，等 M1 数据 → `--embedding-mining-mode dynamic` 生成 candidate_pools.jsonl → `--dynamic-mining` 训练

### 5. 🎯 战略上下文
- **核心研究**: StructFuse = CodeQL scope-bounded data-flow hard negatives for contrastive code retrieval。目标 EMNLP 2026 ARR (May 25 deadline, ~12 days)
- **决策链**: D001 MVP 设计 → D004 Phase 1 PASS → D007 connected⊆gold 是 scale artifact (Z=40.8% at 50-repo) → D008 MVP conditional pass → D009 Dream 审稿 (median=Weak Reject) → D010 StarCoder2 升 P0
- **M1 的 Z% 是关键分叉点**: 全量 Z% 决定 paper framing 走向，三档阈值已写入 paper_framing.md
- **易错点**:
  - train.py 已有 `--temperature` 参数（τ pilot 加的），默认 0.05。M2 训练时注意是否要改回 0.07
  - `build_m1_training_data.py` 有 two-layer connectivity（positive_files vs full_connected），不要和 MVP 版本的 connected_files 混淆
  - nohup 启动训练会变 orphan 进程，**必须用 submit_training_job**
  - eval 多 checkpoint 不能并行（OOM），必须串行


---
