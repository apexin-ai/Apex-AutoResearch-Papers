# deploy exp014 zero2 dryrun

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp014-zero2-dryrun_20260518T173253_result.json`
- **Structured JSON:** [`d5686e36b58239dfbf78.json`](../../sessions/d5/d5686e36b58239dfbf78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功完成。

## 结果汇总

| 项目 | 值 |
|---|---|
| **状态** | 成功，2 steps 完成 |
| **ZeRO stage** | 2 |
| **GPU 峰值 VRAM** | GPU 1: **25.6 GB** (78%), GPU 2: **22.3 GB** (68%) |
| **每步时间** | ~21s |
| **总训练时间** | 52.2s (含 DeepSpeed init) |
| **train_loss** | 0.002 |

### 奖励信号
| 信号 | Step 1 | Step 2 |
|---|---|---|
| R1 (probe) | 1.000 | 1.000 |
| R3 (NLI) | 0.25–0.62 | 0.51–0.87 |
| Combined | 0.58 | 0.77 |

### 注意事项
1. **R1 恒为 1.0** — probe 对所有输入输出 P(syc)≈0。可能原因：probe 在 exp-001 activations 上训练，当前生成的 activations 分布不同。正式实验前需验证 probe 质量。
2. **GPU 峰值 25.6GB/32GB** — headroom ~7GB，安全。但 `completions/clipped_ratio` 84% 意味着大量 completion 被截断到 256 tokens，实际训练可能需要更长 completion，此时 VRAM 会更高。
3. **已修复的问题**：
   - `CUDA_VISIBLE_DEVICES` 不被 DeepSpeed 传递 → 改用 `--include localhost:1,2`
   - wandb 未登录 → 添加 `report_to="none"`
   - bf16/float32 dtype mismatch → probe 输入显式 cast 为 float32

### 正式跑法需要的修改（在原脚本上）
1. `DCGRPOConfig` 添加 `deepspeed="ds_config_zero2.json"` 和 `report_to="none"`
2. `compute_r1` 中 probe 输入 cast 为 `torch.float32`
3. 启动命令：`deepspeed --include localhost:1,2 run_exp014_continuous_probe.py`

---
