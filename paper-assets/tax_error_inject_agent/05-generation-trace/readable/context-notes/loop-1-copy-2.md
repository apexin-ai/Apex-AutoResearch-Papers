# agent / loop_1.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`1352f167d9800d179372.json`](../../sessions/13/1352f167d9800d179372.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T10:30:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090:cuda:0/1/2/3，不可用其他设备
- ms-swift 4.2.0 **不支持 `--config &lt;yaml>`**，正式训练必须用命令行参数传入
- eval 必须用 `--task_list eval/eval_tasks_47.json`（固化的 47 任务子集），否则与 baseline 不可比
- Qwen3 `enable_thinking=False`，训练数据用纯文本 `&lt;think>` 标签，不是原生 thinking mode
- 模型路径是 `/root/autodl-tmp/models/Qwen/Qwen3-8B`（注意 Qwen/ 子目录），之前 registry 写错过
- formatter.py 有 DRY_RUN / API_ERROR 安全检查，dry_run 数据不能混入正式训练

### 2. 🖥️ 基础设施快照
- **服务器**：autodl-5090，工作目录 `/root/autodl-tmp/tax_error_inject_agent/`
- **Python**：conda base，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **PyTorch**：2.10.0+cu128，CUDA 12.8，4×RTX 5090 32GB
- **模型**：Qwen3-8B `/root/autodl-tmp/models/Qwen/Qwen3-8B/`，Qwen3-32B-AWQ `/root/autodl-tmp/models/Qwen/Qwen3-32B-AWQ/`（fallback teacher）
- **API**：base_url `http://47.94.22.126/v1`，模型 `openai/gpt-5.2`，key 通过 `request_secret("openrouter_api_key")` 或 .env
- **活跃进程**：traj_collect_500 PID 11045（轨迹收集，cron 监控中，~242/500 成功）
- **活跃 Worker**：`worker_exp_mini-pipeline-e2e_20260514T094954`（正在跑 SFT 训练阶段，TaxEI 155/195 steps）

### 3. 📊 当前状态
**刚完成**：所有代码修复（注入格式兼容、injection_detected 删除、API auth retry、recovery 失败处理、formatter 安全检查、eval 任务列表固化、SFT gradient_checkpointing OOM 修复、related work 对比表）。

**正在跑**：
- `mini-pipeline-e2e` Worker：用 ~242 条轨迹跑完整非 dry_run pipeline（注入→recovery→SFT→eval）。最新进度：TaxEI SFT 训练 155/195 steps (~79%)，接下来是 eval
- `traj_collect_500`：PID 11045，~242/500 成功轨迹，预计还需 ~2-3h

**Registry**：
- `traj_collect_500` — RUNNING，轨迹收集
- `vanilla-react-baseline` — DONE (success)，42.6% (20/47)
- `sft-dryrun-73` — DONE (success)，pipeline 验证

**等待中**：mini-pipeline Worker callback → 汇报 TaxEI vs vanilla 信号方向给 Director

### 4. 📋 待办
- mini-pipeline Worker 回调 → 分析 TaxEI vs vanilla clean SR + recovery rate，更新 registry，汇报 Director（含 [资源] 行）
- traj_collect_500 cron 回调（PID 11045 退出）→ 检查最终成功条数，若 ≥400 条立即启动正式 800 条 recovery generation + 正式 SFT 训练
- 正式 recovery generation 完成 → 格式化 SFT 数据（确认 wc -l + md5 不同）→ 并行训练 TaxEI-SFT (cuda:0) + vanilla-SFT (cuda:2)
- 正式训练完成 → eval with `--task_list eval/eval_tasks_47.json`，clean + inject 两轮，McNemar 统计检验
- Director 要求写论文 → 先 Read red-section skill，related work 对比表已就绪在 `docs/related_work_comparison.md`

### 5. 🎯 战略上下文
- **核心假设**：taxonomy-guided error injection 对 planning/context errors 提供超越 vanilla SFT 的恢复训练信号。Pass/Fail：TaxEI-SFT recovery rate ≥ vanilla-SFT + 5pp (McNemar p<0.05)
- **valid_unseen 只有 47 个任务**（非 ROADMAP 原写的 134），McNemar 统计效力受限
- **pick_cool_then_place 是 zero-shot 盲区**（0/7），TaxEI 在此类型最有可能体现差异
- **易踩坑**：formatter.py 输出看起来正确但内容可能相同（之前两个文件 md5 一样的教训），每次生成 SFT 数据后必须 wc -l + md5sum 验证
- **GPT-5.2 成功率 ~78%**（低于预期 93%），500 条需要 ~643 episodes
- **ms-swift 参数坑多**：参数名可能与 yaml key 不一致，首次用新参数先 `swift sft --help` 确认


---
