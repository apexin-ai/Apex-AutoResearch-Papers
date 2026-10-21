# agent / loop_21.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`4a073f258d09561bec82.json`](../../sessions/4a/4a073f258d09561bec82.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: idle_timeout
updated: '2026-05-19T11:19:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 上 python 路径必须用 `/root/miniconda3/bin/python`，bare `python` 会 EXIT_CODE=127（已踩两次：eval-perdof-object-norm003-seed44 和 r2）
- GPU 白名单必须从 `get_project_resource_usage` 实时查，不要凭记忆假设哪张卡空闲
- 当前 4 台服务器：bjb1-18228、bjb1-32546、bjb2-28827、bjb2-40593，每台环境不同，提交前必须确认 python 路径和 conda env
- CoRL 2026 DDL 2026-05-29，剩 10 天，所有实验决策以此为硬约束

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 ~/runs/acr-vla-conformal-refinement/，Python=/root/miniconda3/bin/python。当前跑 3 个实验（cuda:0 obs-only-norm02-seed48-r2, cuda:1 obs-only-norm003-seed43, cuda:3 perdof-default-seed43）
- **bjb1-32546**: 当前跑 6 个实验（cuda:0-5 全占满：obs-only-norm003-seed44, perdof-norm005-seed43, perdof-norm003-seed43, obs-only-norm003-seed45, perdof-default-seed45, perdof-norm003-seed45）
- **bjb2-28827**: 当前跑 6 个实验（cuda:0-5 全占满：perdof-norm005-seed45, obs-only-norm01-seed45-r2, obs-only-norm02-k5-seed44, obs-only-default-seed45-r2, random-selection-seed44, perdof-norm03-seed43）
- **bjb2-40593**: cuda:0 跑 scalar-object-seed45-r2
- 共 16 GPU 在跑，0 张空闲
- W&B 项目: acr-vla-conformal-refinement（eval 实验通过 W&B metrics 判定完成）
- 预置镜像: `aml-train`

### 3. 📊 当前状态
**刚做完**：Session 初始化（read_registry + reconcile_crons + report.md + ROADMAP）

**正在做**：诊断 `eval-perdof-object-norm003-seed44-r2` 失败（已派 Worker `diag:eval-perdof-object-norm003-seed44-r2` 去 bjb1-18228 读日志，尚未回调）

**RUNNING 实验**（16 个，全是 magnitude curve / seed 补充 eval）：
- obs-only 系列：norm003-seed43/44/45, norm01-seed45-r2, norm02-seed48-r2, norm02-k5-seed44, default-seed45-r2
- perdof 系列：norm003-seed43/seed45, norm005-seed43/seed45, norm03-seed43, default-seed43/seed45
- random-selection-seed44, scalar-object-seed45-r2

**等待中**：
- Worker `diag:eval-perdof-object-norm003-seed44-r2` 回调 → 根据诊断决定是否重试
- Worker `ops:harvest-scan-bjb1-32546-and-bjb1-18228` 回调（采集完成指标）
- Worker `ops:fix-deploy-bjb1-18228` 回调（可能与 seed44-r2 失败相关的部署修复）
- 16 个 RUNNING 实验的 cron 完成回调

### 4. 📋 待办
- `diag:eval-perdof-object-norm003-seed44-r2` Worker 回调 → 读诊断结果，update_registry 写 notes，若可修复则在 bjb1-18228 空闲卡上重试 r3
- 任一 eval 实验 cron 回调(success) → 按 on-experiment-done 流程：update_registry metrics + 更新 report.md + 汇报 Director（带 [资源] 行）+ 检查 magnitude curve 数据点是否够
- 任一 eval 实验 cron 回调(failed) → 读日志诊断 + 在空闲卡重试
- random-selection-seed44 完成 → 这是 component decomposition 确认的关键数据点，完成后触发 Paper Agent data patch（连同 VLA-only 11.6% + p=0.0064）
- obs-only-norm02-k5-seed44 完成 → K-value curve 达 n=3，更新 ROADMAP
- 所有 magnitude sweep 完成 → 汇总 perdof collapse evidence（目标 n≥4）+ obs_only stability evidence → 通知 Director 启动最终 Paper Agent 审查
- bjb1-18228 有卡空闲时 → 部署待办队列：eval-perdof-object-norm03-seed48、eval-obs-only-object-norm003-seed47 等

### 5. 🎯 战略上下文
- **核心结论**：K=10 obs_only CRM (17.5%) 显著优于 VLA-only (11.6%), Fisher p=0.0064。perdof 随 ε 增大 collapse（14%→0%），obs_only 全 ε 稳定（13.5-17.5%）。这是 paper 的 primary evidence。
- **D061 锁定**：CoRL 2026 main conference, Option A（K=10 primary + mechanism insights）
- **D058**：CRM 是 correction 模块不是 selection 模块——论文 framing 必须一致
- **D064**：Component decomposition reframing——selection 通过 random baseline 验证
- **Paper 状态**：初稿 8 页完成，story upgrade 完成（test-time compute contrast）。等 random seed43/44 + data patch 后提交 Reviewer 审查
- **易错点**：
  1. bjb1-18228 的 python 路径问题已导致 2 次失败，提交命令必须用 `/root/miniconda3/bin/python` 或 `source /root/miniconda3/bin/activate && python`
  2. perdof default (uncapped) 数据点只有 3 个（全 0%），仍需补到 n≥4，seed43/45 在跑
  3. 不要把 obs_only 的 "stable across ε" 和 perdof 的 "collapse" 搞混——paper narrative 依赖这个对比
  4. 已有 98 success / 26 negative / 26 failed，failed 大多是环境问题非方法问题


---
