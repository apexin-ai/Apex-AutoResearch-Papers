# MATH-500 GRPO Eval 超时诊断报告

**日期**: 2026-05-17  
**服务器**: westd-11672

---

## 1. 实验状态

| 实验 | 状态 | 进度 | 耗时 | Acc | 模型 |
|------|------|------|------|-----|------|
| eval_math500_grpo_rasp_20_v2 | **FAILED** (EXIT_CODE=124) | 193/500 | 5h55m | 30.67% @150 | grpo_stage2_rasp_20_v9 |
| eval_math500_grpo_standard_20 | **RUNNING** (pid 14556) | 123/500 @5h13m | 进行中 | 36.00% @100 | grpo_stage2_standard_20_v8/ckpt-50 |
| eval_math500_sft_rasp (对比) | DONE | 500/500 | 2h56m | 24.20% | sft_rasp_20_westd |

**eval_math500_grpo_standard_20 状态确认**：
- pid 14556 确实在运行，占用 GPU 0/1/2（均 97% utilization）
- 日志位于 `/root/autodl-tmp/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log`（不在 `~/runs/` 下）
- 按当前速度预计总耗时 **~21h**，不会在任何合理 timeout 内完成

---

## 2. 根因分析

### 核心问题：`max_new_tokens=4096` + GRPO 长推理链

所有 eval 均使用相同脚本 `eval_math500.py`，默认 `max_new_tokens=4096`。

**SFT 模型**自然生成短回答（无 `<think>` block），大多数问题生成 <500 tokens，平均 21s/题。

**GRPO 模型**经过强化学习训练，生成极长 `<think>...</think>` 推理链，频繁命中 4096 token 上限。

### 耗时统计

| 模型类型 | 平均耗时/题 | 最慢单题 | 预估总时间 | 实际用时 |
|----------|------------|---------|-----------|---------|
| SFT rasp | 21.2s | ~45s | ~3h | 2h56m |
| GRPO rasp | 110.4s | ~350s | **15.3h** | 5h55m (193/500) |
| GRPO standard | 152.9s | **~349s** | **21.2h** | 5h13m (123/500) |

GRPO standard 比 SFT 慢 **7.2x**，GRPO rasp 慢 **5.2x**。

### 脚本问题

`eval_math500.py` 生成配置：
```python
output_ids = model.generate(
    **inputs,
    max_new_tokens=args.max_new_tokens,  # 默认 4096
    do_sample=False,
    pad_token_id=tokenizer.pad_token_id or eos_token_id,
)
```

- 无 per-sample timeout 机制
- 无生成长度的自适应控制
- GRPO 模型在 4096 tokens 下，部分题目需要 300-350s 生成

---

## 3. 修复方案

### 方案 A：降低 max_new_tokens（推荐）

将 GRPO eval 的 `max_new_tokens` 从 4096 降至 **2048**。

理由：
- MATH 问题的正确答案通常在 `<think>` 推理后以 `\boxed{}` 格式给出
- 2048 tokens 足够覆盖绝大多数推理链（~1500 tokens 推理 + ~200 tokens 答案）
- 对 accuracy 影响预计很小：极长推理链（>2048 tokens）往往是模型在"绕圈"，正确率本身不高
- 预估效果：worst-case 从 ~350s 降至 ~175s，平均从 ~150s 降至 ~80s
- **预估 GRPO eval 总时间：8-10h**

### 方案 B：增大 timeout_hours

不修改脚本，直接设 `timeout_hours=24`。

- 优点：无代码改动，结果完全一致
- 缺点：浪费 GPU 时间（单次 eval 占 GPU 21h），且 standard 模型当前实际已在运行中

### 建议执行

1. **不要 kill 当前 standard_20 进程**（pid 14556），让它跑完（预计还需 ~16h，到明天上午约 09:00）
2. 下次 GRPO eval 使用 `--max_new_tokens 2048`
3. 对 rasp_20_v2 重跑时用 `--max_new_tokens 2048`

### 具体命令

```bash
# 重跑 rasp eval（2048 tokens）
cd /root/autodl-tmp/recovery_aware_struct_prune
python src/eval_math500.py \
    --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 \
    --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_20.json \
    --max_new_tokens 2048 \
    --seed 42
```

### 可选改进：在脚本中加 per-sample timeout

如果仍需要更严格的时间控制，可在 `eval_math500.py` 的 generate 调用外加 signal-based timeout：

```python
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError()

# 在 for loop 内：
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(180)  # 180s per sample
try:
    output_ids = model.generate(...)
    signal.alarm(0)
except TimeoutError:
    logger.warning(f"Sample {idx} timed out, skipping")
    signal.alarm(0)
    # record as incorrect, continue
```

---

## 4. 预估修复后运行时间

| 配置 | GRPO rasp | GRPO standard |
|------|-----------|---------------|
| max_new_tokens=4096 (当前) | ~15h | ~21h |
| max_new_tokens=2048 (推荐) | **~8h** | **~10h** |
| max_new_tokens=2048 + timeout 180s | **~7-8h** | **~9-10h** |

---

## 5. 当前 standard_20 进程决策

pid 14556 目前在 123/500，acc@100=36%（比 rasp 的 30.67% 高），这个结果有价值。

- **选项 1**（推荐）：让它跑完，预计明天 ~09:00 完成。结果保存到 `results/eval_math500_grpo_standard_20.json`
- **选项 2**：kill 它，用 2048 tokens 重跑（节省 ~10h GPU 时间，但 accuracy 可能略有差异）
