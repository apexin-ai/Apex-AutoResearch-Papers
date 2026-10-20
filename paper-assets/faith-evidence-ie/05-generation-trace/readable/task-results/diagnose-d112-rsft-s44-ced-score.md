# diagnose d112 rsft s44 ced score

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d112_rsft_s44_ced_score_20260519T033040_result.json`
- **Structured JSON:** [`0b1327b75f09378572be.json`](../../sessions/0b/0b1327b75f09378572be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d112_rsft_s44_ced_score 诊断

**根因：之前的失败是历史问题，当前已被重新启动且正在运行。**

证据：
- tmux session `d112_ced_score` 存在（创建于今天 11:20:09）
- PID 604576 在 GPU 0 上运行（1492MiB），执行 `freige.training.rsft_score_filter`
- 输入：`/root/autodl-tmp/rsft_generations_4b_sft_s44`（注意是 **4b_sft** 不是之前名称里的 8B）
- 输出：`/root/autodl-tmp/rsft_scored_4b_sft_s44`
- 进度：3500/24216 records（14.4%），~1.5min/500条，预计还需约 1 小时
- 脚本位置：`/root/autodl-tmp/scripts/d112/step2_ced_score.sh`（不在 freige/scripts 下）
- 日志：`/root/autodl-tmp/logs/d112_ced_score.log`

修复建议：无需修复，正在运行中。之前 5× dead 的根因无法追溯（无旧日志），但当前实例正常。

---

## plan019_1_7b_rsft_s43 诊断

**根因：训练已正常完成，"5× dead" 是误报。**

证据：
- 3021 samples ÷ (batch=4 × grad_accum=4) = 189 steps/epoch × 3 epochs = **567 steps**
- `checkpoint-567`（最终 checkpoint）和 `adapter_model.safetensors`（278MB）均存在，时间戳 11:18
- 进程正常退出，tmux session 已消失
- 无 sentinel 文件/W&B 上报 → 监控系统检测不到完成信号 → 误判为 dead

修复建议：无需重试。标记为 **completed**。可直接用 `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43` 的 adapter 进行 eval。

---

## RUNNING 实验状态

**plan019_8b_rsft_s44_eval：存活** ✓
- PID 598911 在 GPU 3 运行（18882MiB，66% util）
- 进度：116/247 batches（47%），已运行 ~1h20m，预计还需 ~1.5h
- 日志：`/root/autodl-tmp/eval_results/rsft_8b_k1_s44_eval.log`

**plan019_1_7b_rsft_s44：已完成（非失败）**
- PID 602749 不存在，GPU 1 空闲
- 输出目录 `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44/` 有完整的 `checkpoint-567` + `adapter_model.safetensors`（278MB，11:29）
- 与 s43 相同模式：训练跑完 567 步正常退出，监控误判
- 标记为 **completed**

---

## nvidia-smi 输出

| GPU | 显存 | 进程 | 用途 |
|-----|------|------|------|
| 0 | 1501/32607 MiB | PID 604576 | d112 CED scoring（NLI-DeBERTa）|
| 1 | 0 MiB | 空 | 可用 |
| 2 | 0 MiB | 空 | 可用 |
| 3 | 18891/32607 MiB | PID 598911 | 8B eval inference |

---

## 重试建议

1. **d112_rsft_s44_ced_score**：正在跑，不需重试。等 ~1h 完成。
2. **plan019_1_7b_rsft_s43**：已完成，不需重试。更新 registry 为 completed，排队 eval。
3. **plan019_1_7b_rsft_s44**：已完成，不需重试。更新 registry 为 completed，排队 eval。
4. **可立即启动的工作**：GPU 1 和 GPU 2 空闲，可用于 1.7B s43/s44 的 eval（注意遵守 C001：eval 前确认目标 GPU 显存 < 2GB ✓）。

---
