# Server Status Check — 2026-05-21 17:02 UTC

## westd-17855 (6× RTX PRO 6000 Blackwell, 98GB each)

| GPU | exp_id | Status | PID | Gen Progress | Current Activity | Output Dir |
|-----|--------|--------|-----|--------------|------------------|------------|
| 0 | alpha_sweep_a000_s47_fp32 | RUNNING | 454255 | 5/10 complete | Generating synth data for gen_5 | results/alpha_sweep/a000_s47_fp32 |
| 1 | gen_gpt2m_s43_fp32 | RUNNING | 442662 | 9/10 complete | Training gen_9 (last gen) | results/generalize/gpt2m_wiki_a100_s43_fp32 |
| 2 | alpha_sweep_a000_s45_fp32 | RUNNING | 448950 | 8/10 complete | Generating synth data for gen_8 | results/alpha_sweep/a000_s45_fp32 |
| 3 | scale_69b_a100_s43_bf16 | RUNNING | 400550 | 7/10 complete | Training gen_7 (97%, ~4897/5000 steps) | results/scale_check/pythia69b_wiki_a100_s43_bf16 |
| 4 | alpha_sweep_a052_s43_fp32 | RUNNING | 454331 | 5/10 complete | Generating synth data for gen_5 | results/alpha_sweep/a052_s43_fp32 |
| 5 | alpha_sweep_a046_s43_fp32 | RUNNING | 454886 | 5/10 complete | Training gen_5 (77%, 3896/5000 steps) | results/alpha_sweep/a046_s43_fp32 |

GPU memory: all 6 GPUs active (14.2–70.8 GiB used). GPU utilization 63–99%.

**Note**: tmux session `interv_react_s43` still alive (PID 382885) but experiment `reactive_d1_s43_fp32` already completed (gen_0–gen_10). No active python process — just leftover shell.

## westd-19828 (2× RTX PRO 6000 Blackwell, 98GB each)

| GPU | exp_id | Status | PID | Gen Progress | Current Activity | Output Dir |
|-----|--------|--------|-----|--------------|------------------|------------|
| 0 | alpha_sweep_a000_s48_fp32 | RUNNING | 656193 | 2/10 complete | Generating synth data for gen_2 | results/alpha_sweep/a000_s48_fp32 |
| 1 | alpha_sweep_a000_s46_fp32 | RUNNING | 647974 | 6/10 complete | Training gen_6 (6%, 362/5000 steps) | results/alpha_sweep/a000_s46_fp32 |

GPU memory: both GPUs active (~14.5 GiB each). GPU utilization 79–80%.

## Summary

**All 8 experiments confirmed RUNNING** — active python processes on GPUs with real memory utilization.

Closest to completion:
1. **gen_gpt2m_s43_fp32** — 9/10 gens done, training final gen (~1–2h left)
2. **scale_69b_a100_s43_bf16** — 7/10, gen_7 at 97% (~minutes to gen_8 start)
3. **alpha_sweep_a000_s45_fp32** — 8/10, starting gen_8

Furthest from completion:
1. **alpha_sweep_a000_s48_fp32** — only 2/10 gens done (started later, ~16:10 UTC)

## 需要的操作

1. **Registry PID update**: 6 experiments have pid=? in registry — update with actual PIDs:
   - a000_s47_fp32: PID 454255
   - gen_gpt2m_s43_fp32: PID 442662
   - a000_s45_fp32: PID 448950
   - a052_s43_fp32: PID 454331
   - a046_s43_fp32: PID 454886
   - a000_s46_fp32: PID 647974
2. **Cron registration**: Only scale_69b has a cron. The other 7 experiments are running via tmux/nohup/direct bash — they have no auto-completion detection. Consider adding monitoring crons or polling scripts.
3. **Cleanup**: tmux session `interv_react_s43` on 17855 can be killed — experiment already completed.
