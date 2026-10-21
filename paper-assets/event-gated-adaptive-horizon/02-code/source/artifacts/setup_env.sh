#!/bin/bash
# ============================================================
# Cold-start environment setup for CIVO experiments
# Supports: AutoDL (aml-train image) and generic servers
# Project: event-gated-adaptive-horizon
#
# Usage:
#   bash setup_env.sh              # Full setup
#   bash setup_env.sh --skip-code  # Skip git clone/pull (deps only)
# ============================================================
set -e

PROJ_NAME="event-gated-adaptive-horizon"
DATA_DIR="${AUTODL_TMP:-/root/autodl-tmp}"
PROJ_DIR="${DATA_DIR}/${PROJ_NAME}"
STORM_DMC="${PROJ_DIR}/storm_dmc"
SKIP_CODE=false
[[ "$1" == "--skip-code" ]] && SKIP_CODE=true

echo "========================================="
echo "  CIVO Cold-Start Setup"
echo "  Data dir: ${DATA_DIR}"
echo "========================================="

# ---- Phase 0: Image detection ----
echo ""
echo "[Phase 0] Image detection..."
IMAGE="generic"
if [ -d "/root/miniconda3" ]; then
    source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
    if python3 -c "import torch" 2>/dev/null; then
        echo "  ✓ aml-train image detected (conda base active)"
        IMAGE="aml-train"
    fi
fi

# ---- Phase 1: AutoDL network + env vars ----
echo ""
echo "[Phase 1] Network & environment..."
if [ -f "/etc/network_turbo" ]; then
    echo "  [AutoDL] Enabling proxy acceleration..."
    source /etc/network_turbo
    export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
    export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
    echo "  ✓ Proxy + SSL certs configured"
fi
export HF_HOME="${DATA_DIR}/.hf_cache"
export HF_HUB_DISABLE_XET=1
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
echo "  ✓ MuJoCo EGL rendering configured"

# ---- Phase 2: Dependencies ----
echo ""
echo "[Phase 2] Installing dependencies..."
if [ "$IMAGE" = "aml-train" ]; then
    echo "  aml-train detected — installing project-specific deps only"
    pip install --quiet --no-warn-script-location \
        dm_control mujoco gymnasium \
        ruamel.yaml pyyaml \
        einops tqdm colorama wandb \
        tensorboard opencv-python-headless \
        moviepy protobuf 2>&1 | tail -3
else
    echo "  ⚠ Generic image — checking torch..."
    if ! python3 -c "import torch; assert torch.cuda.is_available()" 2>/dev/null; then
        echo ""
        echo "  ╔══════════════════════════════════════════════════════╗"
        echo "  ║  torch not found or CUDA unavailable.               ║"
        echo "  ║  Install manually:                                  ║"
        echo "  ║    nvcc --version  # check CUDA version             ║"
        echo "  ║    pip install torch --index-url                    ║"
        echo "  ║      https://download.pytorch.org/whl/cu<VER>      ║"
        echo "  ║  Then re-run this script.                           ║"
        echo "  ╚══════════════════════════════════════════════════════╝"
        exit 1
    fi
    pip install --quiet --no-warn-script-location \
        numpy dm_control mujoco gymnasium \
        ruamel.yaml pyyaml \
        einops tqdm colorama wandb \
        tensorboard opencv-python-headless \
        moviepy protobuf 2>&1 | tail -3
fi
echo "  ✓ Dependencies installed"

# ---- Phase 3: Verification ----
echo ""
echo "[Phase 3] Verification..."
python3 << 'PYEOF'
import torch
print(f"  torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}")
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(i)
        print(f"    GPU {i}: {torch.cuda.get_device_name(i)} ({props.total_mem // 1024**3}GB)")
else:
    print("  ⚠ NO CUDA — experiments will fail")
    exit(1)

import dm_control; print("  ✓ dm_control")
import gymnasium;  print("  ✓ gymnasium")

