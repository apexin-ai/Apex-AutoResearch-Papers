# ops m64 train exit diagnosis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m64-train-exit-diagnosis_20260521T023947_result.json`
- **Structured JSON:** [`bc3db4edbca9f9eddc01.json`](../../sessions/bc/bc3db4edbca9f9eddc01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：train_openvla_sc_m64_seed42_v3 失败 — 磁盘写满。**

- 训练本身正常运行到 step 50000/100000（loss ~2.5-2.9, eval_loss=2.9016）
- 在 step 50000 保存 checkpoint 时 crash：`RuntimeError: PytorchStreamWriter failed writing file`
- 根因：westd-41074 数据盘 250G/250G（100% 满）
- checkpoint_step50000.pt（14G）存在但损坏
- cuda:3 已释放

已完成：
- Registry: `train_openvla_sc_m64_seed42_v3` → DONE(failed)
- Cron: `train_openvla_sc_m64_seed42` 已删除

**⚠️ 紧急风险：M96 训练（同一磁盘，cuda:2，当前 step 40450）也会在下一次 checkpoint save 时 crash。** 磁盘上有 M128 旧 checkpoint（38G）和 M64 损坏 checkpoint（14G），合计 52G 可清理。建议尽快清理磁盘以拯救 M96 训练。

---
