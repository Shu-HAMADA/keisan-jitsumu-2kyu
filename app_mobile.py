import random
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR, ROUND_CEILING
import streamlit as st

# ページ設定（サイドバーを閉じ、スマホで見やすいレイアウトに固定）
st.set_page_config(
    page_title="計算実務2級 全20問特訓ドリル", 
    page_icon="📱", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# 1. 多言語翻訳辞書（全9言語対応）
# =========================================================================
LANG_OPTIONS = [
    "日本語のみ",
    "英語 (English)",
    "ネパール語 (नेपाली)",
    "シンハラ語 (සිංහල)",
    "ベトナム語 (Tiếng Việt)",
    "中国語 (中文)",
    "ミャンマー語 (မြန်မာ)",
    "タイ語 (ไทย)",
    "タガログ語 (Tagalog)",
    "ベンガル語 (বাংলা)"
]
