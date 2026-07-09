import streamlit as st
from PIL import Image
import time
from google import genai
from supabase import create_client, Client
import urllib.parse

# Import decoupled 100+ item master database registry index
from database_registry import SRI_LANKA_REGIONAL_DB

# ==========================================
# 1. CLOUD GATEWAYS & INITIALIZATION
# ==========================================
try:
    GEMINI_KEY = st.secrets["GEMINI_API_KEY"]
    ai_client = genai.Client(api_key=GEMINI_KEY)
    
    SB_URL = st.secrets["SUPABASE_URL"]
    SB_KEY = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(SB_URL, SB_KEY)
except Exception as config_err:
    st.error(f"🚨 Production Configuration Missing: Verify secret tokens inside `.streamlit/secrets.toml`. Error: {config_err}")
    st.stop()

# Build comprehensive lists for search boundaries
ALL_REGISTRY_FOODS = []
for region in SRI_LANKA_REGIONAL_DB.values():
    for f in region["foods"]:
        if f["name"] not in ALL_REGISTRY_FOODS:
            ALL_REGISTRY_FOODS.append(f["name"])

GLOBAL_COUNTRIES = [
    "Germany", "France", "United Kingdom", "United States", "Austria", "Switzerland", 
    "Netherlands", "Belgium", "Italy", "Spain", "Australia", "Canada", "Sri Lanka", "India"
]

ALL_25_DISTRICTS = [
    "Colombo", "Gampaha", "Kalutara", "Kandy", "Matale", "Nuwara Eliya", 
    "Galle", "Matara", "Hambantota", "Jaffna", "Kilinochchi", "Mannar", 
    "Vavuniya", "Mullaitivu", "Batticaloa", "Ampara", "Trincomalee", 
    "Kurunegala", "Puttalam", "Anuradhapura", "Polonnaruwa", 
    "Badulla", "Monaragala", "Ratnapura", "Kegalle"
]

DIETARY_PROFILES = ["All Profiles", "Spicy", "Sweet", "Fried", "Baked", "Vegan", "Vegetarian", "Non-Vegan"]

