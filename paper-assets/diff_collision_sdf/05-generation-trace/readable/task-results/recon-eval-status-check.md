# recon eval status check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_eval-status-check_20260528T101542_result.json`
- **Structured JSON:** [`48e60ca54ae9950609b7.json`](../../sessions/48/48e60ca54ae9950609b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| exp_id | 服务器 | 状态 | Avg TSR | Avg CAR |
|--------|--------|------|---------|---------|
| eval_multiseed_lora_s0_eseed0 | westd-35807 | **完成** | 55.5% | 53.0% |
| eval_multiseed_lora_s0_eseed99 | westd-35807 | **完成** | 52.0% | 57.5% |
| eval_multiseed_sdf_l01_s0_eseed0 | westd-35807 | **完成** | 48.5% | 52.5% |
| eval_multiseed_sdf_l01_s0_eseed99 | westd-35807 | **完成** | 46.5% | 57.0% |
| eval_multiseed_lora_s1_eseed0 | westd-45947 | **失败** | — | — |
| eval_multiseed_lora_s1_eseed99 | westd-45947 | **失败** | — | — |

### westd-35807: 4/4 成功

JSON 已保存到 `/root/autodl-tmp/eval_results/`，均 EXIT_CODE=0。

### westd-45947: 2/2 失败

**原因**: `RuntimeError` — state_dict key 不匹配。checkpoint 路径 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` 中的 key 使用 `layernorm.dense.weight/bias` 格式，但模型期望 `layernorm.weight` 格式（无 dense 层）。同时缺少 `action_time_mlp_*` 和 `time_mlp_*` 等 key。

这是代码版本与 checkpoint 不匹配的问题——westd-45947 上的代码或模型配置和 westd-35807 不一致。需要同步代码后重跑这两个 eval，预计单个 eval ~25min，DDL 前可完成。

---
