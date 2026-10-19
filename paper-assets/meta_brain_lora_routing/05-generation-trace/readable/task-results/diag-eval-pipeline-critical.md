# diag eval pipeline critical

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_pipeline_critical_20260516T122143_result.json`
- **Structured JSON:** [`0bfacb0765c9d92de08f.json`](../../sessions/0b/0bfacb0765c9d92de08f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已完成。

---

## 总结

### 根因

**`evaluate_libero_plus.py:211-212` — 图像只做了垂直翻转，缺少水平翻转**

```diff
- agentview = np.ascontiguousarray(obs["agentview_image"][::-1])
- wrist = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1])
+ agentview = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
+ wrist = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
```

### 影响机制

1. 模型训练数据使用 180° 旋转（垂直+水平翻转）
2. 我们只做了垂直翻转 → 图像左右镜像
3. 模型看到镜像图像 → 预测的空间动作方向全反
4. 第一步就偏，后续 observation 也持续错误 → cascading divergence
5. 到 step 40-60 action 值已经完全发散到 ±5，机器人飞离工作区

### 修复状态

已在服务器上直接修复 `/root/meta_brain_lora_routing/phase1/evaluate_libero_plus.py`。训练不受影响（训练管线不使用这个文件）。修复后重跑 eval 即可验证。

---
