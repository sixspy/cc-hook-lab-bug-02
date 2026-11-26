"""作废分栏读轨审计。"""
from __future__ import annotations

from app.services import bucket as core
from app.services import bucket_cutover as cutover
from app.services import bucket_dualwrite as dual


def audit_summary() -> dict:
    return {
        "title": "作废分栏审计",
        "core": core.dashboard(),
        "cutover": cutover.board(),
        "dualwrite": dual.dual_board(),
        "half": core.half_fix_display(),
    }
