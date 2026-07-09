# database_registry.py
# Production Asset Registry: 100+ Authenticated Sri Lankan Culinary Items

SRI_LANKA_REGIONAL_DB = {
    "Western Province (Colombo/Negombo)": {
        "summary": "Commercial hub showcasing modern twists on night street snacks and historic lagoon seafood markets.",
        "lat_long": "6.9271° N, 79.8612° E",
        "bg_image": "https://images.unsplash.com/photo-1588598126217-1fc94d50c187?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "Kottu Roti", "type": "Street Food", "desc": "Chopped godamba roti stir-fried with vegetables, egg, chicken, beef, or cheese. The iconic Sri Lankan street food. Profile: Spicy, Fried, Non-Vegan."},
            {"name": "Cheese Kottu", "type": "Street Food", "desc": "A rich, modern variation of standard kottu creamy milk and melted processed cheeses. Profile: Spicy, Fried, Vegetarian."},
            {"name": "Isso Wade", "type": "Street Food", "desc": "Deep-fried spicy lentil cakes topped with whole prawns. Famous along coastal walkways. Profile: Spicy, Fried, Non-Vegan."},
            {"name": "Chinese Rolls", "type": "Street Food", "desc": "Crispy deep-fried rolled crepes filled with spiced vegetables, fish, or minced meat. Profile: Spicy, Fried, Non-Vegan."},
            {"name": "Fish Cutlets", "type": "Street Food", "desc": "Savory bite-sized potato and fish croquettes rolled in breadcrumbs and deep-fried. Profile: Spicy, Fried, Non-Vegan."},
            {"name": "Short Eats", "type": "Street Food", "desc": "A collective term for local savory bakery snacks eaten on the go during tea time. Profile: Baked, Fried, Non-Vegan."},
            {"name": "Street Seafood", "type": "Street Food", "desc": "Freshly caught marine catches fried or deviled dynamically at beachside night stalls. Profile: Spicy, Fried, Non-Vegan."},
            {"name": "Lagoon Crab", "type": "Traditional Dish", "desc": "World-famous giant mud crabs from Negombo lagoon, stewed in rich local masalas. Profile: Spicy, Non-Vegan."},
            {"name": "Prawn Curry", "type": "Traditional Dish", "desc": "Plump lagoon prawns simmered in a golden coconut gravy infused with fenugreek and chili. Profile: Spicy, Non-Vegan."},
            {"name": "Negombo Fish Curry", "type": "Traditional Dish", "desc": "A fiery coastal fish curry utilizing traditional unroasted red spice blends. Profile: Spicy, Non-Vegan."},
            {"name": "Catholic Sri Lankan Foods", "type": "Traditional Dish", "desc": "Specialty pork curries and festive dishes traditional to western coastal communities. Profile: Spicy, Non-Vegan."}
        ]
    },
    "Central Province (Kandy/Nuwara Eliya)": {
        "summary": "Highland hill country kingdoms featuring royal sweetmeats, fresh produce, and colonial plantation tea cultures.",
        "lat_long": "7.2906° N, 80.6337° E",
        "bg_image": "https://images.unsplash.com/photo-1546708973-b339540b5162?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "Egg Hopper (Biththara Appa)", "type": "Street Food", "desc": "Bowl-shaped crispy rice flour pancake with a soft-steamed egg in the center. Profile: Baked, Non-Vegan, Vegetarian."},
            {"name": "Plain Hopper (Appa)", "type": "Street Food", "desc": "Fermented rice flour and coconut milk pancake with crispy edges and a soft center. Profile: Baked, Vegan, Vegetarian."},
            {"name": "Hoppers with Seeni Sambol", "type": "Traditional Dish", "desc": "Classic combination of hoppers served with a sweet and fiery caramelized onion relish. Profile: Spicy, Sweet, Vegetarian."},
            {"name": "Kandyan Sweetmeats", "type": "Traditional Dish", "desc": "Assorted ceremonial confectionery unique to the highland Kandyan kingdoms. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Kavum", "type": "Traditional Dish", "desc": "A deep-fried oil cake sweet made from rice flour and kithul treacle with a distinct top hump. Profile: Sweet, Fried, Vegan, Vegetarian."},
            {"name": "Kokis", "type": "Traditional Dish", "desc": "A Dutch-influenced crispy, deep-fried rosette snack made from rice flour and coconut milk. Profile: Fried, Vegan, Vegetarian."},
            {"name": "Aluwa", "type": "Traditional Dish", "desc": "Flat, diamond-shaped rice flour sweet spiced heavily with cardamom and roasted cashew nuts. Profile: Sweet, Baked, Vegan, Vegetarian."},
            {"name": "Athiraha", "type": "Traditional Dish", "desc": "An ancient, extremely sweet fried festive patty made of rice flour and jaggery paste. Profile: Sweet, Fried, Vegan, Vegetarian."},
            {"name": "Kiri Toffee", "type": "Traditional Dish", "desc": "A rich, sweet milk fudge confection boiled down with sugar, butter, and cardamoms. Profile: Sweet, Vegetarian."},
            {"name": "Vegetable Roti", "type": "Street Food", "desc": "Triangular flatbread envelopes stuffed with spiced potato and mixed vegetable stir-fries. Profile: Spicy, Baked, Vegan, Vegetarian."},
            {"name": "Estate Tamil Parotta", "type": "Street Food", "desc": "Multi-layered, flaky flatbreads traditional to the central tea-plantation communities. Profile: Fried, Vegan, Vegetarian."},
            {"name": "Tea", "type": "Traditional Dish", "desc": "World-class Pure Ceylon tea harvested by hand from the mist-covered mountain valleys. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Fresh Strawberries", "type": "Endemic Fruit", "desc": "High-altitude cold climate mountain berries grown around Nuwara Eliya farmlands. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Mutton Rolls", "type": "Street Food", "desc": "Deep-fried cylindrical pastry sheets packed with finely shredded spiced mutton and potatoes. Profile: Spicy, Fried, Non-Vegan."}
        ]
    },
    "Southern Province (Galle/Matara)": {
        "summary": "Coastal culinary heritage focusing on sour preservation techniques and claypot seafood cookery.",
        "lat_long": "6.0367° N, 80.2170° E",
        "bg_image": "https://images.unsplash.com/photo-1590001155093-a3c66ab0c3ff?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "Ambul Thiyal", "type": "Traditional Dish", "desc": "A dry, black sour tuna fish curry unique to the south, preserved using claypots and dried goraka paste. Profile: Spicy, Non-Vegan."},
            {"name": "Curd & Kithul Treacle", "type": "Traditional Dish", "desc": "Famous southern dessert consisting of creamy water buffalo milk curd topped with sweet palm sap syrups. Profile: Sweet, Vegetarian."},
            {"name": "Crab Curry (Southern Style)", "type": "Traditional Dish", "desc": "An excellent coastal version of crab stewed with fresh local garden herbs and heavy coconut milk infusions. Profile: Spicy, Non-Vegan."},
            {"name": "Coconut Roti", "type": "Street Food", "desc": "Rustic flatbreads mixed with freshly grated coconut kernels, green chilies, and onions. Profile: Spicy, Baked, Vegan, Vegetarian."},
            {"name": "Dry Fish Sambol", "type": "Traditional Dish", "desc": "A sharp relish made from shredded sun-dried salted fish tossed with chili flakes, lime, and onions. Profile: Spicy, Non-Vegan."},
            {"name": "Seafood Kottu", "type": "Street Food", "desc": "Stir-fried chopped flatbread mixed with fresh reef fish, squid, and prawns straight from southern nets. Profile: Spicy, Fried, Non-Vegan."}
        ]
    },
    "Northern Province (Jaffna)": {
        "summary": "Fiery culinary culture using unroasted red spices, lagoon seafood, and palmyra palm root flours.",
        "lat_long": "9.6615° N, 80.0255° E",
        "bg_image": "https://images.unsplash.com/photo-1625736319760-b6df332f1704?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "Jaffna Crab Curry", "type": "Traditional Dish", "desc": "Considered by many the ultimate crab curry in Sri Lanka, prepared with unroasted red chilies and murunga leaves. Profile: Spicy, Non-Vegan."},
            {"name": "Odiyal Kool", "type": "Traditional Dish", "desc": "A fiery, highly traditional northern seafood bouillabaisse thickened with processed palmyra root flour. Profile: Spicy, Non-Vegan."},
            {"name": "Jaffna Kool", "type": "Traditional Dish", "desc": "A thick, spicy variant of local seafood broth loaded with cuttlefish, prawns, and long beans. Profile: Spicy, Non-Vegan."},
            {"name": "Jaffna Dosai", "type": "Traditional Dish", "desc": "Soft, savory fermented lentil and rice crepes traditional to northern Tamil households. Profile: Fried, Vegan, Vegetarian."},
            {"name": "Kool Seafood Soup", "type": "Traditional Dish", "desc": "The signature coastal variant of Odiyal soup served piping hot across local northern eateries. Profile: Spicy, Non-Vegan."},
            {"name": "Palmyra Products", "type": "Traditional Dish", "desc": "Traditional culinary components harvested from the native northern Palmyra palm trees. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Palmyra jaggery", "type": "Traditional Dish", "desc": "Unrefined dark sweet sugar molds made from concentrated sweet sap of the Palmyra palm tree. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Palmyra sweets", "type": "Traditional Dish", "desc": "Handcrafted traditional sweets utilizing palmyra fruit pulp and root fibers. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Palmyra tubers", "type": "Traditional Dish", "desc": "Boiled or dry-roasted root starch sprouts of the Palmyra palm eaten as high-fiber snacks. Profile: Baked, Vegan, Vegetarian."},
            {"name": "Mutton Curry", "type": "Traditional Dish", "desc": "A dark, deeply spicy tender mutton curry prepared using authentic Jaffna unroasted milling powders. Profile: Spicy, Non-Vegan."},
            {"name": "Nandu Rasam", "type": "Traditional Dish", "desc": "A fiery, medicinal crab broth packed with heavy black pepper, cumin seeds, and garlic. Profile: Spicy, Non-Vegan."}
        ]
    },
    "Eastern Province (Batticaloa/Trincomalee)": {
        "summary": "Maritime food networks featuring deep-sea catches, rich cuttlefish curries, and traditional Muslim-style biriyanis.",
        "lat_long": "7.7170° N, 81.7010° E",
        "bg_image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "Batticaloa Prawn Curry", "type": "Traditional Dish", "desc": "A rich lagoon prawn curry using signature eastern unroasted red spice powders. Profile: Spicy, Non-Vegan."},
            {"name": "Batticaloa Fish Curry", "type": "Traditional Dish", "desc": "A sharp, aromatic coastal fish curry balanced with toasted fenugreek seeds. Profile: Spicy, Non-Vegan."},
            {"name": "Veechu Roti", "type": "Street Food", "desc": "Thin, large dough sheets tossed and folded on hot iron plates, often filled with egg. Profile: Fried, Non-Vegan, Vegetarian."},
            {"name": "Muslim Biriyani", "type": "Traditional Dish", "desc": "A highly aromatic spiced rice dish slow-cooked with meat, ghee, and served with sweet mint sambols. Profile: Spiced, Non-Vegan."},
            {"name": "Wattalappam", "type": "Traditional Dish", "desc": "A rich, baked cardamom-spiced coconut custard pudding sweetened with dark kithul jaggery sap. Profile: Sweet, Baked, Vegetarian."},
            {"name": "Fresh Lobster", "type": "Street Food", "desc": "Deep-sea rock lobsters grilled fresh at beachside night stalls in Trincomalee. Profile: Fried, Non-Vegan."},
            {"name": "Giant Prawns", "type": "Street Food", "desc": "Jumbo tiger prawns grilled over open wood fires along eastern bay fronts. Profile: Fried, Non-Vegan."},
            {"name": "Shark Curry", "type": "Traditional Dish", "desc": "Finely minced baby shark meat stir-fried with heavy turmeric, garlic, and wild curry leaves. Profile: Spicy, Non-Vegan."},
            {"name": "Seafood Rice", "type": "Street Food", "desc": "High-heat wok fried rice packed with local squid, reef fish chunks, and small prawns. Profile: Fried, Non-Vegan."},
            {"name": "Ampara Muslim Style Biriyani", "type": "Traditional Dish", "desc": "A distinct eastern inland rice variant utilizing small-grain samba rice and slow-cooked mutton. Profile: Spiced, Non-Vegan."},
            {"name": "Beef Curry", "type": "Traditional Dish", "desc": "A dark, slow-simmered beef curry utilizing heavy black pepper and dry lemongrass leaves. Profile: Spicy, Non-Vegan."},
            {"name": "Coastal Seafood", "type": "Street Food", "desc": "A generalized menu of daily coastal catches fried instantly by beachfront food vendors. Profile: Spicy, Fried, Non-Vegan."}
        ]
    },
    "North Central & Uva Provinces": {
        "summary": "Ancient dry zone agricultural plains focusing on wild forest honeys, village lake fishes, and indigenous millet flatbreads.",
        "lat_long": "8.3114° N, 80.4037° E",
        "bg_image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "Kurakkan Roti", "type": "Traditional Dish", "desc": "A rustic, highly nutritious flatbread made from finger millet flour and fresh coconut flakes. Profile: Baked, Vegan, Vegetarian."},
            {"name": "Forest Honey", "type": "Endemic Fruit", "desc": "Pure wild honey collected by indigenous communities from high forest beehives. Profile: Sweet, Vegetarian."},
            {"name": "Dry Zone Venison Curries", "type": "Traditional Dish", "desc": "A highly spiced, rich wild game curry traditional to the remote dry zone plains. Profile: Spicy, Non-Vegan."},
            {"name": "Traditional Village Rice & Curry", "type": "Traditional Dish", "desc": "Authentic multi-dish meals cooked entirely inside unglazed claypots over wood fires. Profile: Spicy, Vegan, Non-Vegan, Vegetarian."},
            {"name": "Lotus Root Curry", "type": "Traditional Dish", "desc": "Sliced aquatic lotus roots simmered in a light, aromatic coconut milk broth. Profile: Vegan, Vegetarian."},
            {"name": "Mountain Honey", "type": "Endemic Fruit", "desc": "A clear, herbal wild honey harvested from the elevated mountain cliffs of Uva province. Profile: Sweet, Vegetarian."},
            {"name": "Wild Boar Curry", "type": "Traditional Dish", "desc": "A fiery game meat curry cooked with black pepper, wild herbs, and dried chili bases. Profile: Spicy, Non-Vegan."}
        ]
    },
    "Sabaragamuwa & North Western Provinces": {
        "summary": "Dense gem-mining valleys and coconut triangles featuring wild mountain sap syrups and forest tubers.",
        "lat_long": "6.7056° N, 80.3847° E",
        "bg_image": "https://images.unsplash.com/photo-1605666804746-43d45bdb1647?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "Durian (seasonal)", "type": "Endemic Fruit", "desc": "A famous, intensely pungent tropical fruit with a rich custard-like texture, seasonal to the lowlands. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Gem-miners' Rice & Curry", "type": "Traditional Dish", "desc": "A heavy, high-energy traditional lunch packed inside banana leaves for gem miners in Ratnapura. Profile: Spicy, Non-Vegan."},
            {"name": "Kithul Treacle", "type": "Endemic Fruit", "desc": "Pure liquid sweet syrup tapped from the flowering stalks of the native Kithul fishtail palm tree. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Elephant Foot Yam Curry", "type": "Traditional Dish", "desc": "A unique, starchy native forest tuber curry simmered in heavy spiced coconut milk. Profile: Vegan, Vegetarian."},
            {"name": "Village Chicken Curry", "type": "Traditional Dish", "desc": "Free-range country chicken slow-cooked with roasted spices, ginger, and thick lemongrass stocks. Profile: Spicy, Non-Vegan."}
        ]
    },
    "National Core & Hidden Exotics": {
        "summary": "Traditional dishes staples and rare, exotic items that foreign travelers rarely discover.",
        "lat_long": "7.8731° N, 80.7718° E",
        "bg_image": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=800&q=80",
        "foods": [
            {"name": "String Hoppers (Indi Appa)", "type": "Traditional Dish", "desc": "Steamed nests of fine rice flour noodles, traditionally served for breakfast with dhal and k wholesale sambols. Profile: Baked, Vegan, Vegetarian."},
            {"name": "Ulundu Wade", "type": "Street Food", "desc": "A savory, crispy, doughnut-shaped fritter made from fermented black gram lentil batters and curry leaves. Profile: Fried, Vegan, Vegetarian."},
            {"name": "Patties", "type": "Street Food", "desc": "Hand-folded half-moon shortcrust pastries packed with spiced minced fish or potato masalas. Profile: Fried, Baked, Non-Vegan."},
            {"name": "Manioc (Cassava) with Lunu Miris", "type": "Street Food", "desc": "Boiled starchy cassava root chunks served warm alongside a fiery red onion and chili relish. Profile: Spicy, Vegan, Vegetarian."},
            {"name": "Roast Paan with Curry", "type": "Street Food", "desc": "Wood-fired, crusty, flat-sided sliced bread perfect for dipping into thick spicy meat or dhal curries. Profile: Spicy, Baked, Non-Vegan, Vegetarian."},
            {"name": "Samosa", "type": "Street Food", "desc": "Crispy, deep-fried triangular pastry pockets stuffed with potatoes, leeks, or minced beef spikes. Profile: Spicy, Fried, Non-Vegan."},
            {"name": "Vadai", "type": "Street Food", "desc": "Crunchy Tamil-style fritters made from coarse split-pea lentils, onions, and deep-fried green chilies. Profile: Spicy, Fried, Vegan, Vegetarian."},
            {"name": "Masala Peanuts", "type": "Street Food", "desc": "Spiced paper cones filled with roasted peanuts tossed in chili powder, raw onions, and lime juice. Profile: Spicy, Vegan, Vegetarian."},
            {"name": "Rice & Curry", "type": "Traditional Dish", "desc": "The national culinary meal structure comprising steamed rice alongside multiple vegetable, fish, or meat claypots. Profile: Spicy, Non-Vegan, Vegetarian."},
            {"name": "Kiribath", "type": "Traditional Dish", "desc": "Traditional milk rice slabs prepared with starchy white rice and rich creamed coconut milk milk. Profile: Vegan, Vegetarian."},
            {"name": "Pittu", "type": "Traditional Dish", "desc": "Steamed cylinders of freshly ground rice flour layered structurally with freshly grated coconut kernels. Profile: Baked, Vegan, Vegetarian."},
            {"name": "Pol Sambol", "type": "Traditional Dish", "desc": "The raw national relish consisting of freshly grated coconut ground with dry red chilies, red onions, and lime juice. Profile: Spicy, Vegan, Vegetarian."},
            {"name": "Lunu Miris", "type": "Traditional Dish", "desc": "A fiery mortar-and-pestle paste made of ground red onion bulbs, sea salt, dry bird's eye chilies, and lime juice. Profile: Spicy, Vegan, Vegetarian."},
            {"name": "Parippu", "type": "Traditional Dish", "desc": "Sri Lankan red lentil dhal curry simmered in a light coconut milk gravy with turmeric, fenugreek, and tempered mustard seeds. Profile: Vegan, Vegetarian."},
            {"name": "Wambatu Moju", "type": "Traditional Dish", "desc": "A luxurious deep-fried eggplant pickle candied with red onions, green chilies, mustard seeds, and coconut vinegar syrup. Profile: Sweet, Sour, Fried, Vegetarian."},
            {"name": "Mallung", "type": "Traditional Dish", "desc": "Finely shredded leafy green vegetables briefly tossed on a hot pan with grated coconut, turmeric, and lime. Profile: Vegan, Vegetarian."},
            {"name": "Jackfruit Curry", "type": "Traditional Dish", "desc": "Traditional curry utilizing native jackfruits, prepared as raw green flesh or mature seeds. Profile: Vegan, Vegetarian."},
            {"name": "Polos (young jackfruit)", "type": "Traditional Dish", "desc": "Young green jackfruit chunks slow-cooked for hours until it develops a tender, savory, meat-like texture. Profile: Spicy, Vegan, Vegetarian."},
            {"name": "Kos (mature jackfruit)", "type": "Traditional Dish", "desc": "Mature starch-rich jackfruit bulbs boiled or curried in a mild, sweet coconut milk gravy. Profile: Vegan, Vegetarian."},
            {"name": "Lamprais", "type": "Traditional Dish", "desc": "A Dutch Burgher specialty consisting of rice boiled in stock, mixed meats, and ash plantain wrapped and slow-baked inside a banana leaf envelope. Profile: Spiced, Baked, Non-Vegan."},
            {"name": "Hala Pe", "type": "Traditional Dish", "desc": "A hidden sweet dough snack made of ragi millet flour and jaggery paste, flattened and steamed inside a green kenda leaf envelope. Profile: Sweet, Baked, Vegan, Vegetarian."},
            {"name": "Thalapa", "type": "Traditional Dish", "desc": "A thick, heavy traditional peasant millet flour pudding ball eaten dipped into spicy coconut milk stocks. Profile: Vegan, Vegetarian."},
            {"name": "Kiri Hodi", "type": "Traditional Dish", "desc": "A rich, yellow coconut milk gravy soured with lime and seasoned with fenugreek seeds and onions. Profile: Vegetarian."},
            {"name": "Polos Curry", "type": "Traditional Dish", "desc": "The signature spicy claypot version of baby young jackfruit cooked with heavily roasted dark curry powders. Profile: Spicy, Vegan, Vegetarian."},
            {"name": "Wood Apple Juice", "type": "Endemic Fruit", "desc": "A thick, sweet-sour brown juice blended from the native hard-shelled tropical wood apple fruit pulp and coconut milk. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Veralu Achcharu", "type": "Street Food", "desc": "Boiled native wild green olives crushed and tossed in a sweet-spicy chili, salt, and vinegar glaze. Profile: Spicy, Sweet, Vegan, Vegetarian."},
            {"name": "Divul Juice", "type": "Endemic Fruit", "desc": "The authentic local beverage blended straight from fresh wild tropical wood apple tree orchards. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Kithul Jaggery", "type": "Endemic Fruit", "desc": "Solid sweet candy molds made from reducing the sweet sap juice of the mountain Kithul palm tree flower. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Palmyra Jaggery", "type": "Traditional Dish", "desc": "Dense northern crystalline sugar blocks crafted from unrefined sweet sap tapped from palmyra palm trees. Profile: Sweet, Vegan, Vegetarian."},
            {"name": "Smoked Dry Fish Curry", "type": "Traditional Dish", "desc": "A deeply aromatic, intense curry utilizing wood-smoked salted sea fish chunks simmered in dark spice mixtures. Profile: Spicy, Non-Vegan."},
            {"name": "Breadfruit Curry", "type": "Traditional Dish", "desc": "A rich, starchy native tropical breadfruit curry prepared inside light coconut milk yellow stocks. Profile: Vegan, Vegetarian."},
            {"name": "Murunga (Drumstick) Curry", "type": "Traditional Dish", "desc": "Native tree drumstick pods cut into segments and cooked inside a highly aromatic, fibrous coconut curry broth. Profile: Vegan, Vegetarian."},
            {"name": "Kohila Curry", "type": "Traditional Dish", "desc": "A fibrous native aquatic plant rhizome stem curry highly traditional for digestive wellness properties. Profile: Vegan, Vegetarian."},
            {"name": "Gotukola Sambol", "type": "Traditional Dish", "desc": "A refreshing salad consisting of finely shredded Asiatic pennywort leaves mixed with grated coconut, shallots, and lime juice. Profile: Vegan, Vegetarian."}
        ]
    }
}