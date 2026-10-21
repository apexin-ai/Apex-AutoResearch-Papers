# ops kill dup and qwen14b eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-dup-and-qwen14b-eval_20260521T023734_result.json`
- **Structured JSON:** [`a3f3a982063760801948.json`](../../sessions/a3/a3f3a982063760801948.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### Part 1: 重复进程清理
- PID 464499（Gemma-2 MMLU eval）和 PID 464645（Gemma-2 ARC eval）已 kill
- GPU 0 和 GPU 2 已释放（确认 0 MiB）

### Part 2: Qwen-14B d100_s0 adapter
- 路径：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s0/lora_adapter/`
- `adapter_model.safetensors`: 275MB ✓
- `lora_alpha`: 32（C006 合规）✓
- `.done` 标记存在 ✓
- 训练配置：lr=5e-5, r=16, alpha=32, seed=0, epochs=1

### Part 3: Eval 启动
| Eval | tmux session | GPU | 显存占用 | 利用率 | Registry |
|------|-------------|-----|---------|--------|----------|
| MMLU | `eval_qwen14b_mmlu` | cuda:0 | 32.7GB | 96% | `eval_qwen14b_d100_mmlu_s0` RUNNING |
| ARC | `eval_qwen14b_arc` | cuda:2 | 32.7GB | 95% | `eval_qwen14b_d100_arc_s0` RUNNING |

### ⚠️ C009 注意
evaluate.py md5 `17673bf3...`（37775 bytes）与参考 hash `001a9bc2...`（37591 bytes）不匹配。两个 eval 使用同一版本，内部一致性无问题（C010 合规），但与其他服务器产出对比时需注意版本差异。

---
