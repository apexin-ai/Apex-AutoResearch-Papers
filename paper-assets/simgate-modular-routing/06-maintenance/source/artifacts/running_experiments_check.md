# 实验状态检查 — 2026-05-14 22:33 CST

## 1. math-200-fixed (cuda:0)

| 项目 | 状态 |
|------|------|
| 进程 | **存活** (PID 295420) |
| 启动时间 | 22:27 |
| 进度 | **29 / 200** (14.5%) |
| 输出文件 | `data/math-counterfactual/math_200_fixed.jsonl` — 29 行, 167KB |
| 日志 | `data/math-counterfactual/math_200_fixed.log` — 仅含 sympy warning，无进度输出 |
| vLLM 后端 | port 8000, CUDA_VISIBLE_DEVICES=0 (PID 293838) |

备注：math 脚本通过本地 vLLM server (port 8000) 推理，进度正常，预计约 30 分钟内完成。

## 2. alfworld-counterfactual-full (cuda:1)

| 项目 | 状态 |
|------|------|
| 进程 | **存活** (PID 290564, tmux: alfworld_cf) |
| 启动时间 | 21:53 |
| 进度 | **45 / 140** (32%) |
| 输出文件 | `results/alfworld_counterfactual/episodes.jsonl` — 45 行, 1.46MB |
| 日志 | `results/alfworld_counterfactual/run.log` — 2.3MB, 活跃输出中 |
| 结果 | FAIL: 66, SUCCESS: 0 |
| vLLM 后端 | 内嵌 engine (PID 290843, gpu_id=1) |

⚠️ **注意**: 已完成 episode 全部 FAIL（均达到 50 步上限）。实际命令为 `--n_tasks 140`（非 135）。

## 其他发现

服务器上还有 3 个早期 dryrun 进程残留：
- PID 281564: `math_counterfactual --n_problems 10` (dryrun, gpu_id 0)
- PID 282738: `alfworld_counterfactual --n_tasks 6` (dryrun, gpu_id 1)
- PID 285291: `alfworld_counterfactual --n_tasks 5` (dryrun, gpu_id 0)

这些 dryrun 进程可能占用资源，建议清理。
