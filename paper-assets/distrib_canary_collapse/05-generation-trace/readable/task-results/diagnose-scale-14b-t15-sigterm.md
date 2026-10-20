# diagnose scale 14b t15 sigterm

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t15_sigterm_20260522T091110_result.json`
- **Structured JSON:** [`7b7865293f2b02b63ed8.json`](../../sessions/7b/7b7865293f2b02b63ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结论

### 根因：外部 SIGTERM（非 OOM）

Exit code 143 = SIGTERM (signal 15)。Linux OOM killer 发送的是 SIGKILL (signal 9, exit code 137)，不是 SIGTERM。两个进程在 17:07:58 CST 几乎同一秒被 kill，日志中无任何 OOM/error 信息，确认是**外部主动发送 SIGTERM**。

同一时段 t10 实验组（scale_14b_t10_a060/a075）也被杀/重启过多次（有 _v2 日志），说明可能是另一个 agent session 在管理 GPU 分配时批量杀进程。与 C004 约束描述的模式一致。

### 进度

| 实验 | Gen 0 | Gen 1 | Gen 2+ |
|------|-------|-------|--------|
| a050 (α=0.50) | 完成 (ppl=19.83) | 完成 (ppl=20.89, mauve=0.033) | 被 kill |
| a060 (α=0.60) | 完成 (ppl=19.83) | 完成 (ppl=30.40, mauve=0.033) | 被 kill |

两个实验各完成 **2/15 代**（gen_0 baseline + gen_1），在 gen_2 "Generating synthetic data" 阶段被终止。

### Checkpoint 状态

两个实验的 gen_1 checkpoint 完整保存（~5.3GB model.safetensors）：
- `results/phase_diagram/t15_a050_s42_fp32_14b/gen_1/checkpoint/`
- `results/phase_diagram/t15_a060_s42_fp32_14b/gen_1/checkpoint/`

gen_2 目录为空（kill 发生在数据生成阶段，未写入任何文件）。

### 当前状态：已自动恢复

两个实验**已经被重新启动**，正在运行：
- PID 657037 → a050 (cuda:1, 11GB, 90% util) — `--start_gen 2`
- PID 656957 → a060 (cuda:0, 11GB, 89% util) — `--start_gen 2`

**无需额外操作。** 实验已从 gen_2 恢复运行。

---
