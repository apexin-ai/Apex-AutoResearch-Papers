# code nora goal pipeline prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nora_goal_pipeline_prep_20260521T021532_result.json`
- **Structured JSON:** [`eea97320323f21ead40e.json`](../../sessions/ee/eea97320323f21ead40e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## NORA LIBERO-Goal Pipeline — Dry-run 报告

### 脚本状态

`/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py` (649 行) — **就绪，dry-run 全部通过。**

### Dry-run 结果 (trained condition)

| Phase | 耗时 | 输出文件 | 状态 |
|-------|------|----------|------|
| 1. Feature extraction | 1.1s | (in-memory) | 4 samples (2 tasks × 1 demo × 2 timesteps) |
| 2. Action R² probing | 434.5s | `action_r2_probing.json` | 36 layers × 2 positions × 2 seeds |
| 3. L1 attention profile | 0.0s | `l1_attention_profile.json` | 16 heads: 13 instr-dom, 0 img-dom, 3 mixed |
| 4. Cross-instruction classification | 0.4s | `cross_instruction_classification.json` | 5 layers × 2 positions |
| 5. Counterfactual (cosine distance) | 8.5s | `counterfactual_combined.json` | 4 conditions × 13 layers |
| **Total** | **8.0 min** | | |

### Token layout 验证

```
input_ids: [1, 53]
bos=(0,14)  image=(15,40)=25 tokens  text=(41,53)
Hidden: [1, 53, 2048]  Attention: 36 layers × [1, 16, 53, 53]
```

### 注意事项

- Phase 2 主导运行时间（~7 min / 8 min total），full run 预计 ~3-4 小时（10 tasks × 20 demos × 50 timesteps × 36 layers × 3 seeds）
- numpy "Degrees of freedom" warning 是 dry-run 样本量太小导致，full run 不会出现
- Counterfactual 使用 representation cosine distance（非 action MSE），因 NORA 的 FAST+ action tokens 无法直接解码为连续 7-DoF 动作
- 脚本支持 `--conditions trained untrained` 顺序跑两个模型，untrained 时自动跳过 counterfactual

### 提交命令（等 TraceVLA-Spatial 完成后执行）

```bash
source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate
CUDA_VISIBLE_DEVICES=1 nohup python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py \
  --conditions trained untrained > /tmp/nora_pipeline_full.log 2>&1 &
```

---
