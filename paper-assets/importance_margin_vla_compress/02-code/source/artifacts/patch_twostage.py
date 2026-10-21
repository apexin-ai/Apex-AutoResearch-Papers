"""Patch train_twostage.py to support Full FT mode (twostage_fullft)."""

filepath = "/root/autodl-tmp/importance_margin_vla_compress/train_twostage.py"
with open(filepath, "r") as f:
    content = f.read()

original = content

# ============================================================
# 1. Add get_expert_params() after get_acis_params()
# ============================================================
old_1 = 'def get_acis_params(model) -> List[torch.nn.Parameter]:\n    return list(model.acis.parameters())'

new_1 = '''def get_acis_params(model) -> List[torch.nn.Parameter]:
    return list(model.acis.parameters())


def get_expert_params(model) -> List[torch.nn.Parameter]:
    """Non-ACIS trainable params for Full FT mode. Call before stage freeze/unfreeze."""
    acis_param_ids = {id(p) for p in model.acis.parameters()}
    return [p for p in model.parameters() if id(p) not in acis_param_ids and p.requires_grad]'''

assert old_1 in content, "PATCH 1: old text not found"
content = content.replace(old_1, new_1, 1)

# ============================================================
# 2. Modify verify_grad_state() to support fullft mode
# ============================================================
old_2 = '''def verify_grad_state(model, stage: str, dry_run: bool = False):
    lora_params = get_lora_params(model)
    acis_params = get_acis_params(model)
    lora_trainable = sum(p.requires_grad for p in lora_params)
    acis_trainable = sum(p.requires_grad for p in acis_params)
    log.info("[%s] LoRA params: %d total, %d trainable", stage, len(lora_params), lora_trainable)
    log.info("[%s] ACIS params: %d total, %d trainable", stage, len(acis_params), acis_trainable)
    if dry_run:
        if stage == "stage1":
            assert lora_trainable == 0, f"Stage1: LoRA should be frozen but {lora_trainable} are trainable"
            assert acis_trainable == len(acis_params), f"Stage1: all ACIS params should be trainable"
        elif stage == "stage2":
            assert acis_trainable == 0, f"Stage2: ACIS should be frozen but {acis_trainable} are trainable"
            assert lora_trainable == len(lora_params), f"Stage2: all LoRA params should be trainable"'''

new_2 = '''def verify_grad_state(model, stage: str, dry_run: bool = False,
                     train_mode: str = "twostage", expert_params=None):
    acis_params = get_acis_params(model)
    acis_trainable = sum(p.requires_grad for p in acis_params)

    if train_mode == "twostage_fullft":
        expert_trainable = sum(p.requires_grad for p in expert_params) if expert_params else 0
        log.info("[%s] Expert params: %d total, %d trainable", stage, len(expert_params or []), expert_trainable)
        log.info("[%s] ACIS params: %d total, %d trainable", stage, len(acis_params), acis_trainable)
        if dry_run:
            if stage == "stage1":
                assert expert_trainable == 0, f"Stage1: expert should be frozen but {expert_trainable} are trainable"
                assert acis_trainable == len(acis_params), f"Stage1: all ACIS params should be trainable"
            elif stage == "stage2":
                assert acis_trainable == 0, f"Stage2: ACIS should be frozen but {acis_trainable} are trainable"
                assert expert_trainable == len(expert_params), f"Stage2: all expert params should be trainable"
    else:
        lora_params = get_lora_params(model)
        lora_trainable = sum(p.requires_grad for p in lora_params)
        log.info("[%s] LoRA params: %d total, %d trainable", stage, len(lora_params), lora_trainable)
        log.info("[%s] ACIS params: %d total, %d trainable", stage, len(acis_params), acis_trainable)
        if dry_run:
            if stage == "stage1":
                assert lora_trainable == 0, f"Stage1: LoRA should be frozen but {lora_trainable} are trainable"
                assert acis_trainable == len(acis_params), f"Stage1: all ACIS params should be trainable"
            elif stage == "stage2":
                assert acis_trainable == 0, f"Stage2: ACIS should be frozen but {acis_trainable} are trainable"
                assert lora_trainable == len(lora_params), f"Stage2: all LoRA params should be trainable"'''

