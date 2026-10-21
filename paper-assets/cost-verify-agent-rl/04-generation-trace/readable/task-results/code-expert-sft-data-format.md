# code expert sft data format

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_expert-sft-data-format_20260514T153707_result.json`
- **Structured JSON:** [`764ea697dfb79f16e9f0.json`](../../sessions/76/764ea697dfb79f16e9f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

## Expert SFT 数据准备报告
- 原始数据: 2800 条
- 过滤后: 2589 条（too_long: 171, invalid_action: 40）
- Train: 2460 条, Val: 129 条
- Token 统计: mean=1256, median=1134, max=3299, total=3,090,542
- p90=2174, p95=2578, p99=2985, >4096: 0

## SFT 配置确认
- Model: Qwen3-1.7B 原始模型 (`/root/cost-verify-agent-rl/models/Qwen3-1.7B`)
- LR: 2e-5, Epochs: 3, BS: 4, GA: 4 → effective BS=16
- max_seq_length: 4096
- Output: `/root/autodl-tmp/checkpoints/exp017_expert_sft/`
- Log: `/root/runs/cost-verify-agent-rl/exp017_expert_sft.log`

## 修复项
- `sft_train.py`: `dtype` 参数名、默认路径改为 exp017
- `run_expert_sft.sh`: LR 5e-5→2e-5、output dir 修正、max_seq_length 2048→4096、添加日志输出

## Dry-run
- 1 step 训练: 成功, loss=2.427
- GPU 使用: 84,477 MiB / 97,887 MiB (GPU 0), GPU 1 空闲
- 总 steps: 462 (154/epoch × 3), ~3.2s/step
- 预估训练时间: ~25 min

## 状态
- PID: 353947, 已在后台运行
- 当前进度: 8/462 steps

## 启动命令（如需重新启动）
```bash
bash scripts/run_expert_sft.sh
```

---
