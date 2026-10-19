# reviewer / loop_8.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`6dbe8ec63042da83997d.json`](../../sessions/6d/6dbe8ec63042da83997d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-14T19:04:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-42106 上仅此两张分配给本项目）。之前发生过重复进程占满 GPU 1 的事故。
- StarCoder 模型路径：`/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`（不是 `/root/autodl-tmp/structfuse/models/bigcode/starcoder2-3b`，后者不存在，BM25 脚本已修正）
- 两个代码目录共存：训练代码在 `/root/structfuse/`，评估代码在 `/root/structfuse-context/`。import 路径要注意一致性。
- D026：s42 = 3 epochs 无 early stopping；s43/s44 = 2 epochs + patience=2。resume 脚本给所有 run 加了 patience=2（含 s42），与原设计略有偏差但影响不大。
- Claim 2 framing 过强：pilot 数据中两个编码器都是 dataflow < embedding，"beyond embedding mining" 不成立。D028 已提议降级。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106(root)，2× RTX PRO 6000 96GB
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- Qwen 模型：`/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`
- StarCoder 模型：`/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`
- 训练数据：`/root/autodl-tmp/structfuse/full_m2_training_data/`（Qwen）、`/root/autodl-tmp/structfuse/full_m2_starcoder_data/`（StarCoder）
- BM25 数据：`/root/autodl-tmp/structfuse/full_m2_training_data/train_bm25_s{42,43,44}.jsonl`
- Checkpoints：`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 和 `m2_full_starcoder/`
- wandb：offline 模式
- 活跃进程（截至 handoff）：
  - cuda:0：Qwen random_s44 训练（Qwen 链 3/9，PID ~504138）
  - cuda:1：StarCoder random_s43 训练（resume 脚本 1/9，PID ~519805，wrapper PID 519791 timeout=518400）
  - CPU：m1_reextract_v2（CodeQL 提取，PID via batch_extract.py）
  - Qwen watcher：PID 966920（`watch_and_chain_qwen_s42.sh`，等 s43+ 完成后跑 s42 supplement）
  - StarCoder 旧 watcher 已 kill

### 3. 📊 当前状态
**刚完成的审查**：
- 覆盖率全面审查已提交（15.8% overall，Claim 2 = 0% 最薄弱）
- GPU 1 重复进程 CRITICAL 已修复验证（95GB → 48GB）
- BM25 Phase 2 脚本审查（StarCoder 路径已修正）
- K + checkpoint 文档审查（"Qwen always same" 被 random_s43 打破）
- SWE-bench 就绪度审查（pipeline ready，random_s42 可先跑）
- D034 ROADMAP 审查（override 逻辑合理）

**Registry 状态**：
- m2_full_qwen：ANALYZING（实际 RUNNING，random s42/s43 done，s44 running）
- m2_full_starcoder：DONE/failed（registry 状态过时，实际 resume 在跑 random_s43）
- m1_reextract_v2：RUNNING
- plan_018_bm25：QUEUED（Phase 1 done，Phase 2 已集成到 StarCoder resume run 3/9）
- plan_015_dynamic：QUEUED

**等待中**：无 pending worker 回调。监控模式。

### 4. 📋 待办（条件触发式）
- Qwen random_s44 完成（~6h）→ 检查 early stopping pattern，更新 checkpoint 文档
- StarCoder random_s43 首次 eval@500 → 核实 R@1 与 pilot (0.454) 一致性
- resume 脚本跑到 bm25_s42（run 3/9，约 ~May 16-17）→ 这是 plan_018 Phase 2 首个结果，关键审查：BM25 R@1 vs random R@1 决定叙事方向
- Qwen 链完成全部 9 runs（~May 17）→ 检查 embedding vs random 多 seed 统计差异，这是 Claim 1 的硬证据
- SWE-bench eval 启动通知 → 核实用的是 best_by_recall_at_1 checkpoint，验证 eval 脚本 import 路径
- Director 转发 Claim 2 framing 调整提案 → 按 negative-framing-review skill 四维度审查
- 任何新实验启动 → 核对 CUDA_VISIBLE_DEVICES 在 {0,1} 内

### 5. 🎯 战略上下文
- **论文核心**：systematic study of hard negative mining for code retrieval。3 claims，Claim 1（embedding helps）最强，Claim 2（dataflow conditional）最弱，Claim 3（CodeQL scalability）是 supporting。
- **关键决策链**：D017 falsified "embedding harms" → D024 pivot framing → D026/D027 epoch/early-stop 调整 → D028 Claim 2 降级待定 → D030 Dream 共识 BM25 是最大缺口 → D033 BM25 overlap 在大 repo 仅 30% → D034 re-dream gate override
- **最容易判断错的事**：
  1. plan_002 在 tracker 标 DONE（是 pilot m2_embed_verify），但 full M2 (m2_full_qwen/starcoder) 还在跑。别看到 DONE 就以为 M2 训练结束了。
  2. plan_013 conclusion="negative" 不是说 method 失败——是说 dataflow 对 StarCoder 不 work。embedding 对两个编码器都 work。
  3. Claim 2 的 framing 写的是 "beyond embedding mining"，但 pilot 数据两个编码器都是 dataflow < embedding。这是当前最大的 claim-evidence mismatch。
  4. BM25 Phase 2 结果（~May 17）决定 paper 叙事走 "correcting misconception" 还是 "systematic comparison"——不要在结果出来前 commit 叙事。
  5. 覆盖率 15.8% 是 misleading——plan_017 实际已完成但 tracker 标 planned，m2_full 在跑但不在 plan tracker 反映。


---
