# infra gemini extraction prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gemini-extraction-prep_20260521T225721_result.json`
- **Structured JSON:** [`f8a641b1d625e72978a1.json`](../../sessions/f8/f8a641b1d625e72978a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

---

## 汇报

### 1. Mistral:8004 状态：✅ 运行中

- PID 466338，GPU3 (CUDA_VISIBLE_DEVICES=3)
- 模型: `Mistral-7B-Instruct-v0.3`, max_model_len=8192
- API 响应正常

### 2. 路径确认

| 项目 | 路径 |
|------|------|
| SC traces (95条) | `/root/symb_invariant_consensus/results/exp_d135_frontier_scb/google_gemini-2.5-pro/intermediates/` (folio_0~94.json) |
| 已完成 extraction | `/root/symb_invariant_consensus/results/exp_d135_frontier_scb/google_gemini-2.5-pro/cross_model/cross_model_mistral.json` (95条, acc=86.32%) |
| 脚本 | `/root/symb_invariant_consensus/scripts/cross_model_extract.py` |

### 3. 启动命令（增量模式）

```bash
cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python scripts/cross_model_extract.py \
  --traces-dir results/exp_d135_frontier_scb/google_gemini-2.5-pro/intermediates/ \
  --api-base http://localhost:8004/v1 \
  --output results/exp_d135_frontier_scb/google_gemini-2.5-pro/cross_model/cross_model_mistral.json \
  --resume \
  > /tmp/gemini_extraction_full.log 2>&1 & echo "PID=$!"
```

`--resume` 机制：读取 output 文件中已有的 `problem_id` 集合，跳过已完成的 95 条，只处理新增 traces。

### 4. 时间预估

- 已完成 95 条用时 1554.5s → **~16.4s/问题**
- 若 FOLIO 全集 204 题，剩余 109 条 → **预计 ~30 分钟**
- 若总数不同，按 `(N - 95) × 16.4s` 估算

**前置条件全部就绪**，等 westd-25068 恢复后 sync 剩余 traces 到 intermediates 目录即可直接执行上述命令。

---
