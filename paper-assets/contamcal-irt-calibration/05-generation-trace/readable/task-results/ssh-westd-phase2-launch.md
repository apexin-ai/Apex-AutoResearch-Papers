# ssh westd phase2 launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-launch_20260519T104124_result.json`
- **Structured JSON:** [`9a4f648e92ea08c4f22e.json`](../../sessions/9a/9a4f648e92ea08c4f22e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部满载运行，无 error。

### 产出汇总

**1. Phi-4 d100 训练 metrics**
```json
{"final_loss": 1.191, "mean_token_accuracy": 0.7244, "train_runtime_sec": 9234}
```
- lora_alpha=32, lr=5e-5, epochs=1, 4159 steps, 66533 samples

**2. Phi-4 d100 checkpoint 完整性** ✅
- `adapter_model.safetensors` (222MB) + `adapter_config.json` + `.done` sentinel 均存在

**3. Phase 2 进程 PID**

| GPU | 模型/任务 | PID | VRAM |
|-----|----------|-----|------|
| 0 | Phi-4 (5 evals) | 146957 | 31.7GB |
| 1 | Qwen2.5-14B (5 evals) | 147458 | 32.7GB |
| 2 | Qwen2.5-7B + Gemma-d000 (6 evals) | 147533 | 17.7GB |
| 3 | Gemma-d005~d100 + OLMo-2 (9 evals) | 147609 | 19.3GB |

**4. 启动验证** ✅ 全部 4 GPU 90%+ utilization，log 正常输出（MMLU eval 进行中）

**5. 预估完成时间**
- GPU 0 (Phi-4): MMLU 14042 items @ ~18 it/s ≈ 13min/benchmark × 5 = ~65min → ~19:50
- GPU 1 (14B): 类似速度 × 5 ≈ ~65min → ~19:50
- GPU 2 (7B): 更快 ~30 it/s × 6 ≈ ~50min → ~19:35
- GPU 3 (9B×4 + 7B×5 = 9 evals): 最慢，≈ ~120min → ~20:45

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "final_loss": 1.191,
    "mean_token_accuracy": 0.7244,
    "train_runtime_sec": 9234
  }
}
```

</details>

---
