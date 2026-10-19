"""Patch evaluate.py to add OpenVLA support."""
import sys

filepath = "/root/acr-vla-conformal-refinement/src/evaluate.py"
with open(filepath, "r") as f:
    code = f.read()

changes = 0

# 1. Add --openvla and --openvla_path args after --smolvla_path
old = '    p.add_argument("--smolvla_path", type=str, default="/root/autodl-tmp/models/smolvla_libero/")'
new = '''    p.add_argument("--smolvla_path", type=str, default="/root/autodl-tmp/models/smolvla_libero/")
    p.add_argument("--openvla", action="store_true",
                   help="Use OpenVLA instead of SmolVLA")
    p.add_argument("--openvla_path", type=str,
                   default="/root/autodl-tmp/models/openvla-libero-object",
                   help="Path to OpenVLA model")'''
if old in code:
    code = code.replace(old, new)
    changes += 1
    print("1. Added --openvla args")
else:
    print("1. SKIP: --smolvla_path not found")

# 2. Add OpenVLA action functions before rollout_single
old = 'def rollout_single(env, init_state, action_fn, max_steps=300):'
new = '''def select_action_crm_openvla(openvla_wrapper, obs, task_name, crm, device):
    """OpenVLA K=1 CRM obs_only: single prediction + CRM correction."""
    agentview = obs["agentview_image"]
    action_7d, features = openvla_wrapper.predict_action_with_features(
        agentview, task_name
    )
    base_pose = torch.tensor(
        action_7d[:CORRECTION_DIM], dtype=torch.float32
    ).unsqueeze(0).to(device)  # (1, 6)
    obs_feat = features[-1].to(device)  # (1, 4096)
    with torch.no_grad():
        refined_pose = crm(base_pose, None, obs_feat)  # (1, 6)
    refined_7d = np.concatenate([
        refined_pose[0].cpu().numpy(), action_7d[CORRECTION_DIM:]
    ])
    return refined_7d


def select_action_openvla_only(openvla_wrapper, obs, task_name):
    """OpenVLA baseline: single-step deterministic prediction."""
    agentview = obs["agentview_image"]
    return openvla_wrapper.predict_action(agentview, task_name)


def rollout_single(env, init_state, action_fn, max_steps=300):'''
if 'def rollout_single(env, init_state, action_fn, max_steps=300):' in code and 'select_action_crm_openvla' not in code:
    code = code.replace(old, new)
    changes += 1
    print("2. Added OpenVLA action functions")
else:
    print("2. SKIP: already patched or rollout_single not found")

# 3. Replace SmolVLA loading with conditional
old = '''    # Load SmolVLA
    from smolvla_wrapper import SmolVLAWrapper
    print(f"[eval] Loading SmolVLA from {args.smolvla_path}...")
    wrapper = SmolVLAWrapper(args.smolvla_path, device=str(device))'''
new = '''    # Load VLA
    openvla_wrapper = None
    h_eff = H_EFF
    if args.openvla:
        from openvla_wrapper import OpenVLAWrapper
        print(f"[eval] Loading OpenVLA from {args.openvla_path}...")
        openvla_wrapper = OpenVLAWrapper(
            model_path=args.openvla_path, device=str(device)
        )
        wrapper = None
        h_eff = 1
    else:
        from smolvla_wrapper import SmolVLAWrapper
        print(f"[eval] Loading SmolVLA from {args.smolvla_path}...")
        wrapper = SmolVLAWrapper(args.smolvla_path, device=str(device))'''
if old in code:
    code = code.replace(old, new)
    changes += 1
    print("3. Conditional VLA loading")
else:
    print("3. SKIP: SmolVLA load block not found")

# 4. CGS uses h_eff
old = '    cgs = ConformilizedGaussianScoring(K=args.K, horizon=H_EFF, action_dim=CORRECTION_DIM)'
new = '    cgs = ConformilizedGaussianScoring(K=args.K, horizon=h_eff, action_dim=CORRECTION_DIM)'
if old in code:
    code = code.replace(old, new)
    changes += 1
    print("4. CGS uses h_eff")
else:
    print("4. SKIP: CGS line not found")

# 5. CRM action_dim uses h_eff
old = '''            crm = ConformalRefinementModule(
                action_dim=H_EFF * CORRECTION_DIM,'''
new = '''            crm = ConformalRefinementModule(
                action_dim=h_eff * CORRECTION_DIM,'''
if old in code:
    code = code.replace(old, new)
    changes += 1
    print("5. CRM action_dim uses h_eff")
else:
    print("5. SKIP: CRM construction not found")

# 6. vla_only dispatch: add OpenVLA branch
old = '''            elif args.mode == "vla_only":
                action_fn = lambda obs: select_action_vla_only(
                    wrapper, obs, task_desc, args.K, cgs
                )'''
new = '''            elif args.mode == "vla_only":
                if args.openvla:
                    action_fn = lambda obs: select_action_openvla_only(
                        openvla_wrapper, obs, task_desc
                    )
                else:
                    action_fn = lambda obs: select_action_vla_only(
                        wrapper, obs, task_desc, args.K, cgs
                    )'''
if old in code:
    code = code.replace(old, new)
    changes += 1
    print("6. vla_only dispatch with OpenVLA branch")
else:
    print("6. SKIP: vla_only dispatch not found")

# 7. CRM default dispatch: add OpenVLA branch
old = '''            else:
                action_fn = lambda obs: select_action_crm(
                    wrapper, obs, task_desc, args.K, cgs, crm, device, args.mode
                )'''
new = '''            else:
                if args.openvla and args.mode == "crm_obs_only":
                    action_fn = lambda obs: select_action_crm_openvla(
                        openvla_wrapper, obs, task_desc, crm, device
                    )
                else:
                    action_fn = lambda obs: select_action_crm(
                        wrapper, obs, task_desc, args.K, cgs, crm, device, args.mode
                    )'''
if old in code:
    code = code.replace(old, new)
    changes += 1
    print("7. CRM dispatch with OpenVLA branch")
else:
    print("7. SKIP: CRM default dispatch not found")

with open(filepath, "w") as f:
    f.write(code)

print(f"\nTotal changes: {changes}/7")
if changes == 7:
    print("ALL PATCHES APPLIED SUCCESSFULLY")
else:
    print("WARNING: Some patches were skipped!")