assert old_2 in content, "PATCH 2: old text not found"
content = content.replace(old_2, new_2, 1)

# ============================================================
# 3. Modify verify_gradients_after_backward() to support fullft
# ============================================================
old_3 = '''def verify_gradients_after_backward(model, stage: str):
    lora_params = get_lora_params(model)
    acis_params = get_acis_params(model)
    if stage == "stage1":
        lora_with_grad = sum(1 for p in lora_params if p.grad is not None and p.grad.abs().sum() > 0)
        acis_with_grad = sum(1 for p in acis_params if p.grad is not None and p.grad.abs().sum() > 0)
        log.info("[stage1 grad check] LoRA with grad: %d (expect 0), ACIS with grad: %d",
                 lora_with_grad, acis_with_grad)
        assert lora_with_grad == 0, f"Stage1: LoRA got gradients ({lora_with_grad} params)"
    elif stage == "stage2":
        acis_with_grad = sum(1 for p in acis_params if p.grad is not None and p.grad.abs().sum() > 0)
        lora_with_grad = sum(1 for p in lora_params if p.grad is not None and p.grad.abs().sum() > 0)
        log.info("[stage2 grad check] ACIS with grad: %d (expect 0), LoRA with grad: %d",
                 acis_with_grad, lora_with_grad)
        assert acis_with_grad == 0, f"Stage2: ACIS got gradients ({acis_with_grad} params)"'''

new_3 = '''def verify_gradients_after_backward(model, stage: str, train_mode: str = "twostage", expert_params=None):
    acis_params = get_acis_params(model)
    if train_mode == "twostage_fullft":
        if stage == "stage1":
            expert_with_grad = sum(1 for p in (expert_params or []) if p.grad is not None and p.grad.abs().sum() > 0)
            acis_with_grad = sum(1 for p in acis_params if p.grad is not None and p.grad.abs().sum() > 0)
            log.info("[stage1 grad check] Expert with grad: %d (expect 0), ACIS with grad: %d",
                     expert_with_grad, acis_with_grad)
            assert expert_with_grad == 0, f"Stage1: expert got gradients ({expert_with_grad} params)"
        elif stage == "stage2":
            acis_with_grad = sum(1 for p in acis_params if p.grad is not None and p.grad.abs().sum() > 0)
            expert_with_grad = sum(1 for p in (expert_params or []) if p.grad is not None and p.grad.abs().sum() > 0)
            log.info("[stage2 grad check] ACIS with grad: %d (expect 0), Expert with grad: %d",
                     acis_with_grad, expert_with_grad)
            assert acis_with_grad == 0, f"Stage2: ACIS got gradients ({acis_with_grad} params)"
    else:
        lora_params = get_lora_params(model)
        if stage == "stage1":
            lora_with_grad = sum(1 for p in lora_params if p.grad is not None and p.grad.abs().sum() > 0)
            acis_with_grad = sum(1 for p in acis_params if p.grad is not None and p.grad.abs().sum() > 0)
            log.info("[stage1 grad check] LoRA with grad: %d (expect 0), ACIS with grad: %d",
                     lora_with_grad, acis_with_grad)
            assert lora_with_grad == 0, f"Stage1: LoRA got gradients ({lora_with_grad} params)"
        elif stage == "stage2":
            acis_with_grad = sum(1 for p in acis_params if p.grad is not None and p.grad.abs().sum() > 0)
            lora_with_grad = sum(1 for p in lora_params if p.grad is not None and p.grad.abs().sum() > 0)
            log.info("[stage2 grad check] ACIS with grad: %d (expect 0), LoRA with grad: %d",
                     acis_with_grad, lora_with_grad)
            assert acis_with_grad == 0, f"Stage2: ACIS got gradients ({acis_with_grad} params)"'''

