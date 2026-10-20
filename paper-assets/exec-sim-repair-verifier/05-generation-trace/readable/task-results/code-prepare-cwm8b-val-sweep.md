# code prepare cwm8b val sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-cwm8b-val-sweep_20260515T234937_result.json`
- **Structured JSON:** [`884fdb164ea3df81770a.json`](../../sessions/88/884fdb164ea3df81770a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总

### 1. 可用 Checkpoints（5 个）

| Checkpoint | 备注 |
|---|---|
| checkpoint-400 | 早期训练（step 400） |
| checkpoint-5700 | |
| checkpoint-5800 | |
| checkpoint-5900 | |
| checkpoint-6000 | 最新 |

`save_total_limit` 已清除中间 checkpoint，只保留了 400 和最后连续 4 个。

### 2. Dry-run 结果：成功

- 3/3 样本正确（label=pass, pred=pass）
- unparseable: 0
- 生成长度: mean=4050.7 chars, median=4124.0, max=5036（接近 max_new_tokens=1024 tokens 上限）
- 模型生成了完整的 pytest 模拟输出（不是简单 pass/fail，而是完整 trace）
- **速度: ~37 秒/样本**（batch_size=1, SDPA attention, 无 flash_attn）

### 3. Unparseable 统计

**无需修改脚本。** 已内置：
- `n_cwm_unparseable` 写入 summary JSON
- 每条预测有 `"unparseable": true/false` 字段
- 无法解析时 fallback 到 majority class

### 4. Val Sweep 文件

- `val_sweep_cwm8b.sh` — 自动化全流程脚本（Round 1: 4 GPU 并行 5700-6000, Round 2: ckpt-400）
- `val_sweep_cwm8b_commands.txt` — 单条命令列表

### 5. 耗时估算（核心问题）

| 参数 | 值 |
|---|---|
| Val 样本数 | 9,335 |
| batch_size (auto) | 2（val split 自动设置） |
| 每样本速度 | ~37s (bs=1), 估 ~25s (bs=2) |
| **单 checkpoint 耗时** | **~65 小时** |
| 4 GPU 并行 Round 1 | ~65 小时 |
| Round 2 (ckpt-400) | +65 小时 |
| **总计** | **~130 小时 (5.4 天)** |

### 6. GPU 分配方案

训练完成后 4 卡全空：
- **Round 1**: ckpt-5700→cuda:0, 5800→cuda:1, 5900→cuda:2, 6000→cuda:3
- **Round 2**: ckpt-400→cuda:0

### 7. 严重时间问题 — 建议

65 小时/checkpoint 太慢，主因：
1. **无 flash_attn**（当前用 SDPA）— 安装后推理速度可能提升 30-50%
2. **模型生成接近满 1024 tokens** — CWM 输出完整 execution trace
3. **SDPA + 8192 context + bf16** 的组合较慢

可选加速方案：

| 方案 | 预计改善 | 备注 |
|---|---|---|
| 安装 flash_attn | ~1.5x | `pip install flash-attn --no-build-isolation` |
| 减少 val 样本到 2000 | ~4.7x | 加 `--max_samples 2000`，但正式 eval 不建议 |
| 跳过 ckpt-400 | 省 1 round | 早期 checkpoint，大概率质量差 |
| batch_size=4 + 看 VRAM | ~1.3x | 8B + LoRA + 8192 ctx 可能 OOM |

**建议优先级**：先装 flash_attn，然后 4 卡并行跑 5700-6000（跳 400），预计降到 ~40 小时。是否需要我现在装 flash_attn 到服务器？

---
