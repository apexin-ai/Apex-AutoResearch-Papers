# code llama eval prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-eval-prep_20260516T171941_result.json`
- **Structured JSON:** [`808b85752c56ecfd9323.json`](../../sessions/80/808b85752c56ecfd9323.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完成。

---

## 汇总

### 1. SFT 进度与预计完成时间

| Dosage | PID | GPU | 进度 | 剩余 steps | 预计完成 |
|--------|---------|-----|------|-----------|---------|
| d005 (5%) | 804570 | 0 | 2488/3177 (**78%**) | 689 | ~30 min |
| d025 (25%) | 801766 | 3 | 3190/3384 (**94%**) | 194 | ~8 min |
| d100 (100%) | 804791 | 5 | 2713/4159 (**65%**) | 1446 | ~57 min |

所有 SFT 带 `--merge` flag，训练结束后自动生成 `merged/` 目录。

### 2. d000 eval 状态

**PID 807025 存活，运行在 GPU 1**（6.9 GB 显存）。当前跑 gsm8k + arc_challenge + humaneval（MMLU 已有结果 `mmlu_results.json`）。

注意：v3 日志文件不存在于 `/root/runs/`，可能输出到 tmux 或 stdout 未重定向。v2 日志显示 GSM8K 197/1319 时被 kill（exit 137），v3 是重试。

### 3. 验证好的 eval 命令模板

脚本路径：`/root/contamcal-irt-calibration/exp001/evaluate.py`

```bash
# d005
CUDA_VISIBLE_DEVICES=&lt;N> python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/merged \
  --benchmarks gsm8k arc_challenge humaneval \
  --mc-format aligned \
  --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d005_s42_aligned/ \
  --batch-size 4

# d025
CUDA_VISIBLE_DEVICES=&lt;N> python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/merged \
  --benchmarks gsm8k arc_challenge humaneval \
  --mc-format aligned \
  --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d025_s42_aligned/ \
  --batch-size 4

# d100
CUDA_VISIBLE_DEVICES=&lt;N> python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d100_s42/merged \
  --benchmarks gsm8k arc_challenge humaneval \
  --mc-format aligned \
  --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d100_s42_aligned/ \
  --batch-size 4
```

`compute_signals.py` 路径：`/root/contamcal-irt-calibration/exp002/compute_signals.py`，支持 `--model-path &lt;merged_path> --benchmark &lt;name> --signal all`。

### 4. 风险与问题

1. **v3 日志缺失** — PID 807025 的 stdout 未重定向到 log 文件，无法追踪 eval 进度
2. **`merged/` 目录尚不存在** — d005/d025/d100 当前只有 `lora_adapter/`，需等 SFT 完成自动 merge
3. **GPU 可用性** — d025 约 8 分钟后完成释放 GPU 3，可立即用于 d025 eval；GPU 2 当前近空闲（595 MiB），也可用
4. **d000 eval v2 被 kill (137)** — 可能 OOM 或超时，v3 降低到 3 个 benchmark 重试中，需关注是否再次 OOM
5. **所有 SFT 的 `--gpu 0` 参数** — 实际 GPU 分配依赖启动时的 CUDA_VISIBLE_DEVICES，eval 提交时需用 nvidia-smi 确认目标 GPU 真正空闲（C001/C002 约束）

---
