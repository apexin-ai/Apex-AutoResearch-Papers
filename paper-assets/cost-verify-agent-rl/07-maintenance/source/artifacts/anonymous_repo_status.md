# Anonymous Repository Status

## Repository
- **URL**: https://github.com/anonymous-nlp-2026-2/cost-verify-agent-rl
- **Branch**: main
- **Commit**: `d57f53edef2194da63a01a736ddb6e9e2e58e077`
- **Message**: "Initial release: Sign Misattribution in Step-Independent Agent RL"
- **File count**: 1947 (excluding .git)
- **Push date**: 2026-05-23

## Anonymization Checklist
- [x] Personal identifiers (caoxiaoyu, caoxiaoyuyuyuyuyu, 1844118046) — not found in source
- [x] Email addresses (qq.com, personal emails) — clean (only third-party verl docs contain mp.weixin.qq.com URLs)
- [x] GitHub token — cleaned from remote URL after push
- [x] `/root/autodl-tmp/` paths → replaced with `./checkpoints`, `./models`, `/data`
- [x] `/root/cost-verify-agent-rl` paths → replaced with `.`
- [x] `/root/runs/` paths → replaced with `./logs/`, `./runs/`
- [x] wandb entity — none hardcoded (commented out in init_wandb.sh)
- [x] No `.env`, `.git`, `wandb/`, `checkpoints/`, model weights, or logs included
- [x] No files > 50MB

## Excluded Content
- `.git/` history
- `wandb/`, `wandb_tmp/` logs
- `data/`, `checkpoints/`, model weights (*.pt, *.bin, *.safetensors, *.ckpt)
- `.env`, `*.log`, `logs/`, `ray_results/`, `ray_tmp/`
- Project management files (ROADMAP.md, memory.md, ideas.md, artifacts/, .claude/, etc.)
- RAGEN PDFs (RAGEN.pdf, RAGEN-2.pdf)
- RAGEN/outputs/ (hydra run configs)
- ragen.egg-info/
- All .bak files

## Retained Third-Party Content
- `RAGEN/verl/` — verl project (third-party, has its own author info and emails in docs)
- `RAGEN/external/` — kimina-lean-server, webshop-minimal (third-party)
- `RAGEN/README.md` — original RAGEN project README with original authors' citations

## Notes
- `/root/miniconda3` paths remain in shell scripts — this is a standard conda path, not identifying
- Server on bjb1-17606 still has the anon_repo at `/root/autodl-tmp/anon_repo/`
