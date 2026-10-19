# hotfix eval use delta and rerun

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_hotfix_eval_use_delta_and_rerun_20260516T144711_result.json`
- **Structured JSON:** [`f2e2e8a728876550d3c5.json`](../../sessions/f2/f2e2e8a728876550d3c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。完整结果：

## Eval 最终结果

```
Meta-Brain Evaluation Results [routing=par]

Per-perturbation:
  camera_viewpoints         visual       0.0%  (0/5)
  light_conditions          visual       0.0%  (0/5)
  background_textures       visual       0.0%  (0/5)
  sensor_noise              visual       0.0%  (0/5)
  objects_layout            spatial      0.0%  (0/5)
  robot_initial_states      physical     0.0%  (0/5)
  nominal                   nominal      0.0%  (0/5)

Per-category:
  nominal    0.0%  (0/5)
  physical   0.0%  (0/5)
  spatial    0.0%  (0/5)
  visual     0.0%  (0/20)

  OVERALL    0.0%  (0/35)
```

**结果已保存**: `/root/meta_brain_lora_routing/phase1/outputs/eval_par_libero_spatial_20260516_230321.json`

**结论：Hotfix 未修复问题。** 所有 7 个 perturbation 全 0/35，包括 nominal（无扰动基线）。连基线都 0% 说明问题不在 `use_delta` flag，更可能是：

1. **Dummy LoRA 权重** — 未加载训练过的 LoRA checkpoint，用的是随机初始化的 dummy adapters
2. **eval 未指定 `--router_checkpoint` / `--lora_*_dir`** — 没有指向实际训练过的权重路径
3. **PI0 base checkpoint** (`pi0_libero`) 可能不是 fine-tuned 版本

日志中没有 action 值采样，无法确认 action range。每个 episode 都跑满了 220 steps 然后 FAIL（表示到达最大步数超时，而非 crash）。

---
