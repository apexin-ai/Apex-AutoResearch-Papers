# ops pilot finish and eval launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pilot-finish-and-eval-launch_20260518T113512_result.json`
- **Structured JSON:** [`e5c035290b7917d967ce.json`](../../sessions/e5/e5c035290b7917d967ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### Step 1: 7B Pilot 完成
- PID 17819 已结束，EXIT_CODE=0

### Step 2: Checkpoint 验证 (M011 硬证据)
| 项目 | 值 |
|---|---|
| Checkpoint 路径 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/` |
| adapter_model.safetensors | 155M |
| lora_alpha | **32** (符合规范) |
| lora_r | 16 |
| **Final loss** (step 3120) | **0.8814** |
| **Avg train_loss** | **0.9247** |
| Total steps | **3125/3125** |
| mean_token_accuracy | 0.7917 |
| Runtime | 5358s (~89 min) |

### Step 3: GSM8K Eval
- **PID: 22359**, GPU 0 (17.7GB), 模型已加载，评估进行中

### Step 4 & 5: 14B 状态
- **14B 未就绪**: incomplete=1, safetensors=7/8 (缺 model-00005-of-00008), 当前 26GB
- **未启动 14B pilot**

---
