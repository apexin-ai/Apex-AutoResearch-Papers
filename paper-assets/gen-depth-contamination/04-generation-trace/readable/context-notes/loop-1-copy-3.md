# reviewer / loop_1.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`43b853a34cedd91bb33b.json`](../../sessions/43/43b853a34cedd91bb33b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T15:00:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 `cuda:0`@`autodl-4090d`（仅 1 块 GPU，无越界可能，但须确认进程确实在 cuda:0）
- AutoDL 环境变量必须写入 `run_*.sh` 脚本（`source /etc/network_turbo` + SSL 证书 + HF 配置），tmux session 不继承 shell env
- HF 下载必须设 `HF_ENDPOINT=https://hf-mirror.com` + `HF_HUB_DISABLE_XET=1`，C4 用单 shard URL 不要用 `load_dataset("allenai/c4")` 全量加载
- 所有模型/数据/cache 放 `/root/autodl-tmp/`，根分区只有 30GB

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-4090d`（1×RTX 4090D 24GB），SSH 账号 `root`
- 工作目录：`/root/autodl-tmp/gen-depth-contamination/`
- 模型路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct`（双层嵌套是 HF cache 正常结构）
- 数据目录：`/root/autodl-tmp/gen-depth-contamination/data/`（depth_0.jsonl 已生成 5000 docs）
- 日志：`~/runs/gen-depth-contamination/mvp_pilot_sat_v1.log`
- 活跃进程：`mvp_pilot_sat_v1`（PID 5922，tmux，cuda:0）— 正在跑 Step 3 depth chain 生成（上次检查在 depth 2 ~15%）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- 无 W&B 配置

### 3. 📊 当前状态
**我是 Loop #1 的 Reviewer，项目刚启动半天。**

已完成的审查：
- MVP 设计审查（3 个 warning 已被 Director 采纳修复：K* 定义、生成方式、解码策略）
- Pipeline 代码审查（发现 right-padding 问题，Director 确认 MVP 不中断、full study 修复）
- Full study 实验计划审查（建议下游评估加多 seed，experiment_plan.yaml 未创建）
- 引用验证审查（8 处 [需验证] 已全部补全）

Registry：`mvp_pilot_sat_v1` RUNNING（depth chain 生成中，预计还需 ~2-3h 完成全 pipeline）

等待中：MVP 结果出来后需立即审查 K* 判定和 gate check 结论。

### 4. 📋 待办
- `mvp_pilot_sat_v1` 状态变 DONE → 立即读 registry conclusion + `results/summary.txt` + `results/pairwise_auc.json` → 核实 K* 计算是否与 AUC 数据一致，AUC(0v1) 是否 >0.70，gate 判定是否正确
- K* ≥ 3 → 验证 Agent 是否走 Route A（depth estimation 主线），检查 ROADMAP 更新
- K* = 2 → 验证 Agent 是否走 Route B（saturation characterization），检查 framing 调整提案（如有需按 negative-framing-review skill 四维度审）
- K* ≤ 1 → 验证 kill decision，检查是否排除了实现 bug（right-padding 可能影响结果）
- Full study 启动后 → 检查 experiment_plan.yaml 是否创建，首批实验 spec 是否完整
- 下游评估实验出结果 → 重点检查是否有多 seed、bootstrap CI、paired significance test

### 5. 🎯 战略上下文
- **核心科学量是 K***（判别饱和边界）。MVP 的唯一目的是测量 K* 并决定走哪条论文路线。
- **双路线已预备**：K*≥3 走 Route A（depth estimation + graduated filtering），K*=2 走 Route B（saturation characterization as contribution）。两条路线的 claim 结构、story arc、审稿人攻击面预演均已写好（`docs/claim_routes.md`）。
- **最容易判断错的事**：如果 K* 在边界（如 K*=2 但某些配置 K*=3），不要急于判定——right-padding bug 可能压低了真实 K*，修复后重跑可能改变结果。在边界情况下应建议 Director 修复 padding 后重跑 MVP 确认。
- **EMNLP ARR May 25 deadline 仅剩 13 天**（从 2026-05-12 起算）。MVP 必须今天出结果，否则 full study 时间不够。
- **理论框架**（`docs/theory_framework.md`）将 K* 定位为 information-theoretic impossibility boundary（DPI），不是分类器能力问题。这个 framing 在 K*=2 时尤其关键——把 limitation 变成 contribution。
- **已知代码问题**：(1) right-padding（full study 必修）；(2) batch_size 偏小（gen 16→64, feat 8→24）；(3) torch_dtype deprecation warning（cosmetic）。


---
