# code activation collection run

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_activation_collection_run_20260516T221034_result.json`
- **Structured JSON:** [`2a4b896adbbfe651d947.json`](../../sessions/2a/2a4b896adbbfe651d947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Activation collection 完成。

**结果总结：**

| 指标 | 值 |
|------|------|
| 输出路径 | `/root/autodl-tmp/activations_v3/activations.pt` |
| 总样本数 | 3000 (0 errors) |
| visual | 1000 |
| spatial | 1000 |
| physical | 1000 |
| Activation shape | (2048,) float16 |
| 非零率 | 97% (2909/3000) |
| 文件大小 | 12.6 MB |
| 采集耗时 | ~3 min (不含模型加载) |

**关键改动：**
- 脚本改为 `policy.infer(obs_dict)` 模式（参照 `eval_lora_openpi.py`）
- 使用 `OpenPIMetaBrainPolicy.from_checkpoint()` 加载模型，确保预处理链与 eval 完全一致
- Hook 注册在 `policy_wrapper.model` 上，路径 `paligemma_with_expert.paligemma.model.language_model.layers.6`
- 扰动直接在 raw numpy (uint8 HWC) 上操作后送入 policy.infer

数据可直接用于 PAR router 重训。

---
