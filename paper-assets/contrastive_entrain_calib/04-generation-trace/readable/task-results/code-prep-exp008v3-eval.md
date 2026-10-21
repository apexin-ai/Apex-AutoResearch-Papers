# code prep exp008v3 eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp008v3-eval_20260519T102942_result.json`
- **Structured JSON:** [`e4cb91584a9b84f060fe.json`](../../sessions/e4/e4cb91584a9b84f060fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完毕，语法检查通过。

## 报告

### Checkpoint 格式
- **LoRA adapter**：每个 checkpoint 包含 `adapter_model.safetensors` + `adapter_config.json`（r=64, alpha=64, targets=q/k/v/o_proj）
- **不需要 DeepSpeed 合并**：虽然 `global_step500/` 内有 ZeRO-2 optimizer states，但 HF Trainer + PEFT 已自动保存了 merged LoRA adapter，eval 直接用 `--lora_path` 加载即可
- Base model: Qwen3-8B (`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`)

### Checkpoint 保存节奏
- `save_steps=500`, `max_steps=8000` → 最多 16 个 checkpoint + 1 个 `final`
- 当前已有：`checkpoint-500`（训练 step ~291 时还没到 500，但日志看时间戳已保存）

### Eval 脚本
`/root/contrastive_entrain_calib/eval/run_exp008v3_unified_eval.sh`

- 遍历 checkpoint-500 到 checkpoint-8000 + final
- 自动跳过不存在的 checkpoint 和已完成的 eval
- GPU 通过 `CUDA_VISIBLE_DEVICES` 外部传入
- 输出到 `/root/contrastive_entrain_calib/results/exp008v3_unified_eval/`
- exp_id 格式：`exp008v3-ckptNNNN` / `exp008v3-final`

### 运行方式
```bash
CUDA_VISIBLE_DEVICES=0 bash /root/contrastive_entrain_calib/eval/run_exp008v3_unified_eval.sh
```

不需要额外步骤，直接可跑。

---
