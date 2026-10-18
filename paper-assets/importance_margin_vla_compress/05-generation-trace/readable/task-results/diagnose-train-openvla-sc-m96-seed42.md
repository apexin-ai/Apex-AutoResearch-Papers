# diagnose train openvla sc m96 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_openvla_sc_m96_seed42_20260520T040532_result.json`
- **Structured JSON:** [`a07634ee56009e0af9ff.json`](../../sessions/a0/a07634ee56009e0af9ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。磁盘充足（根分区 9G free，数据盘 812G free）。

## 诊断结论

**根因：提交实验时配置文件不存在。**

config 文件 Birth 时间对比：

| 配置文件 | Birth 时间 | 实验提交时间 | 结果 |
|---------|-----------|------------|------|
| `openvla_smart_compress_m128.yaml` | **01:32** | 02:33 | cuda:0 正常运行 |
| `openvla_smart_compress_m96.yaml` | **11:40** | 03:28 | 03:28时不存在 → 崩溃 |
| `openvla_smart_compress_m64.yaml` | **11:40** | 03:28 | 03:28时不存在 → 崩溃 |
| `*vtconly*` 系列 | **从未创建** | 03:22 | 不存在 → 崩溃 |

- vtconly 变体：configs 目录下**从未存在**任何含 "vtconly" 的 yaml 文件
- m96/m64 非 vtconly 变体：配置文件直到 **11:40 才被创建**（Birth 时间），提交时（03:28）不存在
- 训练脚本 `train_openvla_smart_compress.py` 通过 `open(config_path)` 加载 yaml，文件不存在会抛 `FileNotFoundError` 立即退出
- vtconly ~1min 标记失败 vs 非 vtconly ~35min 标记失败的差异是监控轮询间隔，实际进程都是秒级崩溃
- GPU 硬件无问题：4 卡 RTX PRO 6000 Black 全部健康，当前 GPU 0/2/3 正在正常训练
- 11:40 创建配置文件后重启的 m96/m64 已正常训练到 step 450+/500+

```json
{"root_cause":"FileNotFoundError: config files openvla_smart_compress_m96.yaml / m64.yaml (Birth=11:40) did not exist at job submission time (03:22-03:28); vtconly configs never existed at all","error_type":"infrastructure","fix_steps":["已自动修复：m96/m64 配置文件在 11:40 创建，重启后正常训练中","vtconly 实验需确认是否仍需要——如需要，须先创建对应 vtconly 配置文件再提交"],"can_auto_fix":false,"affected_gpus":"cuda:2,3","healthy_gpus":"cuda:0,1,2,3"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "FileNotFoundError: config files openvla_smart_compress_m96.yaml / m64.yaml (Birth=11:40) did not exist at job submission time (03:22-03:28); vtconly configs never existed at all",
    "error_type": "infrastructure",
    "fix_steps": [
      "已自动修复：m96/m64 配置文件在 11:40 创建，重启后正常训练中",
      "vtconly 实验需确认是否仍需要——如需要，须先创建对应 vtconly 配置文件再提交"
    ],
    "can_auto_fix": false,
    "affected_gpus": "cuda:2,3",
    "healthy_gpus": "cuda:0,1,2,3"
  }
}
```

</details>

---
