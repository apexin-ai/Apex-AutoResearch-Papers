# GPU Health Check — Loop 10
**Time**: 2026-05-15 20:43 UTC

## GPU Overview

| GPU | VRAM Used | Util | Temp | Power | Processes |
|-----|-----------|------|------|-------|-----------|
| 0 | 14903/24564 MiB (61%) | 57% | 48°C | 212/425W | PID 549516 (1.5B d025 SFT) |
| 1 | 15967/24564 MiB (65%) | 98% | 61°C | 285/425W | PID 549858 (1.5B d005 SFT) |
| 2 | 22942/24564 MiB (93%) | 100% | 67°C | 342/425W | PID 553256 (0.5B base eval, 3612 MiB) + PID 555936 (3B d005 SFT child, 19316 MiB) |
| 3 | 8985/24564 MiB (37%) | 67% | 53°C | 198/425W | PID 551219 (3B d000 eval) |
| 4 | 19289/24564 MiB (79%) | 100% | 71°C | 358/425W | PID 556016 (3B d025 SFT child) |
| 5 | 8985/24564 MiB (37%) | 65% | 52°C | 188/425W | PID 551290 (3B d005 s42 eval) |

## Process Status (All 8 Alive)

| PID | Task | Uptime | GPU | Status |
|-----|------|--------|-----|--------|
| 528993 | exp_004 gamma sweep (CPU) | 4h 07m | CPU | ✅ Running |
| 549516 | 1.5B d025 s123 SFT | 1h 38m | cuda:0 | ✅ Running |
| 549858 | 1.5B d005 s123 SFT | 1h 38m | cuda:1 | ✅ Running |
| 551219 | 3B d000 s123 eval | 1h 30m | cuda:3 | ✅ Running |
| 551290 | 3B d005 s42 eval | 1h 30m | cuda:5 | ✅ Running |
| 553256 | 0.5B base eval | 1h 12m | cuda:2 | ✅ Running |
| 555931 | 3B d005 s123 SFT (wrapper) | 44m | cuda:2 (child PID 555936) | ✅ Running |
| 556011 | 3B d025 s123 SFT (wrapper) | 44m | cuda:4 (child PID 556016) | ✅ Running |

## 3B SFT Training Progress

### 3B d005 s123 (cuda:2, PID 555931→555936)
- **Progress**: step 715/3177 (22.5%), epoch ~0.23
- **Loss**: ~1.08–1.19, token accuracy ~0.73–0.75
- **Speed**: ~3.5–4.0 s/step
- **ETA**: ~2h 35m remaining

### 3B d025 s123 (cuda:4, PID 556011→556016)
- **Progress**: step 893/3384 (26.4%), epoch ~0.26
- **Loss**: ~1.09–1.24, token accuracy ~0.73–0.76
- **Speed**: ~2.7–3.2 s/step
- **ETA**: ~2h 05m remaining

## Eval Progress

### 0.5B base pretrained (cuda:2, PID 553256)
- **MMLU**: ✅ Complete (14042 items)
- **GSM8K**: 689/1319 (52%), ~7.2 s/item → ~1h 16m left for GSM8K
- **Remaining benchmarks**: arc_challenge, humaneval
- **Total estimated remaining**: ~2.5–3h

### 3B d000 s123 aligned (cuda:3, PID 551219)
- **MMLU**: ✅ Complete
- **GSM8K**: 676/1319 (51%), ~7.6 s/item → ~1h 21m left for GSM8K
- **Remaining benchmarks**: arc_challenge, humaneval
- **Total estimated remaining**: ~2.5–3h

### 3B d005 s42 aligned (cuda:5, PID 551290)
- **MMLU**: ✅ Complete
- **GSM8K**: 652/1319 (49%), ~7.8 s/item → ~1h 27m left for GSM8K
- **Remaining benchmarks**: arc_challenge, humaneval
- **Total estimated remaining**: ~3h

## Notes
- GPU 2 heavily loaded (93% VRAM) with both 0.5B eval + 3B SFT — both progressing fine
- GPU 4 running warm (71°C, 358W) under 3B SFT — within safe limits
- All evals hit non-fatal `libnvJitLink.so.13` warning but continued successfully
- No processes dead or stuck; all showing active progress
