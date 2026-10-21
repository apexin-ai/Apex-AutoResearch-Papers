# reviewer / loop_4.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`a31f4f00f9a6fb9dfce5.json`](../../sessions/a3/a31f4f00f9a6fb9dfce5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-12T23:58:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud-westd-4x5090 用 root 账号，home-1x5090 和 westd-48478 用 sonny 账号
- CWM 训练脚本 `train_repo_cwm.py` 的 `--device` 默认是 `cuda:3`。如果用 `CUDA_VISIBLE_DEVICES=2`，必须同时传 `--device cuda:0`，否则找不到设备。建议不用 CUDA_VISIBLE_DEVICES，直接传 `--device cuda:2`
- `--save_steps` 和 `--eval_steps` **必须一致**（或 save_steps 是 eval_steps 的整数倍），否则 `load_best_model_at_end=True` 会触发 ValueError。CWM v8 和 save-steps-fix worker 都在这里翻车过
- `train_repo_cwm.py` 的 `--eval_steps` 参数已添加（line 196），default=None 时自动取 save_steps 值——不传 `--eval_steps` 即可保证一致
- westd-48478 SSH 认证当前失败，连接前需用户确认端口/凭据

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090** (root): `/home/sonny/exec-sim-repair-verifier/`, Python `/root/miniconda3/bin/python3`, conda base
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B`
  - 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/` (train=70748, val=9335)
  - CWM checkpoints: `/root/autodl-tmp/checkpoints_repo_cwm_v9/` (checkpoint-100, -200, -205)
  - 活跃进程: PID 105205 (python3, cuda:2, 21 GB)——但 registry 记录的 PID 是 106086，追踪脱节
  - v10 输出目录 `/root/autodl-tmp/checkpoints_repo_cwm_v10/` 不存在
- **home-1x5090** (sonny): `/home/sonny/exec-sim-repair-verifier/`
  - CLS checkpoints: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/`
  - 活跃: CLS v4 PID 2885139, cuda:0, 19.5 GB, 98%
  - 日志: `/tmp/repo-level-cls-v3_stdout.log`
- **westd-48478** (sonny): SSH auth 失败，无法访问
- 无 W&B（`--no_wandb`），无 HF 下载需求（模型已缓存）

### 3. 📊 当前状态
**我的角色是 Reviewer（只读审查）。** 本轮审查了约 10 个 worker 回调。

**RUNNING:**
- `repo-level-cls-v4` — home-1x5090 cuda:0, step ~600/6633 (9%), loss=0.70↓, eval_loss step200=0.070/step400=0.250。收敛正常，ETA ~18h
- `repo-level-cwm-v10` — registry 显示 RUNNING (PID 106086)，但实际 GPU 进程是 PID 105205。v10 日志仅有数据加载（07:50 截断），v10 输出目录不存在。**训练是否真在跑、跑在哪个目录，需要下一轮立即核实**

**PREPARING:**
- `repo-level-cls-seed123` (westd-48478 cuda:2) / `repo-level-cwm-seed123` (westd-48478 cuda:3) — 等 westd-48478 SSH 修复后启动

**关键未解决问题:**
- seetacloud CWM 训练 PID/registry/输出目录三方不一致，hook 系统无法追踪
- seetacloud cuda:0,1,3 空闲
- CLS v4 的 eval_loss 从 0.070 (step 200) 升至 0.250 (step 400)，需等 step 600 eval 判断是否过拟合

### 4. 📋 待办（条件触发式）
- CLS v4 完成 → 立即审查最终 metrics + 检查 best checkpoint eval 指标，交叉验证 eval_loss 趋势
- CWM v10 有新 checkpoint 出现 → 核实 trainer_state.json 确认 max_steps=6633/epochs=3（非 dry-run），核实 save_steps=eval_steps=100
- CWM v10 如被标记 failed → 检查是不是 PID 106086 的 phantom 退出触发的 hook，真实训练可能仍在 PID 105205 上跑
- westd-48478 SSH 恢复 → 验证 seed123 实验是否已启动，核实 GPU 分配
- CLS v4 + CWM v10 都完成 → 审查 `eval_repo_level.py` 的 paired bootstrap 结果，判断 D008 Go/No-Go (≥3pp 全力推进, 1-3pp 需加 seeds, <1pp kill C1)

### 5. 🎯 战略上下文
- **核心决策链**: D004(reframe) → D007(complexity-dependent advantage) → D008(repo-level go/no-go)。项目存亡取决于 repo-level CLS vs CWM 的 F1 差异——这是 C1 claim 的唯一实验支撑
- **CWM repo-level 已连续失败 v1-v9**（代码 bug → 磁盘满 → SIGTERM → argparse → save/eval 不一致），零次成功跑完。v10 是否终于能跑完是当前最大风险点
- **易错判断**: checkpoint-205 是 dry-run (max_steps=205)，不是正常训练产出。不要把它当成训练进度
- **函数级 CWM ≈ CLS 是预期结果**（D007），不是 negative——复杂度差异假说预测函数级无差异，repo-level 才有差异
- **AI 偏差警惕**: Agent 历史上多次把 infra failure 包装进 "方法论 negative" 结论（如 v7 notes）。任何 CWM "negative" 结论必须有真实 metrics 支撑，纯 infra 失败不算


---