# ==========================================
# 2. DESIGN SYSTEM & CONTRAST LOCK (CSS)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    /* Strict Premium Dark Theme Override */
    .stApp, .stApp [data-testid="stAppViewContainer"] { 
        background: linear-gradient(180deg, #090D1A 0%, #03050F 100%) !important; 
        color: #F1F5F9 !important; 
        font-family: 'Plus Jakarta Sans', sans-serif; 
    }
    
    /* Font Contrast Locks */
    .stApp p, .stApp label, .stApp div, .stApp span, .stApp th, .stApp td { color: #E2E8F0 !important; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; color: #FFFFFF !important; }
    
    .app-header {
        background: radial-gradient(circle at top left, rgba(37, 99, 235, 0.12), transparent 70%);
        padding: 40px 20px; text-align: center; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin-bottom: 30px;
        border-radius: 20px;
    }
    .main-card {
        background: rgba(30, 41, 59, 0.45) !important; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        padding: 30px; border-radius: 24px; border: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 25px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    .kpi-metric-box {
        background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 20px; border-radius: 16px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .feed-card-premium {
        background: rgba(15, 23, 42, 0.65) !important; border: 1px solid rgba(255, 255, 255, 0.06);
        padding: 24px; border-radius: 20px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .city-banner-gradient {
        background: linear-gradient(135deg, #1E3A8A 0%, #070B14 100%);
        height: 150px; border-radius: 16px; display: flex; align-items: flex-end; padding: 20px;
        border: 1px solid rgba(255,255,255,0.08); margin-bottom: 20px;
    }
    
    .badge-star { color: #F59E0B !important; font-weight: 700; font-size: 1.1em; }
    .tag-pill { background: rgba(59, 130, 246, 0.12); border: 1px solid rgba(59, 130, 246, 0.25); padding: 4px 12px; border-radius: 8px; font-size: 0.8em; color: #93C5FD !important; font-weight: 500; }
    .allergen-box { background: rgba(220, 38, 38, 0.12); border: 1px solid rgba(220, 38, 38, 0.3); padding: 16px; border-radius: 14px; color: #FCA5A5 !important; margin: 15px 0; }
    .etiquette-box { background: rgba(245, 158, 11, 0.08); border-left: 4px solid #F59E0B; padding: 16px; border-radius: 0 14px 14px 0; color: #FDE68A !important; margin: 15px 0; }
    .star-glowing { color: #F59E0B !important; font-weight: bold; }
    
    .stTabs [data-baseweb="tab"] p { color: #64748B !important; font-weight: 600; font-size: 1.05em; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] p { color: #3B82F6 !important; }
    div[data-testid="stFileUploader"] { background: rgba(255,255,255,0.02) !important; border: 1px dashed rgba(255,255,255,0.1) !important; border-radius: 16px; padding: 10px; }
    
    div.stButton > button {
        background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%) !important; color: white !important;
        border: none !important; border-radius: 12px !important; padding: 12px 24px !important; font-weight: 600 !important; width: 100%;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 4px 15px rgba(37,99,235,0.4); }
    .nav-box-header { font-size: 0.85em; text-transform: uppercase; letter-spacing: 1px; color: #64748B !important; margin-bottom: 10px; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

selected_lang = st.selectbox("🌐 System Language Framework Context:", ["English", "Deutsch", "Français"])
TXT_MAP = {
    "English": {"maps": "🗺️ Open Sourcing Route in Google Maps", "rev_hdr": "💬 Traveler Community Reviews"},
    "Deutsch": {"maps": "🗺️ In Google Maps öffnen", "rev_hdr": "💬 Bewertungen von Reisenden"},
    "Français": {"maps": "🗺️ Ouvrir Google Maps", "rev_hdr": "💬 Avis des Voyageurs"}
}
TXT = TXT_MAP[selected_lang]
st.write("---")

tab1, tab2, tab3 = st.tabs(["📸 AI Vision Scanner", "🖼️ Community Analytics Feed", "🗺️ Regional Dashboard"])

# ==========================================
# 3. TAB 1: VISION CLASSIFICATION ENGINE
# ==========================================
with tab1:
    st.subheader("Visual Asset Identification")
    uploaded_file = st.file_uploader("Upload an operational item photo...", type=["jpg", "jpeg", "png"], key="scanner_upload_box")
    
    if uploaded_file is not None:
        img_obj = Image.open(uploaded_file).convert("RGB")
        st.image(img_obj, use_container_width=True)
        
        with st.spinner("Streaming binary pixel vectors to Google vision cluster..."):
            try:
                # CRITICAL SYSTEM FIX: Explicit translation grounding instruction added to avoid Sinhala fallback output text
                prompt = f"""
                You are a Sri Lankan street food master guide. Analyze this image.
                Compare it against this master list of authentic foods: {', '.join(ALL_REGISTRY_FOODS)}.
                If it matches an item closely, you MUST output that exact name as the 'Dish Title Name'.
                If it is NOT food, write 'REJECT: Not food'.
                
                CRITICAL INSTRUCTION: You MUST write the '2-sentence description' and the 'Cultural Etiquette Rules' entirely in the '{selected_lang}' language. 
                Do NOT use Sinhala script characters, Tamil script characters, or any language other than '{selected_lang}'.
                
                Reply strictly in this layout template separated by double pipes (||):
                Dish Title Name || English Translation || 2-sentence description written in {selected_lang} || Core Structural Ingredients || Hidden Allergen Contamination Watch || Cultural Etiquette Rules written in {selected_lang} || Recommended Street Sourcing Point || Category Tag (Street Food, Traditional Dish, or Endemic Fruit) || Dietary Attribute (Match closest keyword: Spicy, Sweet, Fried, Baked, Vegan, Vegetarian, Non-Vegan) || Recommended District (Choose closest matching option from our directory list)
                """
                response = ai_client.models.generate_content(model='gemini-2.5-flash', contents=[img_obj, prompt])
                ai_output = response.text.strip()
            except Exception as api_err:
                st.error(f"AI Ingestion Pipeline Offline: {api_err}")
                ai_output = None
                
        if ai_output and not ai_output.startswith("REJECT:"):
            try:
                nodes = ai_output.split("||")
                detected_title = nodes[0].strip()
                translation = nodes[1].strip()
                desc = nodes[2].strip()
                ingredients = nodes[3].strip()
                allergens = nodes[4].strip()
                etiquette = nodes[5].strip()
                vendor = nodes[6].strip()
                category_tag = nodes[7].strip()
                dietary_tag = nodes[8].strip()
                district_tag = nodes[9].strip()
                
                # Fetch row records metrics out of cloud Supabase database
                try:
                    stats_query = supabase.table("food_reviews").select("*").eq("food_name", detected_title).execute().data
                    if stats_query:
                        count_rev = len(stats_query)
                        avg_stars = round(sum(x["stars_overall"] for x in stats_query) / count_rev, 1)
                        total_must_try = sum(1 for x in stats_query if x["must_try"])
                    else:
                        count_rev, avg_stars, total_must_try = 0, 0.0, 0
                except Exception:
                    count_rev, avg_stars, total_must_try = 0, 0.0, 0

                st.markdown(f"""
                <div class="main-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                        <div style="display:flex; gap:8px;">
                            <span style="background:#1E3A8A; padding:4px 10px; border-radius:6px; font-size:0.8em; font-weight:bold;">✨ {category_tag}</span>
                            <span style="background:#065F46; padding:4px 10px; border-radius:6px; font-size:0.8em; font-weight:bold;">🍃 {dietary_tag}</span>
                        </div>
                        <div style="display:flex; gap:10px;">
                            <span class="tag-pill" style="color:#F59E0B !important; border-color:#F59E0B;">⭐ {avg_stars} ({count_rev} Reviews)</span>
                            <span class="tag-pill" style="color:#10B981 !important; border-color:#10B981;">🔥 Must Try: {total_must_try}</span>
                        </div>
                    </div>
                    <h2 style="color:#3B82F6 !important; margin:0; font-size:1.8em;">🎯 {detected_title}</h2>
                    <p style="color:#64748B !important; font-style:italic; margin-top:-2px;">({translation})</p>
                    <hr style="border:0.5px solid rgba(255,255,255,0.06); margin:15px 0;">
                    <p style="font-size:1.05em; line-height:1.6;">{desc}</p>
                    <p><b>🧱 Core Ingredients:</b> {ingredients}</p>
                    <div class="allergen-box">⚠️ <b>Allergen Watch Metrics:</b><br>{allergens}</div>
                    <div class="etiquette-box">💡 <b>Cultural Etiquette Index:</b><br>{etiquette}</div>
                </div>
                """, unsafe_allow_html=True)
                
                map_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(vendor + ', ' + district_tag + ', Sri Lanka')}"
                st.link_button(TXT["maps"], map_url)
                
                # --- LIVE OVERHAULED MULTI-FACTOR TRANSACTION FORM ---
                st.write("---")
                st.markdown("### ✍️ Submit Verified Professional Analytics Review")
                
                with st.form(key="supabase_review_form", clear_on_submit=True):
                    col_form1, col_form2 = st.columns(2)
                    with col_form1:
                        final_food_name = st.selectbox("Verified Food Name (Registry Grounded):", options=ALL_REGISTRY_FOODS, index=ALL_REGISTRY_FOODS.index(detected_title) if detected_title in ALL_REGISTRY_FOODS else 0)
                        input_nickname = st.text_input("Your Profile Nickname (Required):", placeholder="e.g. TravelerMax")
                        visitor_home_country = st.selectbox("Your Home Country (Origin Directory):", GLOBAL_COUNTRIES)
                    with col_form2:
                        input_stall_name = st.text_input("Visited Food Store / Stall Name (Required):", placeholder="e.g. Nana's Pride Galle Face")
                        confirmed_location = st.selectbox("Select Visited District Location (All 25 Districts Available):", ALL_25_DISTRICTS, index=ALL_25_DISTRICTS.index(district_tag) if district_tag in ALL_25_DISTRICTS else 0)
                        must_try_value_toggle = st.checkbox("🔥 Mark and count this specific dish as a 'MUST TRY'?", value=True)
                    
                    st.write("---")
                    st.markdown("##### 📊 Multi-Factor Travel Sentiment Metrics (Select Stars)")
                    
                    col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns(5)
                    with col_s1:
                        star_overall = st.selectbox("⭐ Overall Rating:", [5, 4, 3, 2, 1], format_func=lambda x: "★" * x, key="scan_s1")
                    with col_s2:
                        star_taste = st.selectbox("👅 Taste & Freshness:", [5, 4, 3, 2, 1], format_func=lambda x: "★" * x, key="scan_s2")
                    with col_s3:
                        star_hygiene = st.selectbox("🧼 Cleanliness & Hygiene:", [5, 4, 3, 2, 1], format_func=lambda x: "★" * x, key="scan_s3")
                    with col_s4:
                        star_service = st.selectbox("🤝 Service Quality:", [5, 4, 3, 2, 1], format_func=lambda x: "★" * x, key="scan_s4")
                    with col_s5:
                        star_spicy = st.selectbox("🌶️ Spiciness Intensity:", [5, 4, 3, 2, 1], format_func=lambda x: "🔥" * x, key="scan_s5")
                        
                    review_comment_text = st.text_area("Observation Review Logs (Optional - Share extra flavor profiles, preparation style notes):")
                    
                    submit_transaction_btn = st.form_submit_button("Commit Cryptographic Record to Supabase Cluster")
                    
                    if submit_transaction_btn:
                        # --- STRICT VALIDATION GUARDS ---
                        if not input_nickname.strip():
                            st.error("❌ Form Submission Denied: The 'Profile Nickname' field cannot be left blank.")
                        elif not input_stall_name.strip():
                            st.error("❌ Form Submission Denied: The 'Food Store / Stall Name' field cannot be left blank.")
                        else:
                            supabase.table("food_reviews").insert({
                                "food_name": final_food_name, 
                                "username": input_nickname.strip(), 
                                "visitor_country": visitor_home_country,
                                "stall_name": input_stall_name.strip(), 
                                "location_province": confirmed_location,
                                "stars_overall": int(star_overall), 
                                "stars_taste": int(star_taste),
                                "stars_hygiene": int(star_hygiene), 
                                "stars_service": int(star_service),
                                "stars_spicy": int(star_spicy),
                                "must_try": must_try_value_toggle, 
                                "comment": review_comment_text.strip() if review_comment_text.strip() else "No additional comments added."
                            }).execute()
                            
                            st.success("🎉 Transaction committed to cloud PostgreSQL table successfully! Analytics dashboards synchronized.")
                            time.sleep(0.5)
                            st.rerun()
            except IndexError:
                st.error("Matrix partitioning segmentation logic parsing error.")
        elif ai_output:
            st.error("🚨 Ingestion Terminated: Non-culinary element flagged by security layers.")

# ==========================================
# 4. TAB 2: PUBLIC USER ANALYTICS TRAVEL FEED
# ==========================================
with tab2:
    st.subheader("Public Crowdsourced Travel Stream")
    
    try:
        global_reviews = supabase.table("food_reviews").select("*").execute().data
    except Exception:
        global_reviews = []
        
    if not global_reviews:
        st.info("No traveler records currently populated inside the remote database tables cluster.")
    else:
        st.markdown("### 📊 Platform Core Metric Aggregates")
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        with kpi1:
            st.markdown(f'<div class="kpi-metric-box"><span style="font-size:0.85em; color:#64748B !important;">TOTAL REVIEWS</span><br><h3 style="margin:0; font-size:1.8em; color:#3B82F6 !important;">{len(global_reviews)}</h3></div>', unsafe_allow_html=True)
        with kpi2:
            computed_avg = round(sum(x["stars_overall"] for x in global_reviews) / len(global_reviews), 1)
            st.markdown(f'<div class="kpi-metric-box"><span style="font-size:0.85em; color:#64748B !important;">GLOBAL SCORE</span><br><h3 style="margin:0; font-size:1.8em; color:#F59E0B !important;">★ {computed_avg}</h3></div>', unsafe_allow_html=True)
        with kpi3:
            unique_foods_tracked = len(set(x["food_name"] for x in global_reviews))
            st.markdown(f'<div class="kpi-metric-box"><span style="font-size:0.85em; color:#64748B !important;">ITEMS DECODED</span><br><h3 style="margin:0; font-size:1.8em; color:#10B981 !important;">{unique_foods_tracked}</h3></div>', unsafe_allow_html=True)
        with kpi4:
            total_must_tries = sum(1 for x in global_reviews if x["must_try"])
            st.markdown(f'<div class="kpi-metric-box"><span style="font-size:0.85em; color:#64748B !important;">MUST TRY METRICS</span><br><h3 style="margin:0; font-size:1.8em; color:#EC4899 !important;">❤️ {total_must_tries}</h3></div>', unsafe_allow_html=True)
            
        st.write("---")
        
        # --- FILTRATION DECK CONFIGURATIONS ---
        st.markdown("##### 🔍 Global Stream Filters & Engine Sorting")
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            search_food_query = st.text_input("📝 Search Bar (Type Food Name):", value="", placeholder="Start typing... (e.g. Kottu)")
            filter_loc_var = st.selectbox("📍 Filter by Specific District Node:", ["All Districts"] + ALL_25_DISTRICTS)
        with f_col2:
            filter_diet_var = st.selectbox("🥗 Filter by Dietary Profile Type:", DIETARY_PROFILES, key="feed_diet_select")
            sort_metric_var = st.selectbox("📊 Sort Dashboard Matrix By:", ["Newest Logs", "Overall Stars: High to Low", "Overall Stars: Low to High"])
        with f_col3:
            st.markdown("<p style='font-size:0.85em; opacity:0.5; margin-top:28px;'><i>Filters match across your 100+ native dishes index in real-time.</i></p>", unsafe_allow_html=True)

        # Apply Sort Frameworks
        if sort_metric_var == "Newest Logs":
            global_reviews.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        elif sort_metric_var == "Overall Stars: High to Low":
            global_reviews.sort(key=lambda x: x["stars_overall"], reverse=True)
        elif sort_metric_var == "Overall Stars: Low to High":
            global_reviews.sort(key=lambda x: x["stars_overall"])

        st.write("---")
        
        rendered_count = 0
        for record in global_reviews:
            match_search = search_food_query.lower() in record["food_name"].lower() if search_food_query else True
            match_p = (filter_loc_var == "All Districts") or (record.get("location_province", "Colombo") == filter_loc_var)
            
            matched_dietary_flag = True
            if filter_diet_var != "All Profiles":
                reg_match = None
                for region in SRI_LANKA_REGIONAL_DB.values():
                    for food in region["foods"]:
                        if food["name"] == record["food_name"]:
                            reg_match = food
                            break
                if reg_match:
                    if filter_diet_var.lower() not in reg_match.get("desc", "").lower() and filter_diet_var.lower() not in record["comment"].lower():
                        matched_dietary_flag = False
                else:
                    matched_dietary_flag = False
            
            if match_search and match_p and matched_dietary_flag:
                rendered_count += 1
                stars_overall_str = "★" * record["stars_overall"] + "☆" * (5 - record["stars_overall"])
                stars_taste_str = "★" * record["stars_taste"] + "☆" * (5 - record["stars_taste"])
                stars_hygiene_str = "★" * record["stars_hygiene"] + "☆" * (5 - record["stars_hygiene"])
                stars_service_str = "★" * record["stars_service"] + "☆" * (5 - record["stars_service"])
                stars_spicy_val = record.get("stars_spicy", 3) if record.get("stars_spicy") is not None else 3
                stars_spicy_str = "🔥" * stars_spicy_val
                
                must_try_tag = "🔥 HIGHLY RECOMMENDED ITEM" if record["must_try"] else "⚖️ Standard Review Log"
                
                mock_gallery_img = "https://images.unsplash.com/photo-1605666804746-43d45bdb1647?auto=format&fit=crop&w=500&q=80"
                if "kottu" in record["food_name"].lower():
                    mock_gallery_img = "https://images.unsplash.com/photo-1627575031651-7890ecb5c49d?auto=format&fit=crop&w=500&q=80"
                elif "vade" in record["food_name"].lower() or "wade" in record["food_name"].lower():
                    mock_gallery_img = "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=500&q=80"

                st.markdown(f"""
                <div class="feed-card-premium">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="margin:0; font-size:1.3em; color:#3B82F6 !important;">🥘 {record['food_name']}</h4>
                        <div>
                            <span class="badge-star">{stars_overall_str}</span>
                            <span style="margin-left:12px; font-size:0.75em; font-weight:700; color:#10B981 !important; background:rgba(16,185,129,0.1); padding:3px 8px; border-radius:4px;">{must_try_tag}</span>
                        </div>
                    </div>
                    <div style="margin: 12px 0; display:flex; gap:10px; flex-wrap:wrap;">
                        <span class="tag-pill">👤 Traveler: {record['username']} ({record['visitor_country']})</span>
                        <span class="tag-pill">🏪 Store Stall: {record['stall_name']}</span>
                        <span class="tag-pill">📍 District Node: {record.get('location_province', 'Colombo')}</span>
                    </div>
                    <div style="margin-bottom:15px; background:rgba(255,255,255,0.02); padding:12px; border-radius:8px; font-size:0.85em; line-height:1.8;">
                        👅 Taste: <span style="color:#F59E0B;">{stars_taste_str}</span>  |  
                        🧼 Hygiene: <span style="color:#F59E0B;">{stars_hygiene_str}</span>  |  
                        🤝 Service: <span style="color:#F59E0B;">{stars_service_str}</span><br>
                        🌶️ Spiciness Intensity Score: <span>{stars_spicy_str}</span>
                    </div>
                    <p style="margin-bottom:15px; color:#CBD5E1 !important; font-style:italic;">
                        "{record['comment']}"
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                search_query_param = f"{record['stall_name']}, {record.get('location_province', 'Colombo')}, Sri Lanka"
                destination_maps_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(search_query_param)}"
                st.link_button(f"🗺️ Route Directly to {record['stall_name']}", destination_maps_url)
                st.markdown("<br>", unsafe_allow_html=True)
                
        if rendered_count == 0:
            st.warning("No review records found matching your active filter configuration matrix parameters.")

# ==========================================
# 5. TAB 3: MUTUALLY EXCLUSIVE REGIONAL DIRECTORY
# ==========================================
with tab3:
    st.subheader("Geospatial Database Directory")
    st.write("Browse the master registry of 100+ native items. Selecting an item collapses the previous one to keep performance clean.")
    st.write("---")
    
    col_navigation, col_viewer_pane = st.columns([1, 1.8])
    
    with col_navigation:
        st.markdown('<div class="nav-box-header">📍 Core Regional Clusters</div>', unsafe_allow_html=True)
        chosen_province_node = st.radio(
            label="Province Registry Navigation Nodes",
            options=list(SRI_LANKA_REGIONAL_DB.keys()),
            label_visibility="collapsed"
        )
        
    with col_viewer_pane:
        target_dataset = SRI_LANKA_REGIONAL_DB[chosen_province_node]
        
        st.markdown(f"""
        <div class="city-banner-gradient">
            <div>
                <h3 style="margin:0; font-size:1.4em; color:#FFF !important;">{chosen_province_node}</h3>
                <p style="margin:0; font-size:0.8em; color:#93C5FD !important; font-family:monospace;">Telemetry Sector Hub Base Line: {target_dataset['lat_long']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<p style='color:#94A3B8 !important; font-size:0.95em; line-height:1.5; margin-bottom:20px;'><i>{target_dataset['summary']}</i></p>", unsafe_allow_html=True)
        
        st.markdown("##### 🛠️ District Directory Dietary Profile Filter")
        directory_diet_filter = st.selectbox("🥗 Select Profile Filter Rule:", DIETARY_PROFILES, key="directory_diet_select")
        
        filtered_foods_list = []
        for food_item in target_dataset["foods"]:
            match_diet = True
            if directory_diet_filter != "All Profiles":
                if directory_diet_filter.lower() not in food_item["desc"].lower() and directory_diet_filter.lower() not in food_item["name"].lower():
                    match_diet = False
            if match_diet:
                filtered_foods_list.append(food_item)
                
        st.write("---")
        
        if not filtered_foods_list:
            st.warning("No traditional registry items match this dietary filter option inside this province partition cluster node.")
        else:
            food_titles_array = [f["name"] for f in filtered_foods_list]
            state_key_string = f"selected_food_for_{chosen_province_node.split()[0]}"
            
            selected_dish_row = st.selectbox(
                "🥘 Select Food Card to Expand Layer Parameters:", 
                options=food_titles_array,
                key=f"selectbox_{state_key_string}"
            )
            
            matching_food_dictionary = next(x for x in filtered_foods_list if x["name"] == selected_dish_row)
            
            try:
                postgres_rows = supabase.table("food_reviews").select("*").eq("food_name", selected_dish_row).execute().data
                if postgres_rows:
                    vote_count = sum(1 for v in postgres_rows if v["must_try"])
                    score_average = round(sum(s["stars_overall"] for s in postgres_rows) / len(postgres_rows), 1)
                    taste_avg = round(sum(s["stars_taste"] for s in postgres_rows) / len(postgres_rows), 1)
                    hygiene_avg = round(sum(s["stars_hygiene"] for s in postgres_rows) / len(postgres_rows), 1)
                    
                    st.markdown(f"""
                    <div style="display:flex; flex-wrap:wrap; gap:10px; margin-top:15px; margin-bottom:15px;">
                        <span class="metric-pill">⭐ {score_average} / 5 Score</span>
                        <span class="metric-pill">👅 Taste: {taste_avg}★</span>
                        <span class="metric-pill">🧼 Hygiene: {hygiene_avg}★</span>
                        <span class="must-try-badge">❤️ {vote_count} Must-Try Votes</span>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="display:flex; gap:10px; margin-top:15px; margin-bottom:15px;">
                        <span style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06); padding:4px 12px; border-radius:8px; font-size:0.8em; color:#64748B !important;">⚖️ No Live Database Metrics Seeded Yet</span>
                    </div>
                    """, unsafe_allow_html=True)
            except Exception:
                pass
                
            st.markdown(f"""
            <div class="main-card" style="margin-top:10px;">
                <h3 style="color:#3B82F6 !important; margin:0; font-size:1.35em;">🥘 {matching_food_dictionary['name']}</h3>
                <p style="color:#E2E8F0 !important; font-size:1em; line-height:1.6; margin-top:10px;">{matching_food_dictionary['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            directory_search_query = f"{matching_food_dictionary['name']}, {chosen_province_node.split('(')[0].strip()}, Sri Lanka"
            map_route_link = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(directory_search_query)}"
            st.link_button(f"🗺️ Open Sourcing Points Map for {matching_food_dictionary['name']}", map_route_link)