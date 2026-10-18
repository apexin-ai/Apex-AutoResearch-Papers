# exp pythia14b constrained pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pythia14b_constrained_pipeline_20260515T123706_result.json`
- **Structured JSON:** [`59644f7622a4a7977bda.json`](../../sessions/59/59644f7622a4a7977bda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正常运行中。Solver 结果和 concentration 数据已出：

- **t1=0.0289, t5=0.2439** — 确认 Flat shape
- **Constrained**: 372×4bit + 4×8bit + 8×2bit (受 max_2bit=8 约束)
- **Unconstrained**: 90×2bit + 249×4bit + 45×8bit
- **Uniform-4bit**: 384×4bit

正在跑 BF16 baseline PPL eval（563 chunks），预计 4 个 eval 共 ~10-15min。

产出汇总：
1. **脚本**: `/root/ratekv/run_pythia14b_constrained_pipeline.py`（本地 + 远程）
2. **Dry-run**: solver OK，profiles 加载正确，模型加载成功，eval 已开始
3. **PID**: 333915
4. **预计完成**: ~15min 后（4 轮 WikiText-2 eval，563 chunks/轮）
5. **输出 JSON**: `/root/ratekv/artifacts/pythia14b_constrained_pipeline_results.json`
6. **日志**: `/tmp/pythia14b_constrained.log`

---
