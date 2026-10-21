# agent / loop_2.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`aab3d5ff971038ef8312.json`](../../sessions/aa/aab3d5ff971038ef8312.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-13T18:40:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 `westc-26893:cuda:0`（项目 config 中 gpu_constraint 仍写着 `autodl-4090d:cuda:0`，但实际服务器别名已变为 `westc-26893`，提交实验时 server 参数必须用 `westc-26893`）
- exp_003 的 cron 用旧服务器名 `autodl-4090d` 注册，已全部失效。新实验的 cron 必须用 `westc-26893` 注册
- 论文 DDL 05-25 ARR，关键路径：exp-003 → exp-006 (~21h) → exp-015 (3h)，不能拖
- exp_003 结果如果可恢复，不要重新跑——直接用已有产出，节省 ~10h GPU 时间

### 2. 🖥️ 基础设施快照
- 服务器：`westc-26893`（原 `autodl-4090d`，同一物理机，AutoDL 重启后 SSH 端口/别名变更）
- 工作目录：`/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（Qwen2.5-1.5B-Instruct、Pythia-1.4b、OLMo-1B-hf）
- HF 镜像：`HF_ENDPOINT=https://hf-mirror.com`，必须 `source /etc/network_turbo` + SSL 证书环境变量
- 活跃进程：无确认的 RUNNING 实验。exp_003 的 tmux session 可能仍存在（Worker 正在诊断）
- Cron：reconcile 返回 0 条活跃 cron

### 3. 📊 当前状态
**刚做的事**：收到 exp_003_decoding_ablation 的 cron 失败回调（进程退出 + 无 W&B metrics）。诊断发现是 SSH 别名变更导致 cron 监控断连，不是实验本身错误。日志显示 config 1 (greedy) 和 config 2 (nucleus_p0.9_t1.0) 已完成，config 3 (nucleus_p0.95_t0.7) 在 depth 4 ~90% 时日志截止。

**正在做**：Worker `worker_diagnose_exp_003_decoding_ablation_20260513T153757` 已 SSH 到 westc-26893 检查进程存活状态和 4 个 config 的产出完整性。**等这个 Worker 回调**。

**Registry 状态**：10 个实验全部 DONE（9 success + 1 failed=exp_003）。无 RUNNING/PREPARING。

**已通知 Director**：发了初步诊断报告，等 Worker 结果后再发完整汇报。

### 4. 📋 待办
- Worker diagnose 回调 → 根据产出完整性分两种：
  - 4 个 config 全完成 → 更新 registry metrics + conclusion=success + 通知 Director 数据已恢复 → 立即启动 exp-006
  - 部分完成 → 只重跑缺失的 config（不要全部重跑），更新 spec 用 `westc-26893` 提交
- exp-003 完成后 → 零间隔启动 exp-006 graduated filtering（~21h GPU，关键路径实验）
- exp-006 完成后 → exp-015 neural probe（3h GPU，D014 升 P0，论文生死实验）
- GPU 空闲时 → 向 Director 申请并行跑 exp-004 cross-scale Qwen-7B（optional，~3h）

### 5. 🎯 战略上下文
- **核心结论**：K*=2 跨 4 个模型族一致（Qwen-rewrite/Qwen-cont/Pythia/OLMo），bootstrap CI 全部显著。论文 2+1 claim 结构：C1'(K* characterization) + C3(graduated filtering) + supporting analysis
- **关键决策链**：D012(2+1 重构) → D013(C3 fallback) → D014(exp-015 升 P0) → D015(跨档一致问题) → D016(场景 A+C 叙事)
- **C2 限定**：degradation ordering 只能说 "mode-conditioned consistency with architecture residuals"，不能说 "universal"（D008/D010/D011）
- **易错点**：
  - 服务器名已变——所有新 submit_training_job / cron 必须用 `westc-26893`，不能用 `autodl-4090d`
  - exp_003 的 greedy config 数据目录名可能不叫 `data_exp003_greedy`——需要看 `run_exp003_ablation.sh` 脚本里的实际目录名
  - Qwen-rewrite (mvp-001) 的 transfer 很差（61-63%），论文 cross-model claims 必须基于 continuation mode
  - exp-015 neural probe 是 Reviewer 最可能攻击的点（"你们只有统计特征没有 learned representation"），必须跑


---
