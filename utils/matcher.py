def get_outfit_recommendations(color, aesthetic, occasion):

    recommendations = {

        "Streetwear": {
            "tops": ["Oversized Hoodie", "Graphic Tee"],
            "bottoms": ["Cargo Pants", "Baggy Jeans"],
            "shoes": ["Nike Dunks"]
        },

        "Old Money": {
            "tops": ["Polo Shirt", "Linen Shirt"],
            "bottoms": ["Tailored Trousers"],
            "shoes": ["Loafers"]
        },

        "Korean Casual": {
            "tops": ["Neutral Cardigan"],
            "bottoms": ["Wide-fit Pants"],
            "shoes": ["Canvas Shoes"]
        },

        "Minimalist": {
            "tops": ["Plain Black Tee"],
            "bottoms": ["Grey Trousers"],
            "shoes": ["White Sneakers"]
        }
    }

    outfit = recommendations.get(
        aesthetic,
        recommendations["Minimalist"]
    )

    # Occasion logic
    if occasion == "Party":
        outfit["shoes"].append("Chunky Sneakers")

    elif occasion == "Office":
        outfit["shoes"].append("Formal Loafers")

    elif occasion == "College":
        outfit["shoes"].append("Canvas Sneakers")

    return outfit