# diagnose train openvla sc m64 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_openvla_sc_m64_seed42_20260520T040546_result.json`
- **Structured JSON:** [`20fa25ad2166b1482815.json`](../../sessions/20/20fa25ad2166b1482815.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结果汇总：**

**实验 1 & 2（vtconly）**— 根因确定：`train_openvla_vtc.py` 脚本在服务器上不存在。`ls` 确认只有 `train_openvla_smart_compress.py`。进程启动即 exit（`python: can't open file`），反复重试 5 次都立即失败，没有 sentinel/W&B 输出。服务器上也没有这两个实验的日志文件。

**实验 3 & 4（smart_compress m96/m64）**— 已自动恢复并正在运行。当前 GPU 2 上 PID 68539（非原始 66050）、GPU 3 上 PID 68852（非原始 66389），说明原进程崩溃后被重启。日志显示：
- m96: step 450/100000, loss=4.33, sps=0.5（正常）
- m64: step 500/100000, loss=3.67, sps=0.6（正常）

原始 m96/m64 崩溃的痕迹保留在 checkpoint 中（`checkpoint_step443.pt` 和 `checkpoint_step458.pt` 时间戳 11:37），但日志已被重启覆盖（当前日志从 11:40 开始、step 0 重新训练而非 resume）。

**GPU/磁盘状态正常**：4× RTX PRO 6000 96GB，温度 31-55°C，磁盘 46GB 可用。

```json
{"root_cause":"train_openvla_vtc.py: No such file or directory — 脚本未部署到服务器；m96/m64 smart_compress 原始进程崩溃原因不明（日志被重启覆盖），但已自动恢复运行","error_type":"infrastructure","fix_steps":["将 train_openvla_vtc.py 部署到 /root/autodl-tmp/importance_margin_vla_compress/","重新提交 vtconly m96 和 m64 实验","m96/m64 smart_compress 已在运行无需操作，但注意当前从 step 0 重训而非 resume checkpoint"],"can_auto_fix":true,"affected_exps":["train_openvla_sc_m96_vtconly_seed42","train_openvla_sc_m64_vtconly_seed42","train_openvla_sc_m96_seed42","train_openvla_sc_m64_seed42"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "train_openvla_vtc.py: No such file or directory — 脚本未部署到服务器；m96/m64 smart_compress 原始进程崩溃原因不明（日志被重启覆盖），但已自动恢复运行",
    "error_type": "infrastructure",
    "fix_steps": [
      "将 train_openvla_vtc.py 部署到 /root/autodl-tmp/importance_margin_vla_compress/",
      "重新提交 vtconly m96 和 m64 实验",
      "m96/m64 smart_compress 已在运行无需操作，但注意当前从 step 0 重训而非 resume checkpoint"
    ],
    "can_auto_fix": true,
    "affected_exps": [
      "train_openvla_sc_m96_vtconly_seed42",
      "train_openvla_sc_m64_vtconly_seed42",
      "train_openvla_sc_m96_seed42",
      "train_openvla_sc_m64_seed42"
    ]
  }
}
```

</details>

---
