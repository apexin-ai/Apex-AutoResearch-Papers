# Experiment Status Report — 2026-05-24 01:25 UTC

## GPU Status

### westd-16639 (4× H100 96GB)

| GPU | VRAM Used | Util | Process |
|-----|-----------|------|---------|
| 0 | 88.3/97.9 GB | 0% | vLLM Llama-8B (port 8009) — **IDLE, no clients** |
| 1 | 0/97.9 GB | 0% | **IDLE** |
| 2 | 90.2/97.9 GB | 0% | vLLM Qwen2.5-14B (port 8007) — **IDLE, no clients** |
| 3 | 83.4/97.9 GB | 0% | vLLM Qwen2.5-14B (port 8005) — **IDLE, no clients** |

No experiment processes running. Three vLLM servers loaded but idle.
No tmux sessions.

### westd-30973 (3× H100 96GB)

| GPU | VRAM Used | Util | Process |
|-----|-----------|------|---------|
| 0 | 0/97.9 GB | 0% | **IDLE** |
| 1 | 0/97.9 GB | 0% | **IDLE** |
| 2 | 88.3/97.9 GB | 97% | vLLM Llama-8B (port 8002) — **ACTIVE** |

Two tmux sessions: `exp-multi-seed-llama-pw-seed456-v2`, `exp-multi-seed-llama-pw-seed789-v2-resume`.

## Experiment Progress

| Server | GPU | Experiment | Progress | Status | Notes |
|--------|-----|-----------|----------|--------|-------|
| westd-30973 | 2 | llama8b_pw_seed456_v2 | **496/600** (82.7%) | 🟢 Running | Sharing vLLM on port 8002 |
| westd-30973 | 2 | llama8b_pw_seed789_v2 | **330/600** (55.0%) | 🟢 Running (resumed 01:18) | Resumed from 326, sharing port 8002 |
| westd-30973 | — | qwen25_pw_seed789_v3 | **339/600** (56.5%) | 🔴 STOPPED | Exit code 143 (SIGTERM) at May 23 12:40 UTC |
| westd-16639 | — | llama8b_pw_seed789 (orig) | **600/600** | ✅ Done | Completed May 24 00:48 |
| westd-16639 | — | qwen25_pw_seed789 (orig) | **600/600** | ✅ Done | Completed May 23 23:32 |
| westd-16639 | — | qwen25_pw_seed456 | **600/600** | ✅ Done | Completed May 23 23:03 |
| westd-16639 | — | qwen25_pw_seed123 | **600/600** | ✅ Done | Completed May 23 15:36 |
| westd-16639 | — | llama8b_pw_seed123 | **600/600** | ✅ Done | Completed May 23 16:48 |

### Multi-seed ProofWriter — Complete Matrix

| Model | seed42 | seed123 | seed456 | seed789 |
|-------|--------|---------|---------|---------|
| Mistral-7B | 600 ✅ | 600 ✅ | 600 ✅ | 600 ✅ |
| LLaMA-3.1-8B | 223 ⚠️ | 600 ✅ | 496/600 🟢 (v2) | 330/600 🟢 (v2) |
| Qwen2.5-14B | — | 600 ✅ | 600 ✅ | 600 ✅ (orig) / 339 🔴 (v3 stopped) |

### Multi-seed FOLIO — Complete (all 204/204)

| Model | seed123 | seed456 | seed789 |
|-------|---------|---------|---------|
| Mistral-7B | ✅ | ✅ | ✅ |
| LLaMA-3.1-8B | ✅ | ✅ | ✅ |
| Qwen2.5-14B | ✅ | ✅ | ✅ |

### NLI Combo — Complete

| Dataset | DeBERTa | BART | RoBERTa |
|---------|---------|------|---------|
| LogiQA-200 | ✅ | ✅ | ✅ |
| ProofWriter-600 | — | ✅ | ✅ |

## Idle GPU Summary

| Server | GPU | Status | Available VRAM |
|--------|-----|--------|----------------|
| westd-16639 | 1 | Completely idle | 97.9 GB |
| westd-16639 | 0, 2, 3 | vLLM loaded, no clients | Can free by killing vLLM |
| westd-30973 | 0 | Completely idle | 97.9 GB |
| westd-30973 | 1 | Completely idle | 97.9 GB |

**Total idle: 5 GPUs** (2 fully free + 3 with idle vLLM that can be reclaimed)

## Issues Requiring Attention

1. **qwen25_pw_seed789_v3 stopped (SIGTERM)** at 339/600 on westd-30973. No running process. Needs restart or decision on whether orig (600/600 on westd-16639) suffices.
2. **llama8b_pw_seed42** stuck at 223/600 (old run on westd-16639). No active process. Needs restart if still needed.
3. **westd-16639 has 3 idle vLLM servers** consuming ~260 GB VRAM total. Can be killed to free GPUs 0, 2, 3.
4. **Two experiments sharing one GPU** on westd-30973 (seed456_v2 + seed789_v2 both on cuda:2 via port 8002). Throughput is split.

## Candidate Deployments for Idle GPUs

- Restart qwen25_pw_seed789_v3 from 339/600 (if v3 results needed beyond orig)
- Move llama8b_pw_seed789_v2 to its own GPU to double throughput
- Start llama8b_pw_seed42 rerun (if needed for full 4-seed matrix)
- New experiments (e.g., Qwen3 PW seeds, additional datasets)
