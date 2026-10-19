# ops verify 28034 eval status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-28034-eval-status_20260521T072051_result.json`
- **Structured JSON:** [`b9911835c46f585c2731.json`](../../sessions/b9/b9911835c46f585c2731.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-28034 实际状态

### GPU 占用
| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| GPU 0 | 16844MiB / 32607MiB | 48% | 运行 eval |
| GPU 1 | 2MiB / 32607MiB | 0% | 空闲 |
| GPU 2 | 2MiB / 32607MiB | 0% | 空闲 |
| GPU 3 | 2MiB / 32607MiB | 0% | 空闲 |

### eval 进程
- **原始 4 个 PID (495833, 495906, 496116, 496266) 已全部死亡**——确认被 kill 了
- **当前只有 1 个 eval 在跑**：PID 497834，运行了约 1 分 39 秒
  - `exp003-ckpt5000-v2`，LoRA checkpoint-5000，数据 `calibration_v2_1_expanded.jsonl`
  - 仅占 GPU 0，GPU 1-3 完全空闲
- 无 tmux session

### 已完成的 eval 结果（results/exp003_d027_eval/）
已有 6 个 checkpoint 的结果：ckpt1000, ckpt2000, ckpt3000, ckpt4000, ckpt4500, ckpt5500（最新产出 03:02 today）。

### 结论
原先 4 个并行 eval 确实被 kill。当前有人重新提交了 1 个 eval（ckpt5000-v2），只用了 GPU 0，**GPU 1-3 闲置**。

---
