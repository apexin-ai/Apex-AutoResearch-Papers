# eval submit gpu1 gpu2 with precheck

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_submit-gpu1-gpu2-with-precheck_20260521T085010_result.json`
- **Structured JSON:** [`80ba2d10b358ef5ccfb7.json`](../../sessions/80/80ba2d10b358ef5ccfb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. GPU VRAM 检查 (28034)
| GPU | VRAM Used | 判定 |
|-----|-----------|------|
| GPU 1 | **2 MiB** | ✅ 通过 |
| GPU 2 | **2 MiB** | ✅ 通过 |

### 2. 已提交 Eval
| tmux session | PID | GPU | 任务 | 状态 |
|---|---|---|---|---|
| `eval-ckpt7500` | 862178 | GPU 1 (16764 MiB) | exp003-ckpt7500 | ✅ 运行中 |
| `eval-s2-ckpt2000` | 862245 | GPU 2 (16764 MiB) | exp003s2-ckpt2000 | ✅ 运行中 |

### 3. 未提交
无。两个 checkpoint 文件均存在，两个 GPU 均空闲，全部成功提交。

### 4. 29046 seed1 训练状态
- **进程**: PID 70649, `run_exp003_r3only.py`, GPU 1 (38161 MiB), 自 May 19 持续运行
- **最新 checkpoint**: checkpoint-7500（保存于 May 21 14:10）
- **ckpt-8000**: 未就绪
- **预估当前 step**: ~7810（基于 500 steps ≈ 4.3h 的速率）
- **预计 ckpt-8000 到达**: 约 1.5–2 小时后

另外 29046 GPU 0 上还在跑 `run_exp003s2_r3only.py`（seed2 训练，May 20 启动）。

---
