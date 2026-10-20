# code d036 gpu experiment prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d036-gpu-experiment-prep_20260517T120242_result.json`
- **Structured JSON:** [`7fc7c3f4c76cd7f60420.json`](../../sessions/7f/7fc7c3f4c76cd7f60420.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个脚本全部通过语法检查。总结：

| 脚本 | 模型 | 数据 | 预计时间 |
|------|------|------|---------|
| `run_temperature_ablation.sh` | Qwen2.5-14B | D012 (60题) × 3温度 | ~3h |
| `run_exp012_gsm8k.sh` | Qwen2.5-14B | GSM8K 30题 | ~1h |
| `run_exp004_qwen7b.sh` | Qwen2.5-7B* | D012 (60题) | ~2h |
| `run_mistral_strategyqa.sh` | Mistral-7B | StrategyQA 60题 | ~1.5h |

**注意事项：**
- Qwen2.5-7B-Instruct 当前不在服务器上，`run_exp004_qwen7b.sh` 包含了自动通过 modelscope 下载的逻辑（首次运行会多花 10-15 分钟下载）
- 所有脚本已改用端口检测替代 `pkill`——如果端口被占用会报错退出而非强杀进程
- GSM8K 数据 (`data/gsm8k_200.json`) 和 StrategyQA 数据 (`data/strategyqa_200.json`) 均已就绪
- 建议执行顺序：temperature_ablation → gsm8k → mistral_strategyqa → qwen7b（下载耗时放最后）

---
