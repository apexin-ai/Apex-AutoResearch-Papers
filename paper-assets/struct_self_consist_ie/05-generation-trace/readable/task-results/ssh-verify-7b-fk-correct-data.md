# ssh verify 7b fk correct data

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-7b-fk-correct-data_20260520T081620_result.json`
- **Structured JSON:** [`f6b9ef8979320a8cf271.json`](../../sessions/f6/f6b9ef8979320a8cf271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 数据验证
- 路径确认: **1/3 存在**
  - `qwen25_7b_n8_seed42/full_signal_report.json` ✓（1984 bytes, May 20 12:06）
  - `qwen25_7b_n8_seed123/` 目录存在但为空（无 samples.jsonl，无 report）
  - `qwen25_7b_n8_seed456/` 目录不存在
- 数据来源: Qwen2.5-7B FewNERD（确认非 LLaMA）
- hostname: `autodl-container-jb1uyxxe0t-1a1cc6c5`

## FK Signal 结果
- **seed42: FK ρ = 0.2822**
- seed123: **缺失** — 推理未完成（无 samples.jsonl）
- seed456: **缺失** — 推理未完成（目录都不存在）
- 3-seed mean: **无法计算**，仅 1/3 seed 有数据

## 补算可行性
- `compute_signals.py` 支持 FK（使用 `fleiss_kappa_surface`），但前提是需要 `samples.jsonl` 推理输出
- **瓶颈不在 signal 计算，而在推理**：seed123 和 seed456 的 FewNERD 推理还没跑，必须先跑推理生成 `samples.jsonl`，之后才能算 signal
- 补算 signal 的命令（推理完成后）：
  ```bash
  python3 code/pipeline/compute_signals.py \
    --input-dir output/fewnerd_7b/qwen25_7b_n8_seed{123,456} \
    --model-size 7 --regime ft
  ```

---
