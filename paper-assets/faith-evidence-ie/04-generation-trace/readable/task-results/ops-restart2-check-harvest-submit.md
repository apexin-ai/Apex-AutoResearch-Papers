# ops restart2 check harvest submit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart2_check_harvest_submit_20260520T032606_result.json`
- **Structured JSON:** [`f15357356661906be616.json`](../../sessions/f1/f15357356661906be616.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部在运行中：

1. **eval_llama_rsft_s43_no_evidence** (PID 745299) — 运行 1h15m，推理进度 59% (145/247)，预计还需 ~50min
2. **llama_rsft_s44_pipeline** (cuda:3) — eval 阶段，推理进度 64% (158/247)，预计还需 ~45min
3. **plan017_14b_rsft_generate** (PID 712685) — 运行 9h53m，生成进度 51% (1540/3027)，format_ok_rate=99.8%，truncation_rate=6.5%，mean_diversity=7.4/8，预计还需 ~10h

前两个 eval 约 1 小时内完成，届可收割结果并启动后续 SFT 任务。14B 生成还需较长时间。

---
