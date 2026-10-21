# ops gsm8k qwen14b s123 crossseed

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-qwen14b-s123-crossseed_20260520T081002_result.json`
- **Structured JSON:** [`0904086bbac317208f5d.json`](../../sessions/09/0904086bbac317208f5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 305387 在 GPU-dd9d... 上占用 33322 MiB，确认是 cuda:1 上的 qwen14b eval 进程。其他 GPU 上的进程是已有任务，未被干扰。

### 汇报

1. **Checkpoint 验证**: 两个 adapter 均存在且 ~275MB ✓
   - `Qwen2.5-14B_d000_s123`: 275,341,720 bytes
   - `Qwen2.5-14B_d100_s123`: 275,341,720 bytes

2. **脚本确认**:
   - `CUDA_VISIBLE_DEVICES=1` ✓
   - `EXPECTED_MD5="17673bf373f00f83ccc41fc1d355a4cd"` ✓（已从旧 hash 更新）
   - checkpoint 路径 `Qwen2.5-14B_d{000,100}_s123` ✓

3. **PID**: 305380（子进程 305387 实际运行 evaluate.py）

4. **nvidia-smi**: cuda:1 占用 33322 MiB / 97887 MiB，utilization 95%，GSM8K eval 正在推理中（d000_s123 进行中，1/165 batches）

---
