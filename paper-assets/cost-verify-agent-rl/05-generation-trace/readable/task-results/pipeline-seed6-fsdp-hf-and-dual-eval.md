# pipeline seed6 fsdp hf and dual eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_seed6_fsdp_hf_and_dual_eval_20260521T130652_result.json`
- **Structured JSON:** [`b4777488e6a6167876a6.json`](../../sessions/b4/b4777488e6a6167876a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部在工作。

---

### 汇总

| 项目 | 结果 |
|------|------|
| **FSDP→HF 转换** | 成功，3.8G，`/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf/` |
| **Seed 6 OOD eval** | PID 291159，GPU 2（8.1GB 已加载） |
| **SFT baseline OOD eval** | PID 282634，GPU 3（8.1GB 已加载） |
| **Seed 7 训练** | PID 226699，GPU 0,1，未受影响 |
| **GPU 使用** | 4/4 全部有任务 |
| **磁盘** | 110G/250G used（44%），剩余 141G |

**修复记录**：首次提交 Seed 6 eval 因 `enable_response_mask` 断言失败（model_path 不含 "qwen"），已在 config 中追加 `enable_response_mask: False` 后重新提交成功。

---
