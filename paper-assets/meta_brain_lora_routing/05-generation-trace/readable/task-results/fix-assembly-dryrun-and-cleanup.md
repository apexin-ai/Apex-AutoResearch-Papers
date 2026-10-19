# fix assembly dryrun and cleanup

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_assembly-dryrun-and-cleanup_20260515T164453_result.json`
- **Structured JSON:** [`5858994b2c039da33b52.json`](../../sessions/58/5858994b2c039da33b52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

```
P1 assembly dry-run: PASS — Router forward → LoRA merge → action generation 端到端通过
   actions=(1,50,32), routing=[0.15, 0.58, 0.27]
   注：需设 CUDA_VISIBLE_DEVICES 隔离（JAX 默认预分配所有 GPU 导致并行加载冲突）

P2 ablation+eval dry-run: PASS — 两个脚本均通过
   evaluate_libero_plus.py: actions=(1,50,32), routing=[0.37, 0.42, 0.21], exit=0
   ablation_ladder.py: 5 configs 全部通过 (none/universal/random/par/oracle), exit=0

P3 LoRA training dry-run: PASS — 模型加载 → LoRA 注入 → forward+backward 完成
   3,686,400 trainable params (0.11%), 2 步 loss: 8.81→1.91, exit=0

P4 first-token pooling: CONFIRMED — 两文件默认均为 "first"
   par_router.py:49  → config.get("pooling", "first")
   train_par_router.py:465 → default="first"
   注：meta_brain_assembly.py from_dummy() 的测试 router 仍用 "mean"，不影响实际推理

P5 代码合并: N/A — artifacts/phase1/train_lora_expert.py 已不存在，
   仅保留规范路径 phase1/train_lora_expert.py（336 行，含 data_loader + augmentation + PEFT LoRA + flow-matching loss）
```

---
