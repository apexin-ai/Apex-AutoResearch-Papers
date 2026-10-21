# fix mauve gpt2large and resume both

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mauve_gpt2large_and_resume_both_20260517T200842_result.json`
- **Structured JSON:** [`2d2154060192cfa90214.json`](../../sessions/2d/2d2154060192cfa90214.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

1. **方案 A 成功** — gpt2-large 已在 `/root/autodl-tmp/.hf_cache/hub/models--gpt2-large/` 缓存中，设置 `HF_ENDPOINT=https://hf-mirror.com` 后从缓存正常加载，无需方案 B（跳过 MAUVE）。

2. **Pythia-1.4B 恢复**：先计算 gen_7 metrics（`compute_gen7_metrics.py`），再 `--start_gen 8`。
   - gen_7 metrics: ppl=466.84, entropy=1.2829, eff_rank=102.9, mauve=0.0294
   - 已进入 Generation 8/10
   - PID: 292246 (cuda:1)
   - 日志: `~/runs/distrib_canary_collapse/generalize_pythia14b_wiki_a100_s42.log`

3. **C4 seed-43**：已由另一个 Worker 启动（PID 291516，cuda:0），当前在 Generation 0 (baseline)，运行正常，未重复启动。
   - 日志: `~/runs/distrib_canary_collapse/generalize_pythia1b_c4_a100_s43.log`

4. **初始日志确认**：两个实验均无错误，MAUVE 正常工作。

---
