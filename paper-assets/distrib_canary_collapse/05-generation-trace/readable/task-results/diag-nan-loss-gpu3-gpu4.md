# diag nan loss gpu3 gpu4

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_nan_loss_gpu3_gpu4_20260518T235354_result.json`
- **Structured JSON:** [`5f087d7130cd76b46297.json`](../../sessions/5f/5f087d7130cd76b46297.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3/4 已经自动退出（0 MiB，无进程），tmux sessions 也已关闭。无需 kill。

---

## 诊断报告

### 根因
**模型以 fp16 加载，但训练未启用混精度保护（无 GradScaler/AMP），导致梯度溢出 → 全模型 NaN。**

代码 `iterative_train.py` 第 218 行：
```python
model = AutoModelForCausalLM.from_pretrained(
    args.model_name, **{_DTYPE_KWARG: torch.bfloat16 if args.bf16 else None})
```

`bf16=False` 时传入 `torch_dtype=None`，Pythia-410m 的原生 dtype 是 float16，所以模型以 fp16 加载。但 `TrainingArguments` 中 `fp16=False, bf16=False`，Trainer 不会启用 AMP 或 GradScaler，导致 AdamW 的 momentum/variance 在 fp16 中累积，warmup 结束后 lr 达峰值时梯度溢出。

**验证**：保存的 checkpoint dtype 确认是 `torch.float16`（不是 float32）。两个实验都在 ~step 900（warmup 结束后）发散，100% 参数变 NaN，可复现（v2 重跑同样崩溃）。

### 当前状态
- 两个进程已自动退出，GPU 3/4 已释放
- `a005_s42_fp32`: EXIT_CODE=1 "Eigenvalues did not converge"（NaN 模型无法算 metric）
- `a005_s42_fp32_v2`: EXIT_CODE=1 "CUDA error: device-side assert triggered"（用 NaN 模型做 gen_2 推理崩溃）
- `interv_pred_a075_s42_fp32`: gen_1 metrics 中 token_entropy/perplexity/effective_rank 全 NaN
- **不需要 kill**

### 修复方案
`iterative_train.py` 一行改动：

```python
# 修改前
model = AutoModelForCausalLM.from_pretrained(
    args.model_name, **{_DTYPE_KWARG: torch.bfloat16 if args.bf16 else None})

# 修改后
model = AutoModelForCausalLM.from_pretrained(
    args.model_name, **{_DTYPE_KWARG: torch.bfloat16 if args.bf16 else torch.float32})
```

两处（初始加载和 resume 加载）都要改。改完后清除失败的 gen_1 目录重跑。

---
