# ops urgent fix deploy v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_fix_deploy_v1_20260522T092357_result.json`
- **Structured JSON:** [`9abfe7986c6754cdf918.json`](../../sessions/9a/9abfe7986c6754cdf918.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## P0: L2norm k=0.95 Object s43 结果
状态: **完成**
SR: **98.4%** (492/500, 68.3 min)
Log: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.95_libero_object_seed43.json`
Registry 已更新为 DONE。
注：GPU 1 上有人刚启动了 v2 重跑 (PID 325931)。

## P1: l2norm_k0925_object_s43 部署
部署位置: westd-27271 GPU 0（**已在运行**）
PID: 325659（elapsed 3:26）
验证: ✓ 进程存活 / ✓ Log 存在 / ✓ 内容健康（模型已加载, pruning l2norm keep 236/256 tokens）/ ✓ GPU 占用 9700 MiB
无需重新部署。

## P2: L2norm k=0.5 Object s43 澄清
- `eval_pi05_l2norm_k05_object_seed43`: **存在, DONE, SR = 33.6%** (168/500)
- 39.2% 实际对应: **`eval_openvla_l2norm_k05_object_seed43`**（OpenVLA 实验，非 pi05）
- 无缺口，pi05 版本已完成。

## P3: westd-27271 GPU 0 部署
**无法部署** — 两个 GPU 均被占用：
- GPU 0: l2norm k=0.925 object s43 (PID 325659)
- GPU 1: l2norm k=0.95 object s43 v2 (PID 325931)

4 个候选实验已全部 DONE：
| 实验 | 状态 | SR |
|------|------|----|
| eval_pi05_l2norm_k03_object_seed43 | DONE | 55.4% |
| eval_pi05_l2norm_k05_object_seed43 | DONE | 33.6% |
| eval_pi05_random_k09_object_seed43 | DONE | 9.6% |
| eval_pi05_l2norm_k07_object_seed43 | DONE | 56.4% |

无缺口需要填补。

---
