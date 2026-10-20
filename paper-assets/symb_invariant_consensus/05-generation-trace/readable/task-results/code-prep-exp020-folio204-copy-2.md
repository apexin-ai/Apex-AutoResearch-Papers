# code prep exp020 folio204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp020-folio204_20260517T085951_result.json`
- **Structured JSON:** [`29e41166d50f41d74893.json`](../../sessions/29/29e41166d50f41d74893.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，无需创建。以下是验证报告：

## exp-020 脚本状态：Ready-to-run

**脚本路径**: `/root/symb_invariant_consensus/scripts/run_exp020_llama8b_folio204.sh`

**验证通过项**:
| 项目 | 状态 |
|------|------|
| 模型路径 | `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/` — 4 shards 完整 |
| 数据文件 | `data/folio_full.json` — 204 条记录，格式正确（含 premises_fol, conclusion_fol） |
| 评估脚本 | `run_full_mvp.py` 存在，`--folio-data` / `--no-proofwriter` 参数已确认 |
| 辅助文件 | `data/empty.json` 存在（用于 --math-data 占位） |
| 语法检查 | `bash -n` 通过 |

**配置参数**:
- K=12, T=0.7, max-tokens=4096, seed=42
- vLLM: max-model-len=8192, gpu-memory-utilization=0.90
- 输出: `results/exp020_llama8b_folio204/`

**预估运行指标**:
- GPU 内存: ~18-20GB（LLaMA-8B FP16，98GB 卡绰绰有余）
- 运行时间: ~40-60 分钟（204 题 × K=12 = 2448 次推理，vLLM batch 加速）
- vLLM 启动: ~30-60 秒

**运行命令**:
```bash
nohup bash /root/symb_invariant_consensus/scripts/run_exp020_llama8b_folio204.sh > /tmp/exp020.log 2>&1 &
```

---
