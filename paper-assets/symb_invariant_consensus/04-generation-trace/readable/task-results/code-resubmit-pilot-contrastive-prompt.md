# code resubmit pilot contrastive prompt

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_resubmit-pilot-contrastive-prompt_20260517T080153_result.json`
- **Structured JSON:** [`93ca46b1455e369d3c31.json`](../../sessions/93/93ca46b1455e369d3c31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **GPU 状态**：exp-010-mistral-v3 正在运行（vLLM 占用 87880 MiB），不能提交
- **脚本验证**：`run_pilot_contrastive_v2.sh` 和 `pilot_contrastive_constraints.py` 均存在且完整
- **修复方案确认**：提交时使用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/symb_invariant_consensus/scripts/run_pilot_contrastive_v2.sh"` 即可解决 EXIT_CODE=127
- **Registry 已更新**：notes 记录了修复方案和等待状态

等 exp-010-mistral-v3 完成释放 GPU 后，提交命令为：

```
submit_training_job(
  server="westd-32608",
  gpu_ids=["cuda:0"],
  exp_id="pilot-contrastive-prompt",
  command='bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/symb_invariant_consensus/scripts/run_pilot_contrastive_v2.sh"',
  account="root",
  project="symb_invariant_consensus"
)
```

---
