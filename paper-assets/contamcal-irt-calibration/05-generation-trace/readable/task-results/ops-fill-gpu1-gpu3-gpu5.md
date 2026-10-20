# ops fill gpu1 gpu3 gpu5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-gpu1-gpu3-gpu5_20260515T110656_result.json`
- **Structured JSON:** [`60d56ce721b4e82c8cf6.json`](../../sessions/60/60d56ce721b4e82c8cf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。两个 eval 进程已正确运行在目标 GPU 上。

## 提交结果

### GPU 任务

| GPU | 任务 | PID | VRAM | 状态 |
|-----|------|-----|------|------|
| 0 | 1.5B d025 s123 SFT | 549516 | 14892 MiB | 已有 |
| 1 | 1.5B d005 s123 SFT | 549858 | 15958 MiB | **已在运行（v2），跳过** |
| 2 | 0.5B base eval | 530893 | 8216 MiB | 已有 |
| 3 | **3B d000 s123 aligned eval** | **551219** | **6782 MiB** | **新提交 ✓** |
| 4 | 1.5B base eval | 530975 | 5674 MiB | 已有 |
| 5 | **3B d005 s42 aligned eval** | **551290** | **6782 MiB** | **新提交 ✓** |

### GPU 1 未提交原因
PID 549858 正在运行完全相同的 1.5B d005 s123 SFT 训练（运行约 5 分钟），对应 registry `exp_001_sft_15B_d005_s123_v2`。按 C001 不重复提交。

### Eval 候选选择逻辑
- **GPU 3: 3B_d000_s123** — checkpoint 有但完全无 aligned eval dir（P1 s123 + P2 3B）
- **GPU 5: 3B_d005_s42** — checkpoint 有但无标准 aligned eval（P2 3B）

### CPU 状态
- **PID 528993** (extreme gamma sweep): 存活，运行 2h32m33s
- **exp004 目录**: 不存在
- **2PL matched/v3 结果**: 均不存在

### 附注
修复了 registry.yaml 中两处 YAML 解析错误（`C004 violation:` 冒号未转义）。`libnvJitLink.so.13` 警告是已知非致命问题，eval 已正常开始 mmlu 评估。

---
