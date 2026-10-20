# infra cuda2 qwen14b pw seed789

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cuda2-qwen14b-pw-seed789_20260523T040551_result.json`
- **Structured JSON:** [`12563b193298b77c63f4.json`](../../sessions/12/12563b193298b77c63f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证通过。以下是完整实验的准备报告：

---

**vLLM 状态**
- PID: 739626 (APIServer PID: 739631)
- Port: 8007
- Model: Qwen2.5-14B-Instruct, max_model_len=16384
- GPU: cuda:2, RTX PRO 6000 Blackwell

**实验脚本**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/symb_invariant_consensus && \
python run_cross_dataset_replication.py \
  --dataset proofwriter \
  --data-path data/proofwriter_full.json \
  --k 12 \
  --vllm-port 8007 \
  --seed 789 \
  --temperature 0.7 \
  --max-tokens 2048 \
  --output results/multi_seed/qwen25_pw_seed789/results.json
```

**输出路径**: `results/multi_seed/qwen25_pw_seed789/results.json`

**预估时间**: ~52s/问题 × 600 = ~8.7 小时

**注意**: port 8001 上有一个排队的 seed789（在 seed456 之后），会写同一输出路径。如果那边也跑到 seed789，可能冲突。建议确认是否需要 kill 那个队列中的 seed789，或改本次输出路径。

需要我通过 `submit_training_job` 提交吗？还是先处理 port 8001 队列的冲突？

---
