# ops gsm8k westd status collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-westd-status-collect_20260521T074214_result.json`
- **Structured JSON:** [`cc12a922982f79d8516c.json`](../../sessions/cc/cc12a922982f79d8516c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 进程状态：4 个 eval 全部仍在运行

| GPU | Model | PID | Runtime | GPU Util | VRAM |
|-----|-------|-----|---------|----------|------|
| 0 | Gemma-2 d000 s0 | 492703 | 29m15s | 91% | 20.3/97.9 GB |
| 1 | Qwen-14B d100 s0 | 481803 | 1h38m46s | 93% | 32.7/97.9 GB |
| 2 | Qwen-14B d050 s0 | 492186 | 29m46s | 93% | 32.7/97.9 GB |
| 3 | Phi-4 d000 s0 | 493644 | 28m44s | 100% | 31.7/97.9 GB |

**Qwen-14B d100 s0 已跑 ~1h40m，应该接近完成。** 其余 3 个跑了约 30 分钟，估计还需 30-60 分钟。

### 2. 已完成 GSM8K 结果

**westd（已落盘）：**

| Model | Dosage | Seed | Accuracy |
|-------|--------|------|----------|
| Qwen-14B | d000 | s0 | **74.98%** |
| Qwen-14B | d005 | s0 | **71.19%** |
| Qwen-14B | d025 | s0 | **79.30%** |

**cqa1（已落盘）：**

| Model | Dosage | Seed | Accuracy |
|-------|--------|------|----------|
| Qwen-7B | d000 | s42 | 70.58% |
| Qwen-7B | d005 | s42 | 76.95% |
| Qwen-7B | d025 | s42 | 80.06% |
| Qwen-7B | d050 | s42 | 79.23% |
| Qwen-7B | d100 | s42 | 81.65% |
| Qwen-7B | d000 | s123 | 70.05% |
| Qwen-7B | d100 | s123 | 79.23% |

注意 Qwen-14B d005 s0 (71.19%) < d000 s0 (74.98%)，有轻微反转。

### 3. 空闲 GPU

**当前无空闲 GPU**，4 块全部在用。GPU 1 (Qwen-14B d100 s0) 预计最快释放。

### 4. westd 下一批建议

当前 eval 完成后，westd 完成 Qwen-14B s0 全部 5 个 dosage。下一优先级：

**高优先（覆盖新模型 d000 基线）：**
1. OLMo-2-7B d000 s0 — 唯一没有任何 GSM8K 结果的模型
2. Gemma-2 d005/d025/d050/d100 s0 — 补齐 Gemma-2 s0 dosage 梯度
3. Phi-4 d005/d025/d050/d100 s0 — 补齐 Phi-4 s0 dosage 梯度

**启动命令模板（参考当前运行进程）：**
```bash
CUDA_VISIBLE_DEVICES=N nohup python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/models/&lt;MODEL> \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/&lt;CHECKPOINT>/lora_adapter \
  --benchmarks gsm8k --batch-size 2 \
  --output-dir /root/contamcal-irt-calibration/results/gsm8k_eval/&lt;model>/&lt;dosage_seed> \
  > /tmp/gsm8k_&lt;model>_&lt;dosage_seed>.log 2>&1 &
```

建议 GPU 1 最先释放时跑 OLMo-2-7B d000 s0（模型小，约 7B，速度快）。其余 GPU 释放后各跑一个 Gemma-2 或 Phi-4 dosage。

---
