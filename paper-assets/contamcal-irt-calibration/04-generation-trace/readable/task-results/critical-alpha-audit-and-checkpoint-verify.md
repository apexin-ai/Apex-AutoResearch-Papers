# critical alpha audit and checkpoint verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_alpha-audit-and-checkpoint-verify_20260515T185036_result.json`
- **Structured JSON:** [`4218c1d0be283fd14cc9.json`](../../sessions/42/4218c1d0be283fd14cc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是完整审计结果。

---

## 子任务 B：全量 checkpoint lora_alpha 审计

### 完整对照表

| Model | Checkpoint | lora_alpha | r | Created | Bug Affected? |
|-------|-----------|------------|---|---------|--------------|
| **0.5B** | d000_s42 | **32** | 16 | May 14 04:31 | YES |
| | d000_s123 | **32** | 16 | May 14 05:36 | YES |
| | d005_s42 | **32** | 16 | May 14 08:54 | YES |
| | d005_s123 | **32** | 16 | May 15 08:42 | YES |
| | d025_s42 | **32** | 16 | May 14 16:30 | YES |
| | d025_s123 | **32** | 16 | May 15 13:40 | YES |
| | d100_s42 | **32** | 16 | May 14 08:50 | YES |
| | d100_s123 | **32** | 16 | May 15 05:29 | YES |
| **1.5B** | d000_s42 | **32** | 16 | May 14 05:23 | YES |
| | d000_s123 | **32** | 16 | May 14 06:23 | YES |
| | d005_s42 | **32** | 16 | May 14 16:45 | YES |
| | d005_s123 | **32** | 16 | May 15 20:52 | YES |
| | d025_s42 | **32** | 16 | May 15 01:33 | YES |
| | d025_s123 | **32** | 16 | May 15 20:57 | YES |
| | d100_s42 | **32** | 16 | May 14 15:39 | YES |
| | d100_s123 | **32** | 16 | May 15 08:27 | YES |
| **3B** | d000_s42 | **32** | 16 | May 14 07:20 | YES |
| | d000_s123 | **32** | 16 | May 14 08:15 | YES |
| | d000_v2_s42 | 16 | 16 | May 15 03:46 | no (fixed) |
| | d000_v2_s123 | 16 | 16 | May 15 08:02 | no (fixed) |
| | d005_s42 | **32** | 16 | May 14 20:56 | YES |
| | d005_s123 | **32** | 16 | May 15 23:03 | YES |
| | d025_s42 | 16 | 16 | May 15 11:56 | no |
| | d025_s123 | **32** | 16 | May 15 22:42 | YES |
| | d100_s42 | 16 | 16 | May 15 07:06 | no |
| | d100_s123 | 16 | 16 | May 15 13:17 | no |
| | d000_a32_s42 | N/A (空目录) | - | May 16 00:52 | 训练未完成 |

### 统计

- **alpha=32（受影响）：22 个 checkpoint**（全部 0.5B × 8、全部 1.5B × 8、3B × 6）
- **alpha=16（正确）：5 个 checkpoint**（3B d000_v2_s42/s123、d025_s42、d100_s42/s123）
- **空目录：1 个**（3B d000_a32_s42，训练中或失败）

### train_sft.py 代码分析

**根因不是参数传递 bug，而是默认值问题：**

```python
# line 34: 默认值是 32
DEFAULT_LORA_CONFIG = {
    "r": 16,
    "lora_alpha": 32,   # ← 这里
}

# line 97: argparse default 引用了这个 32
parser.add_argument("--lora-alpha", type=int, 
                    default=DEFAULT_LORA_CONFIG["lora_alpha"])

# line 135-137: 参数传递本身是正确的
lora_config = LoraConfig(
    r=args.lora_r,
    lora_alpha=args.lora_alpha,  # ← 正确传递
)
```

**结论**：代码逻辑没问题，`args.lora_alpha` 正确传入 `LoraConfig`。问题是 `DEFAULT_LORA_CONFIG["lora_alpha"]` = 32。凡是训练命令未显式指定 `--lora-alpha 16` 的，都会默认用 32。v2 runs 的 SFT 日志确认 `alpha=16`，说明 v2 训练时显式传了 `--lora-alpha 16`。

---

## 子任务 C：d000_s123 版本确认

### d000 相关 3B checkpoint 对比

| 目录 | alpha | r | 创建时间 | 状态 |
|------|-------|---|---------|------|
| Qwen2.5-3B_d000_s123 | 32 | 16 | May 14 08:15 | 完整 |
| Qwen2.5-3B_d000_s42 | 32 | 16 | May 14 07:20 | 完整 |
| Qwen2.5-3B_d000_v2_s123 | 16 | 16 | May 15 08:02 | 完整 |
| Qwen2.5-3B_d000_v2_s42 | 16 | 16 | May 15 03:46 | 完整 |
| Qwen2.5-3B_d000_a32_s42 | N/A | - | May 16 00:52 | 空目录 |

### Eval 用了哪个 checkpoint？

**3B d000_s123 eval（`exp_001_eval_3B_d000_s123.log`）：**
```
Loading adapter: .../Qwen2.5-3B_d000_s123/lora_adapter
```
→ 用的是**原始 d000_s123（alpha=32）**，不是 v2

**3B d000_s123_aligned eval：**
- 结果目录 `eval_results/Qwen2.5-3B_d000_s123_aligned/` 存在（May 15 22:24）
- runs 目录无单独 log 文件
- eval_results.json 未记录 adapter_path
- 按命名约定，使用的也是 `Qwen2.5-3B_d000_s123`（alpha=32）

**3B d000_v2 aligned eval（`exp_001_eval_3B_d000_v2_aligned.log`）：**
```
Loading adapter: .../Qwen2.5-3B_d000_v2_s42/lora_adapter
```
→ v2 eval 用的是 v2_s42（alpha=16）

### 结论

1. **Baseline eval（3B d000_s123）用的是 alpha=32 的原始 checkpoint**，不是 registry 中记录的 v2 版本
2. d000_s123（alpha=32，May 14）和 d000_v2_s123（alpha=16，May 15）是两个不同的 checkpoint
3. **全部 0.5B 和 1.5B checkpoint 均为 alpha=32，从未被重训**
4. 3B 中只有 5/11 个 checkpoint 是 alpha=16（v2 修复版 + 部分后续训练），其余 6 个仍为 alpha=32
5. **3B d005_s123（May 15 23:03）和 d025_s123（May 15 22:42）在 v2 修复之后仍训出 alpha=32**，说明这些训练命令未显式传 `--lora-alpha 16`

---