# Quick EGL render test
try:
    from dm_control import suite
    env = suite.load("walker", "walk")
    ts = env.reset()
    assert ts.observation['orientations'].shape[0] > 0
    print("  ✓ DMC Walker Walk loads OK")
except Exception as e:
    print(f"  ⚠ DMC load failed: {e}")
    print("    Check: export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl")
PYEOF

if [ "$SKIP_CODE" = true ]; then
    echo ""
    echo "  --skip-code: skipping git clone/pull and STORM setup"
    echo "========================================="
    echo "  Setup complete (deps only)!"
    echo "========================================="
    exit 0
fi

# ---- Phase 4: Project code sync ----
echo ""
echo "[Phase 4] Project code sync..."
if [ ! -d "$PROJ_DIR" ]; then
    echo "  ⚠ Project dir not found: $PROJ_DIR"
    echo "  >>> Clone manually: git clone <REPO_URL> $PROJ_DIR"
    echo "  >>> Then re-run this script."
    exit 1
else
    echo "  Project dir exists: $PROJ_DIR"
    cd "$PROJ_DIR" && git pull --ff-only 2>/dev/null && echo "  ✓ git pull OK" \
        || echo "  ⚠ git pull failed (offline or dirty), using existing code"
fi

# ---- Phase 5: STORM DMC setup ----
echo ""
echo "[Phase 5] STORM DMC setup..."
STORM_BASE="${DATA_DIR}/storm_base"

if [ ! -d "$STORM_BASE" ]; then
    echo "  Cloning STORM base repo..."
    git clone https://github.com/weipu-zhang/STORM.git "$STORM_BASE"
    echo "  ✓ STORM base cloned"
else
    echo "  ✓ STORM base exists: $STORM_BASE"
fi

if [ ! -d "$STORM_DMC" ]; then
    echo "  Creating STORM DMC working directory..."
    # Start with full STORM base (preserves utils.py, attention_blocks.py, etc.)
    cp -r "$STORM_BASE" "$STORM_DMC"
    # Overlay our DMC adaptation files (overrides agents.py, replay_buffer.py, etc.)
    cp -f "${PROJ_DIR}/artifacts/storm_dmc/train_dmc.py"   "$STORM_DMC/"
    cp -f "${PROJ_DIR}/artifacts/storm_dmc/agents.py"      "$STORM_DMC/"
    cp -f "${PROJ_DIR}/artifacts/storm_dmc/replay_buffer.py" "$STORM_DMC/"
    # Sub-models (new + modified)
    cp -f "${PROJ_DIR}/artifacts/storm_dmc/sub_models/mlp_encoder.py"       "$STORM_DMC/sub_models/"
    cp -f "${PROJ_DIR}/artifacts/storm_dmc/sub_models/transformer_model.py" "$STORM_DMC/sub_models/"
    cp -f "${PROJ_DIR}/artifacts/storm_dmc/sub_models/world_models.py"      "$STORM_DMC/sub_models/"
    cp -f "${PROJ_DIR}/artifacts/storm_dmc/sub_models/__init__.py"          "$STORM_DMC/sub_models/"
    # New directories
    cp -r "${PROJ_DIR}/artifacts/storm_dmc/envs"   "$STORM_DMC/"
    cp -r "${PROJ_DIR}/artifacts/storm_dmc/config"  "$STORM_DMC/"
    echo "  ✓ STORM DMC ready at $STORM_DMC"
else
    echo "  ✓ STORM DMC already exists: $STORM_DMC"
    echo "  To refresh: rm -rf $STORM_DMC && re-run"
fi

echo ""
echo "========================================="
echo "  Setup complete!"
echo ""
echo "  DreamerV3 dir: $PROJ_DIR"
echo "  STORM DMC dir: $STORM_DMC"
echo ""
echo "  Next: see launch_commands.md for experiment commands"
echo "========================================="
