# setup home eval env

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_home-eval-env_20260517T094051_result.json`
- **Structured JSON:** [`9f4ac01ff11136db1c57.json`](../../sessions/9f/9f4ac01ff11136db1c57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输受限于 MCP 工具输出大小和服务器间网络隔离。但 `eval_repo_cls.py` 已验证可直接用于 DeepSeek CLS eval。以下是完整 checklist：

---

```
❌ eval_deepseek_repo.py 存在
   → 不存在于 home，存在于 seetacloud
   → 替代方案：eval_repo_cls.py 已验证可用于 CLS eval（支持 DeepSeek via detect_model_family）
✅ transformers 版本: 4.57.6
✅ torch 版本: 2.10.0+cu128, CUDA: True
✅ peft 版本: 0.19.1
✅ datasets: ok
✅ sklearn 版本: 1.7.2
✅ DeepSeek base model 路径: ~/.cache/huggingface/hub/models--deepseek-ai--deepseek-coder-6.7b-instruct (snapshot e5d64addd26a)
✅ Tokenizer: 从 base model 加载（内置于 checkpoint，无需单独路径）
✅ Repo-level test data: /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl (9784 instances)
✅ Repo-level val data: /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_val.jsonl (9335 instances)
✅ Dry-run 通过（eval_repo_cls.py --model_name deepseek-ai/deepseek-coder-6.7b-instruct --dry_run）
✅ GPU: RTX 5090, 32GB VRAM, 32GB free

需要提前做的事项：
- [ ] 传输 eval_deepseek_repo.py（两台服务器无法互联，需手动 scp 或通过中间节点）
      临时方案：直接用 eval_repo_cls.py --model_name deepseek-ai/deepseek-coder-6.7b-instruct 做 CLS eval
- [ ] DeepSeek LoRA checkpoint 尚未训练（seetacloud 上也没有），需先训练才能 eval
- [ ] eval_deepseek_repo.py 的 --base_model 默认路径 /root/autodl-tmp/... 需改为 deepseek-ai/deepseek-coder-6.7b-instruct（HF cache 会自动命中本地）
```

**结论**: 环境就绪，所有依赖和数据已到位。唯一 blocker 是没有 DeepSeek LoRA checkpoint 可供 eval。一旦训练完成，直接运行：
```bash
python3 eval_repo_cls.py --checkpoint_dir &lt;path> --model_name deepseek-ai/deepseek-coder-6.7b-instruct --split test --device cuda:0
```

---
