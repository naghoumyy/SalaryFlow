import streamlit as st
import streamlit.components.v1 as components
from html import escape

st.set_page_config(
    page_title="SalaryFlow",
    page_icon="💰",
    layout="centered",
)

st.session_state.setdefault("page", "home")
st.session_state.setdefault("expense_categories", {})
st.session_state.setdefault("salary", 0.0)
st.session_state.setdefault("savings_goal", 0.0)
st.session_state.setdefault("saved_to_goal", 0.0)
st.session_state.setdefault("category_celebration", None)
st.session_state.setdefault("active_category", None)
st.session_state.setdefault("section_entering", False)

st.markdown(
    """
    <style>
    :root {
        --emerald: #087f5b;
        --forest: #103b2d;
        --mint: #e0eddf;
        --pastel-green: #6c9274;
        --soft-green: #edf5ed;
        --lime: #c4e86b;
        --ink: #28543c;
    }
    .stApp {
        color: var(--ink);
        background-color: #ffffff;
        background-image: none;
    }
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background-color: #ffffff;
    }
    [data-testid="stHeader"] { background: transparent; }
    .main .block-container {
        max-width: 860px;
        padding: 2.3rem 2rem 3.5rem;
    }
    h1, h2, h3 { color: var(--forest); }
    h1 {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 2.7rem;
        letter-spacing: 0;
    }
    h1::after {
        content: "";
        display: block;
        width: 54px;
        height: 4px;
        margin-top: 0.55rem;
        border-radius: 2px;
        background: var(--lime);
    }
    [data-testid="stMetric"] {
        padding: 0.8rem 1rem;
        border-left: 4px solid var(--emerald);
        border-radius: 4px;
        background: var(--mint);
        transition: transform 180ms ease, box-shadow 180ms ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 18px rgba(16, 59, 45, 0.1);
    }
    [data-testid="stMetricValue"] { color: var(--forest); }
    .savings-highlight {
        display: grid;
        gap: 5px;
        margin: 0.4rem 0 1.2rem;
        padding: 1rem 1.2rem;
        border-left: 5px solid #43865c;
        border-radius: 4px;
        background: #dcebd9;
    }
    .savings-highlight span {
        color: #365b42;
        font-size: 0.92rem;
        font-weight: 600;
    }
    .savings-highlight strong {
        color: #174a31;
        font-size: 1.8rem;
        font-weight: 700;
    }
    [class*="st-key-nav_"] button {
        width: 100%;
        min-height: 2.7rem;
        border: 1px solid #557c60 !important;
        background: #557c60 !important;
        color: #faf9f4 !important;
        transition: transform 160ms ease, background-color 160ms ease, box-shadow 160ms ease;
    }
    [class*="st-key-nav_"] button:hover {
        border-color: #496f55 !important;
        background: #496f55 !important;
        color: #faf9f4 !important;
        box-shadow: 0 3px 9px rgba(35, 70, 45, 0.16);
        transform: translateY(-1px);
    }
    [class*="st-key-nav_"] button:active {
        transform: translateY(0) scale(0.98);
    }
    [class*="st-key-manage_expense_categories"] button {
        border: 1px solid var(--emerald) !important;
        background: var(--emerald) !important;
        color: #ffffff !important;
        transition: transform 160ms ease, background-color 160ms ease, box-shadow 160ms ease;
    }
    [class*="st-key-manage_expense_categories"] button:hover {
        border-color: var(--forest) !important;
        background: var(--forest) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 12px rgba(16, 59, 45, 0.18);
        transform: translateY(-1px);
    }
    .section-enter-marker {
        display: none;
    }
    .main .block-container:has(.section-enter-marker) {
        animation: section-enter 380ms ease-out both;
    }
    .main .block-container:has(.section-enter-marker) [data-testid="stMetric"] {
        animation: metric-enter 420ms cubic-bezier(.2, .8, .2, 1) both;
    }
    .main .block-container:has(.section-enter-marker) [data-testid="stMetric"]:nth-of-type(2) {
        animation-delay: 70ms;
    }
    .main .block-container:has(.section-enter-marker) [data-testid="stMetric"]:nth-of-type(3) {
        animation-delay: 140ms;
    }
    @keyframes section-enter {
        from { opacity: 0.5; transform: translateY(9px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes metric-enter {
        from { opacity: 0; transform: translateY(8px) scale(0.985); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    @media (prefers-reduced-motion: reduce) {
        [class*="st-key-nav_"] button,
        [class*="st-key-manage_expense_categories"] button,
        [data-testid="stMetric"] { transition: none; }
        .main .block-container:has(.section-enter-marker) { animation: none; }
        .main .block-container:has(.section-enter-marker) [data-testid="stMetric"] { animation: none; }
    }
    div[data-testid="stButton"] > button[kind="primary"] {
        border: 1px solid var(--emerald);
        background: var(--emerald);
        color: white;
    }
    div[data-testid="stButton"] > button[kind="primary"]:hover {
        border-color: var(--forest);
        background: var(--forest);
        color: white;
    }
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        border-color: #b7d4c4;
        background-color: var(--soft-green);
    }
    [data-testid="stNumberInput"] [data-baseweb="input"] > div,
    [data-testid="stNumberInput"] input,
    [data-testid="stNumberInput"] button {
        background-color: #ffffff !important;
    }
    [data-testid="stNumberInput"] button {
        color: var(--emerald) !important;
        border-color: #d5e5d8 !important;
    }
    [data-testid="stWidgetLabel"] p,
    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label,
    .stRadio label,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stCaptionContainer"] {
        color: var(--pastel-green);
    }
    input, textarea,
    div[data-baseweb="select"] input {
        color: var(--emerald) !important;
        -webkit-text-fill-color: var(--emerald) !important;
    }
    input::placeholder, textarea::placeholder {
        color: #86a992 !important;
        -webkit-text-fill-color: #86a992 !important;
        opacity: 1;
    }
    [data-testid="stDivider"] { border-color: #d7e6dc; }
    @media (max-width: 600px) {
        .main .block-container { padding: 1.4rem 1rem 2.5rem; }
        h1 { font-size: 2.2rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def save_salary_input():
    st.session_state.salary = st.session_state.salary_input


def save_savings_goal_inputs():
    st.session_state.savings_goal = st.session_state.savings_goal_input
    st.session_state.saved_to_goal = st.session_state.saved_to_goal_input

st.title("💰 SalaryFlow")
dashboard_nav, savings_nav, categories_nav = st.columns(3)

if dashboard_nav.button(
    "Dashboard",
    key="nav_dashboard",
    type="primary" if st.session_state.page == "home" else "secondary",
):
    st.session_state.page = "home"
    st.session_state.section_entering = True
    st.rerun()

if savings_nav.button(
    "Savings Goals",
    key="nav_savings",
    type="primary" if st.session_state.page == "savings" else "secondary",
):
    st.session_state.page = "savings"
    st.session_state.section_entering = True
    st.rerun()

if categories_nav.button(
    "Expense Categories",
    key="nav_categories",
    type=(
        "primary"
        if st.session_state.page in {"categories", "add_category"}
        else "secondary"
    ),
):
    st.session_state.page = "categories"
    st.session_state.section_entering = True
    st.rerun()

if st.session_state.section_entering:
    st.markdown('<div class="section-enter-marker"></div>', unsafe_allow_html=True)
    st.session_state.section_entering = False

st.subheader("Your salary. Your plan. Your goals.")

if st.session_state.page != "home":
    st.divider()

if st.session_state.page == "home":
    st.write(
        "Take control of your money, "
        "track your expenses, and plan your savings."
    )
    st.divider()
    st.header("Your financial details")

    salary = st.number_input(
        "Monthly salary (in EGP):",
        min_value=0.0,
        step=500.0,
        value=st.session_state.salary,
        key="salary_input",
        on_change=save_salary_input,
    )

    expenses = sum(st.session_state.expense_categories.values())
    st.divider()
    st.subheader("Where your salary goes most")
    if st.session_state.expense_categories:
        top_category, top_amount = max(
            st.session_state.expense_categories.items(),
            key=lambda item: item[1],
        )
        insight_category, insight_share = st.columns(2)
        insight_category.metric(
            "Largest expense",
            top_category,
            f"{top_amount:,.2f} EGP / month",
            delta_color="off",
        )
        salary_share = f"{top_amount / salary:.1%}" if salary > 0 else "Enter salary"
        insight_share.metric("Share of salary", salary_share)
        st.caption(f"This category is {top_amount / expenses:.1%} of your recorded expenses.")
    else:
        st.info("Add expense categories to see what consumes most of your salary.")

    st.divider()
    st.header("Expense Categories")
    st.write(
        f"{len(st.session_state.expense_categories)} categories added. "
        f"Monthly total: {expenses:,.2f} EGP."
    )
    if st.button("Manage expense categories", key="manage_expense_categories"):
        st.session_state.page = "categories"
        st.rerun()

    savings = salary - expenses
    st.subheader("Your Financial Summary")
    st.metric("Monthly Expenses", f"{expenses:,.2f} EGP")
    st.markdown(
        f"""
        <div class="savings-highlight">
            <span>Monthly Savings</span>
            <strong>{savings:,.2f} EGP</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif st.session_state.page == "savings":
    st.header("Savings Goals")
    savings_goal = st.number_input(
        "Savings goal (in EGP)",
        min_value=0.0,
        step=500.0,
        value=st.session_state.savings_goal,
        key="savings_goal_input",
        on_change=save_savings_goal_inputs,
    )
    saved_to_goal = st.number_input(
        "Already saved toward this goal (in EGP)",
        min_value=0.0,
        step=100.0,
        value=st.session_state.saved_to_goal,
        key="saved_to_goal_input",
        on_change=save_savings_goal_inputs,
    )

    expenses = sum(st.session_state.expense_categories.values())
    savings = st.session_state.salary - expenses
    st.markdown(
        f"""
        <div class="savings-highlight">
            <span>Monthly Savings Available</span>
            <strong>{savings:,.2f} EGP</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Goal Progress")
    if savings_goal > 0:
        remaining = max(savings_goal - saved_to_goal, 0.0)
        progress = min(saved_to_goal / savings_goal, 1.0)
        st.progress(progress, text=f"{progress:.0%} of your goal saved")

        progress_saved, progress_remaining, progress_time = st.columns(3)
        progress_saved.metric("Saved so far", f"{saved_to_goal:,.2f} EGP")
        progress_remaining.metric("Still to go", f"{remaining:,.2f} EGP")
        if remaining == 0:
            progress_time.metric("Estimated time", "Goal reached")
        elif savings > 0:
            months_remaining = remaining / savings
            progress_time.metric("Estimated time", f"{months_remaining:.1f} months")
        else:
            progress_time.metric("Estimated time", "Not yet saving")

    if savings < 0:
        st.error(
            "Your expenses exceed your salary. You need to reduce your "
            "expenses or increase your income to save money."
        )
    elif savings_goal > 0 and saved_to_goal >= savings_goal:
        st.success("You have reached your savings goal!")
    elif savings_goal > 0 and savings <= 0:
        st.warning("Your expenses leave no monthly savings to put toward this goal yet.")
    elif savings_goal <= 0:
        st.info("Enter a savings goal greater than zero.")

elif st.session_state.page == "categories":
    st.header("Expense Categories")
    celebration = st.session_state.category_celebration
    if celebration:
        category_name, category_amount = celebration
        components.html(
            f"""
            <style>
            body {{ margin: 0; background: transparent; font-family: Arial, sans-serif; }}
            .cash-pop {{
                box-sizing: border-box;
                display: flex;
                align-items: center;
                gap: 12px;
                width: max-content;
                max-width: 100%;
                margin: 8px auto;
                padding: 12px 18px;
                border: 1px solid #b7d9c4;
                border-radius: 8px;
                background: #eff9f1;
                color: #124638;
                box-shadow: 0 8px 24px rgba(18, 70, 56, 0.14);
                animation: pop-in 420ms cubic-bezier(.2, .8, .2, 1) both;
            }}
            .cash-icon {{ font-size: 30px; animation: cash-bounce 700ms ease-out both; }}
            .cash-copy {{ display: grid; gap: 2px; }}
            .cash-copy strong {{ font-size: 15px; }}
            .cash-copy span {{ color: #45665a; font-size: 13px; }}
            .cash-check {{
                display: grid;
                width: 24px;
                height: 24px;
                place-items: center;
                border-radius: 50%;
                background: #087f5b;
                color: white;
                font-weight: 700;
            }}
            @keyframes pop-in {{ from {{ opacity: 0; transform: translateY(12px) scale(.94); }} to {{ opacity: 1; transform: translateY(0) scale(1); }} }}
            @keyframes cash-bounce {{ 0% {{ transform: translateY(8px) rotate(-12deg); }} 60% {{ transform: translateY(-4px) rotate(7deg); }} 100% {{ transform: translateY(0) rotate(0); }} }}
            @media (prefers-reduced-motion: reduce) {{ .cash-pop, .cash-icon {{ animation: none; }} }}
            </style>
            <div class="cash-pop" role="status" aria-live="polite">
                <span class="cash-icon" aria-hidden="true">💸</span>
                <span class="cash-copy"><strong>Category added</strong>
                <span>{escape(category_name)} · {category_amount:,.2f} EGP / month</span></span>
                <span class="cash-check" aria-hidden="true">✓</span>
            </div>
            <script>
            try {{
                const audio = new (window.AudioContext || window.webkitAudioContext)();
                const tick = () => {{
                    const oscillator = audio.createOscillator();
                    const volume = audio.createGain();
                    oscillator.type = "sine";
                    oscillator.frequency.setValueAtTime(1320, audio.currentTime);
                    volume.gain.setValueAtTime(0.0001, audio.currentTime);
                    volume.gain.exponentialRampToValueAtTime(0.12, audio.currentTime + 0.008);
                    volume.gain.exponentialRampToValueAtTime(0.0001, audio.currentTime + 0.11);
                    oscillator.connect(volume);
                    volume.connect(audio.destination);
                    oscillator.start();
                    oscillator.stop(audio.currentTime + 0.12);
                }};
                if (audio.state === "suspended") {{ audio.resume().then(tick).catch(() => {{}}); }}
                else {{ tick(); }}
            }} catch (error) {{}}
            </script>
            """,
            height=92,
            scrolling=False,
        )
        st.session_state.category_celebration = None

    categories = st.session_state.expense_categories
    category_total = sum(categories.values())
    st.metric("Monthly total", f"{category_total:,.2f} EGP")

    if categories:
        st.caption("Select a category to view or change its monthly amount.")
        for category, amount in list(st.session_state.expense_categories.items()):
            name_column, amount_column, remove_column = st.columns([3, 2, 1])
            if name_column.button(category, key=f"category_{category}"):
                if st.session_state.active_category == category:
                    st.session_state.active_category = None
                else:
                    st.session_state.active_category = category
                st.rerun()
            amount_column.write(f"**{amount:,.2f} EGP** / month")
            if remove_column.button("Remove", key=f"remove_{category}"):
                del st.session_state.expense_categories[category]
                if st.session_state.active_category == category:
                    st.session_state.active_category = None
                st.rerun()

            if st.session_state.active_category == category:
                st.caption(f"Monthly expense for {category}")
                updated_amount = st.number_input(
                    "Monthly expense (in EGP)",
                    min_value=0.01,
                    step=100.0,
                    value=float(amount),
                    format="%.2f",
                    key=f"category_amount_{category}",
                )
                save_column, cancel_column, _ = st.columns([1, 1, 4])
                if save_column.button(
                    "Save amount",
                    key=f"save_amount_{category}",
                    type="primary",
                ):
                    st.session_state.expense_categories[category] = updated_amount
                    st.session_state.active_category = None
                    st.rerun()
                if cancel_column.button("Cancel", key=f"cancel_amount_{category}"):
                    st.session_state.active_category = None
                    st.rerun()
                st.divider()
    else:
        st.info("No categories yet. Add one to start tracking your expenses.")

    if st.button("+ Add category", type="primary"):
        st.session_state.page = "add_category"
        st.rerun()

elif st.session_state.page == "add_category":
    st.header("Add an Expense Category")
    st.write("Choose a recommended category or create your own.")

    category_type = st.radio(
        "Category type",
        ["Recommended", "Custom"],
        horizontal=True,
    )
    if category_type == "Recommended":
        recommended_categories = [
            "Housing",
            "Groceries",
            "Transportation",
            "Utilities",
            "Healthcare",
            "Dining",
            "Entertainment",
            "Education",
            "Personal care",
            "Debt payments",
        ]
        category = st.selectbox("Recommended categories", recommended_categories)
    else:
        category = st.text_input("Custom category name")

    amount = st.number_input(
        "Monthly expense (in EGP)",
        min_value=0.0,
        step=100.0,
        format="%.2f",
    )

    if st.button("Add category", type="primary"):
        category = category.strip()
        if not category:
            st.error("Enter a category name.")
        elif amount <= 0:
            st.error("Enter a monthly expense greater than zero.")
        elif category.casefold() in {
            name.casefold() for name in st.session_state.expense_categories
        }:
            st.error("That category already exists.")
        else:
            st.session_state.expense_categories[category] = amount
            st.session_state.category_celebration = (category, amount)
            st.session_state.page = "categories"
            st.rerun()
