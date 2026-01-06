# Simple AI-like logic (dummy)
def recommend_product(user_interest):
    products = {
        "tech": ["Laptop", "Smartphone", "Headphones"],
        "fashion": ["Shirt", "Shoes", "Watch"],
        "fitness": ["Dumbbells", "Yoga Mat", "Protein Powder"]
    }
    return products.get(user_interest, [])

if __name__ == "__main__":
    print(recommend_product("tech"))