assert old_3 in content, "PATCH 3: old text not found"
content = content.replace(old_3, new_3, 1)

# ============================================================
# 3b. Modify run_stage signature to accept train_mode/expert_params
# ============================================================
old_3b = '''def run_stage(
    model, dataloader, stage, forward_fn, optimizer, scheduler,
    total_steps, config, device, output_dir, dry_run=False, graceful=None,
):'''

new_3b = '''def run_stage(
    model, dataloader, stage, forward_fn, optimizer, scheduler,
    total_steps, config, device, output_dir, dry_run=False, graceful=None,
    train_mode="twostage", expert_params=None,
):'''

assert old_3b in content, "PATCH 3b: old text not found"
content = content.replace(old_3b, new_3b, 1)

old_3c = '            verify_gradients_after_backward(model, stage)'
new_3c = '            verify_gradients_after_backward(model, stage, train_mode=train_mode, expert_params=expert_params)'
assert old_3c in content, "PATCH 3c: old text not found"
content = content.replace(old_3c, new_3c, 1)

# ============================================================
# 4a. Add train_mode reading after twostage_cfg parsing
# ============================================================
old_4 = '    stage2_warmup = twostage_cfg.get("stage2_warmup_steps", 1000)\n\n    if args.max_steps:'

new_4 = '    stage2_warmup = twostage_cfg.get("stage2_warmup_steps", 1000)\n    train_mode = twostage_cfg.get("train_mode", "twostage")\n\n    if args.max_steps:'

assert old_4 in content, "PATCH 4a: old text not found"
content = content.replace(old_4, new_4, 1)

# ============================================================
# 4b. After model loading, capture expert_params for fullft mode
# ============================================================
old_4b = '    log.info("Loading dataset...")'

new_4b = '''    # For fullft mode, capture expert params before any stage freeze/unfreeze
    if train_mode == "twostage_fullft":
        expert_params = get_expert_params(model)
        log.info("Full FT mode: %d expert params, %d ACIS params",
                 len(expert_params), sum(1 for _ in model.acis.parameters()))
    else:
        expert_params = None

    log.info("Loading dataset...")'''

assert old_4b in content, "PATCH 4b: old text not found"
content = content.replace(old_4b, new_4b, 1)

# ============================================================
# 4c. Modify Stage 1 freeze/verify logic
# ============================================================
old_4c = '''    if not skip_stage1:
        log.info("=" * 60)
        log.info("STAGE 1: Freeze LoRA, train ACIS (margin_loss only)")
        log.info("=" * 60)

        lora_params = get_lora_params(model)
        acis_params = get_acis_params(model)
        freeze_params(lora_params)
        unfreeze_params(acis_params)
        verify_grad_state(model, "stage1", dry_run=args.dry_run)'''

new_4c = '''    if not skip_stage1:
        log.info("=" * 60)
        if train_mode == "twostage_fullft":
            log.info("STAGE 1: Freeze expert, train ACIS (margin_loss only) [Full FT]")
        else:
            log.info("STAGE 1: Freeze LoRA, train ACIS (margin_loss only)")
        log.info("=" * 60)

        acis_params = get_acis_params(model)
        if train_mode == "twostage_fullft":
            freeze_params(expert_params)
        else:
            lora_params = get_lora_params(model)
            freeze_params(lora_params)
        unfreeze_params(acis_params)
        verify_grad_state(model, "stage1", dry_run=args.dry_run,
                         train_mode=train_mode, expert_params=expert_params)'''

assert old_4c in content, "PATCH 4c: old text not found"
content = content.replace(old_4c, new_4c, 1)

# ============================================================
# 4d. Modify Stage 1 run_stage call
# ============================================================
old_4d = '''        completed = run_stage(
            model=model, dataloader=dataloader, stage="stage1",
            forward_fn=stage1_forward, optimizer=optimizer1, scheduler=scheduler1,
            total_steps=stage1_steps, config=config, device=device,
            output_dir=output_dir, dry_run=args.dry_run, graceful=graceful,
        )'''

