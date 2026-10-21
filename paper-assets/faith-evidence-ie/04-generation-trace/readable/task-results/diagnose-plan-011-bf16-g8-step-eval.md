# diagnose plan 011 bf16 g8 step eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_011_bf16_g8_step_eval_20260515T195026_result.json`
- **Structured JSON:** [`55d25e2a31e4deb3f2af.json`](../../sessions/55/55d25e2a31e4deb3f2af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。PID 246051 已死，GPU 1 完全空闲（32.6GB）。

**诊断结论**：

- 日志尾行：`Terminated` → `EXIT_CODE=143`（SIGTERM）
- 推理代码 `device_map="auto"` 无 `CUDA_VISIBLE_DEVICES` 限制，模型自动加载到 GPU 0
- GPU 0 已被 plan_001 训练（PID 236779）占用 16.3GB，eval 加载后双进程共占 31.4/32.6GB
- 完成 1/62 batch 后被 SIGTERM kill
- GPU 1 完全空闲，32.6GB 可用

**重提交命令**（添加 `CUDA_VISIBLE_DEVICES=1`）：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 bash /root/autodl-tmp/freige/scripts/eval_plan_011_steps.sh"
```

无需修改脚本代码——`device_map="auto"` 会尊重 `CUDA_VISIBLE_DEVICES`。

```json
{"root_cause":"SIGTERM (EXIT_CODE=143) at inference 1/62. device_map='auto' placed model on GPU 0 alongside plan_001 training (PID 236779, 16.3GB). Two processes shared 31.4/32.6GB, process was killed.","error_type":"resource","fix_steps":["重提交时设 CUDA_VISIBLE_DEVICES=1（GPU 1 空闲 32.6GB）","清理空产物目录: rm -rf /root/autodl-tmp/eval_results/plan_011_bf16_g8_step30"],"can_auto_fix":true,"script_gpu_mode":"env_var","resubmit_ready":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "SIGTERM (EXIT_CODE=143) at inference 1/62. device_map='auto' placed model on GPU 0 alongside plan_001 training (PID 236779, 16.3GB). Two processes shared 31.4/32.6GB, process was killed.",
    "error_type": "resource",
    "fix_steps": [
      "重提交时设 CUDA_VISIBLE_DEVICES=1（GPU 1 空闲 32.6GB）",
      "清理空产物目录: rm -rf /root/autodl-tmp/eval_results/plan_011_bf16_g8_step30"
    ],
    "can_auto_fix": true,
    "script_gpu_mode": "env_var",
    "resubmit_ready": true
  }
}
```

</details>

---
