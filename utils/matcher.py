
def get_outfit_recommendations(hex_color):

    recommendations = {

        "#480c0d": {
            "tops": ["Black Jacket", "Cream Hoodie"],
            "bottoms": ["Black Jeans", "Beige Trousers"],
            "shoes": ["White Sneakers", "Black Boots"]
        },

        "#000000": {
            "tops": ["Grey Hoodie", "White Shirt"],
            "bottoms": ["Black Cargo Pants", "Blue Jeans"],
            "shoes": ["White Sneakers", "Chunky Shoes"]
        },

        "#ffffff": {
            "tops": ["Denim Jacket", "Brown Overshirt"],
            "bottoms": ["Black Jeans", "Grey Trousers"],
            "shoes": ["White Sneakers", "Loafers"]
        }
    }

    return recommendations.get(
        hex_color,
        {
            "tops": ["Neutral Jacket"],
            "bottoms": ["Black Jeans"],
            "shoes": ["White Sneakers"]
        }
    )