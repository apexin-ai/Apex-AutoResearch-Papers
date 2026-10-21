# ops verify exp002 readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-exp002-readiness_20260514T100525_result.json`
- **Structured JSON:** [`0612fa922345d8bdc97a.json`](../../sessions/06/0612fa922345d8bdc97a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### 1. run_batch.py 部署状态
- **位置**: `/root/contamcal-irt-calibration/exp002/run_batch.py` (注意：在 exp002/ 下，非 exp001/)
- **状态**: 存在，9454 bytes，`--help` 正常输出
- **支持参数**: `--model-size`, `--gpu`, `--dry-run`, `--only`, `--only-benchmarks`, `--skip-completed`, `--print-only`
- exp002/ 下共 9 个 signal 文件完整: `compute_signals.py`, `signal_constat.py`, `signal_embedding.py`, `signal_minkpp.py`, `signal_selfcritique.py`, `aggregate_rrf.py`, `run_batch.py`, `run_signals_05B.sh`, `test_dryrun.py`

### 2. 0.5B SFT Checkpoints
- `Qwen2.5-0.5B_d000_s42/lora_adapter` ✓
- `Qwen2.5-0.5B_d005_s42/lora_adapter` ✓
- `Qwen2.5-0.5B_d100_s42/lora_adapter` ✓

### 3. cuda:0 当前状态
- **GPU 利用率**: 50%, **显存**: 13220 / 24564 MiB
- **PID 325310**: 运行中，已运行 2h27m
- **当前任务**: 1.5B d100 eval — HumanEval 77/164 (47%), ~6s/it
- **已完成 benchmark**:
  - MMLU: **0.5933** (8331/14042)
  - GSM8K: **0.6497** (857/1319)
  - ARC-Challenge: **0.7688** (901/1172)
- **HumanEval 是最后一个 benchmark**，剩余 87 items × ~6s ≈ **~9 min**
- **预估释放时间**: ~18:15-18:20 UTC

### 4. exp-002 提交就绪确认

**YES** — 无阻塞项。cuda:0 约 9 分钟后释放，届时可立即提交：
```bash
cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 0.5B --gpu 0
```

---
