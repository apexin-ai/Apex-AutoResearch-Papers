# ops scp seed1 seed3 to westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp_seed1_seed3_to_westd_20260522T060453_result.json`
- **Structured JSON:** [`db0ec6abd8ee7eb0fba2.json`](../../sessions/db/db0ec6abd8ee7eb0fba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**传输失败——checkpoint 不存在。**

两台服务器彻底搜索结果：

- **bjb1** 上仅有 `exp029-seed4/global_step_15_hf` 的 safetensors
- **westd** 上有 `exp029-seed4` 和 `exp029-seed6` 的 `global_step_15_hf`
- **seed1** (`exp029_episode_level`) 和 **seed3** (`exp029_seed3_v2`) 的 step15 checkpoint 在两台服务器上均不存在——HF 格式和 FSDP 格式都没有。目录要么不存在，要么为空。

这两个 checkpoint 很可能在之前的磁盘清理中被删除了。Table 1 中已有的 OOD 结果（seed1: 23.88%, seed3: 10.45%）应该来自删除前的评估。

**后续选项：**
1. 接受已有 OOD 结果，不重新评估
2. 重新训练 seed1 (seed=10001) 和 seed3 (seed=42) 的 episode-level GRPO 至 step 15，生成新 checkpoint

---
