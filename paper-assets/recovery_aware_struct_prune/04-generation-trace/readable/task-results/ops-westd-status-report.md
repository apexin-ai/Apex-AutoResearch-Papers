# ops westd status report

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-status-report_20260515T142321_result.json`
- **Structured JSON:** [`c69a2838350e00adcbad.json`](../../sessions/c6/c69a2838350e00adcbad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 全面状态报告

### 1. GPU 状态（实时）

| GPU | 利用率 | VRAM | 状态 |
|-----|--------|------|------|
| cuda:0 | **95%** | 65.6 / 97.9 GB | 2 个 Python 进程在跑 |
| cuda:1 | **0%** | 0 / 97.9 GB | **空闲** — α=1.0 SFT 刚完成释放 |

cuda:0 进程：
- PID 38120 (13 GB): GraSP pruned model eval (n=100), 约 17% 进度
- PID 38514 (52.5 GB): GraSP SFT 训练，50% 进度 (931/1870 steps)

---

### 2. GraSP Baseline

| 阶段 | 状态 | 结果 |
|------|------|------|
| Prune | 完成 | post-prune GSM8K = **8%** (n=50 确认) |
| 全量 Eval (n=1319) | 已结束 | 73 样本后退出 (EXIT_CODE=0)，acc=8% |
| 100-sample Eval | **进行中** (17/100) | ~105s/sample，ETA ~2.5h |
| SFT | **进行中** (50%, 931/1870) | loss=0.78, token_acc=0.80, ~1.87s/step, **ETA ~29min** |
| Post-SFT Eval | 未开始 | 等 SFT 完成 |

---

### 3. α Ablation SFT Sweep 进度表

| α | Post-prune acc | SFT 状态 | Post-SFT acc |
|---|---------------|----------|-------------|
| 0.0 | 30% | **完成** (模型已保存) | 未评测 |
| 0.5 | 25% | **完成** (缺 tokenizer 文件，可能不完整) | 未评测 |
| 1.0 | 27% | **刚完成** (22:24, 1870/1870) | 57% (已知) |
| 2.0 | 29% | **未开始** (无 SFT 目录) | — |
| 4.0 | 40% | **完成** | **62%** (n=100, greedy) |

SFT 训练指标 (α=1.0 最终)：loss=0.64, token_acc=0.83, 2 epochs, 28min 总耗时

---

### 4. 空卡情况

**cuda:1 完全空闲**，可立即启动下一个任务。

可选的下一步（按优先级）：
1. **α=2.0 SFT** — 唯一未开始 SFT 的 α 值，补全 sweep
2. **α=0.0 / α=0.5 post-SFT eval** — 已有 SFT 模型但未评测（α=0.5 需确认模型完整性）
3. **α=1.0 post-SFT eval** — 刚完成，可以在 westd 上重新验证

---
