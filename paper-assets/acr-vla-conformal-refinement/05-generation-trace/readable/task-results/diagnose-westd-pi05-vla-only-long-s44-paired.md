# diagnose westd pi05 vla only long s44 paired

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-pi05-vla-only-long-s44-paired_20260526T131625_result.json`
- **Structured JSON:** [`fa47890caea0171494d6.json`](../../sessions/fa/fa47890caea0171494d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志已经给出了完整答案。

## 诊断报告

### 失败根因：**实验实际上成功完成了**

日志显示实验完整跑完了全部 10 个 task × 20 rollouts = 200 次评估，并输出了最终结果：

```
Overall success rate (vla_only): 96.0% (192/200)
[eval] Results saved to logs/eval_long_vla_only_pi05_seed44_westd.json
EXIT_CODE=129
```

**EXIT_CODE=129 (SIGHUP) 发生在结果写入之后。** 最可能的原因是：实验完成后 tmux/shell session 断开（例如 tmux server 超时、SSH 连接关闭），此时 SIGHUP 信号发给了已经完成写入但尚未干净退出的 Python 进程。Python 进程在 `sys.exit(0)` 或清理阶段收到 SIGHUP，导致退出码被覆盖为 128+1=129。

**这不是 OOM、不是手动 kill、不是崩溃。**

### 实验进度

- 10/10 tasks 全部完成
- 200/200 rollouts 全部完成
- 总体 SR = **96.0%** (192/200)

各 task 明细：
| Task | SR |
|------|-----|
| LIVING_ROOM_SCENE2 (soup+sauce) | 95.0% |
| LIVING_ROOM_SCENE2 (cheese+butter) | 100.0% |
| KITCHEN_SCENE3 (stove+moka) | 95.0% |
| KITCHEN_SCENE4 (bowl+drawer) | 100.0% |
| LIVING_ROOM_SCENE5 (mugs+plates) | 95.0% |
| STUDY_SCENE1 (book+caddy) | 100.0% |
| LIVING_ROOM_SCENE6 (mug+pudding) | 95.0% |
| LIVING_ROOM_SCENE1 (soup+cheese) | 95.0% |
| KITCHEN_SCENE8 (moka pots) | 90.0% |
| KITCHEN_SCENE6 (mug+microwave) | 95.0% |

### 结果文件

输出文件存在且完整：`/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_pi05_seed44_westd.json` (1795 bytes)

### 结论

**无需重跑。** 实验已成功完成，结果文件完整。EXIT_CODE=129 是假阳性——SIGHUP 发生在结果保存之后。可以直接使用该 JSON 结果。GPU cuda:5 上当前仍有 ~10.5GB 显存占用（可能是模型未完全释放），其余 GPU 空闲。

---
