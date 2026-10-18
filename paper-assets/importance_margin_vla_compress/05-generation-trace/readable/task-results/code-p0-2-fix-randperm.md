# code p0 2 fix randperm

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0-2-fix-randperm_20260523T142628_result.json`
- **Structured JSON:** [`f63eb36d5e0b52b485b3.json`](../../sessions/f6/f63eb36d5e0b52b485b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。所有 `torch.randperm` 调用现在都不再传 `device=` 参数（`evaluate.py` 的 `device="cpu"` 保持不变，本身就是正确的）。

## 修改汇总

| 服务器 | 修改文件数 | 修改详情 |
|--------|-----------|---------|
| **westd-27271** | 5 | `eval_openvla_l2norm_libero.py:138`, `eval_openvla_libero.py:135`, `eval_pi05_pruning_libero.py:58`, `eval_xvla_pruning_libero.py:105+108`, `test_openvla_load.py:73` |
| **cqa1-33015** | 4 | `eval_openvla_pruning_libero.py:107+110`, `eval_pi05_libero.py:98`, `eval_pi05_pruning_libero.py:58`, `eval_xvla_pruning_libero.py:105+108` |
| **westd-41074** | 6 | `eval_oft_libero.py:182`, `eval_oft_prune_libero.py:107`, `eval_openvla_l2norm_libero.py:138`, `eval_openvla_libero.py:137`, `eval_pi05_libero.py:98`, `eval_pi05_pruning_libero.py:61+206` |
| **westd-38929** | 6 | `eval_oft_libero.py:223`, `eval_openvla_l2norm_libero.py:135`, `eval_openvla_libero.py:135`, `eval_pi05_libero.py:98`, `eval_pi05_pruning_libero.py:58`, `eval_xvla_pruning_libero.py:105+108` |

所有修改统一模式：`torch.randperm(N)` 在 CPU 生成随机排列，末尾 `.to(device)` 移回 GPU。跨服务器相同 seed 现在会产生相同的 permutation。

---
