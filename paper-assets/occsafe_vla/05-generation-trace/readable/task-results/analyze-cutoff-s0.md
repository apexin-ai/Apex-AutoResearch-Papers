# analyze cutoff s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cutoff_s0_20260523T005240_result.json`
- **Structured JSON:** [`51eb1a88363714bc7837.json`](../../sessions/51/51eb1a88363714bc7837.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

1. **训练完成**: 到达 50005 步，EXIT_CODE=0
2. **最终指标** (step 50000):
   - action_loss = **0.0513** (初始 0.6914)
   - occ_loss = **0.0087** (初始 0.0979)
   - depth_loss = 0.0000
3. **Checkpoint 完整**: `50000_chkpt/` 包含 4 个 safetensors 分片 (~14.5GB)、action_head、occ_head、proprio_projector、lora_adapter、tokenizer、config 等全部文件
4. **Eval 已提交**:
   - exp_id: `cutoff_s0_eval`
   - server: westd-34685, cuda:0
   - log: `~/runs/occsafe_vla/cutoff_s0_eval.log`
   - 50 rollouts, seed 42

---
