# pipeline alpha ablation qwen math

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_alpha_ablation_qwen_math_20260516T191349_result.json`
- **Structured JSON:** [`bdf11334df2b28c11c1a.json`](../../sessions/bd/bdf11334df2b28c11c1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase B 正在 GPU 3 上正常运行。状态总结：

**Phase A**: 完成。6 个 pruned 模型：
- `/root/autodl-tmp/recovery_aware_struct_prune/outputs/alpha_ablation/pruned_alpha_{0.0,0.3,0.5,0.7,1.0,2.0}`

**Phase B**: 运行中（PID 39816, GPU 3, 12458 MiB）
- 当前：SFT alpha=0.0
- 速度：~1.1 it/s, 1870 steps/alpha
- 预计每个 alpha: SFT ~28min + eval ~10min ≈ 38min
- 6 个 alpha 总计：~3.8h
- 预计完成：约 07:00 CST

**监控命令**：
```bash
# 查看当前进度
tail -5 /tmp/alpha_ablation_phaseB.log

# 检查是否完成
grep "PHASE_B_COMPLETE" /tmp/alpha_ablation_phaseB.log

# 查看最终结果
for alpha in 0.0 0.3 0.5 0.7 1.0 2.0; do cat /root/autodl-tmp/recovery_aware_struct_prune/outputs/alpha_ablation/eval_alpha_${alpha}.json; done
```

---
