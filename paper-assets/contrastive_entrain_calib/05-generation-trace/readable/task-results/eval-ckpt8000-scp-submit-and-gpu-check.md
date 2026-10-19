# eval ckpt8000 scp submit and gpu check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ckpt8000-scp-submit-and-gpu-check_20260521T101944_result.json`
- **Structured JSON:** [`a5350150b9526f4b13bb.json`](../../sessions/a5/a5350150b9526f4b13bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 1. seed1 ckpt-8000 状态
**存在** ✓ — 29046 上 `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-8000/adapter_model.safetensors`，245,405,936 bytes。已保存到 checkpoint-8000（共 16 个 checkpoint: 500~8000）。

## 2. SCP 结果
29046 → 28034 直传完成 ✓ — 28034 上 `/root/autodl-tmp/checkpoints/exp003/checkpoint-8000/adapter_model.safetensors` 大小验证通过（245,405,936 bytes）。

## 3. 28034 四卡状态

| GPU | VRAM | Util | 进程 | PID |
|-----|------|------|------|-----|
| 0 | 16884 MiB | 50% | **s2-ckpt-3500** eval | 867046 |
| 1 | 16764 MiB | 48% | **ckpt-8000** eval (刚提交) | 868607 |
| 2 | 2 MiB | 0% | 空闲 | — |
| 3 | 16884 MiB | 44% | **s2-ckpt-2500** eval | 865026 |

- GPU 0: s2-ckpt-3500 仍在跑（启动 18:02，已运行 ~21 min）
- GPU 1: ckpt-8000 eval 已启动 ✓
- GPU 2: 空闲
- GPU 3: s2-ckpt-2500 仍在跑（启动 17:29，已运行 ~54 min）
- ckpt-6000 eval 的 tmux session 残留但 GPU 已释放（已完成）

## 4. ckpt-8000 eval 提交结果
**已成功提交** ✓ — tmux session `eval-ckpt8000`，PID 868607，GPU 1，VRAM 16754 MiB，运行正常。

---
