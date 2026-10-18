# infra local openrouter setup

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_local-openrouter-setup_20260522T132529_result.json`
- **Structured JSON:** [`ec5e4004397f86cdf687.json`](../../sessions/ec/ec5e4004397f86cdf687.json)

## Before a recorded user message

1 recorded events

### Log line

_source line 1_

{
  "raw": "汇报：\n\n| 项目 | 状态 |\n|------|------|\n| seetacloud scoring 进程 | 已 kill（或已无进程） |\n| 文件拉取 | 全部成功：5 src + 1 script + 23 checkpoints + 1 taxonomy data (5.7MB) |\n| Checkpoint 数量 | 23/23（claude-3-haiku 14 + gpt-4o 9） |\n| 数据 | MMLU 300 pairs, ARC 300 pairs |\n| 依赖安装 | venv 已创建，requests + numpy 已安装 |\n| 脚本路径调整 | 全部改为本地相对路径（`_SCORING_ROOT` 动态计算） |\n| API 配置 | `API_BASE = \"https://openrouter.ai/api/v1\"`, `API_KEY = [REDACTED]"OPENROUTER_API_KEY\"]` |\n| 并发配置 | 所有 batch max_workers=5, max_rps=5.0 |\n| Import 测试 | OK |\n| OpenRouter 连通性 | HTTP 200, gpt-4o-mini 响应正常 |\n\n**Ready to start.** 启动命令：\n\n```bash\nexport OPENROUTER_API_KEY=\"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\"\ncd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scoring\n.venv/bin/python3 scripts/run_plan001_step1_batched.py\n```"
}


---
