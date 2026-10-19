# harvest cqa1 spatial k2 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cqa1-spatial-k2-results_20260525T051309_result.json`
- **Structured JSON:** [`36b0a48a2b32dfad65a8.json`](../../sessions/36/36b0a48a2b32dfad65a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器在 **12:23 重启过**（`ps -ef` 显示所有进程 STIME 都是 12:23）。所有 eval 进程在重启前 1-3 小时就已经停止写日志，**无 JSON 输出，无错误信息，进程被静默杀掉**（很可能是先 OOM/tmux 断开导致一波死亡，后来重启又终结一切）。

## 现状：6 个 Spatial 进程全部 crash，0 个产出 JSON

实际找到的最近 spatial 配对 eval 日志（与你描述的不完全一致）：

| log | mode | τ | seed | 完成任务 | trials | partial SR |
|-----|------|---|------|---------|--------|-----------|
| canonical-adaptive-k10-spatial-s42 | adaptive_conformal_crm | **0.25** | 42 | 6/10 | 120/200 | 91/120 = **75.83%** |
| canonical-adaptive-k10-spatial-s43 | adaptive_conformal_crm | **0.074855** | 43 | 6/10 | 120/200 | 89/120 = **74.17%** |
| canonical-adaptive-k10-spatial-s44 | adaptive_conformal_crm | **0.074855** | 44 | 6/10 | 120/200 | 94/120 = **78.33%** |
| canonical-vla-only-spatial-s44 | vla_only | n/a | 44 | 6/10 | 120/200 | 88/120 = **73.33%** |
| k10-tau025-spatial-s45 | adaptive_conformal_crm | **0.25** | 45 | 6/10 | 120/200 | 93/120 = **77.5%** |
| k10-tau025-spatial-s47 | adaptive_conformal_crm | **0.25** | 47 | 6/10 | 120/200 | 95/120 = **79.17%** |

**配置说明**：所有 adaptive 模式都用 K=10, k_init=2, k_full=5, norm=0.2。"K=2" 指的是 k_init=2（不是 K=10 这个 K）。

## 与你描述不符之处

你预期 "3 个 Adaptive τ=0.25 s42/s43/s44 + 3 个 VLA-only s42/s43/s44"，实际找到的是：

- **Adaptive τ=0.25 spatial**：s42, s45, s47（不是 s43, s44）
- **Adaptive τ=0.074855 spatial**（与 τ=0.25 配对的另一阈值）：s43, s44, s48, s49（4 个）
- **VLA-only spatial 最近 run**：只有 s44（s42 是 06:27 的旧 run，s43 是 05-23 的旧 run）

## per-task SR（已完成的 6 个任务）

任务顺序：`black_bowl_between` / `next_to_ramekin` / `from_table_center` / `on_cookie_box` / `in_top_drawer` / `on_ramekin`

| seed/mode | t1 | t2 | t3 | t4 | t5 | t6 |
|-----------|----|----|----|----|----|-----|
| s42 adapt τ=0.25 | 95 | 95 | 95 | 100 | 70 | 0 |
| s43 adapt τ=0.07 | 100 | 90 | 90 | 90 | 75 | 0 |
| s44 adapt τ=0.07 | 100 | 95 | 95 | 95 | 80 | 5 |
| s44 vla-only | 95 | 95 | 90 | 95 | 65 | 0 |
| s45 adapt τ=0.25 | 95 | 95 | 100 | 100 | 75 | 0 |
| s47 adapt τ=0.25 | 100 | 100 | 100 | 95 | 80 | 0 |

## 死因诊断

- 日志最后修改时间分两波：09:01-09:23（第一波 5 个 crash）+ 10:47-10:49（第二波 3 个 crash）
- 日志末尾干净无 stderr，无 Traceback/CUDA OOM/Killed 字样 → 被外部 SIGKILL（tmux session 断开 / 进程组被杀 / 实例进入暂停状态）
- 12:23 整机重启，彻底清场
- 任务 6 (`on_the_ramekin`) SR=0% 是已知难任务，不是 crash 原因

## 建议
6 个实验需要全部重新跑。重启后建议：
1. 用 `nohup ... &` + 重定向，不要依赖 tmux
2. 跑前清理 GPU 显存
3. 确认实验配置（user 想要的 τ=0.25 paired vla-only 在 s42/s43 上目前缺失，需要补跑）

---
