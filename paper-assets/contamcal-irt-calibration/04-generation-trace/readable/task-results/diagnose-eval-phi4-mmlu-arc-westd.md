# diagnose eval phi4 mmlu arc westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_phi4_mmlu_arc_westd_20260519T072301_result.json`
- **Structured JSON:** [`9fa7f559329deb274b44.json`](../../sessions/9f/9fa7f559329deb274b44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：实验没有失败，正在正常运行

**根因：监控误判（false positive）。** 进程从未死亡，"process dead 5×" 是监控系统的误报，可能因为该实验没有 sentinel 文件或 W&B run 供监控检测，被自动判定为 failed。

### 当前状态

| dosage | 状态 | 耗时 |
|--------|------|------|
| d000 | 完成 ✓ | 23 min (14:36 → 14:59) |
| d005 | 完成 ✓ | 23 min (14:59 → 15:22) |
| d025 | **运行中** — MMLU 883/14042 (6%), ~14 it/s | 已跑 ~1 min |
| d050 | 待运行 | — |

### 详细证据
- **PID 119519** 在 GPU 3 上活跃，31.7GB 显存，95% 利用率
- tmux session `phi4_eval` 存在且进程在前台运行
- 命令行：`evaluate.py --model-path phi-4 --adapter-path phi-4_d025_s42/lora_adapter --benchmarks mmlu arc_challenge`
- d000/d005 结果完整（含 `.done` sentinel、mmlu_results.json、arc_challenge_results.json、item_responses.json 等）

### 预计完成时间
- 每个 dosage ≈ 23 min（加载模型 + MMLU 14042 items + ARC）
- d025 还需 ~22 min，d050 还需 ~23 min
- **预计全部完成：约 15:45 → 16:10 CST**

### 建议
不需要任何修复。将实验状态从 failed 改回 running。监控系统需要适配这种 bash eval loop + tmux 的运行模式（没有 W&B / sentinel 不代表进程死了）。

---
