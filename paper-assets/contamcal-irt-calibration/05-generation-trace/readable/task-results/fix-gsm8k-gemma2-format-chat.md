# fix gsm8k gemma2 format chat

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gsm8k-gemma2-format-chat_20260520T063516_result.json`
- **Structured JSON:** [`fe87cc27f23ccfe86b28.json`](../../sessions/fe/fe87cc27f23ccfe86b28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gemma-2 d000 GSM8K eval 已启动。PID 303300 在 GPU 3 上，19342 MiB 显存。模型已加载，开始 eval。

## 汇报

### 1. format_as_chat 修复详情
修复了 4 处 generation-based `format_as_chat` 调用，全部加上 `system_prompt="You are a helpful assistant."`：
- **行 321**（evaluate_gsm8k）：GSM8K 8-shot CoT eval
- **行 377**（evaluate_humaneval）：HumanEval eval
- **行 554**（evaluate_paraphrased - GSM8K 分支）：paraphrased GSM8K eval
- **行 586**（evaluate_paraphrased - HumanEval 分支）：paraphrased HumanEval eval

未修改的调用：
- 行 215, 505（log-prob MCQ 路径，不需要 system_prompt）
- 行 223, 510（generation MCQ 路径，已有 system_prompt）

`format_as_chat` 函数签名已支持 `system_prompt` 参数（default=None），无需修改函数本身。

### 2. evaluate.py 新 md5
```
17673bf373f00f83ccc41fc1d355a4cd
```

### 3. Smoke test 对比结果
- Qwen-14B d000 旧版（无 system_prompt）: **60.80%**
- Qwen-14B d000 新版（加 system_prompt）: **61.18%**
- 偏差: **+0.38pp**，在 ±1pp 范围内 → **通过**

修复不影响 Qwen 模型数据有效性，仅影响 Gemma-2 的 chat template 格式。

### 4. Gemma-2 重跑状态
- **PID**: 303300（实际 Python 进程）
- **GPU**: cuda:3，19342 MiB
- **脚本**: `run_gemma2_gsm8k_fixed.sh`，顺序跑 d000 → d100
- **日志**: `/root/contamcal-irt-calibration/gsm8k_gemma2_s42_fixed.log`
- **输出目录**: `results/gsm8k/gemma2_d000_s42_fixed/` 和 `results/gsm8k/gemma2_d100_s42_fixed/`
- 模型已加载完成，GSM8K eval 已开始

---
