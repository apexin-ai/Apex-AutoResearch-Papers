# code prep temp ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-temp-ablation_20260517T120251_result.json`
- **Structured JSON:** [`f6d4b9ec41099ea61331.json`](../../sessions/f6/f6d4b9ec41099ea61331.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本已创建并验证完毕。

| 脚本 | 温度 | 输出目录 |
|------|------|----------|
| `scripts/run_exp021_temp_t03.sh` | T=0.3 | `results/exp021_temp_t03/` |
| `scripts/run_exp022_temp_t05.sh` | T=0.5 | `results/exp022_temp_t05/` |
| `scripts/run_exp023_temp_t10.sh` | T=1.0 | `results/exp023_temp_t10/` |

所有脚本共享参数：
- 模型：`/root/autodl-tmp/models/Qwen2.5-14B-Instruct`（路径已确认存在）
- 数据：`proofwriter_30.json` + `folio_30.json`（60 problems，路径已确认）
- K=12, seed=42, max-tokens=4096
- 包含 vLLM cleanup、conda 激活、vLLM 启动等待、运行后清理

脚本已 `chmod +x`，未启动实验。三个脚本需顺序执行（共用 GPU port 8000）。

---
