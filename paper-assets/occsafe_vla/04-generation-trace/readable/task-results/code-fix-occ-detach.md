# code fix occ detach

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_occ_detach_20260520T103506_result.json`
- **Structured JSON:** [`27bf98eed87630ce2e21.json`](../../sessions/27/27bf98eed87630ce2e21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0,1,2 的 vanilla 训练进程（PID 100203/97847/98174）未受影响，显存占用与修改前完全一致。

---

## 总结

### 修复内容

`/root/occsafe_vla/openvla-oft/vla-scripts/finetune.py` L306：

```
修复前: occ_detach=True,    (函数默认值硬编码 True)
修复后: occ_detach=False,   (函数默认值改为 False)
```

其余不变：L94 config 默认值保持 `True`，L1129 训练调用 `occ_detach=cfg.occ_detach` 已正确传参。

### 分析说明

实际上 L1129 的训练调用**已经**显式传了 `occ_detach=cfg.occ_detach`，所以 L306 的函数默认值对训练路径无影响。`--occ_detach false` 经 draccus 解析后 `cfg.occ_detach=False`，通过 L1129 正确传入 `run_forward_pass`。L306 的默认值仅在 L751 的 validation 调用中生效（但 validation 不传 `occ_head`，occ 分支整个被跳过，所以也无影响）。

修改 L306 为 `False` 的意义：防止未来新增调用者遗漏 `occ_detach` 参数时意外截断梯度。

### 5-step 验证结果

| 测试项 | 结果 |
|---|---|
| `--occ_detach false` 解析为 `False` | PASS |
| `occ_detach=False` 时 patch_features 不 detach | PASS |
| backward 后 vision_param.grad 非 None（norm=0.000675） | PASS |
| `occ_detach=True` 时 grad 为 None（对照） | PASS |
| vanilla 训练不受影响 | PASS（PID/显存不变） |

---
