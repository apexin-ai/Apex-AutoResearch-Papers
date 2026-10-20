# ssh check gpu state 5090 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_gpu_state_5090_5090c_20260521T101137_result.json`
- **Structured JSON:** [`f9ab63148946f66e7ab5.json`](../../sessions/f9/f9ab63148946f66e7ab5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

（`tmux ls` 被 read-only 模式拦截，已从 `ps aux` 中提取 tmux session 信息）

## autodl-5090

| GPU | 状态 | 显存 | GPU-Util | 进程 |
|-----|------|------|----------|------|
| cuda:0 | 空闲 | 2MiB / 32607MiB | 0% | — |
| cuda:1 | 空闲 | 2MiB / 32607MiB | 0% | — |
| cuda:2 | 空闲 | 2MiB / 32607MiB | 0% | — |
| cuda:3 | **占用** | 30044MiB / 32607MiB | 57% | VLLM::EngineCore (PID 8696) |

**运行中的实验**：
- `run_mvp_pilot.py` — Qwen2.5-7B-Instruct pretrained, fewnerd, n_samples=8, seed=42, `output/e2_pretrained_fewnerd/`（tmux session: `exp_e2_pretrained_fewnerd`，已运行 ~3h12m）

**report.json 状态**：
| 文件 | 状态 | 大小 | 时间 |
|------|------|------|------|
| scierc_mf4v2_seed42 | ❌ 不存在 | — | — |
| scierc_mf4v2_seed123 | ✅ 存在 | 1714B | May 21 17:33 |
| scierc_mf4v2_seed456 | ✅ 存在 | 1728B | May 21 17:33 |
| fewnerd_mf4v2_seed42 | ❌ 不存在 | — | — |
| fewnerd_mf4v2_seed123 | ❌ 不存在 | — | — |
| fewnerd_mf4v2_seed456 | ✅ 存在 | 1640B | May 21 16:06 |

---

## autodl-5090-c

| GPU | 状态 | 显存 | GPU-Util | 进程 |
|-----|------|------|----------|------|
| cuda:0 | **占用** | 30117MiB / 32607MiB | 93% | VLLM::EngineCore (PID 294412) |
| cuda:1 | 空闲 | 0MiB / 32607MiB | 0% | — |
| cuda:2 | 空闲 | 0MiB / 32607MiB | 0% | — |
| cuda:3 | 空闲 | 0MiB / 32607MiB | 0% | — |

**运行中的实验**：
- `run_mvp_pilot.py` — qwen3-8b-fewnerd-exp021-merged, fewnerd, n_samples=16, seed=456, `output/fewnerd_n16_seed456_v2/`（tmux session: `exp_fewnerd_n16_s456_v2`，已运行 ~2h54m）

**output 目录**：含 54 个子目录，近期活跃的包括 `frontier_sc_deepseek`、`frontier_sc_gemini25pro`、`frontier_sc_gpt55_fewnerd`（今天产出），以及多组 conll/scierc/fewnerd temperature 实验结果。

---

**汇总**：两台机器各有 1 张 GPU 在跑实验（5090 用 cuda:3，5090-c 用 cuda:0），各剩 3 张空闲。6 个 mf4v2 report.json 中已完成 3 个（scierc seed123/456、fewnerd seed456），缺 3 个（scierc seed42、fewnerd seed42/123）。

---
