import os
import json
import numpy as np
import torch
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

from htb_ai_library import (
    set_reproducibility, use_htb_style,
    MLP, AttackModel,
    load_adult_census,
    train_fixed_epochs, train_with_early_stopping, evaluate_model,
    get_model_predictions, prepare_attack_data, create_dataloader,
    plot_training_history, plot_overfitting_gap, plot_confidence_distributions,
    plot_shadow_confidence_distributions, plot_attack_roc_curve, plot_precision_recall_curve,
    plot_attack_accuracy_comparison, analyze_attack_decision_boundary, plot_decision_boundary,
)

RANDOM_SEED = 1337
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
set_reproducibility(RANDOM_SEED)
use_htb_style()

OUTPUT_DIR = "output"
MODEL_DIR = f"{OUTPUT_DIR}/models"
FIGS_DIR = "figs"
FIG_PREFIX = "Introduction_"
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(FIGS_DIR, exist_ok=True)

DATASET_CONFIG = {
    "num_classes": 2,
}