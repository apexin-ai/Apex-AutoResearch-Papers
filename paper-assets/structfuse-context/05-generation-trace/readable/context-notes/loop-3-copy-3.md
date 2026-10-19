# reviewer / loop_3.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`09ed21ee3a41376a164c.json`](../../sessions/09/09ed21ee3a41376a164c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-13T01:27:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:4**（cqa1-21977 上）。D005 记录了 GPU 越界事故（PID 59170 跑在 GPU 5）。train.py 第 4 行已硬编码 `os.environ["CUDA_VISIBLE_DEVICES"] = "4"`。
- M1 提取是 CPU 任务（8 workers），不占 GPU，但 repos 克隆持续占磁盘——当前 m1_repos 11GB 且在增长，磁盘 38GB 余量需持续关注。
- StarCoder2 只保留单份 HF cache（`/root/autodl-tmp/.hf_cache/starcoder2-3b`, 12GB）。之前 ModelScope 副本已删。**不要重新下载到 ModelScope**。
- `ssh_read_only` 不支持 `|`、`;`、`&&` 等 shell 元字符。grep 多模式用 `-e` 或 `-i`，不用管道。

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977**（root），工作目录 `/root/structfuse`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Qwen2.5-Coder-3B → `/root/structfuse/models/Qwen/Qwen2.5-Coder-3B`；StarCoder2-3B → `/root/autodl-tmp/.hf_cache/starcoder2-3b`（hidden_size=3072, `models/` 目录无 symlink）
- 数据：M1 提取输出 → `/root/autodl-tmp/structfuse/m1_extraction/`（1.8GB）；M1 repos → `/root/autodl-tmp/structfuse/m1_repos/`（11GB）；MVP 数据 → `/root/autodl-tmp/structfuse/mvp_data/`
- Checkpoints：`/root/autodl-tmp/structfuse/checkpoints/`（4 dirs：p2b_random_s42/123/456 + p2b_embedding_distance_s42）
- W&B：`WANDB_MODE=disabled`（tau pilot 期间确认）
- 活跃进程：M1 extraction（PID 577874 主进程 + 577875-577881 八 workers），CPU only
- 磁盘：/root/autodl-tmp 38GB free / 169GB total (79%)

### 3. 📊 当前状态
**刚完成的审查：**
- worker_code_dynamic_mining_impl → PASS。`_mine_dynamic_negatives` 实现正确，但不含 dataflow 约束（WARNING 已通知 Director）。
- worker_ops_urgent_disk_cleanup → PASS。磁盘从 25GB 恢复至 38GB。
- worker_code_starcoder2_support → WARNING。模型已下载，代码兼容（AutoModel + 动态 hidden_size），但重复存储导致磁盘危险（已清理）。
- worker_monitor_tau_pilot_results / finish_and_cleanup → WARNING。tau_pilot_0.05/0.1 checkpoint 全部删除，无 eval 结果，无 registry 条目。Director 已收到两次通知但尚无回应。

**Registry RUNNING/PREPARING：**
- `m1_extraction`（RUNNING）— 全量 50,869 instances CodeQL 提取，8 CPU workers，skip_log 660 条（全是 pdfminer 解析 bug）
- `p2b_eval_all`（PREPARING）— 搁置中
- `p2b_dataflow_retrain`（QUEUED, conclusion=negative）— 因 connected⊆gold 被阻塞

**等待中：**
- 无活跃 cron/worker 回调
- M1 提取完成通知（预计还需 ~30h）

### 4. 📋 待办（条件触发式）
- M1 提取完成 → 核实总 instance 数、skip_log 最终行数、pdfminer 660 条是否修复、磁盘余量是否够 M2
- M2 训练数据生成（build_m1_training_data.py）→ 验证 MD5 divergence（embedding vs dataflow 池是否真正不同）、repo-level split 正确性、candidate_pools.jsonl 格式
- M2 训练启动 → 核实 GPU 合规（cuda:4）、registry 条目、log 捕获、W&B 配置
- StarCoder2 训练启动 → 确认 `models/` symlink 或完整路径、LoRA target_modules 兼容性（已确认 q_proj/v_proj 可用）、checkpoint 大小估算（~8GB，比 Qwen 大）
- Director 回应 tau_pilot 清理原因 → 确认是否需要重跑 pilot 或直接进 plan_014 全量温度消融
- plan_015 dynamic mining 实验 → 确认是否需要增加 "dynamic + dataflow 约束" 变体（当前实现只有纯 embedding dynamic）

### 5. 🎯 战略上下文
- **决策链**：D001(MVP设计) → D004(P1 PASS) → D006(recall@1 标准) → D007(connected⊆gold, 50-repo 验证) → D008(MVP 条件性通过, Z=40.8%) → D009(Dream: WA/WR/R, 5 共识弱点) → D010(plan_013 升 P0)
- **核心假设赌注**：Z%（dataflow connected ⊃ gold 的比例）。50-repo 验证 Z=40.8%，但全量 M1 的 Z% 未知。Z≥35% → best framing；20-35% → pivot Claim 2；<20% → 重大调整（paper_framing.md 缺少 <20% 场景描述，已在 Dream 审查中标注）
- **3 Core Claims**：(1) dataflow negatives > random/embedding；(2) embedding negatives 有害；(3) CodeQL 可扩展。Claim 1 是 headline，Claim 2 已有 MVP 数据支撑（random>>embedding -27pp recall@1）
- **最容易判断错的事**：
  1. MVP 阶段 dataflow ≡ embedding（code bug，因 connected⊆gold 在小 repo 上），**不等于**方法本身无效——只是规模不够。M2 全量数据是关键验证点。
  2. tau_pilot 数据已丢失（checkpoint 删了没做 eval），不要假设有温度先验数据。plan_014 需从零开始。
  3. `_mine_dynamic_negatives` 不使用 dataflow 约束——"dynamic + dataflow_aware" 策略组合当前不存在，别误以为 `--dynamic-mining --hard-negative-strategy dataflow_aware` 有效。
  4. 磁盘 38GB 看似充裕但 M1 repos 持续增长 + 每个 checkpoint ~6-8GB，留意别触发第二次磁盘满。


---
