# ops multi diagnosis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_multi-diagnosis_20260516T175241_result.json`
- **Structured JSON:** [`8527c4a0ad07a75e4a2e.json`](../../sessions/85/8527c4a0ad07a75e4a2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，以下是三个任务的结论。

---

### 任务 A：d025 SFT — 成功 ✓

训练正常完成（EXIT_CODE=0, epoch=1.0），merged 模型已存在。

| 指标 | 值 |
|------|-----|
| train_loss | 1.5265 |
| mean_token_accuracy | 0.6755 |
| runtime | 8349s (~2.3h) |
| checkpoint | `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/` |

Registry 已更新：status→DONE, conclusion→success, metrics/checkpoint_path/log_path 均已写入。无后续操作。

---

### 任务 B：gsm8k signals 失败 — 根因：路径不一致，但数据已存在

注册命令的 output_dir 是非标路径 `/root/autodl-tmp/exp002/signals_15B_instruct_gsm8k/`，该目录**从未创建**。但 gsm8k signals 已经完整存在于标准路径：

```
/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/
  signal_s1_embedding_gsm8k.json   (734KB, May 17 01:29)
  signal_s2_minkpp_gsm8k.json      (272KB, May 17 01:33)
  signal_s4_selfcritique_gsm8k.json (316KB, May 17 01:39)
  signals_merged_gsm8k.json        (243KB, May 17 01:39)
```

**失败根因**：注册的 output_dir 与脚本实际写入路径不匹配。监控系统在错误路径检查 sentinel，因此反复报 "process dead, no sentinel"。实际数据由同一或另一个进程写入了标准路径，gsm8k 1.5B-Instruct signals 已完成。

Registry 中无此 exp_id（可能已被删除或注册名不同）。**后续操作**：无需重跑，但应更新相关 registry 条目标记数据位置，并修复未来 Instruct 模型 signals 的 output_dir 模板，统一使用 `/root/autodl-tmp/exp002/signals/{model_name}/` 格式。

---

### 任务 C：PID 818742 — 已死亡，Other 域缺失

PID 818742 已不存在。输出目录有 7/8 domain 的 `irt_results.json`：

| 已完成 | 缺失 |
|--------|------|
| STEM_Math, STEM_Science, STEM_CS_Eng, Medical, Humanities, Social_Sciences, Business_Law | **Other** |

"Other" 域无目录、无文件。进程在完成 Business_Law（最后一个有结果的域，22:50）后死亡，未启动 Other 计算。

**后续操作**：需要重新运行 `run_mmlu_domain_gamma_n24.py`，仅计算 Other 域（如果脚本支持单域参数），或重跑全部（已完成的域应会跳过）。这是 CPU 任务，不占 GPU。

---
