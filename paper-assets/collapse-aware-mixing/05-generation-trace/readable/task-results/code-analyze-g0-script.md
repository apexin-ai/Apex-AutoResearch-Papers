# code analyze g0 script

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze_g0_script_20260512T171452_result.json`
- **Structured JSON:** [`56e723277448eb822ba5.json`](../../sessions/56/56e723277448eb822ba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。

`/root/collapse-aware-mixing/analyze_g0.py` 已部署到服务器，功能：
- 自动发现 `checkpoint-{step}` 目录并按 step 排序
- 复用 `metrics.py` 的 `compute_spectral_effective_rank` 和 `compute_perplexity`
- 生成双 y 轴时序图 (PNG) 和结构化结果 (JSON)
- 基于 1σ 阈值自动判定 GO/NO-GO

G0 完成后运行：
```bash
python analyze_g0.py \
  --checkpoint-dir /root/autodl-tmp/output/G0/training \
  --output-dir /root/autodl-tmp/output/g0_analysis
```

---
