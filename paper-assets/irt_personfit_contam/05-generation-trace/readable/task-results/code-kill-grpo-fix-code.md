# code kill grpo fix code

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kill-grpo-fix-code_20260521T114332_result.json`
- **Structured JSON:** [`7c089af67d3b974706f1.json`](../../sessions/7c/7c089af67d3b974706f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### 1. GRPO PID 130591 — 已 kill

GPU 状态确认：
- GPU 0: PID 129109 (Llama s2 训练，95% util) ✓
- GPU 1: 空闲
- GPU 2: PID 129635 (其他任务，88% util)
- GPU 3: 空闲

### 2. train_grpo.py 完整 diff

```diff
 grpo_config = GRPOConfig(
     output_dir=output_dir,
     num_train_epochs=1,
     per_device_train_batch_size=2,
     gradient_accumulation_steps=4,
     learning_rate=5e-6,
-    num_generations=8,
+    num_generations=16,
     max_completion_length=128,
+    temperature=1.2,
     bf16=True,
     logging_steps=10,
     save_strategy="steps",
-    save_steps=3000,
+    save_steps=500,
     save_total_limit=3,
     seed=42,
     report_to="none" if args.dry_run else "wandb",
     run_name="post-rl-grpo",
-    max_steps=args.max_steps,
+    max_steps=3000,
 )
```

### 3. 修改后参数确认

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| `num_generations` | 8 | **16** |
| `temperature` | (无) | **1.2** |
| `max_steps` | `args.max_steps` (默认 -1) | **3000** |
| `save_steps` | 3000 | **500** |

注意：`max_steps` 现在硬编码为 3000，`--max-steps` CLI 参数不再生效（dry-run 模式仍会覆盖为 2）。如需保留 CLI 覆盖能力可进一步调整。

等待审批，不启动 GRPO v3。

---
