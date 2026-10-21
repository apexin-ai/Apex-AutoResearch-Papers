# eval exp 035 arc60 s2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-035-arc60-s2_20260518T155700_result.json`
- **Structured JSON:** [`becdd8b3cbc02f2b0010.json`](../../sessions/be/becdd8b3cbc02f2b0010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

前 2 题都正确（SICA 和 SC 都对），第 3 题进行中。平均 30s/题，ETA ~29 分钟。

实验稳定运行中。总结如下：

**exp-035 状态：RUNNING**

| 项目 | 详情 |
|------|------|
| 服务器 | westd-16639, cuda:3 (RTX PRO 6000 Blackwell 98GB) |
| 模型 | Qwen2.5-14B-Instruct via vLLM 0.21.0, port 8003 |
| 数据 | ARC-Challenge 60 题 (HF mirror 下载) |
| 参数 | K=12, T=0.7, T_ext=0.3, max_tokens=2048 |
| tmux | `exp035` on westd-16639 |
| 日志 | `results/qwen25_14b_arc60/run.log` |
| 输出 | `results/qwen25_14b_arc60/results.json` |
| 速度 | ~30s/题, ETA ~29 min |
| Registry | exp-035 = RUNNING |

创建的文件：
- `data/prepare_arc.py` / `data/prepare_arc_v2.py` — ARC 数据准备
- `run_arc.py` — ARC 实验主脚本（SICA vs SC@K）
- `scripts/run_exp035_arc60.sh` — 启动脚本（vLLM server + 实验）

---
