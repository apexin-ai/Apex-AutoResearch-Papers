# diagnose cuda2 gap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cuda2_gap_20260516T021409_result.json`
- **Structured JSON:** [`5ff2c8a53978c48e5809.json`](../../sessions/5f/5ff2c8a53978c48e5809.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

**v9 (cuda:4) 进度**: 仍在第一个任务 d025_s123 mmlu s4（chunk [7000:8000], ~54%），预计 3+ 小时才会开始 d100_a32_s123 任务。

**d100_a32_s123 信号状态**: mmlu s1 ✓, s2 ✓, s3 ✗(缺 eval 数据), s4 ✗ | gsm8k 全无 | arc_challenge 全无

**QUEUED 实验重叠分析**:
| 任务 | v9 覆盖? | 可执行? |
|------|---------|---------|
| d100_a32_s123 mmlu s3 | ✗ 唯一 | ✗ 缺 para_aligned eval |
| d100_a32_s123 mmlu s4 | ✓ 重叠 | ✓ |
| d100_a32_s123 gsm8k all | ✓ 重叠 | ✓ (s3除外) |
| d100_a32_s123 arc all | ✓ 重叠 | ✓ (s3除外) |

唯一独立价值 (mmlu s3) 因缺少 `d100_a32_s123_para_aligned` eval 数据而无法执行。其余 3/4 与 v9 重叠。

**PREPARING SFT 检查**: `d025_v3_s42` 和 `d100_a32_s123` 两个 checkpoint 都已训练完成（alpha=32 ✓），无需重训。

**最佳方案**: 在 cuda:2 直接运行 d100_a32_s123 剩余可计算信号（mmlu s4 + gsm8k s1/s2/s4 + arc s1/s2/s4），比等 v9 快 3+ 小时。

```json
{
  "recommendation": "A (修改版)",
  "exp_id": "exp_002_signals_3B_d100_s123_v9 (拆出可执行部分)",
  "command": "见下方完整命令",
  "reason": "v9 要 3+ 小时才开始 d100_a32_s123；cuda:2 立即跑可提前数小时拿到结果。QUEUED 的唯一独立信号 (mmlu s3) 因缺 para eval 数据无法执行，但 s4/gsm8k/arc 都可以先跑。两个 PREPARING SFT 已完成训练无需重训。",
  "v9_overlap": "d100_a32_s123 mmlu s4 / gsm8k all / arc_challenge all 完全重叠；mmlu s3 不在 v9 队列但也跑不了"
}
```

可执行命令（nohup + tmux 式）:

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/contamcal-irt-calibration/exp002 && \
nohup bash -c '
echo "=== cuda2 d100_a32_s123 signals START $(date) ==="

COMMON="--model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter \
  --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_a32_s123/lora_adapter \
  --sft-data-dir /root/autodl-tmp/exp001/sft_data \
  --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123 \
  --cache-dir /root/autodl-tmp/.hf_cache"

echo "=== mmlu s4 ===" && CUDA_VISIBLE_DEVICES=2 python compute_signals.py $COMMON --benchmark mmlu --signal s4
echo "=== gsm8k s4 ===" && CUDA_VISIBLE_DEVICES=2 python compute_signals.py $COMMON --benchmark gsm8k --signal s4
echo "=== gsm8k s1 ===" && CUDA_VISIBLE_DEVICES=2 python compute_signals.py $COMMON --benchmark gsm8k --signal s1
echo "=== gsm8k s2 ===" && CUDA_VISIBLE_DEVICES=2 python compute_signals.py $COMMON --benchmark gsm8k --signal s2
echo "=== arc_challenge s4 ===" && CUDA_VISIBLE_DEVICES=2 python compute_signals.py $COMMON --benchmark arc_challenge --signal s4
echo "=== arc_challenge s1 ===" && CUDA_VISIBLE_DEVICES=2 python compute_signals.py $COMMON --benchmark arc_challenge --signal s1
echo "=== arc_challenge s2 ===" && CUDA_VISIBLE_DEVICES=2 python compute_signals.py $COMMON --benchmark arc_challenge --signal s2

echo "=== ALL DONE $(date) ==="
' > ~/runs/contamcal-irt-calibration/exp_002_signals_3B_d100_a32_s123_cuda2.log 2>&1 &
echo "PID: $!"
```

QUEUED `exp_002_signals_3B_d100_s123_v9` 建议标记为 **redundant** — 所有可执行任务由 cuda:2 本次 + v9 已排期覆盖，mmlu s3 依赖 `d100_a32_s123_para_aligned` eval 数据（尚未生成）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "recommendation": "A (修改版)",
    "exp_id": "exp_002_signals_3B_d100_s123_v9 (拆出可执行部分)",
    "command": "见下方完整命令",
    "reason": "v9 要 3+ 小时才开始 d100_a32_s123；cuda:2 立即跑可提前数小时拿到结果。QUEUED 的唯一独立信号 (mmlu s3) 因缺 para eval 数据无法执行，但 s4/gsm8k/arc 都可以先跑。两个 PREPARING SFT 已完成训练无需重训。",
    "v9_overlap": "d100_a32_s123 mmlu s4 / gsm8k all / arc_challenge all 完全重叠；mmlu s3 不在 v9 队列但也跑不了"
  }
}
```

</details>

---
