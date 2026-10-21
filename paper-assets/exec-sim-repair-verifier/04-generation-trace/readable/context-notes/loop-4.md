# director / loop_4.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`cd86c2ffb9d9fb80acfd.json`](../../sessions/cd/cd86c2ffb9d9fb80acfd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-12T19:22:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- **seetacloud 禁止并行训练**（D028）：cgroup 360GB RAM 限制，两个 4B 训练并行必触发 OOM killer。v3+v4 两次确认。
- **westd-48478 = seetacloud 同一物理机**（同 hostname connect.westd.seetacloud.com）。D028 约束适用于 westd-48478 所有 GPU。不要在上面开新训练。
- **D024: 禁止杀死正在正常训练的进程来应用代码修改**。替换运行中训练必须先提交 Director 审批（D030 强化）。
- **D031: CWM 提交禁止使用 Worker**。Agent 必须亲自用 ssh_execute 逐步完成全流程（清理→验证→提交→确认），每步汇报后再下一步。此规则因 7 次连续失败（多 Worker 并行提交导致进程泄漏）而设立。
- GPU 白名单：cuda:0-3（seetacloud/westd-48478）+ home cuda:0。项目配置 3 台服务器但 westd-48478 SSH 间歇性认证失败，实际可靠的只有 seetacloud + home。

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**：4×RTX 5090, account=root, connect.westd.seetacloud.com。工作目录 `/home/sonny/exec-sim-repair-verifier`（注意 project_path 用 sonny 但 seetacloud 用 root 账号）。cgroup 360GB RAM。
- **home-1x5090**：1×RTX 5090, account=sonny, implicit5638.xyfu.me。工作目录 `/home/sonny/exec-sim-repair-verifier`。非容器，62GB RAM。
- 模型：Qwen3-4B LoRA（函数级已完成）、Qwen3-8B（8B scaling 已完成）
- 数据：函数级 per-test 在两台服务器均有；repo-level SWE-bench 数据已准备
- CLS 训练脚本：`train_repo_verifier.py`（save_strategy 已改为 steps/200/3）
- CWM 训练脚本：`train_repo_cwm.py`（save_strategy 已改为 steps/500/3）
- 活跃进程：**repo-level-cls-home** PID 2840844 (home cuda:0)，cron 300s 监控中。CWM 当前无活跃进程。

### 3. 📊 当前状态
- **repo-level-cls-home**: RUNNING on home cuda:0, step ~872+/6633 (3 epochs), ~7s/step, 首个 epoch checkpoint 在 step 2211。save_strategy=epoch（旧代码启动，无中间 checkpoint 直到 step 2211）。预计完成 ~05:30 UTC May 13。
- **repo-level-cwm**: 7 次失败（v1-v6），seetacloud 4 GPU 全空闲。D031 已发但 Agent 未执行就 idle 超时了。**新 session 启动后第一件事是按 D031 协议提交 CWM v7**。
- **Paper Agent**: Step 4/5 进行中（experiments.tex + method.tex 完成，introduction/related_work/abstract/conclusion 待写）。
- **Error overlap 分析**: 完成，Claim 3 支持（34% complementarity, Oracle 90.14%）。
- **8B seed123**: 已确认权威值 89.37%，bootstrap 用的是正确数据（Reviewer PASS）。
- 等待：CLS cron 回调、CWM 需要重新提交。

### 4. 📋 待办
- **立即** → 按 D031 六步协议亲自 SSH 提交 CWM v7 到 seetacloud cuda:2（最高优先级，4 GPU 空闲太久）
- CLS home cron 报完成 → 检查 checkpoint + eval（home 无 eval_repo 脚本，需提前准备或适配 eval_verifier.py）
- CWM 训练完成 → eval + repo-level paired bootstrap CLS vs CWM → Pillar 1 Go/No-Go（D008: ≥3pp 全力推，1-3pp 加 seed，<1pp kill C1）
- repo-level eval 完成 → repo-level error overlap 分析（验证 complexity-dependent complementarity）
- Paper Agent Step 4 完成 → 审查 writing_plan + 论文初稿

### 5. 🎯 战略上下文
- **核心假设转向**：函数级 CLS≈CWM（TOST 等价 p=0.007），核心假说已改为 **complexity-dependent advantage**——repo-level 是决胜场。
- **四大 Pillar**: P1(Complexity-Dependent)⏳ P2(Function-level Equivalence)✅ P3(Oracle Frontier)✅ P4(8B Scaling gap=2.43pp, p=0.007)✅
- **CWM 是唯一阻塞项**。CLS 在跑，其他 Pillar 全完成。repo-level CWM 训练成功 = 论文数据齐全。
- **ARR May 25 DDL，~13 天，关键路径 ~3-4 天**（CWM 20h + CLS 12h 并行 → eval 3h → paper patch 2d）。时间充裕但 CWM 不能再失败。
- **易错点**：不要把 westd-48478 当独立服务器用；不要用 Worker 提交 CWM；seetacloud 上任何时候只能有一个训练进程。
- `oracle_gain_over_cwm=30.05` 在 error overlap JSON 里是 bug，正确值 2.79pp。如果后续引用该 JSON 需修。


---
