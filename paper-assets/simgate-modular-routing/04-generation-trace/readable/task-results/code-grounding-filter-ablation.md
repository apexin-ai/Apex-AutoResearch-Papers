# code grounding filter ablation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grounding-filter-ablation_20260518T214714_result.json`
- **Structured JSON:** [`59b73fb7606772b122aa.json`](../../sessions/59/59b73fb7606772b122aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 仍在 GPU 0 上运行（29.5GB / 32.6GB）。

## Dry-run 结果汇报

### 实验代码
- **主脚本**: `/root/autodl-tmp/simgate-modular-routing/run_grounding_filter_ablation.py`
- **Wrapper**: `/root/autodl-tmp/simgate-modular-routing/run_grounding_filter_wrapper.sh`

### Dry-run 结果（chemistry-mix, 1 episode）
- **拦截正常工作**: 5 次 `focus on` 被拦截（step 15/20/22/25/26），agent 每次成功重选了替代 action
- **被拦截的 focus on 对象**: kitchen, orange, inventory, picture, picture
- **最终仍死亡**: step 27（remaining=3，进入放行窗口）时 agent `focus on picture` → score -100
- **0 次 passthrough**（没有重试耗尽的情况）
- **耗时**: 28 steps / 25.6s（~0.9s/step）

### Filter 逻辑
- 在 step 0~26（max_steps=30 时 remaining > 3）拦截所有 `focus on`
- 拦截后移除所有 `focus on` 选项，给 agent 反馈消息要求重选
- 最多重试 3 次/step，超过则放行
- 最后 3 步放开 `focus on` 允许答案提交

### vLLM 服务状态
- **端口**: 8000，GPU 0（RTX 5090）
- **模式**: enforce-eager（CUDA graph 与 RTX 5090 不兼容）
- **状态**: 运行中，保持不动

### 完整实验运行命令
```bash
cd /root/autodl-tmp/simgate-modular-routing
bash run_grounding_filter_wrapper.sh
```
或不重启 vLLM（当前已在运行）：
```bash
cd /root/autodl-tmp/simgate-modular-routing
python run_grounding_filter_ablation.py \
  --episodes-per-task 20 --max-steps 30 \
  --model Qwen2.5-7B-Instruct \
  --api-base http://localhost:8000/v1 \
  --seed 42 --output-dir results/grounding_filter_ablation/
```

### 预计运行时间
- 10 tasks × 20 episodes × ~30 steps × ~0.9s/step ≈ **5400s (~1.5h)**
- filter retries 会增加 ~15% 开销 → **~1.7h**

### 关键发现
dry-run 中 agent 即便被拦截 5 次 focus on，在放行窗口内仍然对错误对象执行了 focus on，支持"死亡脆弱性是结构性的"假说。200 episodes 的完整数据将给出统计结论。

---
