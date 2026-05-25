def get_outfit_recommendations(hex_color, aesthetic):

    recommendations = {

        "Streetwear": {
            "tops": ["Oversized Hoodie", "Graphic Tee"],
            "bottoms": ["Cargo Pants", "Baggy Jeans"],
            "shoes": ["Nike Dunks", "Chunky Sneakers"]
        },

        "Old Money": {
            "tops": ["Polo Shirt", "Linen Shirt"],
            "bottoms": ["Tailored Trousers", "Cream Pants"],
            "shoes": ["Loafers", "Leather Shoes"]
        },

        "Korean Casual": {
            "tops": ["Neutral Cardigan", "Oversized Shirt"],
            "bottoms": ["Wide-fit Pants", "Black Trousers"],
            "shoes": ["White Sneakers", "Canvas Shoes"]
        },

        "Minimalist": {
            "tops": ["Plain Black Tee", "Neutral Sweatshirt"],
            "bottoms": ["Slim Black Jeans", "Grey Trousers"],
            "shoes": ["White Sneakers", "Chelsea Boots"]
        }
    }

    return recommendations.get(
        aesthetic,
        recommendations["Minimalist"]
    )