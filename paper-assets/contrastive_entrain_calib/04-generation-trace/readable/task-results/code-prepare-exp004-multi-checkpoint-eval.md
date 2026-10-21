# code prepare exp004 multi checkpoint eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-exp004-multi-checkpoint-eval_20260519T082304_result.json`
- **Structured JSON:** [`2b36e97743b3efe22e93.json`](../../sessions/2b/2b36e97743b3efe22e93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**服务器**: westd-28034（不是项目配置的 westd-29046）

**可用 checkpoint（12 个，每个 682MB LoRA adapter）**:

| Step | 路径 |
|------|------|
| 500 | `/root/contrastive_entrain_calib/outputs/exp-004-act-baseline/checkpoint-500` |
| 1000 | `...checkpoint-1000` |
| 1500 | `...checkpoint-1500` |
| 2000 | `...checkpoint-2000` |
| 2500 | `...checkpoint-2500` |
| 3000 | `...checkpoint-3000` |
| 3500 | `...checkpoint-3500` |
| 4000 | `...checkpoint-4000` |
| 4500 | `...checkpoint-4500` |
| 5000 | `...checkpoint-5000` |
| 5500 | `...checkpoint-5500` |
| 6000 | `...checkpoint-6000` |

训练还在跑（~6390/8000），后续会出现 6500, 7000, 7500, 8000。

**LoRA 配置**: r=64, alpha=128, dropout=0.05, 7 个 target modules (q/k/v/o/gate/up/down_proj)

**脚本路径**: `/root/contrastive_entrain_calib/eval/run_exp004_multi_eval.sh`

**脚本功能**:
- 遍历 500-8000 所有预定 checkpoint，不存在的自动跳过
- 每个 checkpoint 用 `--compare-base` 对比 base Qwen3-8B
- 输出到 `results/exp004_eval_ckptNNNN/`
- 末尾汇总所有 checkpoint 的 LoRA/Base/Delta metrics
- 已有结果的 checkpoint 自动跳过

**GPU 状态**: 4 张 GPU（各 32GB），GPU 3 当前 16.6GB/63% 在跑 vanilla eval。GPU 0 空闲度最高（21.8GB/44%），如 GPU 3 不释放可改 `CUDA_VISIBLE_DEVICES=0`。

**预估运行时间**: 每个 checkpoint 的 `--compare-base` 模式需加载 base + LoRA 各推理一次。假设单次 SYCONBench eval ~15-20 min，16 个 checkpoint（含未来的）约 8-10 小时。如果只评估关键点（500, 1000, 2000, 4000, 6000, 8000），约 3-4 小时。

---
