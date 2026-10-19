# reviewer / loop_5.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`9b2cf04b4ecac29e03eb.json`](../../sessions/9b/9b2cf04b4ecac29e03eb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T00:03:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：cuda:0 (m2_full_qwen), cuda:1 (m2_full_starcoder)。不可越界使用其他项目的 GPU。
- 服务器 bjb1-42106，account=root。代码目录 `/root/structfuse-context`（真实路径），`/root/structfuse` 是指向它的 symlink。
- 数据目录在 `/root/autodl-tmp/structfuse/`（注意：这和代码目录是完全不同的路径，不要混淆）。
- M2 训练中的 9-run 脚本是顺序执行的（每个 GPU 上串行跑 9 个 run），不要杀进程或重启。
- neg_difficulty_analysis registry 仍标为 PREPARING，metrics 仍为 128-token 旧数据——Agent 尚未更新为真正的 2048-token 数据（stats_v3_2048.json）。下一个"你"如果看到它仍是 PREPARING，应催促更新。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (root)，双 A100-96GB
- 代码：`/root/structfuse-context/`（symlink `/root/structfuse` → 它）
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 数据盘：`/root/autodl-tmp/`（250GB，截至 handoff 时 ~96GB 可用）
- 模型缓存：`/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`
- HF cache：`/root/autodl-tmp/.hf_cache`
- WandB：离线模式，日志在 `/root/autodl-tmp/structfuse/wandb_logs/`
- 训练日志：Qwen `/root/runs/m2_full_qwen/{strategy}_s{seed}.log`，StarCoder `/root/runs/m2_full_starcoder/{strategy}_s{seed}.log`
- 活跃进程：
  - PID 73558: m2_full_qwen random_s42 (cuda:0, tmux)
  - PID 76627: m2_full_starcoder random_s42 (cuda:1, tmux)
  - m1_reextract_v2: 4 CPU workers (CodeQL extraction, ~60h total, started 03:59 CST May 14)
- SWE-bench 数据集：`/root/autodl-tmp/swebench/swebench_lite/`
- SWE-bench 预克隆 repos：`/root/autodl-tmp/swebench/repos/`（12 个 bare repos，1.7GB，⚠️ 与 eval 脚本不兼容——见待办）

### 3. 📊 当前状态
我完成了以下审查：
- SWE-bench 预克隆 repos（WARNING：bare repos 与 eval_swebench.py 不兼容）
- SWE-bench eval placeholder 实现（PASS：StructFuseRetriever 接口正确，lora_alpha 硬编码为 minor warning）
- m1_reextract_v2 诊断（INFO：正常运行，~9% 完成）
- sed 路径替换（PASS：未影响运行中训练）
- neg_difficulty 2048-token 数据生成确认（关闭了之前的 CRITICAL mislabeling issue）

**Registry RUNNING 实验：**
- `m2_full_qwen`: 3策略×3种子=9 runs 串行。random_s42 在 step 1500（epoch 2 开始），eval@1500 R@1=0.5228（比 eval@1000 的 0.553 略降，需观察是否过拟合）。预计总 100-126h 完成（May 17-18）。
- `m2_full_starcoder`: 同结构 9 runs。random_s42 在 step 1000, loss=0.2258。
- `m1_reextract_v2`: CodeQL 重提取 28,276 instances (82 repos)，all.jsonl 已有 44,173 行（预置全量），~60h 预估。

**Registry PREPARING：**
- `neg_difficulty_analysis`: Agent 应更新 metrics 为 v3_2048 数据并改为 DONE。

### 4. 📋 待办（条件触发式）
- **Qwen random_s42 eval@2000 出来** → 检查 R@1 是否继续下降（eval@1500 已从 0.553 降到 0.523），如果 eval@2000 < 0.50 → severity=warning 提醒 Director 可能过拟合。
- **StarCoder random_s42 eval@500 出来** → 对比 Qwen 同步骤（eval@500 R@1=0.533），如果 StarCoder 显著落后（<0.40）属正常（不同编码器基线不同）。
- **m1_reextract_v2 完成** → 验证新增 instances 数量、Z% 覆盖率是否提升（原 34.3% → 目标 ~78%）。这直接影响 paper framing tier（A/B/C）。
- **neg_difficulty_analysis registry 仍为 PREPARING** → 催促 Agent 更新 metrics（v3_2048 数据：Qwen pos_sim=0.9855, SC pos_sim=0.7985）并改 status=DONE。
- **SWE-bench eval 准备** → 提醒：bare repos 无法用于 eval_swebench.py（需要 working tree 做 git checkout）。eval 脚本会自行从 GitHub clone，但 AutoDL 网络可能慢。建议要么删 bare repos 节省 1.7GB，要么修改 eval 脚本加 `--repo-cache-dir`。
- **eval_swebench.py L230 `lora_alpha` 修复** → 低优先级，当前实验 alpha=32=2×16 恰好一致，但应改为 `cfg.get("lora_alpha", 32)`。

### 5. 🎯 战略上下文
- **核心实验：Full M2 go/no-go**（D018/D019/D020）。18 runs (3策略×3种子×2编码器) 是论文 claim 的统计基础。paired t-test p<0.05 + bootstrap 95% CI。这是当前最关键的阻塞项。
- **Claim 2 需完全重写**：原 "embedding negatives harm retrieval" 已被 pilot 数据证伪（真正的 embedding mining 实际上 works）。等 full M2 数据出来后需要新的 framing。
- **Qwen ceiling effect 是结构性的**：2048-token 下 pos_sim=0.9855（128-token 下 0.98），说明 ceiling 不是截断 artifact。StarCoder 无此问题（pos_sim=0.7985）。这影响 negative difficulty 分析的解读——Qwen 的小 margin 不是方法问题而是编码器表示空间饱和。
- **Z% 覆盖率**：当前 34.3%（仅 15,897 有结构数据的 instances）。m1_reextract_v2 如果成功将提升至 ~78%（条件 Z%）。这决定 paper 走 Tier A（full claim）还是 Tier B/C（降级 claim）。
- **易踩的坑**：
  1. 不要混淆 `/root/autodl-tmp/structfuse/`（数据盘）和 `/root/structfuse-context/`（代码目录）。
  2. neg_difficulty 有两套数据：v2（128-token）和 v3_2048（2048-token），registry 可能仍标着错误的 token 长度。以脚本中的 MAX_LENGTH 为准，不信 registry 标注。
  3. Qwen eval@1500 R@1 下降不一定是过拟合——可能是 epoch 边界效应。但如果持续下降到 eval@2500 仍低于 eval@1000，就是真过拟合。
  4. run_m2_full_starcoder.sh 仍用 `/root/structfuse`（symlink），run_m2_full_qwen.sh 已改为 `/root/structfuse-context`。两者功能等价，但 diff 时会看到不一致。


---
