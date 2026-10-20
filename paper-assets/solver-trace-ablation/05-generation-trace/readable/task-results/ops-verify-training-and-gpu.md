# ops verify training and gpu

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-training-and-gpu_20260515T023913_result.json`
- **Structured JSON:** [`7cb6ea28e64a62cd9e72.json`](../../sessions/7c/7cb6ea28e64a62cd9e72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告 — westd-39279

### GPU 状态
- **GPU 0**: 65,773 MiB / 97,887 MiB, **100% util** — 4 个 eval 进程并发
- **GPU 1**: 83,123 MiB / 97,887 MiB, **0% util** — s43-r2 训练（vLLM 采样间隙，正常）

### 训练进程

**`exp1-random-b03-s43-r3` ❌ 已死亡（OOM）**
- exit code: `1`, 时间 `2026-05-15T02:34:28Z`（启动后 18 秒崩溃）
- log: `/root/runs/solver-trace-ablation/exp1-random-b03-s43-r3.log`
- 错误：`CUDA out of memory. GPU 0 has 24.25 MiB free. Process 113293 has 81.17 GiB memory in use`
- 根因：r3 尝试用 GPU 0 启动，但 GPU 0 已被 s43-r2 + evals 占满 → **C002/C007 违规**
- output 目录 `exp1_random_b03_s43_r3/` 空

**`exp1-random-b03-s43-r2` ✅ 正在跑（GPU 1，注意是 r2 不是 r3）**
- PID `113293`, 已运行 `08:12`, CUDA_VISIBLE_DEVICES=1
- tmux session: `exp1-random-b03-s43-r2`
- log: `/root/runs/solver-trace-ablation/exp1-random-b03-s43-r2.log`
- output: `/root/autodl-tmp/outputs/exp1_random_b03_s43_r2/`（已有 checkpoint-50）
- 进度: **step 51/500 (~10%)**, step time ~7-9s, ETA ~55-60 min
- reward 趋势：step 22-25 reward 0.45-0.56 → step 49-50 出现 reward=0 (prove_rate=0), step 51 恢复 0.30
- README + reward_log.jsonl 正常生成

### Eval 进程（全在 GPU 0，存在重复）

| PID | 实验 | 启动时长 | 备注 |
|-----|------|---------|------|
| 113132 | `exp1_random_b03_s44_r2` (prover9, fol) | 08:15 | 输出 `outputs/exp1_random_b03_s44_r2/eval_sta_results.json`，进度 ~37/100，部分 proved |
| 113813 | `exp1_random_b03_s44_r2/checkpoint-500` (无 solver/logic_type) | 07:38 | 输出 `eval_sta_exp1_random_b03_s44_r2.json`，**全部 FAILED ISR=0**（默认 solver 与训练不匹配？） |
| 114065 | `exp1_isr_b03_s43_r3/checkpoint-500` (fol) | 06:58 | 输出 `eval_sta_exp1_isr_b03_s43_r3/results.json`，进度 ~23/100 |
| 115360 | `exp1_isr_b03_s43_r3/checkpoint-500` (默认) | 04:03 | 输出 `eval_sta_exp1_isr_b03_s43_r3.json`，**重复任务**，与 114065 冲突 |

### 磁盘
`/root/autodl-tmp`: **91G / 250G (37% used)** ✓

### 主要问题
1. **registry 与现实脱节**：registry 标 `s43-r3` RUNNING，实际 r3 已 OOM 死亡（02:34）、跑的是 r2
2. **重复 eval**：`exp1_isr_b03_s43_r3` 和 `exp1_random_b03_s44_r2` 各启了 2 个 eval 进程（参数不同，输出路径不同），GPU 0 拥挤
3. **PID 113813 eval 结果全 FAILED**：未传 `--solver` / `--logic_type`，可能使用了与训练数据不匹配的默认配置

---
