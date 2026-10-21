# code pooled irt n16 script

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pooled-irt-n16-script_20260515T005717_result.json`
- **Structured JSON:** [`e3b9d1a3326160f2fa7a.json`](../../sessions/e3/e3b9d1a3326160f2fa7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run validated — exits with error as expected (N=12 < 16). Here are all three deliverables.

---

## 产出 1: 完整 model × dosage × seed 矩阵

**GPU 活跃进程：**
| GPU | PID | 任务 |
|-----|-----|------|
| 0 | — | idle |
| 1 | 475651 | eval 0.5B d005 s123 aligned |
| 2 | 473954 | eval 1.5B d100 s123 aligned |
| 3 | 466755 | SFT 3B d025 s42 (v2 重训) |
| 4 | 472742 | eval 3B d000_v2 s42 para_aligned_v2 |
| 5 | 471296 | SFT 3B d100 s123 |

**Aligned Eval 完成矩阵（pooled IRT 所需）：**

| Model | d000 s42 | d005 s42 | d025 s42 | d100 s42 | d000 s123 | d005 s123 | d025 s123 | d100 s123 |
|-------|----------|----------|----------|----------|-----------|-----------|-----------|-----------|
| **0.5B** SFT | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| **0.5B** eval | ✅ | ✅ | ✅ | ✅ | ❌ | 🏃GPU1 | ❌ | ✅ |
| **1.5B** SFT | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| **1.5B** eval | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | 🏃GPU2 |
| **3B** SFT | ✅ | ✅ | 🏃GPU3(v2) | ✅ | ✅ | ❌ | ❌ | 🏃GPU5 |
| **3B** eval | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |

**统计：**
- Aligned eval 完成：**12/24**
- 正在运行（完成后 +2）：0.5B d005 s123, 1.5B d100 s123 → **14**
- Quick wins（SFT 已完成，只需跑 eval，再 +5）：0.5B d000 s123, 1.5B d000 s123, 3B d000 s123, 3B d025 s42, 3B d100 s123 → **19**
- 需要先训 SFT 再 eval（5 个）：0.5B d025 s123, 1.5B d005 s123, 1.5B d025 s123, 3B d005 s123, 3B d025 s123

**与用户初始分析的差异：**
- 0.5B d000 s123：用户标 ✅ DONE，实际 aligned eval 缺失（仅有非 aligned 版本）
- 1.5B d000 s123 / 3B d000 s123：同上
- 3B d025 s42：SFT v1 已完成（有 lora_adapter），但正在 GPU3 重训 v2；aligned eval 缺失
- 3B d100 s123：SFT 有 lora_adapter（可能是中间检查点），GPU5 仍在训

---

## 产出 2: 脚本已部署

`/root/contamcal-irt-calibration/exp006/run_pooled_irt_n16.sh`

用法：
- `./run_pooled_irt_n16.sh --dry-run` — 只检查前置条件
- `./run_pooled_irt_n16.sh` — 完整运行（N≥16 时）
- `./run_pooled_irt_n16.sh --oracle` — 强制使用 oracle exposure

逻辑：自动检查 24 个 aligned eval → N<16 则报错退出并列出缺失 → 检查 S1 信号覆盖（当前不完整，自动 fallback 到 oracle-exposure）→ 对 ARC 和 GSM8K 分别跑 pooled IRT（warmup=2000, samples=2000）。

---

## 产出 3: Dry-run 验证结果

```
Aligned evals complete: 12/24
SFT done, eval needed:  7
SFT missing:            5

ERROR: N=12 < 16. Cannot run pooled IRT.

Quick wins (SFT done, just run aligned eval):
  - 0.5B d000 s123, 0.5B d005 s123
  - 1.5B d000 s123, 1.5B d100 s123
  - 3B d000 s123, 3B d025 s42, 3B d100 s123

Need SFT + eval:
  - 0.5B d025 s123, 1.5B d005 s123, 1.5B d025 s123
  - 3B d005 s123, 3B d025 s123
```

**达到 N≥16 的最短路径**：等 GPU 1/2 上的 eval 完成（+2=14），再跑 d000 s123 × 3 models 的 aligned eval（+3=17）。这 3 个 d000 s123 的 SFT 已经完成，只需 eval。

---