new_4d = '''        completed = run_stage(
            model=model, dataloader=dataloader, stage="stage1",
            forward_fn=stage1_forward, optimizer=optimizer1, scheduler=scheduler1,
            total_steps=stage1_steps, config=config, device=device,
            output_dir=output_dir, dry_run=args.dry_run, graceful=graceful,
            train_mode=train_mode, expert_params=expert_params,
        )'''

assert old_4d in content, "PATCH 4d: old text not found"
content = content.replace(old_4d, new_4d, 1)

# ============================================================
# 5. Modify Stage 2 setup
# ============================================================
old_5 = '''    log.info("=" * 60)
    log.info("STAGE 2: Freeze ACIS, train LoRA (action_loss only)")
    log.info("=" * 60)

    # Clear stale gradients from stage1
    model.zero_grad(set_to_none=True)

    lora_params = get_lora_params(model)
    acis_params = get_acis_params(model)
    unfreeze_params(lora_params)
    freeze_params(acis_params)
    verify_grad_state(model, "stage2", dry_run=args.dry_run)

    optimizer2 = make_stage_optimizer(lora_params, lr=stage2_lr)
    scheduler2 = make_stage_scheduler(optimizer2, stage2_warmup, stage2_steps)'''

new_5 = '''    log.info("=" * 60)
    if train_mode == "twostage_fullft":
        log.info("STAGE 2: Freeze ACIS, train expert (action_loss only) [Full FT]")
    else:
        log.info("STAGE 2: Freeze ACIS, train LoRA (action_loss only)")
    log.info("=" * 60)

    # Clear stale gradients from stage1
    model.zero_grad(set_to_none=True)

    acis_params = get_acis_params(model)
    if train_mode == "twostage_fullft":
        unfreeze_params(expert_params)
        freeze_params(acis_params)
        verify_grad_state(model, "stage2", dry_run=args.dry_run,
                         train_mode=train_mode, expert_params=expert_params)
        optimizer2 = make_stage_optimizer(expert_params, lr=stage2_lr)
    else:
        lora_params = get_lora_params(model)
        unfreeze_params(lora_params)
        freeze_params(acis_params)
        verify_grad_state(model, "stage2", dry_run=args.dry_run)
        optimizer2 = make_stage_optimizer(lora_params, lr=stage2_lr)
    scheduler2 = make_stage_scheduler(optimizer2, stage2_warmup, stage2_steps)'''

assert old_5 in content, "PATCH 5: old text not found"
content = content.replace(old_5, new_5, 1)

# ============================================================
# 5b. Modify Stage 2 run_stage call
# ============================================================
old_5b = '''    completed = run_stage(
        model=model, dataloader=dataloader, stage="stage2",
        forward_fn=stage2_forward, optimizer=optimizer2, scheduler=scheduler2,
        total_steps=stage2_steps, config=config, device=device,
        output_dir=output_dir, dry_run=args.dry_run, graceful=graceful,
    )'''

new_5b = '''    completed = run_stage(
        model=model, dataloader=dataloader, stage="stage2",
        forward_fn=stage2_forward, optimizer=optimizer2, scheduler=scheduler2,
        total_steps=stage2_steps, config=config, device=device,
        output_dir=output_dir, dry_run=args.dry_run, graceful=graceful,
        train_mode=train_mode, expert_params=expert_params,
    )'''

assert old_5b in content, "PATCH 5b: old text not found"
content = content.replace(old_5b, new_5b, 1)

# ============================================================
# Write patched file
# ============================================================
with open(filepath, "w") as f:
    f.write(content)

print("All patches applied successfully.")
print(f"Original size: {len(original)} chars")
print(f"Patched size: {len(content)} chars")
print(f"Delta: +{len(content) - len(original)} chars")
