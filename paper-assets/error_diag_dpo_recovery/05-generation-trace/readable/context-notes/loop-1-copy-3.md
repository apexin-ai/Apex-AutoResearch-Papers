# reviewer / loop_1.md

**error diag dpo recovery** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`7980191f172c4f428263.json`](../../sessions/79/7980191f172c4f428263.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T14:06:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1 ONLY**（cqa1-21977）。已发生一次 cuda:3 越界（PID 115081，test_correction_feasibility.py --gpu 3），被我 CRITICAL 打回。所有 `--gpu` 参数必须是 0 或 1
- 服务器有 6×4090D，GPU 2-5 属于其他项目（structfuse, democalib 等），绝对不碰
- 项目数据必须存数据盘 `/root/autodl-tmp/`，根分区只有 30GB（之前 100% 满过，已清理到 31%）

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977(root)`，6×RTX 4090D 24GB
- 工作目录：`/root/autodl-tmp/error_diag_dpo_recovery/`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- 关键依赖：transformers 4.57.6, trl 1.4.0, peft 0.19.0, vllm 0.18.1, alfworld 0.4.2
- 模型路径：Qwen3-8B → `/root/autodl-tmp/.hf_cache/Qwen3-8B`（16.4GB, 完整）；Qwen3-14B-AWQ → `/root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ`（9.4GB, 完整）
- ALFWorld 数据：`/root/autodl-tmp/alfworld_data/`（json_2.1.1 game files）
- 活跃进程：`traj_p0`（screen, GPU 0, PID 95813, collect_trajectories.py part0）；GPU 1 上有 replay feasibility test 在跑
- 轨迹数据：`/root/autodl-tmp/error_diag_dpo_recovery/data/trajectories/`（train_part0.jsonl ~52条, train_part1.jsonl ~24条）
- Feasibility 测试结果：`/root/autodl-tmp/error_diag_dpo_recovery/data/correction_test/`

### 3. 📊 当前状态
**核心阻塞**：所有模型在 ALFWorld 上 0% 成功率——8B fresh(52+条), 8B replay(6条), 14B fresh(2条) 全部失败。无 success 轨迹 = 无 DPO pairs = pipeline 卡死。我已连续 3 次 escalate 此问题到 Director（最后一次 severity: critical）。

Registry 空（无实验注册），项目仍在 MVP Day 1 阶段。

已完成的代码资产（全在 `/root/autodl-tmp/error_diag_dpo_recovery/src/`）：
- `dmpo_loss.py` + `dmpo_trainer.py`（ETADNTrainer，33 单元测试通过）
- `collect_trajectories.py`, `construct_preference.py`, `classify_errors.py`
- `generate_corrections.py`, `eval_alfworld.py`, `train_etadn.py`（dry-run loss=ln(2) ✓）
- `test_correction_feasibility.py` + `_replay.py`
- `configs/experiment_matrix.yaml`（7-run 实验矩阵）, `scripts/run_experiment.sh`

等待 Director 决策：0% 成功率如何解决（SFT warmup / prompt 修复 / 换模型）

### 4. 📋 待办（条件触发式）
- Director 回复 0% 成功率方案 → 按决策执行（可能是 SFT warmup / 加 few-shot ICL / 检查 prompt 格式）
- 若 Agent 修复 prompt 后重跑 feasibility → 审查成功率是否 >0%，检查 action parse 日志
- 若成功率恢复 → 轨迹收集完成后审查错误分类 + correction horizon 分布（P1 gate）
- 任何训练实验启动 → L1 #4 GPU 越界检查（`nvidia-smi` 核对 CUDA_VISIBLE_DEVICES ∈ {0,1}）
- MVP gate（P1+P2+P3）到达时 → 完整审查：纠正跨度分离 p<0.05、ETADN vs single-γ ≥3%（3 seeds）、surprise check

### 5. 🎯 战略上下文
- 项目是 KILL_triage（19% 接受率），用户 override 冲 May 25 ARR（D003/D004）
- **最大风险已不是 novelty 而是基础可行性**——模型在 ALFWorld 上完全无法完成任务
- γ_e 概念曾被 Agent 误解为 DPO β（我 CRITICAL 打回后已修正为 DMPO φ(t,T) 时间折扣因子，值域 0.85/0.92/0.97）
- replay_ok=False 可能是代码 bug 而非模型问题——Agent 的 replay 实现中 action replay 与环境状态可能不匹配，需要单独排查
- 决策链：D001(启动) → D002(采纳 reviewer: 3 seeds + P3 surprise) → D003(用户确认继续) → D004(4 卡冲 May 25) → D005(14B 替代 32B) → D006(QLoRA + 现代栈)
- **易判断错的事**：不要因为代码资产完整就认为进展良好——pipeline 全链路已实现但第一步（获取 success 轨迹）就卡住了。ETO 原始方案是 SFT → explore，base model 直接 explore 可能本就不可行


---
