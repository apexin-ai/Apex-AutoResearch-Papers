# 诊断：inference_speedup_plan016_v2 实验"失败"

## 失败根因（一句话）

**实验实际成功完成，cron 误判。** 脚本无 W&B 集成，只输出本地 JSON；cron 以 "5次无有效 W&B metrics" 判定失败，属于监控系统 false positive。

## 证据

### v2 运行结果（成功）

日志 `/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench.log` 显示三个模型均跑完：

| Model | tok/s | Peak Memory | Latency/prompt |
|-------|-------|-------------|----------------|
| dense (7B) | 76.25 | 16.22 GB | 6.68s |
| rasp_20 | 52.07 | 11.60 GB | 4.16s |
| standard_20 | 49.78 | 11.61 GB | 6.17s |

结果 JSON 已保存：`/root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark.json`

### v1 失败原因（已在 v2 修复）

v1 日志显示 rasp_20 加载时 shape mismatch：
```
model.layers.{0...27}.mlp.up_proj.weight | MISMATCH | ckpt: torch.Size([8128, 3584]) vs model:torch.Size([18944, 3584])
RuntimeError: You set `ignore_mismatched_sizes` to `False`, thus raising an error.
```

v2 通过 `is_pruned=True` + `load_pruned_model()` 修复了该问题。

### 脚本确认无 W&B

`/root/recovery_aware_struct_prune/src/benchmark_inference.py` 中没有 `import wandb`，没有任何 `wandb.log()` 调用。仅通过 `json.dump()` 写本地文件。

## 修复建议

1. **标记实验为成功**：v2 已正常完成，结果有效
2. **如需 cron 兼容**：在脚本末尾加 W&B 上报（约 5 行代码）：
   ```python
   # benchmark_inference.py line ~100, main() 末尾
   import wandb
   run = wandb.init(project="recovery_aware_struct_prune", name="inference_bench", job_type="benchmark")
   for model_name, metrics in results.items():
       wandb.log({f"{model_name}/{k}": v for k, v in metrics.items() if isinstance(v, (int, float))})
   wandb.finish()
   ```
3. **或调整 cron 监控逻辑**：对 job_type=benchmark 的任务，检查输出 JSON 文件存在性而非 W&B metrics
