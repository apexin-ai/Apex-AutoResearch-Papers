# diagnose random reweight seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_random_reweight_seed42_20260516T072019_result.json`
- **Structured JSON:** [`c0e9097f540c41509ace.json`](../../sessions/c0/c0e9097f540c41509ace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行中，已完成 11/6103 steps，ETA ~3.6h。

---

**报告：**

1. **WANDB_API_KEY 实际来源**：服务器上根本没有配置 wandb API key（无 .netrc、无环境变量）。其他实验通过 `WANDB_MODE=offline` 绕过了 key 需求。

2. **修复内容**：在 `scripts/run_random_reweight_seed42.sh` 中添加了两行：
   - `export WANDB_MODE=offline` — 解决 wandb login 报错
   - `export CUDA_VISIBLE_DEVICES=2` — 避免 OOM（GPU 0/1/3 被其他实验占用）

3. **dry-run 结果**：通过。实验已在 GPU 2 上正常训练，当前 step 11/6103。

4. 
```json
{"root_cause":"wandb API key not configured on server, script missing WANDB_MODE=offline unlike other scripts","error_type":"infrastructure","fix_steps":["added export WANDB_MODE=offline to run_random_reweight_seed42.sh","added export CUDA_VISIBLE_DEVICES=2 to avoid GPU OOM"],"can_auto_fix":true,"fixed":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "wandb API key not configured on server, script missing WANDB_MODE=offline unlike other scripts",
    "error_type": "infrastructure",
    "fix_steps": [
      "added export WANDB_MODE=offline to run_random_reweight_seed42.sh",
      "added export CUDA_VISIBLE_DEVICES=2 to avoid GPU OOM"
    ],
    "can_auto_fix": true,
    "fixed": true
  }
}
```

</details>

---
