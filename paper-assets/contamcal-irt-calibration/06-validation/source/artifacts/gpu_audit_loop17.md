# GPU Audit — Loop 17
**Time**: 2026-05-16 ~23:25 CST | **Server**: cqa1-21977

## GPU Status

| GPU | PID | Runtime | Task | Status |
|-----|-----|---------|------|--------|
| 0 | — | — | — | **IDLE** |
| 1 | 800570 | 19min | Llama-3.2-3B d000 eval aligned (mmlu done 45.45%, gsm8k 3%) | Running ~2h left |
| 2 | 797754 | 40min | Qwen2.5-0.5B-Instruct eval (mmlu done, gsm8k in progress) | Running |
| 3 | 801766 | 13min | Llama-3.2-3B d025 SFT (step 314/3384, 9%) | Running ~2h left |
| 4 | 796493 | 44min | ⚠️ Llama-3.2-3B d000 eval aligned — **DUPLICATE of GPU 1** | CONFLICT |
| 5 | — | — | — | **IDLE** |

## ⚠️ Critical Issues

### C001 Violation: Duplicate Llama d000 eval (GPU 1 + GPU 4)
- **PID 796493** (GPU 4, parent 796488, PPID=1): orphaned nohup from earlier session, logging to `/tmp/llama_eval_d000_s42.log`
- **PID 800570** (GPU 1, managed via tmux `exp_001_eval_llama32_3B_d000_s42_v2`): properly managed job
- Both write to **same output dir**: `/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/`
- **Action needed**: Kill PID 796493 + 796488 (the unmanaged orphan on GPU 4) to free GPU 4 and prevent data corruption

## Completed Since Last Check

### 3B d000 s123 signals (was on cuda:2)
- **COMPLETED**: 6/9 signals computed, 2 skipped, 1 failed
- Output: `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123_a32/`
- Merged signals exist for: arc_challenge, gsm8k
- Missing: `signals_merged_mmlu.json` (only `_s4_chunks_mmlu` dir exists — incomplete)
- Process no longer running on GPU 2

### Instruct evals (recent completions, last 6h)
- `Qwen2.5-3B-Instruct_aligned/eval_results.json` ✓
- `Qwen2.5-3B-Instruct_para_aligned/eval_results.json` ✓
- `Qwen2.5-3B-Instruct_v2_aligned/eval_results.json` ✓
- `Qwen2.5-3B-Instruct_v2_para_aligned/eval_results.json` ✓
- `Qwen2.5-1.5B-Instruct_aligned/eval_results.json` ✓
- `Qwen2.5-1.5B-Instruct_para_aligned/eval_results.json` ✓

## Handoff PID Check
- PID 801761: ✅ ALIVE (Llama d025 SFT wrapper, cuda:3)
- PID 800565: ✅ ALIVE (Llama d000 eval v2 wrapper, cuda:1)
- PID 797754: ✅ ALIVE (0.5B-Instruct eval, cuda:2)
- PID 782625: ☠️ DEAD (1.5B-Instruct eval — expected)

## tmux Sessions
- `exp_001_eval_3B_d100_v2_para_aligned` — stale (May 15), no GPU process
- `exp_001_eval_llama32_3B_d000_s42_v2` — active (GPU 1)
- `exp_001_sft_llama32_3B_d025_s42` — active (GPU 3)

## Available GPUs
- **cuda:0**: IDLE, immediately available
- **cuda:4**: Will be free after killing orphan PID 796493/796488
- **cuda:5**: IDLE, immediately available

## Registry Update Needed
- 3B d000 s123 signals batch completion (6 done, 1 failed — mmlu s4 merged missing)
- 6 Instruct eval results completed but not confirmed registered
- PID 782625 (1.5B-Instruct eval) dead — check if results were saved before death

## Recommendations
1. **Kill** orphan PIDs 796493+796488 on cuda:4 (C001 violation, data corruption risk)
2. **Investigate** why `signals_merged_mmlu.json` is missing for 3B d000 s123 despite batch_complete flag
3. After cleanup: cuda:0, cuda:4, cuda:5 available → per C007, use for 0.5B/1.5B s123 signals
